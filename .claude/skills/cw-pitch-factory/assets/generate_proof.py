#!/usr/bin/env python3
"""cw-pitch-factory — parametrische proof-generator.

Leest een slides-spec (JSON) + huisstijl-tokens en bouwt een CBOE-stijl proof-PPTX
(navy + amber + cream). Content is variabel (uit de spec), layout is vast (CBOE).

Gebruik:  python3 generate_proof.py slides.json house-style-tokens.json out.pptx

Slide-types: cover · contents · scqa · cards · statement · table · kpi · timeline ·
             fee · blank · closing · (fallback: cards).
Elke slide: {"type": "...", ...velden...}. Zie slides.example.json.
"""
import json, sys
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE

spec = json.load(open(sys.argv[1], encoding="utf-8"))
tok = json.load(open(sys.argv[2], encoding="utf-8"))
OUT = sys.argv[3] if len(sys.argv) > 3 else "proof.pptx"

C = {k: RGBColor.from_string(v) for k, v in tok["colours"].items()}
NAVY, NAVY2, AMBER, CREAM = C["navy"], C["navy2"], C["amber"], C["cream"]
WHITE, GREY, HAIR, MID = C["white"], C["grey"], C["hair"], C["mid"]
SANS = tok["fonts"]["sans"]; SERIF = tok["fonts"]["serif"]
THREAD = tok.get("golden_thread", "")
FOOTER = spec.get("meta", {}).get("footer", "Cushman & Wakefield")

prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]
PAGE = [0]


def sld():
    PAGE[0] += 1
    return prs.slides.add_slide(BLANK)


def box(s, x, y, w, h, fill, line=None, lw=0.5):
    sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = fill
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line; sh.line.width = Pt(lw)
    sh.shadow.inherit = False
    return sh


