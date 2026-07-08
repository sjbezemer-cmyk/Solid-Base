#!/usr/bin/env python3
"""Wireframe-PPTX voor de Corum Westgate I 'Paris Proof' pitch.

Wireframe-stijl: witte slides, grijze placeholder-vlakken met stippellijn,
CW_RED accenten. Inhoud is richtinggevend; opmaak volgt in Claude Design.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

CW_RED = RGBColor(0xC3, 0x00, 0x2B)
CW_DARK = RGBColor(0x1C, 0x1C, 0x1C)
GREY = RGBColor(0x8A, 0x8A, 0x8A)
LIGHT = RGBColor(0xF2, 0xF2, 0xF2)
MID = RGBColor(0xD9, 0xD9, 0xD9)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

SW, SH = Inches(13.333), Inches(7.5)

prs = Presentation()
prs.slide_width = SW
prs.slide_height = SH
BLANK = prs.slide_layouts[6]


def slide():
    return prs.slides.add_slide(BLANK)


def box(s, x, y, w, h, fill=LIGHT, line=GREY, dashed=True):
    sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    sh.line.color.rgb = line
    sh.line.width = Pt(0.75)
    if dashed:
        ln = sh.line._get_or_add_ln()
        d = ln.makeelement(qn('a:prstDash'), {'val': 'dash'})
        ln.append(d)
    sh.shadow.inherit = False
    return sh


def txt(s, x, y, w, h, text, size=12, color=CW_DARK, bold=False,
        align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, italic=False):
    tb = s.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    lines = text.split("\n")
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        r = p.add_run()
        r.text = line
        f = r.font
        f.size = Pt(size)
        f.bold = bold
        f.italic = italic
        f.color.rgb = color
        f.name = "Arial"
    return tb


def label(s, x, y, w, text):
    """Klein grijs wireframe-annotatielabel."""
    txt(s, x, y, w, Inches(0.3), text, size=8, color=GREY, italic=True)


def header(s, section, title, num):
    bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.18), SH)
    bar.fill.solid(); bar.fill.fore_color.rgb = CW_RED
    bar.line.fill.background(); bar.shadow.inherit = False
    txt(s, Inches(0.45), Inches(0.25), Inches(9), Inches(0.3),
        section.upper(), size=10, color=CW_RED, bold=True)
    txt(s, Inches(0.45), Inches(0.5), Inches(11), Inches(0.7),
        title, size=26, color=CW_DARK, bold=True)
    txt(s, Inches(12.5), Inches(7.05), Inches(0.6), Inches(0.3),
        str(num), size=10, color=GREY, align=PP_ALIGN.RIGHT)
    txt(s, Inches(0.45), Inches(7.05), Inches(6), Inches(0.3),
        "CUSHMAN & WAKEFIELD  |  CORUM A.M.", size=8, color=GREY)


# ---------------------------------------------------------------- 1 COVER
s = slide()
img = box(s, 0, 0, SW, Inches(4.6), fill=MID)
txt(s, Inches(0.5), Inches(2.0), Inches(12.3), Inches(0.6),
    "[ FULL-BLEED FOTO WESTGATE I — Thomas R. Malthusstraat 5, Amsterdam ]",
    size=14, color=GREY, align=PP_ALIGN.CENTER)
bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(4.6), SW, Inches(0.12))
bar.fill.solid(); bar.fill.fore_color.rgb = CW_RED
bar.line.fill.background(); bar.shadow.inherit = False
txt(s, Inches(0.6), Inches(4.95), Inches(9), Inches(1.5),
    "WESTGATE I — PARIS PROOF", size=40, color=CW_DARK, bold=True)
txt(s, Inches(0.6), Inches(5.75), Inches(9), Inches(0.5),
    "Project Management Proposal", size=20, color=CW_RED)
txt(s, Inches(0.6), Inches(6.4), Inches(9), Inches(0.6),
    "Prepared for Corum A.M.  ·  July 2026", size=13, color=GREY)
box(s, Inches(10.9), Inches(5.6), Inches(1.9), Inches(1.0), fill=LIGHT)
txt(s, Inches(10.9), Inches(5.9), Inches(1.9), Inches(0.4), "[C&W LOGO]",
    size=10, color=GREY, align=PP_ALIGN.CENTER)

# ------------------------------------------------------------- 2 CONTENTS
s = slide()
header(s, "Contents", "CONTENTS", 2)
items = [
    ("01", "INTRODUCTION &\nUNDERSTANDING", "Cover letter, the project,\ntwo Paris Proof scenarios"),
    ("02", "OUR APPROACH", "Role, success factors,\nphased plan & planning"),
    ("03", "ORGANISATION &\nGOVERNANCE", "Two-PM model, governance,\nrisk management"),
    ("04", "TEAM &\nTRACK RECORD", "Team (t.b.d.),\nreferences"),
    ("05", "FEE &\nNEXT STEPS", "Fee structure per phase,\nnext steps"),
]
w = Inches(2.35); gap = Inches(0.15); x0 = Inches(0.55)
for i, (n, t, d) in enumerate(items):
    x = x0 + i * (w + gap)
    box(s, x, Inches(1.8), w, Inches(4.2))
    txt(s, x + Inches(0.15), Inches(2.0), w - Inches(0.3), Inches(0.7),
        n, size=30, color=CW_RED, bold=True)
    txt(s, x + Inches(0.15), Inches(2.8), w - Inches(0.3), Inches(1.1),
        t, size=13, color=CW_DARK, bold=True)
    txt(s, x + Inches(0.15), Inches(4.0), w - Inches(0.3), Inches(1.6),
        d, size=10, color=GREY)

# ----------------------------------------------------- 3 COVER LETTER / EXEC
s = slide()
header(s, "01 — Introduction", "COVER LETTER & EXECUTIVE SUMMARY", 3)
box(s, Inches(0.45), Inches(1.55), Inches(7.4), Inches(3.1))
txt(s, Inches(0.65), Inches(1.7), Inches(7.0), Inches(2.9),
    "Dear Dirk, dear Marcus,\n\n"
    "Thank you for the open discussion on 2 July. Cushman & Wakefield is pleased "
    "to present our proposal to act as project manager on behalf of Corum for the "
    "Paris Proof upgrade of Westgate I — a technically complex programme in a fully "
    "occupied building, where tenant satisfaction is as important as technical delivery.\n\n"
    "[ korte alinea's — definitieve brieftekst volgt ]", size=11)
label(s, Inches(0.65), Inches(4.35), Inches(5), "placeholder: brieftekst ± 120 woorden")
blocks = [
    ("UNDERSTANDING", "Paris Proof is a hard contractual agreement. Works in a live building with PwC as tenant. M3E develops the technical design; contractor via tender."),
    ("APPROACH", "Start small with a preparatory assignment; then three assignments: PM Preparation, PM Execution and Building Consultancy. Two complementary project managers."),
    ("COMMITMENT", "Proactive communication, transparent decision-making, no surprises. We prepare every key decision so Corum decides well-informed and PwC keeps full confidence."),
]
for i, (t, d) in enumerate(blocks):
    y = Inches(1.55) + i * Inches(1.08)
    box(s, Inches(8.05), y, Inches(4.8), Inches(0.98), fill=WHITE)
    txt(s, Inches(8.2), y + Inches(0.06), Inches(4.5), Inches(0.3), t,
        size=10, color=CW_RED, bold=True)
    txt(s, Inches(8.2), y + Inches(0.32), Inches(4.55), Inches(0.62), d, size=8.5)
box(s, Inches(0.45), Inches(4.85), Inches(12.4), Inches(1.9), fill=LIGHT)
txt(s, Inches(0.65), Inches(5.0), Inches(6), Inches(1.6),
    "SJOERD BEZEMER\nAssociate — Business Development / Senior Project Manager\n"
    "M +31 (0)6 128 485 42  ·  sjoerd.bezemer@cushwake.com", size=11, bold=False)
txt(s, Inches(7.0), Inches(5.0), Inches(5.5), Inches(1.6),
    "FRANK OKKER\nHead of Project & Development Services Netherlands\n"
    "[ handtekening / foto placeholder ]", size=11)

# --------------------------------------------------- 4 UNDERSTANDING PROJECT
s = slide()
header(s, "01 — Introduction", "UNDERSTANDING THE PROJECT", 4)
facts = [
    ("BUILDING", "Westgate I, Thomas R. Malthusstraat 5, 1066 JR Amsterdam"),
    ("SIZE", "± 27,000 m² GFA — office"),
    ("OWNER", "Corum A.M."),
    ("TENANT", "PwC — building in full operation"),
    ("OBJECTIVE", "Technically upgrade to Paris Proof — hard contractual agreement"),
    ("DESIGN", "M3E develops technical design; scope fixed, contractor via tender"),
]
for i, (k, v) in enumerate(facts):
    y = Inches(1.6) + i * Inches(0.82)
    txt(s, Inches(0.5), y, Inches(1.7), Inches(0.4), k, size=10, color=CW_RED, bold=True)
    txt(s, Inches(2.2), y, Inches(4.4), Inches(0.75), v, size=11)
box(s, Inches(7.0), Inches(1.6), Inches(5.85), Inches(3.4), fill=WHITE)
txt(s, Inches(7.0), Inches(1.75), Inches(5.85), Inches(0.4),
    "STAKEHOLDER MAP", size=11, color=CW_RED, bold=True, align=PP_ALIGN.CENTER)
positions = [
    ("CORUM\n(owner / client)", 8.2, 2.2),
    ("PWC\n(tenant)", 10.6, 2.2),
    ("C&W\n(project manager)", 9.4, 3.15),
    ("M3E\n(technical advisor)", 8.2, 4.1),
    ("CONTRACTOR\n(via tender)", 10.6, 4.1),
]
for t, x, y in positions:
    b = box(s, Inches(x), Inches(y), Inches(1.9), Inches(0.75),
            fill=LIGHT if "C&W" not in t else CW_RED, dashed=False)
    txt(s, Inches(x), Inches(y + 0.12), Inches(1.9), Inches(0.6), t, size=9,
        color=WHITE if "C&W" in t else CW_DARK, bold=True, align=PP_ALIGN.CENTER)
label(s, Inches(7.2), Inches(4.95), Inches(5), "wireframe: verbindingslijnen + rollen in design uitwerken")
box(s, Inches(7.0), Inches(5.25), Inches(5.85), Inches(1.5), fill=LIGHT)
txt(s, Inches(7.2), Inches(5.45), Inches(5.5), Inches(1.2),
    "KEY MESSAGE — Sustainability upgrade of a fully occupied building:\n"
    "floor-by-floor delivery, tenant experience is the measure of success.",
    size=11, bold=True)

# ------------------------------------------------ 5 TWO SCENARIOS (M3E)
s = slide()
header(s, "01 — Introduction", "TWO ROUTES TO PARIS PROOF", 5)
txt(s, Inches(0.45), Inches(1.45), Inches(12), Inches(0.35),
    "Based on the M3E scenario notes (9 Feb 2026) shared by Corum — summary of both options",
    size=11, color=GREY, italic=True)
cols = [
    ("PREFERRED — LT-WKO + CLIMATE CEILINGS",
     ["Full replacement of gas-fired installation",
      "Low-temperature thermal storage (WKO): warm & cold source",
      "Energy plant in basement (heat pumps, buffers)",
      "Climate ceilings + new VAV (no induction) per floor",
      "New integral building controls, energy metering per floor",
      "Phased floor-by-floor — building stays operational",
      "Future-proof: one intervention, done"]),
    ("ALTERNATIVE — AIR-WATER HP + RETAIN VAV + VRF",
     ["Air-water heat pump for base heating (roof)",
      "Existing VAV induction units retained",
      "VRF system with convectors as zone control per floor",
      "New DX block replaces outdated cooling",
      "Limited interventions on office floors",
      "Hybrid system — careful controls integration required",
      "Residual life VAV ± 6–9 yrs → second intervention later"]),
]
for i, (t, pts) in enumerate(cols):
    x = Inches(0.45) + i * Inches(6.35)
    box(s, x, Inches(1.9), Inches(6.1), Inches(4.15), fill=WHITE)
    hd = box(s, x, Inches(1.9), Inches(6.1), Inches(0.5),
             fill=CW_RED if i == 0 else CW_DARK, dashed=False)
    txt(s, x + Inches(0.1), Inches(1.98), Inches(5.9), Inches(0.4), t,
        size=11, color=WHITE, bold=True)
    body = "\n".join("•  " + p for p in pts)
    txt(s, x + Inches(0.2), Inches(2.55), Inches(5.7), Inches(3.4), body, size=10.5)
box(s, Inches(0.45), Inches(6.25), Inches(12.4), Inches(0.7), fill=LIGHT)
txt(s, Inches(0.65), Inches(6.4), Inches(12), Inches(0.45),
    "Our project management approach is robust for either scenario — phased, floor-by-floor, tenant-first.",
    size=12, bold=True, color=CW_DARK)

# ------------------------------------------------- 6 ASSIGNMENT & ROLE
s = slide()
header(s, "02 — Our Approach", "THE ASSIGNMENT & OUR ROLE", 6)
box(s, Inches(0.45), Inches(1.6), Inches(5.6), Inches(4.9), fill=WHITE)
txt(s, Inches(0.65), Inches(1.75), Inches(5.2), Inches(0.4),
    "PROJECT MANAGER ON BEHALF OF THE OWNER", size=12, color=CW_RED, bold=True)
txt(s, Inches(0.65), Inches(2.2), Inches(5.2), Inches(4.1),
    "C&W acts as project manager on behalf of Corum during preparation and "
    "execution: representing Corum's interests and ensuring effective "
    "collaboration between tenant, technical advisor and contractor.\n\n"
    "We proactively anticipate key decisions by preparing them thoroughly in "
    "advance — Corum is well-advised at every stage, and PwC experiences full "
    "confidence that the project is under control.", size=11.5)
resp = ["Represent Corum's interests towards all parties",
        "Coordinate communication between tenant, advisor & contractor",
        "Monitor planning, budget, quality and risks",
        "Manage the tender and contractor selection",
        "Manage the execution phase, floor-by-floor",
        "Ensure transparent decision-making throughout"]
for i, rtext in enumerate(resp):
    y = Inches(1.6) + i * Inches(0.82)
    n = box(s, Inches(6.35), y, Inches(0.5), Inches(0.5), fill=CW_RED, dashed=False)
    txt(s, Inches(6.35), y + Inches(0.06), Inches(0.5), Inches(0.4), str(i + 1),
        size=14, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    txt(s, Inches(7.0), y + Inches(0.04), Inches(5.8), Inches(0.7), rtext, size=11.5)

# ------------------------------------------------- 7 KEY SUCCESS FACTORS
s = slide()
header(s, "02 — Our Approach", "KEY SUCCESS FACTORS", 7)
tiles = [
    ("TENANT SATISFACTION FIRST",
     "Tenant satisfaction is central to Corum's objectives. A previous project "
     "(Rotterdam) showed how insufficient communication erodes trust — we put the "
     "tenant experience at the heart of planning and communication."),
    ("PHASED DELIVERY IN A LIVE BUILDING",
     "Floor-by-floor execution: one zone temporarily out of use, handed back "
     "before the next starts. The building remains operational throughout."),
    ("CLEAR GOVERNANCE",
     "PwC actively involved in decision-making, continuous insight into progress "
     "and planning, timely communication of impact on business operations, clear "
     "escalation lines, team personally introduced at the outset."),
    ("NO SURPRISES",
     "Risk Register from day one: risks identified early, ownership assigned, "
     "mitigation agreed. Transparent reporting on budget and planning."),
]
for i, (t, d) in enumerate(tiles):
    x = Inches(0.45) + (i % 2) * Inches(6.35)
    y = Inches(1.7) + (i // 2) * Inches(2.6)
    box(s, x, y, Inches(6.1), Inches(2.35), fill=WHITE)
    txt(s, x + Inches(0.2), y + Inches(0.15), Inches(5.7), Inches(0.5), t,
        size=13, color=CW_RED, bold=True)
    txt(s, x + Inches(0.2), y + Inches(0.7), Inches(5.7), Inches(1.55), d, size=10.5)

# ------------------------------------------------- 8 PHASED APPROACH
s = slide()
header(s, "02 — Our Approach", "A PHASED APPROACH — START SMALL, SCALE WITH CONFIDENCE", 8)
phases = [
    ("PHASE 0", "PREPARATORY ASSIGNMENT",
     "Limited assignment: map all stakeholders, set up project organisation, "
     "gather input from M3E, identify tenant requirements → integral project plan.", True),
    ("PHASE 1", "PM PREPARATION",
     "Guide technical design, fix scope, prepare tender documents, run tender "
     "and contractor selection.", False),
    ("PHASE 2", "PM EXECUTION",
     "Site & execution management, floor-by-floor phasing, progress/budget/risk "
     "control, tenant communication.", False),
    ("PHASE 3", "BUILDING CONSULTANCY",
     "Independent quality inspections during construction.", False),
]
w = Inches(2.95); x0 = Inches(0.45)
for i, (n, t, d, hl) in enumerate(phases):
    x = x0 + i * (w + Inches(0.15))
    box(s, x, Inches(1.9), w, Inches(3.6), fill=WHITE)
    hd = box(s, x, Inches(1.9), w, Inches(0.75), fill=CW_RED if hl else CW_DARK, dashed=False)
    txt(s, x + Inches(0.12), Inches(1.98), w - Inches(0.2), Inches(0.3), n,
        size=10, color=WHITE, bold=True)
    txt(s, x + Inches(0.12), Inches(2.22), w - Inches(0.2), Inches(0.45), t,
        size=11, color=WHITE, bold=True)
    txt(s, x + Inches(0.15), Inches(2.85), w - Inches(0.3), Inches(2.5), d, size=10)
    if i < 3:
        ar = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, x + w - Inches(0.05),
                                Inches(3.4), Inches(0.28), Inches(0.3))
        ar.fill.solid(); ar.fill.fore_color.rgb = CW_RED
        ar.line.fill.background(); ar.shadow.inherit = False
box(s, Inches(0.45), Inches(5.75), Inches(12.4), Inches(1.0), fill=LIGHT)
txt(s, Inches(0.65), Inches(5.9), Inches(12), Inches(0.75),
    "Following the preparatory assignment, we propose three separate assignments — "
    "PM Preparation, PM Execution and Building Consultancy — each with its own scope, "
    "deliverables and fee. Corum decides per phase.", size=11.5, bold=True)

# ------------------------------------------------- 9 PROCESS PLANNING
s = slide()
header(s, "02 — Our Approach", "PROCESS PLANNING (INDICATIVE)", 9)
quarters = ["Q3 2026", "Q4 2026", "Q1 2027", "Q2 2027", "Q3 2027", "Q4 2027", "2028"]
gx0, gw = Inches(3.3), Inches(9.4)
colw = Emu(int(gw) // len(quarters))
for i, q in enumerate(quarters):
    txt(s, gx0 + i * colw, Inches(1.7), colw, Inches(0.3), q,
        size=9, color=GREY, align=PP_ALIGN.CENTER)
rows = [
    ("NDA · proposal · award Phase 0", 0.0, 0.7),
    ("Phase 0 — preparatory → project plan", 0.3, 1.0),
    ("Technical design (M3E) — guided by C&W", 1.0, 2.0),
    ("Tender & contractor selection", 2.2, 1.5),
    ("Contracting", 3.5, 0.5),
    ("Execution — floor-by-floor (PM + inspections)", 3.9, 2.8),
    ("Handover · aftercare · fine-tuning", 6.4, 0.6),
]
for i, (name, start, dur) in enumerate(rows):
    y = Inches(2.1) + i * Inches(0.62)
    txt(s, Inches(0.45), y, Inches(2.8), Inches(0.55), name, size=9.5)
    bx = gx0 + Emu(int(colw) * start / 1.0 if False else int(int(colw) * start))
    bx = gx0 + Emu(int(int(colw) * start))
    bw = Emu(int(int(colw) * dur))
    b = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, bx, y + Inches(0.05),
                           bw, Inches(0.32))
    b.fill.solid()
    b.fill.fore_color.rgb = CW_RED if i in (0, 4, 6) else MID
    b.line.fill.background(); b.shadow.inherit = False
label(s, Inches(3.3), Inches(6.6),
      Inches(9), "wireframe: balkenplanning indicatief — te valideren met M3E-ontwerpplanning en Corum–PwC afspraken")
box(s, Inches(0.45), Inches(6.35), Inches(2.8), Inches(0.75), fill=LIGHT)
txt(s, Inches(0.55), Inches(6.45), Inches(2.6), Inches(0.6),
    "◆ = decision milestone Corum", size=9, color=CW_DARK)

# ------------------------------------------------ 10 ORGANISATION
s = slide()
header(s, "03 — Organisation", "PROJECT ORGANISATION — THE TWO-PM MODEL", 10)
def orgbox(x, y, w, h, t, red=False):
    b = box(s, Inches(x), Inches(y), Inches(w), Inches(h),
            fill=CW_RED if red else WHITE, dashed=False,
            line=CW_RED if red else GREY)
    txt(s, Inches(x), Inches(y) + Inches(0.1), Inches(w), Inches(h) - Inches(0.15),
        t, size=10, color=WHITE if red else CW_DARK, bold=True, align=PP_ALIGN.CENTER)
orgbox(5.2, 1.6, 2.9, 0.7, "CORUM A.M.\nClient / Owner")
orgbox(9.3, 1.6, 2.9, 0.7, "PWC\nTenant — involved in governance")
orgbox(3.4, 2.9, 3.0, 1.0, "STAKEHOLDER MANAGEMENT PM\nTenant relations · communication ·\ndecision-making", red=True)
orgbox(6.9, 2.9, 3.0, 1.0, "TECHNICAL PM\nTechnical coordination · site mgmt ·\nM3E alignment · tender & execution", red=True)
orgbox(3.4, 4.6, 3.0, 0.8, "M3E\nTechnical advisor / installation consultant")
orgbox(6.9, 4.6, 3.0, 0.8, "CONTRACTOR\nSelected via tender")
label(s, Inches(3.4), Inches(5.6), Inches(8),
      "wireframe: verbindingslijnen + eventueel cost management / inspecties toevoegen in design")
box(s, Inches(0.45), Inches(6.05), Inches(12.4), Inches(0.95), fill=LIGHT)
txt(s, Inches(0.65), Inches(6.2), Inches(12), Inches(0.7),
    "Two complementary project managers: one guards the relationship and the tenant "
    "experience, one guards the technique and the site — the technical and diplomatic "
    "sides of this project are equally covered.", size=11.5, bold=True)

# ------------------------------------------------ 11 GOVERNANCE & COMMS
s = slide()
header(s, "03 — Organisation", "GOVERNANCE & COMMUNICATION", 11)
gv = [
    ("STEERING MEETING", "Corum · C&W (· PwC where relevant)", "Monthly — direction, decisions, escalation"),
    ("PROJECT TEAM MEETING", "C&W · M3E (· contractor from execution)", "Bi-weekly — progress, planning, actions"),
    ("TENANT ALIGNMENT", "Stakeholder PM · PwC facility/leadership", "Structured cadence + ad-hoc at impact"),
    ("SITE MEETING", "Technical PM · contractor", "Weekly during execution"),
]
for i, (a, b_, c) in enumerate(gv):
    y = Inches(1.7) + i * Inches(0.85)
    box(s, Inches(0.45), y, Inches(7.3), Inches(0.72), fill=WHITE)
    txt(s, Inches(0.6), y + Inches(0.08), Inches(2.5), Inches(0.5), a, size=10.5, color=CW_RED, bold=True)
    txt(s, Inches(3.15), y + Inches(0.08), Inches(2.6), Inches(0.55), b_, size=9.5)
    txt(s, Inches(5.8), y + Inches(0.08), Inches(1.9), Inches(0.55), c, size=9)
principles = ["PwC actively involved in the decision-making process",
              "Continuous insight into progress and planning",
              "Timely communication of changes impacting business operations",
              "Clear escalation lines",
              "Full project team personally introduced to all parties at the outset"]
box(s, Inches(8.05), Inches(1.7), Inches(4.8), Inches(3.3), fill=LIGHT)
txt(s, Inches(8.25), Inches(1.85), Inches(4.4), Inches(0.35),
    "GOVERNANCE PRINCIPLES", size=11, color=CW_RED, bold=True)
txt(s, Inches(8.25), Inches(2.25), Inches(4.45), Inches(2.7),
    "\n".join("•  " + p for p in principles), size=10)
box(s, Inches(0.45), Inches(5.4), Inches(12.4), Inches(1.3), fill=WHITE)
txt(s, Inches(0.65), Inches(5.55), Inches(12), Inches(0.35),
    "REPORTING", size=11, color=CW_RED, bold=True)
txt(s, Inches(0.65), Inches(5.9), Inches(12), Inches(0.7),
    "Monthly progress report: planning · budget · quality · risks · tenant impact — "
    "one page for Corum management, detail in appendix. [ dashboard mock-up placeholder ]", size=10.5)

# ------------------------------------------------ 12 RISK MANAGEMENT
s = slide()
header(s, "03 — Organisation", "RISK MANAGEMENT — NO SURPRISES", 12)
txt(s, Inches(0.45), Inches(1.5), Inches(12.3), Inches(0.6),
    "We work with a Risk Register from the very start: risks identified early, ownership "
    "assigned, mitigation agreed — surprises during execution avoided as much as possible.",
    size=11.5)
hdr = ["#", "RISK (EXAMPLES)", "IMPACT", "MITIGATION", "OWNER", "RAG"]
wds = [0.5, 4.1, 1.3, 4.6, 1.1, 0.7]
risks = [
    ("1", "Tenant disturbance / complaints during works", "High",
     "Floor-by-floor phasing, tenant comms plan, agreed working windows", "SPM", "●"),
    ("2", "Phasing conflicts between floors in a live building", "High",
     "Integral phasing plan, buffer per floor, weekly look-ahead", "TPM", "●"),
    ("3", "WKO permits & source drilling lead time (preferred scenario)", "Med",
     "Early permit inventory & planning, start applications in Phase 1", "TPM", "●"),
    ("4", "Tender result exceeds budget", "Med",
     "Cost estimate at design milestones, VE-options, market sounding", "TPM", "●"),
    ("5", "Controls/systems integration (esp. hybrid alternative)", "Med",
     "Commissioning plan, integral controls party, test per floor", "TPM", "●"),
    ("6", "Decision-making lead time owner/tenant", "Med",
     "Decision calendar, decisions prepared in advance by C&W", "SPM", "●"),
]
x = Inches(0.45); y0 = Inches(2.3)
cx = x
for j, h in enumerate(hdr):
    b = box(s, cx, y0, Inches(wds[j]), Inches(0.4), fill=CW_DARK, dashed=False)
    txt(s, cx + Inches(0.05), y0 + Inches(0.05), Inches(wds[j]) - Inches(0.1),
        Inches(0.3), h, size=9, color=WHITE, bold=True)
    cx += Inches(wds[j])
for i, row in enumerate(risks):
    cy = y0 + Inches(0.4) + i * Inches(0.62)
    cx = x
    for j, cell in enumerate(row):
        b = box(s, cx, cy, Inches(wds[j]), Inches(0.62),
                fill=WHITE if i % 2 == 0 else LIGHT)
        txt(s, cx + Inches(0.05), cy + Inches(0.05), Inches(wds[j]) - Inches(0.1),
            Inches(0.52), cell, size=8.5,
            color=CW_RED if j == 5 else CW_DARK)
        cx += Inches(wds[j])
label(s, Inches(0.45), Inches(6.75), Inches(9),
      "wireframe: voorbeeldrisico's — definitieve register in fase 0 opstellen; RAG-bolletjes in design")

# ------------------------------------------------ 13 TEAM (WIT)
s = slide()
txt(s, Inches(0.45), Inches(0.25), Inches(9), Inches(0.3),
    "04 — TEAM", size=10, color=MID, bold=True)
txt(s, Inches(0), Inches(3.3), SW, Inches(0.5),
    "[ TEAMPAGINA — BEWUST LEEG GELATEN / IN TE VULLEN ]",
    size=12, color=MID, align=PP_ALIGN.CENTER, italic=True)
txt(s, Inches(12.5), Inches(7.05), Inches(0.6), Inches(0.3), "13",
    size=10, color=MID, align=PP_ALIGN.RIGHT)

# ------------------------------------------------ 14 TRACK RECORD
s = slide()
header(s, "04 — Team & Track Record", "TRACK RECORD — COMPARABLE PROJECTS", 14)
for i in range(4):
    x = Inches(0.45) + i * Inches(3.15)
    box(s, x, Inches(1.7), Inches(2.95), Inches(4.6))
    box(s, x + Inches(0.1), Inches(1.8), Inches(2.75), Inches(1.6), fill=MID)
    txt(s, x + Inches(0.1), Inches(2.35), Inches(2.75), Inches(0.4), "[FOTO]",
        size=10, color=GREY, align=PP_ALIGN.CENTER)
    txt(s, x + Inches(0.15), Inches(3.55), Inches(2.65), Inches(0.4),
        f"REFERENCE {i+1}", size=11, color=CW_RED, bold=True)
    txt(s, x + Inches(0.15), Inches(3.95), Inches(2.65), Inches(2.2),
        "Project name\nSustainability upgrade / renovation in occupied office\n"
        "Size · role C&W · result\n[ in te vullen ]", size=9, color=GREY)
label(s, Inches(0.45), Inches(6.5), Inches(11),
      "selectiecriteria: verduurzaming/renovatie in gebruik zijnd kantoor · institutionele eigenaar · huurdercommunicatie")

# ------------------------------------------------ 15 FEE
s = slide()
header(s, "05 — Fee & Next Steps", "FEE PROPOSAL", 15)
fee_rows = [
    ("PHASE 0 — Preparatory assignment", "Lump sum", "€ [ • ]"),
    ("PHASE 1 — PM Preparation", "Fixed fee / monthly rate", "€ [ • ]"),
    ("PHASE 2 — PM Execution", "Fixed fee / monthly rate", "€ [ • ]"),
    ("PHASE 3 — Building Consultancy (quality inspections)", "Unit rate per inspection", "€ [ • ]"),
]
y0 = Inches(1.7)
for i, (a, b_, c) in enumerate(fee_rows):
    y = y0 + i * Inches(0.75)
    box(s, Inches(0.45), y, Inches(7.6), Inches(0.62),
        fill=WHITE if i % 2 == 0 else LIGHT)
    txt(s, Inches(0.6), y + Inches(0.08), Inches(4.6), Inches(0.5), a, size=10.5, bold=True)
    txt(s, Inches(5.3), y + Inches(0.08), Inches(1.6), Inches(0.5), b_, size=9.5)
    txt(s, Inches(7.0), y + Inches(0.08), Inches(1.0), Inches(0.5), c, size=10.5, color=CW_RED, bold=True)
box(s, Inches(8.3), Inches(1.7), Inches(4.55), Inches(2.9), fill=LIGHT)
txt(s, Inches(8.5), Inches(1.85), Inches(4.2), Inches(0.35),
    "RATE CARD (REFERENCE)", size=11, color=CW_RED, bold=True)
txt(s, Inches(8.5), Inches(2.25), Inches(4.2), Inches(2.3),
    "Senior Project Manager   € 145 / hr\nProject Manager             € 135 / hr\n"
    "Technical PM                 € 135 / hr\nCost Manager                € 125 / hr\n"
    "Site Manager                 € 120 / hr\n\n[ tarieven & inzet definitief met Frank ]",
    size=10)
box(s, Inches(0.45), Inches(4.9), Inches(12.4), Inches(1.7), fill=WHITE)
txt(s, Inches(0.65), Inches(5.05), Inches(12), Inches(0.35),
    "ASSUMPTIONS & EXCLUSIONS", size=11, color=CW_RED, bold=True)
txt(s, Inches(0.65), Inches(5.45), Inches(12), Inches(1.1),
    "•  Each phase is a separate assignment — Corum decides per phase\n"
    "•  Technical design, calculations and specifications by M3E (outside C&W scope)\n"
    "•  DNR 2011 applicable  ·  [ verdere uitgangspunten in te vullen ]", size=10)

# ------------------------------------------------ 16 NEXT STEPS
s = slide()
header(s, "05 — Fee & Next Steps", "NEXT STEPS", 16)
steps = [
    ("1", "NDA via Dentons — signed", "in progress"),
    ("2", "Insight into Corum–PwC agreement & Corum–M3E arrangement", "upon NDA"),
    ("3", "Confirmation of Phase 0 — preparatory assignment", "July 2026"),
    ("4", "Kick-off & personal introduction of the full project team", "within 2 weeks of award"),
    ("5", "Integral project plan → decision on Phase 1–3 assignments", "end of Phase 0"),
]
for i, (n, t, w_) in enumerate(steps):
    y = Inches(1.7) + i * Inches(0.85)
    c = box(s, Inches(0.45), y, Inches(0.55), Inches(0.55), fill=CW_RED, dashed=False)
    txt(s, Inches(0.45), y + Inches(0.08), Inches(0.55), Inches(0.4), n,
        size=14, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    txt(s, Inches(1.2), y + Inches(0.02), Inches(8.2), Inches(0.6), t, size=12)
    txt(s, Inches(9.6), y + Inches(0.02), Inches(3.2), Inches(0.6), w_,
        size=10, color=GREY, italic=True)
box(s, Inches(0.45), Inches(6.15), Inches(12.4), Inches(0.9), fill=CW_RED, dashed=False)
txt(s, Inches(0.7), Inches(6.32), Inches(12), Inches(0.6),
    "Sjoerd Bezemer  ·  +31 (0)6 128 485 42  ·  sjoerd.bezemer@cushwake.com      |      "
    "Frank Okker — Head of PDS Netherlands", size=12, color=WHITE, bold=True)

prs.save("corum-pitch/Corum-Westgate-I-Pitch-Wireframe.pptx")
print("OK:", len(prs.slides.__iter__.__self__._sldIdLst), "slides")
