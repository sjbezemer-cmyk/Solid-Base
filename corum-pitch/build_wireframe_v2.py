#!/usr/bin/env python3
"""Corum — Westgate I 'Paris Proof' pitch — WIREFRAME v2 (MBB-grade).

Verbeteringen t.o.v. v1 (na 3 rondes x 5 invalshoeken):
- SCQA executive summary die op zichzelf staat (pyramid principle).
- Action titles: elke slidetitel is de conclusie, niet het onderwerp.
- Golden thread 'CORUM DECIDES - C&W DELIVERS' als terugkerend motief.
- Twee expliciete deep-dives: 'We manage PwC for you' en 'We organize the works'.
- Chronologisch verhaal: Situation -> Complication -> Answer -> Journey -> 2030.
- Meer tekst, investeerder-taal (asset value, tenant retention, de-risking).
- Teampagina bewust wit.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

CW_RED = RGBColor(0xC3, 0x00, 0x2B)
CW_DARK = RGBColor(0x1C, 0x1C, 0x1C)
GREY = RGBColor(0x7A, 0x7A, 0x7A)
LIGHT = RGBColor(0xF3, 0xF3, 0xF3)
MID = RGBColor(0xD9, 0xD9, 0xD9)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
AMBER = RGBColor(0xE8, 0x9A, 0x00)
GREEN = RGBColor(0x2E, 0x7D, 0x32)

SW, SH = Inches(13.333), Inches(7.5)

prs = Presentation()
prs.slide_width = SW
prs.slide_height = SH
BLANK = prs.slide_layouts[6]


def slide():
    return prs.slides.add_slide(BLANK)


def _dash(shape):
    ln = shape.line._get_or_add_ln()
    ln.append(ln.makeelement(qn('a:prstDash'), {'val': 'dash'}))


def box(s, x, y, w, h, fill=LIGHT, line=GREY, dashed=True):
    sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    sh.fill.solid(); sh.fill.fore_color.rgb = fill
    sh.line.color.rgb = line; sh.line.width = Pt(0.75)
    if dashed:
        _dash(sh)
    sh.shadow.inherit = False
    return sh


def txt(s, x, y, w, h, text, size=12, color=CW_DARK, bold=False,
        align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, italic=False, space=None):
    tb = s.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for i, line in enumerate(text.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        if space is not None:
            p.space_after = Pt(space)
        r = p.add_run(); r.text = line
        f = r.font
        f.size = Pt(size); f.bold = bold; f.italic = italic
        f.color.rgb = color; f.name = "Arial"
    return tb


def label(s, x, y, w, text):
    txt(s, x, y, w, Inches(0.3), text, size=8, color=GREY, italic=True)


def thread(s):
    """Golden-thread badge rechtsonder."""
    b = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.75), Inches(7.02),
                           Inches(2.75), Inches(0.32))
    b.fill.solid(); b.fill.fore_color.rgb = CW_RED
    b.line.fill.background(); b.shadow.inherit = False
    txt(s, Inches(9.75), Inches(7.05), Inches(2.75), Inches(0.28),
        "CORUM DECIDES  ·  C&W DELIVERS", size=8, color=WHITE, bold=True,
        align=PP_ALIGN.CENTER)


def header(s, kicker, title, num, tline=True):
    bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.18), SH)
    bar.fill.solid(); bar.fill.fore_color.rgb = CW_RED
    bar.line.fill.background(); bar.shadow.inherit = False
    txt(s, Inches(0.45), Inches(0.24), Inches(11), Inches(0.3),
        kicker.upper(), size=10, color=CW_RED, bold=True)
    txt(s, Inches(0.45), Inches(0.5), Inches(12.2), Inches(0.95),
        title, size=23, color=CW_DARK, bold=True)
    txt(s, Inches(0.45), Inches(7.05), Inches(6), Inches(0.3),
        "CUSHMAN & WAKEFIELD  |  CORUM A.M.  ·  WESTGATE I", size=8, color=GREY)
    txt(s, Inches(12.55), Inches(7.05), Inches(0.55), Inches(0.3),
        str(num), size=10, color=GREY, align=PP_ALIGN.RIGHT)
    if tline:
        thread(s)


# ============================================================= 1 COVER
s = slide()
box(s, 0, 0, SW, Inches(4.5), fill=MID)
txt(s, Inches(0.5), Inches(1.9), Inches(12.3), Inches(0.6),
    "[ FULL-BLEED FOTO WESTGATE I — Thomas R. Malthusstraat 5, Amsterdam ]",
    size=14, color=GREY, align=PP_ALIGN.CENTER)
bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(4.5), SW, Inches(0.12))
bar.fill.solid(); bar.fill.fore_color.rgb = CW_RED
bar.line.fill.background(); bar.shadow.inherit = False
txt(s, Inches(0.6), Inches(4.8), Inches(11), Inches(1.1),
    "WESTGATE I — PARIS PROOF", size=40, color=CW_DARK, bold=True)
txt(s, Inches(0.6), Inches(5.7), Inches(11.5), Inches(0.6),
    "Your single point of control — delivering Paris Proof with tenant PwC fully aware and aligned",
    size=15, color=CW_RED, bold=True)
txt(s, Inches(0.6), Inches(6.5), Inches(9), Inches(0.5),
    "Project Management Proposal  ·  Prepared for Corum A.M.  ·  July 2026",
    size=12, color=GREY)
box(s, Inches(11.0), Inches(5.55), Inches(1.8), Inches(0.9), fill=LIGHT)
txt(s, Inches(11.0), Inches(5.85), Inches(1.8), Inches(0.4), "[C&W LOGO]",
    size=10, color=GREY, align=PP_ALIGN.CENTER)

# ============================================== 2 EXECUTIVE SUMMARY (SCQA)
s = slide()
header(s, "Executive summary — the proposal on one page",
       "Appoint C&W as your single point of control: we deliver Paris Proof\nwith PwC fully aware and aligned — you decide, we deliver", 2)
scqa = [
    ("SITUATION",
     "Corum owns Westgate I — a prime 27,000 m² Amsterdam office, fully let to PwC — and has "
     "committed to make the building Paris Proof. This is a binding contractual obligation, not "
     "an ambition.", CW_DARK),
    ("COMPLICATION",
     "The upgrade must happen inside a live, occupied building without losing PwC's confidence, "
     "within a fixed budget and against a hard sustainability deadline — while being steered from "
     "a distance by an owner whose core business is investment, not Dutch construction management.", CW_DARK),
    ("QUESTION",
     "How does Corum deliver Paris Proof and protect both the PwC tenancy and the asset's value, "
     "without being pulled into day-to-day tenant and project management in the Netherlands?", CW_RED),
    ("ANSWER",
     "Appoint Cushman & Wakefield as your single point of control. We deliver the Paris Proof "
     "transformation end-to-end and keep PwC fully aware and aligned throughout — from a "
     "low-commitment preparatory phase to verified handover. One contact, one report, no surprises.", CW_RED),
]
y = Inches(1.75)
for i, (k, d, c) in enumerate(scqa):
    h = Inches(1.02) if i in (0, 2) else Inches(1.28)
    box(s, Inches(0.45), y, Inches(2.3), h, fill=c if c == CW_RED else CW_DARK, dashed=False)
    txt(s, Inches(0.45), y + Inches(0.08), Inches(2.3), Inches(0.5), k,
        size=13, color=WHITE, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    box(s, Inches(2.8), y, Inches(10.05), h, fill=LIGHT if c == CW_DARK else WHITE,
        line=CW_RED if c == CW_RED else GREY)
    txt(s, Inches(3.0), y + Inches(0.1), Inches(9.7), h - Inches(0.2), d,
        size=11.5, bold=(c == CW_RED), anchor=MSO_ANCHOR.MIDDLE)
    y = y + h + Inches(0.12)

# ===================================================== 3 CONTENTS
s = slide()
header(s, "Contents", "How this proposal is built", 3, tline=False)
items = [
    ("01", "THE CASE FOR ACTION", "Situation, complication\n& our governing answer"),
    ("02", "WHAT WE TAKE\nOFF YOUR PLATE", "Managing PwC & organizing\nthe Paris Proof works"),
    ("03", "THE JOURNEY", "Chronological roadmap,\nphasing & planning"),
    ("04", "HOW WE STAY\nIN CONTROL", "Organisation, governance,\nreporting & risk"),
    ("05", "WHY C&W, TEAM\n& TRACK RECORD", "Differentiation, team (t.b.d.)\n& references"),
    ("06", "COMMERCIALS\n& THE DECISION", "Fee, the 2030 vision\n& next steps"),
]
w = Inches(1.98); gap = Inches(0.1); x0 = Inches(0.5)
for i, (n, t, d) in enumerate(items):
    x = x0 + i * (w + gap)
    box(s, x, Inches(1.9), w, Inches(4.3))
    txt(s, x + Inches(0.12), Inches(2.1), w - Inches(0.24), Inches(0.6),
        n, size=26, color=CW_RED, bold=True)
    txt(s, x + Inches(0.12), Inches(2.85), w - Inches(0.24), Inches(1.3),
        t, size=12, color=CW_DARK, bold=True)
    txt(s, x + Inches(0.12), Inches(4.2), w - Inches(0.24), Inches(1.9),
        d, size=9.5, color=GREY)

# ================================================ 4 SITUATION
s = slide()
header(s, "01 — The case for action  ·  Situation",
       "You own a prime Amsterdam asset with a binding\nParis Proof commitment attached to it", 4)
facts = [
    ("THE ASSET", "Westgate I — Thomas R. Malthusstraat 5, 1066 JR Amsterdam. A prime, single-tenant office building of ± 27,000 m² GFA."),
    ("THE TENANT", "PwC occupies the building and is in full operation every working day. The tenant relationship is the value of the asset."),
    ("THE OWNER", "Corum A.M. — an institutional investor steering the asset from a distance, focused on returns, not on day-to-day Dutch construction."),
    ("THE COMMITMENT", "The building must be brought to Paris Proof. This is a hard contractual obligation with a fixed budget and a fixed horizon."),
]
for i, (k, v) in enumerate(facts):
    y = Inches(1.95) + i * Inches(1.12)
    box(s, Inches(0.45), y, Inches(7.4), Inches(1.0), fill=WHITE)
    txt(s, Inches(0.6), y + Inches(0.1), Inches(2.0), Inches(0.8), k,
        size=12, color=CW_RED, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, Inches(2.55), y + Inches(0.1), Inches(5.15), Inches(0.8), v,
        size=11, anchor=MSO_ANCHOR.MIDDLE)
box(s, Inches(8.1), Inches(1.95), Inches(4.75), Inches(4.45), fill=LIGHT)
txt(s, Inches(8.3), Inches(2.15), Inches(4.4), Inches(0.6),
    "WHAT THIS MEANS FOR CORUM", size=12, color=CW_RED, bold=True)
txt(s, Inches(8.3), Inches(2.8), Inches(4.4), Inches(3.4),
    "Three assets are at stake in one building, at the same time:\n\n"
    "•  The physical asset and its value\n\n"
    "•  The PwC tenancy — and the lease that underpins your return\n\n"
    "•  Your reputation as a reliable, professional landlord\n\n"
    "All three are exposed the moment work starts inside an occupied building.",
    size=11, space=2)

# ================================================ 5 COMPLICATION
s = slide()
header(s, "01 — The case for action  ·  Complication",
       "Three forces threaten the asset — and they all converge\non one building, still in use", 5)
forces = [
    ("THE TENANT RISK", "PwC keeps working while you rebuild",
     "A previous Corum project (Rotterdam) showed how quickly insufficient communication erodes tenant "
     "trust. Disruption, noise and uncertainty can damage the relationship — and a damaged relationship "
     "puts lease renewal, and asset value, at risk."),
    ("THE DELIVERY RISK", "Fixed budget, complex technique, live site",
     "Paris Proof means a full climate-system transformation (see M3E's two scenarios). Executed floor-by-floor "
     "in an occupied building, on a fixed budget, this is unforgiving: every technical or sequencing mistake "
     "becomes visible to the tenant and expensive to the owner."),
    ("THE DEADLINE RISK", "Paris Proof is contractual, not optional",
     "The obligation is binding. Slippage is not a soft cost — it is a breach exposure. The programme must be "
     "driven to a hard finish line, with the critical path owned and defended from day one."),
]
for i, (t, sub, d) in enumerate(forces):
    x = Inches(0.45) + i * Inches(4.18)
    box(s, x, Inches(2.0), Inches(4.0), Inches(4.4), fill=WHITE)
    hd = box(s, x, Inches(2.0), Inches(4.0), Inches(0.95), fill=CW_RED, dashed=False)
    txt(s, x + Inches(0.15), Inches(2.1), Inches(3.7), Inches(0.4), f"0{i+1}",
        size=13, color=WHITE, bold=True)
    txt(s, x + Inches(0.15), Inches(2.45), Inches(3.7), Inches(0.45), t,
        size=13, color=WHITE, bold=True)
    txt(s, x + Inches(0.2), Inches(3.1), Inches(3.6), Inches(0.7), sub,
        size=11, color=CW_RED, bold=True, italic=True)
    txt(s, x + Inches(0.2), Inches(3.85), Inches(3.6), Inches(2.4), d, size=10.5)
txt(s, Inches(0.45), Inches(6.5), Inches(11.5), Inches(0.4),
    "Left unmanaged, these three risks compound. Managed by one accountable party, they become a controlled programme.",
    size=11, color=CW_DARK, bold=True, italic=True)

# ================================================ 6 GOVERNING THOUGHT
s = slide()
box(s, 0, 0, SW, SH, fill=CW_DARK, line=CW_DARK, dashed=False)
bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.18), SH)
bar.fill.solid(); bar.fill.fore_color.rgb = CW_RED
bar.line.fill.background(); bar.shadow.inherit = False
txt(s, Inches(0.7), Inches(1.4), Inches(11), Inches(0.4),
    "OUR GOVERNING ANSWER", size=12, color=CW_RED, bold=True)
txt(s, Inches(0.7), Inches(2.0), Inches(12), Inches(2.6),
    "Make Cushman & Wakefield your single\npoint of control in the Netherlands.",
    size=34, color=WHITE, bold=True)
txt(s, Inches(0.7), Inches(4.3), Inches(11.8), Inches(1.5),
    "We deliver the entire Paris Proof transformation end-to-end and keep PwC "
    "fully aware and aligned at every step. You steer the asset; we run the works and "
    "the tenant relationship — and we bring you every decision, prepared, before it is needed.",
    size=15, color=WHITE)
b = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(6.2),
                       Inches(4.4), Inches(0.5))
b.fill.solid(); b.fill.fore_color.rgb = CW_RED; b.line.fill.background(); b.shadow.inherit = False
txt(s, Inches(0.7), Inches(6.28), Inches(4.4), Inches(0.35),
    "CORUM DECIDES  ·  C&W DELIVERS", size=12, color=WHITE, bold=True, align=PP_ALIGN.CENTER)

# ================================================ 7 WHAT WE TAKE OFF YOUR PLATE
s = slide()
header(s, "01 — The case for action  ·  Our answer",
       "In practice, we take three things entirely off your plate", 7)
cols = [
    ("PwC FULLY AWARE\n& ALIGNED", CW_RED,
     ["One familiar point of contact for PwC",
      "PwC actively involved in decisions that affect them",
      "Continuous insight into progress & planning",
      "Timely notice of anything impacting operations",
      "PwC feels the project is fully under control"]),
    ("WE ORGANIZE THE\nSUSTAINABILITY WORKS", CW_DARK,
     ["Translate M3E's design into deliverable scope",
      "Run the tender & select the contractor",
      "Direct and supervise the site",
      "Drive the programme to Paris Proof",
      "Own budget, quality, planning & risk"]),
    ("WE KEEP YOU IN\nCONTROL FROM AFAR", CW_RED,
     ["One contact, one monthly report",
      "Every key decision prepared in advance",
      "Full transparency on cost & progress",
      "Clear escalation lines to Corum",
      "No surprises — ever"]),
]
for i, (t, c, pts) in enumerate(cols):
    x = Inches(0.45) + i * Inches(4.18)
    box(s, x, Inches(1.85), Inches(4.0), Inches(4.4), fill=WHITE)
    hd = box(s, x, Inches(1.85), Inches(4.0), Inches(1.0), fill=c, dashed=False)
    txt(s, x + Inches(0.15), Inches(1.98), Inches(3.7), Inches(0.85), t,
        size=13, color=WHITE, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    body = "\n".join("•  " + p for p in pts)
    txt(s, x + Inches(0.2), Inches(3.05), Inches(3.6), Inches(3.1), body, size=11, space=8)
txt(s, Inches(0.45), Inches(6.45), Inches(11.5), Inches(0.4),
    "Corum keeps the decisions that matter. We deliver the works and keep PwC fully aware and aligned — so nothing ever lands on Corum by surprise.",
    size=11, bold=True, italic=True)

# ================================================ 8 UNDERSTANDING / STAKEHOLDERS
s = slide()
header(s, "01 — The case for action  ·  The playing field",
       "You already sit at the centre of four parties — we become\nthe hub that connects them", 8)
box(s, Inches(0.45), Inches(1.95), Inches(4.6), Inches(4.4), fill=LIGHT)
txt(s, Inches(0.6), Inches(2.1), Inches(4.3), Inches(0.4), "THE PARTIES", size=12, color=CW_RED, bold=True)
parties = [
    ("CORUM A.M.", "Owner / investor — sets objectives, holds the budget, makes the decisions."),
    ("PwC", "Tenant — must keep operating; their experience defines success."),
    ("M3E", "Technical advisor — develops the climate-system design (two scenarios)."),
    ("CONTRACTOR", "Executes the works — selected and managed through the tender."),
]
for i, (k, v) in enumerate(parties):
    y = Inches(2.55) + i * Inches(0.92)
    txt(s, Inches(0.6), y, Inches(1.7), Inches(0.85), k, size=11, color=CW_DARK, bold=True)
    txt(s, Inches(2.3), y, Inches(2.6), Inches(0.85), v, size=9.5)
box(s, Inches(5.3), Inches(1.95), Inches(7.55), Inches(4.4), fill=WHITE)
txt(s, Inches(5.45), Inches(2.1), Inches(7.2), Inches(0.4),
    "C&W AS THE HUB", size=12, color=CW_RED, bold=True, align=PP_ALIGN.CENTER)
nodes = [
    ("CORUM", 8.35, 2.65, LIGHT),
    ("PwC", 6.0, 3.9, LIGHT),
    ("M3E", 8.35, 5.35, LIGHT),
    ("CONTRACTOR", 10.7, 3.9, LIGHT),
    ("C&W\nSingle point\nof control", 8.35, 3.85, CW_RED),
]
for t, x, y, c in nodes:
    b = box(s, Inches(x), Inches(y), Inches(1.75), Inches(0.95), fill=c, dashed=(c != CW_RED))
    txt(s, Inches(x), Inches(y) + Inches(0.12), Inches(1.75), Inches(0.75), t,
        size=10, color=WHITE if c == CW_RED else CW_DARK, bold=True, align=PP_ALIGN.CENTER)
label(s, Inches(5.45), Inches(6.0), Inches(7), "wireframe: verbindingslijnen van C&W naar alle knopen in design uitwerken")

# ================================================ 9 TWO ROUTES
s = slide()
header(s, "02 — What we take off your plate  ·  The technique",
       "Two technical routes to Paris Proof — we make the choice\ndecision-ready for you", 9)
txt(s, Inches(0.45), Inches(1.75), Inches(12.2), Inches(0.35),
    "Based on M3E's scenario notes (9 Feb 2026). Our job is not to design — it is to turn this choice into a clear, costed, de-risked decision.",
    size=10.5, color=GREY, italic=True)
cols = [
    ("PREFERRED — LT-WKO + CLIMATE CEILINGS", CW_RED,
     ["Full replacement of the gas installation",
      "Low-temperature thermal storage (WKO): warm & cold source",
      "Energy plant in the basement (heat pumps, buffers)",
      "Climate ceilings + new VAV (no induction) per floor",
      "New integral controls; energy metering per floor",
      "Phased floor-by-floor — building stays in use",
      "Future-proof: one intervention, done"]),
    ("ALTERNATIVE — AIR-WATER HP + VRF + RETAINED VAV", CW_DARK,
     ["Air-water heat pump for base heating (roof)",
      "Existing VAV induction units retained",
      "VRF system with convectors for zone control per floor",
      "New DX block replaces outdated cooling",
      "Fewer interventions on the office floors",
      "Hybrid system — careful controls integration needed",
      "Residual VAV life ± 6–9 yrs → a second intervention later"]),
]
for i, (t, c, pts) in enumerate(cols):
    x = Inches(0.45) + i * Inches(6.35)
    box(s, x, Inches(2.2), Inches(6.1), Inches(3.6), fill=WHITE)
    hd = box(s, x, Inches(2.2), Inches(6.1), Inches(0.55), fill=c, dashed=False)
    txt(s, x + Inches(0.12), Inches(2.29), Inches(5.85), Inches(0.4), t,
        size=10.5, color=WHITE, bold=True)
    txt(s, x + Inches(0.2), Inches(2.9), Inches(5.7), Inches(2.8),
        "\n".join("•  " + p for p in pts), size=10.5, space=3)
box(s, Inches(0.45), Inches(5.95), Inches(12.4), Inches(0.85), fill=LIGHT)
txt(s, Inches(0.6), Inches(6.05), Inches(12.1), Inches(0.7),
    "C&W's role: benchmark both routes on cost, disruption to PwC and long-term asset value — then bring Corum a single, "
    "recommended decision. Our management approach is robust for either scenario: phased, floor-by-floor, tenant-first.",
    size=11, bold=True)

# ================================================ 10 MANAGE PwC (DEEP DIVE)
s = slide()
header(s, "02 — What we take off your plate  ·  Deep dive 1 of 2",
       "We deliver the works with PwC fully aware and aligned —\nso your tenant stays confident and your lease stays intact", 10)
txt(s, Inches(0.45), Inches(1.85), Inches(12.3), Inches(0.8),
    "From day one, PwC deals with one familiar C&W face. We keep the tenant actively involved in the decisions "
    "that affect them, with continuous insight into progress and planning and timely notice of anything that "
    "touches their operations. The outcome, in Corum's own words: PwC experiences full confidence that the project is under control.",
    size=11.5)
blocks = [
    ("ONE FAMILIAR INTERFACE",
     "The Stakeholder Management PM owns the PwC relationship end-to-end — one consistent, familiar "
     "point of contact for everything that touches the tenant."),
    ("ACTIVELY INVOLVED IN DECISIONS",
     "PwC is actively involved in the decision-making process on matters that affect them — briefed "
     "early, aligned before we act, never presented with a fait accompli."),
    ("CONTINUOUS INSIGHT & TIMELY NOTICE",
     "Continuous insight into progress and planning, and timely communication of any change that impacts "
     "business operations — noise, access and disruption kept inside agreed windows."),
    ("FULL CONFIDENCE, PROTECTED VALUE",
     "The outcome Corum asked for: PwC experiences full confidence that the project is under control. A "
     "confident tenant renews — protecting lease retention, income and exit value."),
]
for i, (t, d) in enumerate(blocks):
    x = Inches(0.45) + (i % 2) * Inches(6.35)
    y = Inches(3.05) + (i // 2) * Inches(1.75)
    box(s, x, y, Inches(6.1), Inches(1.55), fill=WHITE)
    txt(s, x + Inches(0.18), y + Inches(0.12), Inches(5.7), Inches(0.4), t,
        size=12, color=CW_RED, bold=True)
    txt(s, x + Inches(0.18), y + Inches(0.6), Inches(5.75), Inches(0.9), d, size=10.5)

# ================================================ 11 ORGANIZE WORKS (DEEP DIVE)
s = slide()
header(s, "02 — What we take off your plate  ·  Deep dive 2 of 2",
       "We organize the sustainability works — from M3E's design\nto a building that is Paris Proof", 11)
txt(s, Inches(0.45), Inches(1.85), Inches(12.3), Inches(0.8),
    "C&W is the orchestrator of the transformation. We take M3E's technical concept and turn it into a scope that "
    "can be tendered, contracted, built and commissioned — floor-by-floor, on budget, to the Paris Proof standard. "
    "Corum gets a finished, verified building; not a construction site to supervise.",
    size=11.5)
steps = [
    ("1", "SCOPE", "Translate M3E's chosen scenario into a clear, tenderable scope of work."),
    ("2", "TENDER", "Run a structured tender; select the contractor on price, quality and risk."),
    ("3", "BUILD", "Direct and supervise the site; phased, floor-by-floor, tenant-first."),
    ("4", "COMMISSION", "Test, commission and verify each floor before handing it back in use."),
    ("5", "PARIS PROOF", "Deliver the verified, Paris Proof building and a documented handover."),
]
w = Inches(2.4); x0 = Inches(0.45)
for i, (n, t, d) in enumerate(steps):
    x = x0 + i * (w + Inches(0.05))
    box(s, x, Inches(3.0), w, Inches(2.9), fill=WHITE)
    hd = box(s, x, Inches(3.0), w, Inches(0.65), fill=CW_RED if i in (0, 4) else CW_DARK, dashed=False)
    txt(s, x + Inches(0.12), Inches(3.08), w - Inches(0.2), Inches(0.5),
        f"{n}  {t}", size=11, color=WHITE, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, x + Inches(0.15), Inches(3.85), w - Inches(0.3), Inches(1.9), d, size=10.5)
    if i < 4:
        ar = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, x + w - Inches(0.02),
                                Inches(4.15), Inches(0.22), Inches(0.28))
        ar.fill.solid(); ar.fill.fore_color.rgb = CW_RED
        ar.line.fill.background(); ar.shadow.inherit = False
txt(s, Inches(0.45), Inches(6.1), Inches(12), Inches(0.7),
    "One accountable owner across all five steps. Corum never has to stitch together advisors, contractors and inspectors — that is our job.",
    size=11, bold=True, italic=True)

# ================================================ 12 SUCCESS FACTORS
s = slide()
header(s, "02 — What we take off your plate  ·  What makes it work",
       "Four principles turn a risky rebuild into a controlled programme", 12)
tiles = [
    ("TENANT SATISFACTION FIRST",
     "The tenant experience is the lead indicator of success. Everything — sequencing, timing, "
     "communication — is designed around keeping PwC operational and confident. The lesson from "
     "Rotterdam is built into how we work."),
    ("PHASED DELIVERY IN A LIVE BUILDING",
     "Floor-by-floor execution: one zone temporarily out of use, tested and handed back before the "
     "next begins. The building keeps running; the programme keeps moving."),
    ("CLEAR GOVERNANCE & DECISION RIGHTS",
     "Everyone knows who decides what, and when. PwC is involved where it matters, Corum decides the "
     "big calls, C&W runs the rest — with clean escalation lines."),
    ("NO SURPRISES",
     "A live Risk Register from day one and decisions prepared in advance. Corum hears about issues "
     "as early intelligence, with an option to decide — never as a problem after the fact."),
]
for i, (t, d) in enumerate(tiles):
    x = Inches(0.45) + (i % 2) * Inches(6.35)
    y = Inches(1.85) + (i // 2) * Inches(2.35)
    box(s, x, y, Inches(6.1), Inches(2.1), fill=WHITE)
    txt(s, x + Inches(0.18), y + Inches(0.15), Inches(5.7), Inches(0.5), t,
        size=13, color=CW_RED, bold=True)
    txt(s, x + Inches(0.18), y + Inches(0.75), Inches(5.75), Inches(1.25), d, size=10.5)

# ================================================ 13 THE JOURNEY (chronology)
s = slide()
header(s, "03 — The journey",
       "From today to Paris Proof: the story of the next few years,\non one line", 13)
milestones = [
    ("TODAY", "Jul 2026", "NDA signed, mandate confirmed. C&W becomes Corum's single point of control."),
    ("MOBILISE", "Q3 2026", "Preparatory phase: stakeholders mapped, PwC engaged, project organisation stood up."),
    ("DECIDE", "Q4 2026", "M3E scenario chosen with C&W's decision-ready recommendation; scope fixed."),
    ("TENDER", "Q1–Q2 2027", "Contractor selected on price, quality and risk. Works contracted."),
    ("BUILD", "2027–2029", "Floor-by-floor execution in the live building. PwC operational throughout."),
    ("PARIS PROOF", "target", "Verified handover. Asset compliant, tenant retained, value protected."),
]
n = len(milestones)
x0 = Inches(0.6); span = Inches(12.1)
line = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x0, Inches(3.35), span, Inches(0.06))
line.fill.solid(); line.fill.fore_color.rgb = CW_RED; line.line.fill.background(); line.shadow.inherit = False
step = Emu(int(span) // n)
for i, (t, when, d) in enumerate(milestones):
    cx = x0 + Emu(int(step) * i) + Emu(int(step)//2)
    dia = s.shapes.add_shape(MSO_SHAPE.DIAMOND, cx - Inches(0.16), Inches(3.22),
                             Inches(0.32), Inches(0.32))
    dia.fill.solid(); dia.fill.fore_color.rgb = CW_RED if i in (0, n-1) else CW_DARK
    dia.line.color.rgb = WHITE; dia.shadow.inherit = False
    bx = cx - Emu(int(step)//2) + Inches(0.1)
    bw = step - Inches(0.2)
    up = (i % 2 == 0)
    ty = Inches(1.75) if up else Inches(3.95)
    txt(s, bx, ty, bw, Inches(0.3), t, size=11, color=CW_RED, bold=True, align=PP_ALIGN.CENTER)
    txt(s, bx, ty + Inches(0.28), bw, Inches(0.25), when, size=9, color=GREY,
        bold=True, align=PP_ALIGN.CENTER)
    txt(s, bx, ty + Inches(0.55), bw, Inches(1.1), d, size=9, align=PP_ALIGN.CENTER)
label(s, Inches(0.45), Inches(6.55), Inches(11),
      "wireframe: tijdlijn indicatief — jaartallen te valideren met M3E-ontwerpplanning, Paris Proof-deadline en Corum–PwC afspraken")

# ================================================ 14 PHASED ENGAGEMENT
s = slide()
header(s, "03 — The journey  ·  Engagement model",
       "You commit in steps: start small, then scale with confidence", 14)
phases = [
    ("PHASE 0", "PREPARATORY ASSIGNMENT",
     "A limited, low-commitment start: map all stakeholders, set up the project organisation, gather "
     "M3E's input, capture PwC's requirements. Deliverable: one integral project plan you can rely on.", True),
    ("PHASE 1", "PM PREPARATION",
     "Guide the technical design to a fixed scope, prepare the tender documents, run the tender and "
     "select the contractor.", False),
    ("PHASE 2", "PM EXECUTION",
     "Direct and supervise the works: floor-by-floor phasing, tenant communication, and control of "
     "budget, quality, planning and risk.", False),
    ("PHASE 3", "BUILDING CONSULTANCY",
     "Independent quality inspections during construction — an extra pair of expert eyes protecting "
     "Corum's interest on site.", False),
]
w = Inches(2.95); x0 = Inches(0.45)
for i, (n, t, d, hl) in enumerate(phases):
    x = x0 + i * (w + Inches(0.15))
    box(s, x, Inches(1.95), w, Inches(3.55), fill=WHITE)
    hd = box(s, x, Inches(1.95), w, Inches(0.8), fill=CW_RED if hl else CW_DARK, dashed=False)
    txt(s, x + Inches(0.12), Inches(2.03), w - Inches(0.2), Inches(0.3), n,
        size=10, color=WHITE, bold=True)
    txt(s, x + Inches(0.12), Inches(2.3), w - Inches(0.2), Inches(0.45), t,
        size=11, color=WHITE, bold=True)
    txt(s, x + Inches(0.15), Inches(2.95), w - Inches(0.3), Inches(2.45), d, size=10)
    if i < 3:
        ar = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, x + w - Inches(0.02),
                                Inches(3.45), Inches(0.26), Inches(0.3))
        ar.fill.solid(); ar.fill.fore_color.rgb = CW_RED
        ar.line.fill.background(); ar.shadow.inherit = False
box(s, Inches(0.45), Inches(5.75), Inches(12.4), Inches(1.0), fill=LIGHT)
txt(s, Inches(0.65), Inches(5.9), Inches(12), Inches(0.75),
    "Each phase is a separate assignment with its own scope, deliverables and fee. You are never asked to commit to "
    "the whole programme up front — you decide, phase by phase, on the strength of what we have delivered.",
    size=11.5, bold=True)

# ================================================ 15 PROCESS PLANNING (GANTT)
s = slide()
header(s, "03 — The journey  ·  Planning",
       "The programme on a page — indicative, and ours to defend", 15)
quarters = ["Q3 2026", "Q4 2026", "Q1 2027", "Q2 2027", "Q3 2027", "Q4 2027", "2028", "2029"]
gx0 = Inches(3.5); gw = Inches(9.3)
colw = Emu(int(gw) // len(quarters))
for i, q in enumerate(quarters):
    txt(s, gx0 + Emu(int(colw)*i), Inches(1.8), colw, Inches(0.3), q,
        size=8.5, color=GREY, align=PP_ALIGN.CENTER)
rows = [
    ("NDA · mandate · award Phase 0", 0.0, 0.6, True),
    ("Phase 0 — preparatory → project plan", 0.25, 1.0, False),
    ("Scenario decision (M3E + C&W)", 1.4, 0.4, True),
    ("Technical design guided to fixed scope", 1.0, 1.6, False),
    ("Tender & contractor selection", 2.2, 1.6, False),
    ("Contracting", 3.6, 0.4, True),
    ("Execution — floor-by-floor (PM + inspections)", 3.9, 3.4, False),
    ("Commissioning & Paris Proof handover", 7.1, 0.7, True),
    ("Aftercare & fine-tuning", 7.6, 0.4, False),
]
for i, (name, start, dur, milestone) in enumerate(rows):
    y = Inches(2.2) + i * Inches(0.5)
    txt(s, Inches(0.45), y, Inches(3.0), Inches(0.45), name, size=9)
    bx = gx0 + Emu(int(int(colw) * start))
    bw = Emu(int(int(colw) * dur))
    b = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx, y + Inches(0.03),
                           bw, Inches(0.3))
    b.fill.solid(); b.fill.fore_color.rgb = CW_RED if milestone else MID
    b.line.fill.background(); b.shadow.inherit = False
box(s, Inches(0.45), Inches(6.55), Inches(4.5), Inches(0.45), fill=LIGHT)
txt(s, Inches(0.55), Inches(6.62), Inches(4.3), Inches(0.35),
    "■ red = decision / milestone owned by C&W", size=9, color=CW_DARK)
label(s, Inches(5.2), Inches(6.62), Inches(7.5),
      "indicatief — te valideren met M3E-ontwerpplanning, Paris Proof-deadline en Corum–PwC afspraken")

# ================================================ 16 TWO-PM ORGANISATION
s = slide()
header(s, "04 — How we stay in control  ·  Organisation",
       "Two project managers cover both sides of this project:\nthe diplomatic and the technical", 16)
def orgbox(x, y, w, h, t, red=False):
    b = box(s, Inches(x), Inches(y), Inches(w), Inches(h),
            fill=CW_RED if red else WHITE, dashed=False, line=CW_RED if red else GREY)
    txt(s, Inches(x), Inches(y) + Inches(0.1), Inches(w), Inches(h) - Inches(0.15),
        t, size=10, color=WHITE if red else CW_DARK, bold=True, align=PP_ALIGN.CENTER,
        anchor=MSO_ANCHOR.MIDDLE)
orgbox(5.2, 1.85, 2.9, 0.7, "CORUM A.M.\nClient / Owner — decides")
orgbox(9.4, 1.85, 3.0, 0.7, "PwC\nTenant — kept operational & involved")
orgbox(3.35, 3.0, 3.1, 1.1, "STAKEHOLDER MANAGEMENT PM\nOwns the PwC relationship:\ncommunication · expectations · decisions", red=True)
orgbox(6.85, 3.0, 3.1, 1.1, "TECHNICAL PM\nOwns the works:\ntechnical coordination · site management ·\nM3E alignment · tender & execution", red=True)
orgbox(3.35, 4.7, 3.1, 0.8, "M3E\nTechnical advisor / installation design")
orgbox(6.85, 4.7, 3.1, 0.8, "CONTRACTOR\nSelected & managed via tender")
label(s, Inches(3.35), Inches(5.65), Inches(8),
      "wireframe: verbindingslijnen + eventueel cost management / inspecties toevoegen in design")
box(s, Inches(0.45), Inches(6.05), Inches(12.4), Inches(0.9), fill=LIGHT)
txt(s, Inches(0.65), Inches(6.18), Inches(12), Inches(0.7),
    "One PM guards the relationship and the tenant experience; one guards the technique and the site. Together they are "
    "your single point of control — nothing falls between the diplomatic and the technical.", size=11.5, bold=True)

# ================================================ 17 GOVERNANCE & DECISION RIGHTS
s = slide()
header(s, "04 — How we stay in control  ·  Governance",
       "Clear decision rights: you decide the big calls, we run\neverything around them", 17)
rows = [
    ("Strategic & budget decisions", "DECIDE", "recommend", "consult", "CORUM"),
    ("Scenario / design choice", "DECIDE", "recommend & prepare", "input", "CORUM"),
    ("Tenant communication & impact", "informed", "MANAGE", "involved", "C&W"),
    ("Contractor selection", "approve", "run & recommend", "—", "C&W→Corum"),
    ("Day-to-day site & works", "informed", "DIRECT", "execute", "C&W"),
    ("Risk & escalation", "escalation point", "OWN & flag early", "—", "C&W→Corum"),
]
hdr = ["DECISION AREA", "CORUM", "C&W", "PwC / M3E", "SITS WITH"]
wds = [4.0, 2.2, 2.9, 2.0, 1.4]
x = Inches(0.45); y0 = Inches(1.95)
cx = x
for j, h in enumerate(hdr):
    box(s, cx, y0, Inches(wds[j]), Inches(0.45), fill=CW_DARK, dashed=False)
    txt(s, cx + Inches(0.08), y0 + Inches(0.07), Inches(wds[j]) - Inches(0.15), Inches(0.35),
        h, size=9.5, color=WHITE, bold=True)
    cx += Inches(wds[j])
for i, row in enumerate(rows):
    cy = y0 + Inches(0.45) + i * Inches(0.6)
    cx = x
    for j, cell in enumerate(row):
        emph = cell.isupper() and cell not in ("—",)
        box(s, cx, cy, Inches(wds[j]), Inches(0.6), fill=WHITE if i % 2 == 0 else LIGHT)
        txt(s, cx + Inches(0.08), cy + Inches(0.06), Inches(wds[j]) - Inches(0.15), Inches(0.5),
            cell, size=9, color=CW_RED if emph and j in (1, 2) else CW_DARK,
            bold=emph, anchor=MSO_ANCHOR.MIDDLE)
        cx += Inches(wds[j])
txt(s, Inches(0.45), Inches(5.75), Inches(12), Inches(0.5),
    "The full project team is personally introduced to all parties at the outset — so every name has a face from day one.",
    size=10.5, italic=True)
label(s, Inches(0.45), Inches(6.3), Inches(11), "wireframe: RACI-achtige matrix — definitief af te stemmen met Corum")

# ================================================ 18 REPORTING FROM A DISTANCE
s = slide()
header(s, "04 — How we stay in control  ·  Reporting",
       "You stay fully in control from Paris — on one page a month", 18)
txt(s, Inches(0.45), Inches(1.9), Inches(5.4), Inches(4.4),
    "Corum steers the asset from a distance. Our reporting is built for exactly that: one concise "
    "monthly report that tells you everything you need — and nothing you don't.\n\n"
    "Every report answers four questions:\n\n"
    "•  Are we on schedule?\n"
    "•  Are we on budget?\n"
    "•  Is PwC satisfied?\n"
    "•  What decisions do you need to make next?\n\n"
    "Detail sits in the appendix. Decisions come to you already prepared, with a recommendation.",
    size=11.5, space=3)
box(s, Inches(6.1), Inches(1.9), Inches(6.75), Inches(4.5), fill=WHITE)
txt(s, Inches(6.3), Inches(2.05), Inches(6.4), Inches(0.4),
    "MONTHLY ONE-PAGE REPORT  [ dashboard mock-up ]", size=11, color=CW_RED, bold=True)
tiles = [("SCHEDULE", "on track / at risk"), ("BUDGET", "forecast vs. fixed"),
         ("TENANT (PwC)", "satisfaction & issues"), ("RISK", "top items · RAG"),
         ("DECISIONS DUE", "prepared for Corum"), ("PROGRESS", "floors complete")]
for i, (t, d) in enumerate(tiles):
    x = Inches(6.3) + (i % 3) * Inches(2.15)
    y = Inches(2.6) + (i // 3) * Inches(1.7)
    box(s, x, y, Inches(2.0), Inches(1.5), fill=LIGHT)
    txt(s, x + Inches(0.12), y + Inches(0.12), Inches(1.8), Inches(0.4), t,
        size=10, color=CW_DARK, bold=True)
    txt(s, x + Inches(0.12), y + Inches(0.55), Inches(1.8), Inches(0.5), d, size=9, color=GREY)
    txt(s, x + Inches(0.12), y + Inches(1.05), Inches(1.8), Inches(0.35), "[ ● ]",
        size=12, color=CW_RED, bold=True)

# ================================================ 19 RISK MANAGEMENT
s = slide()
header(s, "04 — How we stay in control  ·  Risk",
       "We manage risk as asset-value protection — not as paperwork", 19)
txt(s, Inches(0.45), Inches(1.75), Inches(12.3), Inches(0.55),
    "A live Risk Register from day one: risks identified early, ownership assigned, mitigation agreed. Each risk is "
    "framed by what it threatens — the tenant, the budget or the deadline — the three things that drive Corum's return.",
    size=11)
hdr = ["#", "RISK", "THREATENS", "MITIGATION", "OWNER", "RAG"]
wds = [0.5, 3.7, 1.5, 4.6, 1.1, 0.7]
risks = [
    ("1", "Tenant disturbance / PwC dissatisfaction", "Tenancy", "Floor-by-floor phasing, tenant comms plan, agreed working windows", "SPM", "●"),
    ("2", "Phasing conflicts between floors in a live building", "Deadline", "Integral phasing plan, buffer per floor, weekly look-ahead", "TPM", "●"),
    ("3", "WKO permits & source-drilling lead time (preferred)", "Deadline", "Early permit inventory & plan; applications started in Phase 1", "TPM", "●"),
    ("4", "Tender result exceeds fixed budget", "Budget", "Cost estimates at design milestones, VE options, market sounding", "TPM", "●"),
    ("5", "Controls / systems integration (esp. hybrid alt.)", "Budget", "Commissioning plan, integral controls party, test per floor", "TPM", "●"),
    ("6", "Slow owner/tenant decision-making", "Deadline", "Decision calendar; every decision prepared in advance by C&W", "SPM", "●"),
]
x = Inches(0.45); y0 = Inches(2.4)
cx = x
for j, h in enumerate(hdr):
    box(s, cx, y0, Inches(wds[j]), Inches(0.4), fill=CW_DARK, dashed=False)
    txt(s, cx + Inches(0.05), y0 + Inches(0.05), Inches(wds[j]) - Inches(0.1), Inches(0.3),
        h, size=9, color=WHITE, bold=True)
    cx += Inches(wds[j])
rag_colors = [AMBER, CW_RED, CW_RED, AMBER, AMBER, AMBER]
for i, row in enumerate(risks):
    cy = y0 + Inches(0.4) + i * Inches(0.56)
    cx = x
    for j, cell in enumerate(row):
        box(s, cx, cy, Inches(wds[j]), Inches(0.56), fill=WHITE if i % 2 == 0 else LIGHT)
        txt(s, cx + Inches(0.05), cy + Inches(0.04), Inches(wds[j]) - Inches(0.1), Inches(0.5),
            cell, size=8.5, color=rag_colors[i] if j == 5 else (CW_RED if j == 2 else CW_DARK),
            bold=(j == 5 or j == 2), anchor=MSO_ANCHOR.MIDDLE)
        cx += Inches(wds[j])
label(s, Inches(0.45), Inches(6.5), Inches(11),
      "wireframe: voorbeeldrisico's — definitief register in fase 0; RAG rood/amber/groen in design")

# ================================================ 20 WHY C&W
s = slide()
header(s, "05 — Why C&W, team & track record",
       "Why Cushman & Wakefield — not a local project-management firm", 20)
reasons = [
    ("WE SPEAK INVESTOR",
     "As a global real estate adviser, we understand Corum's world: returns, lease value, exit. We "
     "manage the project in the language of asset value, not just square metres."),
    ("WE MANAGE CORPORATE OCCUPIERS",
     "Managing demanding corporate tenants like PwC is core C&W business. We know how to keep a blue-chip "
     "occupier confident through disruptive works."),
    ("WE ARE ONE INTEGRATED PARTNER",
     "Project & Development Services, cost management, building consultancy and market knowledge under "
     "one roof — one accountable partner, not a chain of sub-advisers."),
    ("WE ARE LOCAL, FOR A REMOTE OWNER",
     "Feet on the ground in the Netherlands, reporting to an owner abroad. We are your eyes, ears and "
     "hands in Amsterdam — exactly the gap Corum needs filled."),
]
for i, (t, d) in enumerate(reasons):
    x = Inches(0.45) + (i % 2) * Inches(6.35)
    y = Inches(1.9) + (i // 2) * Inches(2.3)
    box(s, x, y, Inches(6.1), Inches(2.05), fill=WHITE)
    txt(s, x + Inches(0.18), y + Inches(0.15), Inches(5.7), Inches(0.5), t,
        size=13, color=CW_RED, bold=True)
    txt(s, x + Inches(0.18), y + Inches(0.7), Inches(5.75), Inches(1.25), d, size=11)

# ================================================ 21 TEAM (WIT)
s = slide()
txt(s, Inches(0.45), Inches(0.25), Inches(9), Inches(0.3),
    "05 — TEAM", size=10, color=MID, bold=True)
txt(s, Inches(0), Inches(3.3), SW, Inches(0.5),
    "[ TEAMPAGINA — BEWUST LEEG GELATEN / IN TE VULLEN ]",
    size=12, color=MID, align=PP_ALIGN.CENTER, italic=True)
txt(s, Inches(12.55), Inches(7.05), Inches(0.55), Inches(0.3), "21",
    size=10, color=MID, align=PP_ALIGN.RIGHT)

# ================================================ 22 TRACK RECORD
s = slide()
header(s, "05 — Why C&W, team & track record",
       "We have done exactly this: sustainability upgrades in\noccupied, blue-chip buildings", 22)
for i in range(4):
    x = Inches(0.45) + i * Inches(3.15)
    box(s, x, Inches(1.95), Inches(2.95), Inches(4.3))
    box(s, x + Inches(0.1), Inches(2.05), Inches(2.75), Inches(1.5), fill=MID)
    txt(s, x + Inches(0.1), Inches(2.6), Inches(2.75), Inches(0.4), "[FOTO]",
        size=10, color=GREY, align=PP_ALIGN.CENTER)
    txt(s, x + Inches(0.15), Inches(3.7), Inches(2.65), Inches(0.4),
        f"REFERENCE {i+1}", size=11, color=CW_RED, bold=True)
    txt(s, x + Inches(0.15), Inches(4.1), Inches(2.65), Inches(2.0),
        "Project name\nSustainability upgrade / renovation in an occupied office\n"
        "Size · C&W role · outcome (tenant retained, on time, on budget)\n[ in te vullen ]",
        size=9, color=GREY)
label(s, Inches(0.45), Inches(6.45), Inches(11.5),
      "selectiecriteria: verduurzaming/renovatie in gebruik zijnd kantoor · institutionele eigenaar · veeleisende huurder behouden")

# ================================================ 23 FEE
s = slide()
header(s, "06 — Commercials & the decision  ·  Fee",
       "A fee structured as a phased investment — low to start,\nearned as we deliver", 23)
fee_rows = [
    ("PHASE 0 — Preparatory assignment", "Lump sum", "€ [ • ]"),
    ("PHASE 1 — PM Preparation", "Fixed fee / monthly rate", "€ [ • ]"),
    ("PHASE 2 — PM Execution", "Fixed fee / monthly rate", "€ [ • ]"),
    ("PHASE 3 — Building Consultancy (inspections)", "Unit rate per inspection", "€ [ • ]"),
]
y0 = Inches(1.95)
for i, (a, b_, c) in enumerate(fee_rows):
    y = y0 + i * Inches(0.72)
    box(s, Inches(0.45), y, Inches(7.6), Inches(0.6), fill=WHITE if i % 2 == 0 else LIGHT)
    txt(s, Inches(0.6), y + Inches(0.08), Inches(4.6), Inches(0.45), a, size=10.5, bold=True,
        anchor=MSO_ANCHOR.MIDDLE)
    txt(s, Inches(5.3), y + Inches(0.08), Inches(1.7), Inches(0.45), b_, size=9.5,
        anchor=MSO_ANCHOR.MIDDLE)
    txt(s, Inches(7.0), y + Inches(0.08), Inches(1.0), Inches(0.45), c, size=10.5,
        color=CW_RED, bold=True, anchor=MSO_ANCHOR.MIDDLE)
box(s, Inches(8.3), Inches(1.95), Inches(4.55), Inches(2.9), fill=LIGHT)
txt(s, Inches(8.5), Inches(2.1), Inches(4.2), Inches(0.35),
    "RATE CARD (REFERENCE)", size=11, color=CW_RED, bold=True)
txt(s, Inches(8.5), Inches(2.5), Inches(4.2), Inches(2.3),
    "Senior Project Manager   € 145 / hr\nProject Manager             € 135 / hr\n"
    "Technical PM                 € 135 / hr\nCost Manager                € 125 / hr\n"
    "Site Manager                 € 120 / hr\n\n[ tarieven & inzet definitief met Frank ]",
    size=10, space=2)
box(s, Inches(0.45), Inches(5.0), Inches(12.4), Inches(1.6), fill=WHITE)
txt(s, Inches(0.65), Inches(5.12), Inches(12), Inches(0.35),
    "WHY THIS STRUCTURE WORKS FOR CORUM", size=11, color=CW_RED, bold=True)
txt(s, Inches(0.65), Inches(5.5), Inches(12), Inches(1.05),
    "•  You commit phase by phase — the Phase 0 fee is small relative to the asset and the Paris Proof exposure it protects\n"
    "•  Design, calculations and specifications are by M3E (outside C&W scope)  ·  DNR 2011 applicable\n"
    "•  [ verdere uitgangspunten & exclusies in te vullen met Frank ]", size=10, space=2)

# ================================================ 24 2030 VISION + NEXT STEPS
s = slide()
box(s, 0, 0, SW, Inches(3.05), fill=CW_DARK, line=CW_DARK, dashed=False)
bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.18), SH)
bar.fill.solid(); bar.fill.fore_color.rgb = CW_RED; bar.line.fill.background(); bar.shadow.inherit = False
txt(s, Inches(0.6), Inches(0.5), Inches(11), Inches(0.35),
    "06 — THE DECISION", size=11, color=CW_RED, bold=True)
txt(s, Inches(0.6), Inches(0.95), Inches(12), Inches(0.7),
    "Picture Westgate I in 2030", size=28, color=WHITE, bold=True)
txt(s, Inches(0.6), Inches(1.75), Inches(12), Inches(1.1),
    "A Paris Proof building. PwC still in place, still confident, lease renewed. An asset whose value is "
    "protected and whose compliance is proven — delivered without Corum ever having to manage a Dutch "
    "building site or a tenant dispute. That is what a single point of control buys you.",
    size=13, color=WHITE)
txt(s, Inches(0.45), Inches(3.3), Inches(6), Inches(0.4),
    "THE DECISION WE ASK YOU TO MAKE NOW", size=12, color=CW_RED, bold=True)
steps = [
    ("1", "Confirm the NDA (via Dentons)", "in progress"),
    ("2", "Share the Corum–PwC agreement & Corum–M3E arrangement", "upon NDA"),
    ("3", "Award Phase 0 — the preparatory assignment", "July 2026"),
    ("4", "Kick-off & personal introduction of the full team", "within 2 weeks"),
    ("5", "Integral project plan → decide on Phases 1–3", "end of Phase 0"),
]
for i, (n, t, w_) in enumerate(steps):
    y = Inches(3.8) + i * Inches(0.56)
    c = box(s, Inches(0.45), y, Inches(0.45), Inches(0.45), fill=CW_RED, dashed=False)
    txt(s, Inches(0.45), y + Inches(0.05), Inches(0.45), Inches(0.35), n,
        size=12, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    txt(s, Inches(1.05), y + Inches(0.03), Inches(8.4), Inches(0.5), t, size=11.5,
        anchor=MSO_ANCHOR.MIDDLE)
    txt(s, Inches(9.55), y + Inches(0.03), Inches(3.2), Inches(0.5), w_, size=9.5,
        color=GREY, italic=True, anchor=MSO_ANCHOR.MIDDLE)
box(s, Inches(0.45), Inches(6.65), Inches(12.4), Inches(0.62), fill=CW_RED, dashed=False)
txt(s, Inches(0.7), Inches(6.75), Inches(12), Inches(0.45),
    "Sjoerd Bezemer  ·  +31 (0)6 128 485 42  ·  sjoerd.bezemer@cushwake.com      |      Frank Okker — Head of PDS Netherlands",
    size=11.5, color=WHITE, bold=True)

prs.save("corum-pitch/Corum-Westgate-I-Pitch-Wireframe.pptx")
print("OK:", len(prs.slides._sldIdLst), "slides")