def txt(s, x, y, w, h, text, size, color, bold=False, align=PP_ALIGN.LEFT,
        anchor=MSO_ANCHOR.TOP, italic=False, font=None):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE; tf.vertical_anchor = anchor
    for i, line in enumerate((text or "").split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        r = p.add_run(); r.text = line
        f = r.font; f.size = Pt(size); f.bold = bold; f.italic = italic
        f.color.rgb = color; f.name = font or SANS
    return tb


def chip(s):
    if not THREAD:
        return
    box(s, 8.45, 7.02, 4.0, 0.34, NAVY)
    txt(s, 8.45, 7.06, 4.0, 0.28, THREAD, 8, AMBER, bold=True, align=PP_ALIGN.CENTER)


def footer(s, no=True):
    txt(s, 0.6, 7.05, 6, 0.3, FOOTER, 8, GREY)
    if no:
        txt(s, 12.55, 7.05, 0.55, 0.3, str(PAGE[0]), 10, GREY, align=PP_ALIGN.RIGHT)


def head(s, label, descriptor, thread=True):
    """CBOE-header: amber label + navy descriptor, geen spine."""
    txt(s, 0.6, 0.46, 12, 0.35, (label or "").upper(), 13, AMBER, bold=True)
    txt(s, 0.6, 0.82, 12.2, 0.7, descriptor or "", 20, NAVY, bold=True)
    footer(s)
    if thread:
        chip(s)


# ---------------- layout-types ----------------
def cover(s, d):
    box(s, 0, 0, 13.333, 4.5, MID)
    txt(s, 0.5, 1.9, 12.3, 0.6, d.get("photo", "[ FULL-BLEED FOTO ]"), 14, GREY, align=PP_ALIGN.CENTER)
    box(s, 0, 4.5, 13.333, 0.12, AMBER)
    txt(s, 0.6, 4.8, 11.5, 1.1, d.get("title", ""), 40, NAVY, bold=True)
    txt(s, 0.6, 5.72, 11.6, 0.6, d.get("subtitle", ""), 15, AMBER, bold=True)
    txt(s, 0.6, 6.5, 9, 0.5, d.get("meta", ""), 12, GREY)
    box(s, 11.2, 6.35, 1.85, 0.78, CREAM)
    txt(s, 11.2, 6.55, 1.85, 0.4, d.get("logo", "[ C&W LOGO ]"), 10, GREY, align=PP_ALIGN.CENTER)


def contents(s, d):
    head(s, d.get("label", "Contents"), d.get("descriptor", ""))
    items = d.get("items", []); n = max(1, len(items))
    w = (12.2 - (n - 1) * 0.15) / n
    for i, it in enumerate(items):
        x = 0.6 + i * (w + 0.15)
        box(s, x, 1.9, w, 4.2, CREAM)
        txt(s, x + 0.12, 2.1, w - 0.24, 0.6, it[0], 26, AMBER, bold=True)
        txt(s, x + 0.12, 2.85, w - 0.24, 1.3, it[1], 12, NAVY, bold=True)
        txt(s, x + 0.12, 4.2, w - 0.24, 1.9, it[2] if len(it) > 2 else "", 9.5, GREY)


def scqa(s, d):
    txt(s, 0.6, 0.46, 12, 0.35, d.get("label", "EXECUTIVE SUMMARY").upper(), 13, AMBER, bold=True)
    txt(s, 0.6, 0.82, 12.2, 0.5, d.get("descriptor", ""), 18, NAVY, bold=True)
    footer(s); chip(s)
    box(s, 0.6, 1.75, 0.045, 4.05, AMBER)
    txt(s, 0.85, 1.78, 5.4, 0.3, "SITUATION", 12, AMBER, bold=True)
    txt(s, 0.85, 2.12, 5.55, 1.55, d.get("situation", ""), 11.5, NAVY)
    txt(s, 0.85, 3.85, 5.4, 0.3, "COMPLICATION", 12, AMBER, bold=True)
    txt(s, 0.85, 4.19, 5.55, 1.6, d.get("complication", ""), 11.5, NAVY)
    txt(s, 6.95, 1.75, 5.9, 2.0, d.get("question", ""), 19, AMBER, italic=True,
        font=SERIF, anchor=MSO_ANCHOR.MIDDLE)
    box(s, 6.95, 4.0, 5.9, 1.95, NAVY)
    txt(s, 7.2, 4.18, 5.5, 0.3, d.get("answer_label", "OUR ANSWER"), 12, AMBER, bold=True)
    txt(s, 7.2, 4.54, 5.45, 1.3, d.get("answer", ""), 11.5, WHITE)


def cards(s, d):
    head(s, d.get("label", ""), d.get("descriptor", ""))
    cds = d.get("cards", []); n = len(cds)
    top, ch = 1.85, 4.35
    if n <= 3:
        w = (12.2 - (n - 1) * 0.25) / max(1, n)
        for i, c in enumerate(cds):
            x = 0.6 + i * (w + 0.25)
            fill = NAVY if c.get("dark") else CREAM
            tcol = WHITE if c.get("dark") else NAVY
            lab = AMBER if c.get("dark") else AMBER
            box(s, x, top, w, ch, fill, line=None if c.get("dark") else HAIR)
            txt(s, x + 0.18, top + 0.18, w - 0.36, 0.55, c.get("title", ""), 13, lab, bold=True)
            txt(s, x + 0.18, top + 0.85, w - 0.36, ch - 1.0, c.get("body", ""), 11, tcol)
    else:  # 2x2
        w, ch = 6.0, 2.05
        for i, c in enumerate(cds[:4]):
            x = 0.6 + (i % 2) * 6.2; y = 1.9 + (i // 2) * 2.25
            box(s, x, y, w, ch, CREAM, line=HAIR)
            txt(s, x + 0.18, y + 0.15, w - 0.36, 0.5, c.get("title", ""), 13, AMBER, bold=True)
            txt(s, x + 0.18, y + 0.72, w - 0.36, ch - 0.85, c.get("body", ""), 10.5, NAVY)
    if d.get("strap"):
        txt(s, 0.6, 6.35, 12, 0.5, d["strap"], 11, NAVY, bold=True, italic=True)


def statement(s, d):
    box(s, 0, 0, 13.333, 7.5, NAVY)
    box(s, 0, 0, 0.14, 7.5, AMBER)
    txt(s, 0.7, 1.4, 11, 0.4, d.get("kicker", "").upper(), 12, AMBER, bold=True)
    txt(s, 0.7, 2.0, 12, 2.4, d.get("statement", ""), 34, WHITE, bold=True)
    box(s, 0.72, 3.95, 3.2, 0.06, AMBER)
    txt(s, 0.7, 4.3, 11.8, 1.6, d.get("body", ""), 15, WHITE)
    if d.get("chip", True) and THREAD:
        b = box(s, 0.7, 6.2, 6.5, 0.5, NAVY2, line=AMBER, lw=1)
        txt(s, 0.7, 6.29, 6.5, 0.35, THREAD, 12, AMBER, bold=True, align=PP_ALIGN.CENTER)


def table(s, d):
    head(s, d.get("label", ""), d.get("descriptor", ""))
    if d.get("intro"):
        txt(s, 0.6, 1.75, 12.3, 0.5, d["intro"], 11, NAVY)
    hdrs = d.get("headers", []); rows = d.get("rows", [])
    widths = d.get("widths") or [12.2 / max(1, len(hdrs))] * len(hdrs)
    y0 = 2.35 if d.get("intro") else 1.9
    x = 0.6
    for j, hh in enumerate(hdrs):
        box(s, x, y0, widths[j], 0.42, NAVY)
        txt(s, x + 0.08, y0 + 0.06, widths[j] - 0.15, 0.32, hh, 9.5, WHITE, bold=True)
        x += widths[j]
    rh = min(0.62, (6.3 - y0) / max(1, len(rows)))
    for i, row in enumerate(rows):
        cy = y0 + 0.42 + i * rh; x = 0.6
        for j, cell in enumerate(row):
            box(s, x, cy, widths[j], rh, WHITE if i % 2 == 0 else CREAM, line=HAIR)
            txt(s, x + 0.08, cy + 0.05, widths[j] - 0.15, rh - 0.08, str(cell), 9, NAVY,
                anchor=MSO_ANCHOR.MIDDLE)
            x += widths[j]
    if d.get("note"):
        txt(s, 0.6, y0 + 0.42 + len(rows) * rh + 0.1, 12, 0.3, d["note"], 8, GREY, italic=True)


def kpi(s, d):
    head(s, d.get("label", ""), d.get("descriptor", ""))
    txt(s, 0.6, 1.9, 5.4, 4.3, d.get("left", ""), 11.5, NAVY)
    tiles = d.get("tiles", [])
    for i, t in enumerate(tiles[:6]):
        x = 6.3 + (i % 3) * 2.15; y = 1.9 + (i // 3) * 1.7
        box(s, x, y, 2.0, 1.5, CREAM, line=HAIR)
        txt(s, x + 0.12, y + 0.12, 1.8, 0.4, t[0], 10, NAVY, bold=True)
        txt(s, x + 0.12, y + 0.55, 1.8, 0.5, t[1] if len(t) > 1 else "", 9, GREY)
        txt(s, x + 0.12, y + 1.05, 1.8, 0.35, "[ ● ]", 12, AMBER, bold=True)


def timeline(s, d):
    head(s, d.get("label", ""), d.get("descriptor", ""))
    steps = d.get("steps", []); n = max(1, len(steps))
    x0, span = 0.6, 12.1
    box(s, x0, 3.35, span, 0.06, AMBER)
    step = span / n
    for i, st in enumerate(steps):
        cx = x0 + step * i + step / 2
        dia = s.shapes.add_shape(MSO_SHAPE.DIAMOND, Inches(cx - 0.16), Inches(3.22), Inches(0.32), Inches(0.32))
        dia.fill.solid(); dia.fill.fore_color.rgb = AMBER if i in (0, n - 1) else NAVY
        dia.line.color.rgb = WHITE; dia.shadow.inherit = False
        up = (i % 2 == 0); ty = 1.75 if up else 3.95
        bx = cx - step / 2 + 0.1; bw = step - 0.2
        txt(s, bx, ty, bw, 0.3, st[0], 11, AMBER, bold=True, align=PP_ALIGN.CENTER)
        txt(s, bx, ty + 0.28, bw, 0.25, st[1] if len(st) > 1 else "", 9, GREY, bold=True, align=PP_ALIGN.CENTER)
        txt(s, bx, ty + 0.55, bw, 1.1, st[2] if len(st) > 2 else "", 9, NAVY, align=PP_ALIGN.CENTER)
    if d.get("note"):
        txt(s, 0.6, 6.55, 11, 0.3, d["note"], 8, GREY, italic=True)


def fee(s, d):
    head(s, d.get("label", ""), d.get("descriptor", ""))
    rows = d.get("rows", [])
    for i, r in enumerate(rows):
        y = 1.95 + i * 0.72
        box(s, 0.6, y, 7.6, 0.6, WHITE if i % 2 == 0 else CREAM, line=HAIR)
        txt(s, 0.75, y + 0.08, 4.6, 0.45, r[0], 10.5, NAVY, bold=True, anchor=MSO_ANCHOR.MIDDLE)
        txt(s, 5.45, y + 0.08, 1.7, 0.45, r[1] if len(r) > 1 else "", 9.5, GREY, anchor=MSO_ANCHOR.MIDDLE)
        txt(s, 7.15, y + 0.08, 1.0, 0.45, r[2] if len(r) > 2 else "€ [ • ]", 10.5, AMBER, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    box(s, 8.45, 1.95, 4.4, 2.9, CREAM, line=HAIR)
    txt(s, 8.65, 2.1, 4.0, 0.35, d.get("ratecard_title", "RATE CARD — C&W PDS 2026"), 11, AMBER, bold=True)
    txt(s, 8.65, 2.5, 4.0, 2.3, d.get("ratecard", ""), 10, NAVY)
    if d.get("assumptions"):
        box(s, 0.6, 5.0, 12.25, 1.6, WHITE, line=HAIR)
        txt(s, 0.8, 5.12, 12, 0.35, "ASSUMPTIONS & EXCLUSIONS", 11, AMBER, bold=True)
        txt(s, 0.8, 5.5, 12, 1.05, d["assumptions"], 10, NAVY)


def blank(s, d):
    txt(s, 0.6, 0.46, 9, 0.3, d.get("label", "TEAM").upper(), 10, MID, bold=True)
    txt(s, 12.55, 7.05, 0.55, 0.3, str(PAGE[0]), 10, MID, align=PP_ALIGN.RIGHT)


def closing(s, d):
    box(s, 0, 0, 13.333, 3.05, NAVY)
    box(s, 0, 0, 0.14, 7.5, AMBER)
    txt(s, 0.6, 0.5, 11, 0.35, d.get("kicker", "THE DECISION").upper(), 11, AMBER, bold=True)
    txt(s, 0.6, 0.95, 12, 0.7, d.get("title", ""), 28, WHITE, bold=True)
    txt(s, 0.6, 1.75, 12, 1.1, d.get("vision", ""), 13, WHITE)
    txt(s, 0.6, 3.3, 8, 0.4, d.get("steps_label", "THE DECISION WE ASK YOU TO MAKE NOW"), 12, AMBER, bold=True)
    for i, st in enumerate(d.get("steps", [])):
        y = 3.8 + i * 0.56
        box(s, 0.6, y, 0.45, 0.45, NAVY)
        txt(s, 0.6, y + 0.05, 0.45, 0.35, str(i + 1), 12, AMBER, bold=True, align=PP_ALIGN.CENTER)
        txt(s, 1.2, y + 0.03, 8.4, 0.5, st[0], 11.5, NAVY, anchor=MSO_ANCHOR.MIDDLE)
        txt(s, 9.6, y + 0.03, 3.2, 0.5, st[1] if len(st) > 1 else "", 9.5, GREY, italic=True, anchor=MSO_ANCHOR.MIDDLE)
    box(s, 0.6, 6.65, 12.25, 0.6, NAVY)
    txt(s, 0.8, 6.75, 12, 0.42, d.get("contact", ""), 11.5, AMBER, bold=True)


DISPATCH = {"cover": cover, "contents": contents, "scqa": scqa, "cards": cards,
            "statement": statement, "table": table, "kpi": kpi, "timeline": timeline,
            "fee": fee, "blank": blank, "closing": closing}

for d in spec["slides"]:
    s = sld()
    DISPATCH.get(d.get("type"), cards)(s, d)

prs.save(OUT)
print("OK:", len(prs.slides._sldIdLst), "slides ->", OUT)
