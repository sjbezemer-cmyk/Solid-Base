#!/usr/bin/env python3
"""Generate C&W PDS proposal (offerte) for Teledyne - Project Plan phase."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

CW_RED = RGBColor(0xC3, 0x00, 0x2B)
CW_DARK = RGBColor(0x1C, 0x1C, 0x1C)
FONT = "Arial"

doc = Document()

# Page setup
for section in doc.sections:
    section.top_margin = Cm(2.2)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(2.2)
    section.right_margin = Cm(2.2)

# Base style
style = doc.styles["Normal"]
style.font.name = FONT
style.font.size = Pt(10)
style.font.color.rgb = CW_DARK
style.paragraph_format.space_after = Pt(6)
style.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)


def para(text="", bold=False, size=10, color=CW_DARK, space_after=6, align=None):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = bold
    r.font.size = Pt(size)
    r.font.name = FONT
    r.font.color.rgb = color
    p.paragraph_format.space_after = Pt(space_after)
    if align:
        p.alignment = align
    return p


def heading(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(14)
    r.font.name = FONT
    r.font.color.rgb = CW_RED
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(8)
    return p


def bullet(text, bold=False):
    p = doc.add_paragraph(style="List Bullet")
    r = p.add_run(text)
    r.bold = bold
    r.font.size = Pt(10)
    r.font.name = FONT
    r.font.color.rgb = CW_DARK
    p.paragraph_format.space_after = Pt(3)
    return p


def set_cell(cell, text, bold=False, color=CW_DARK, size=10):
    cell.text = ""
    p = cell.paragraphs[0]
    r = p.add_run(text)
    r.bold = bold
    r.font.size = Pt(size)
    r.font.name = FONT
    r.font.color.rgb = color
    p.paragraph_format.space_after = Pt(2)


def style_table(t):
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    # header row red text
    for cell in t.rows[0].cells:
        for p in cell.paragraphs:
            for r in p.runs:
                r.bold = True
                r.font.color.rgb = CW_RED


# ----- COVER -----
para()
para()
p = para("PROPOSAL.", bold=True, size=36, color=CW_RED, space_after=24)
para("TELEDYNE", bold=True, size=18, space_after=2)
para("Fit-out High Tech Campus 6, Eindhoven", size=14, space_after=36)

para("Date:\t8 July 2026", space_after=2)
para("Contact:\tSjoerd Bezemer", space_after=2)
para("Mobile:\t+31 (0)6 128 485 42", space_after=2)
para("Email:\tsjoerd.bezemer@cushwake.com", space_after=24)
para("Reykjavikstraat 1 | 3543 KH UTRECHT", bold=True, space_after=2)

doc.add_page_break()

# ----- SITUATION AND REQUEST -----
heading("SITUATION AND REQUEST.")
para("Teledyne has recently leased approximately 1,200 m² at High Tech Campus 6 in Eindhoven. "
     "The programme comprises office space, a cleanroom and logistics space. The lease was arranged "
     "with the support of Cushman & Wakefield and delivery of the leased space to Teledyne has "
     "already taken place.")
para("The current status of the project is as follows:")
bullet("A test-fit has been developed based on a spatial Programme of Requirements (PoR); the spatial layout is well understood.")
bullet("The technical Programme of Requirements is largely clear.")
bullet("Several contractors and specialist lab-builders have been approached for pricing. Their feedback "
       "is that the available information is insufficient for a reliable quotation, or that quotations "
       "carry a significant risk premium due to the remaining uncertainties.")
para("The target move-in date is April 2027.")
para("You have asked us to submit a proposal for the first phase of our structured design-and-delivery "
     "process: the development of a project plan. This project plan will provide the structure, clarity "
     "and decision framework required to de-risk the next phases and to obtain reliable, comparable "
     "pricing from the market.")

# ----- PROPOSAL -----
heading("PROPOSAL.")
para("Following our kick-off meeting at High Tech Campus Eindhoven, we propose to deploy a senior "
     "project manager, supported where required by our in-house MEP and cost specialists given the "
     "technical complexity of the cleanroom component. The senior project manager will act as your "
     "single point of contact and will report directly to Teledyne.")
para("Phase 1 – Project Plan", bold=True, space_after=4)
para("The project plan will cover:")
bullet("The full process from the current situation through to move-in in April 2027.")
bullet("The project phasing: definition, concept design (SO), preliminary design (VO), final design (DO), tender and contracting, construction, and handover.")
bullet("The key milestones and an overall project schedule aligned with the April 2027 move-in date.")
bullet("An overview of outstanding information and decisions, with owners and deadlines.")
bullet("The basis (scope, deliverables and organisation) for the design, engineering and tender phases.")
para("To produce the project plan we will undertake the following activities:")
bullet("Kick-off and site visit at High Tech Campus 6.")
bullet("Review of the available documentation: test-fit, spatial and technical Programme of Requirements, and the delivery documentation of the leased space.")
bullet("Working sessions with the Teledyne stakeholders to validate ambitions, budget framework and schedule constraints.")
bullet("Assessment of the open technical questions (with emphasis on the cleanroom and MEP scope) that currently prevent reliable contractor pricing.")
bullet("Drafting of the project plan, a joint review session, and issue of the final project plan.")

# ----- NEXT STEPS -----
heading("NEXT STEPS AFTER THE PROJECT PLAN.")
para("The project plan forms the basis for the subsequent phases of our structured design-and-delivery "
     "process. Upon completion of the project plan, we can support Teledyne with the following steps:")
bullet("Validate and complete the spatial and technical Programme of Requirements.")
bullet("Develop a concept design (SO) with sufficient detail to lock down the key design decisions.")
bullet("Advance to a preliminary design (VO), including technical engineering.")
bullet("Develop a final design (DO) with all information ready for tender.")
bullet("Organise and manage the tender and advise on the right parties to contract.")
bullet("Advise on contracting the selected contractor(s).")
bullet("Manage the construction phase as Project Manager and Site Manager, including chairing "
       "construction meetings, planning and quality control, progress reporting and periodic photo reporting.")
bullet("Organise the handover, manage the completion of any remaining points and collect all "
       "as-built documentation, guarantees and maintenance instructions.")
para("Cushman & Wakefield can support this full trajectory with its multidisciplinary in-house team: "
     "Design, Architecture, Engineering, Project Management, Cost Management and Site Management. "
     "Each subsequent phase will be quoted separately; the project plan provides the scope definition "
     "on which those fee proposals will be based, so that Teledyne maintains full control over "
     "commitments per phase.")

# ----- FEE -----
heading("FEE.")
para("For the development of the project plan (Phase 1) we estimate the following effort:")
t = doc.add_table(rows=5, cols=4)
hdr = ["Role", "Hours", "Rate (EUR/h)", "Amount (EUR)"]
rows = [
    ("Project manager sr.", "40", "155,-", "6.200,-"),
    ("MEP consultant", "8", "175,-", "1.400,-"),
    ("Cost consultant", "8", "175,-", "1.400,-"),
    ("Total (fixed fee, excl. VAT)", "56", "", "9.000,-"),
]
for i, h in enumerate(hdr):
    set_cell(t.rows[0].cells[i], h, bold=True, color=CW_RED)
for ri, row in enumerate(rows, start=1):
    for ci, v in enumerate(row):
        set_cell(t.rows[ri].cells[ci], v, bold=(ri == 4))
style_table(t)
para()
para("We offer Phase 1 for a fixed fee of EUR 9.000,- excluding VAT, including travel and "
     "accommodation expenses within the Netherlands.", bold=True)

# ----- SCHEDULE -----
heading("SCHEDULE.")
para("Once the signed proposal has been returned to us, we can start the work within two weeks. "
     "The project plan will be delivered within four weeks of the start.")
para("Based on our knowledge and experience, and working back from the target move-in date of "
     "April 2027, we currently anticipate the following indicative durations per project phase. "
     "The definitive schedule will be developed as part of the project plan.")
t2 = doc.add_table(rows=10, cols=2)
sched = [
    ("Phase", "Indicative duration"),
    ("Project plan (this proposal)", "4 weeks"),
    ("Validation and completion of the PoR", "2 weeks"),
    ("Concept design (SO)", "6 weeks"),
    ("Preliminary design (VO), incl. technical engineering", "8 weeks"),
    ("Final design (DO), ready for tender", "8 weeks"),
    ("Tender and contracting", "8 weeks"),
    ("Work preparation / engineering by contractor(s)", "6 weeks"),
    ("Construction, incl. cleanroom fit-out", "20 weeks"),
    ("Handover and move-in", "April 2027"),
]
for ri, (a, b) in enumerate(sched):
    set_cell(t2.rows[ri].cells[0], a, bold=(ri == 0), color=CW_RED if ri == 0 else CW_DARK)
    set_cell(t2.rows[ri].cells[1], b, bold=(ri == 0), color=CW_RED if ri == 0 else CW_DARK)
style_table(t2)

# ----- RATES -----
heading("RATES.")
para("We apply the following hourly rates (PDS 2026) in EUR, which will also form the basis for the "
     "fee proposals of the subsequent phases:")
rates = [
    ("Project manager jr.", "125,-"),
    ("Project manager", "140,-"),
    ("Project manager sr.", "155,-"),
    ("Site manager", "140,-"),
    ("Site manager sr.", "155,-"),
    ("Building surveyor jr.", "125,-"),
    ("Building surveyor", "140,-"),
    ("Building surveyor sr.", "155,-"),
    ("Cost consultant", "175,-"),
    ("MEP consultant", "175,-"),
    ("Technical designer sr.", "135,-"),
    ("Architect jr.", "110,-"),
    ("Architect", "125,-"),
    ("Architect sr.", "135,-"),
    ("Associate Architect", "150,-"),
    ("Interior Architect", "120,-"),
    ("Interior Architect sr.", "135,-"),
    ("Consultant sustainability", "135,-"),
    ("Consultant sustainability sr.", "145,-"),
    ("Associate Director", "175,-"),
    ("Partner", "225,-"),
]
t3 = doc.add_table(rows=len(rates) + 1, cols=2)
set_cell(t3.rows[0].cells[0], "Role", bold=True, color=CW_RED)
set_cell(t3.rows[0].cells[1], "Rate (EUR/h)", bold=True, color=CW_RED)
for ri, (a, b) in enumerate(rates, start=1):
    set_cell(t3.rows[ri].cells[0], a)
    set_cell(t3.rows[ri].cells[1], b)
style_table(t3)

# ----- INVOICING -----
heading("INVOICING.")
para("We will invoice the fixed fee for Phase 1 upon delivery of the project plan. We expect full "
     "payment of our invoice within 30 days of the invoice date. If you require a PO number on our "
     "invoice, or if the invoicing details need to be adjusted, please let us know.")

# ----- CLIENT -----
heading("CLIENT.")
para("Teledyne")
para("Attn. Mr. P. Kilkens, Vice President Global Operations")
para("High Tech Campus 6, Eindhoven")
para("[invoicing entity and address to be confirmed]")

# ----- TERMS -----
heading("TERMS AND CONDITIONS.")
para("De Nieuwe Regeling 2011 (DNR 2011) applies to our proposal. A copy of the DNR 2011 is enclosed "
     "with this proposal.")
para("All amounts stated are exclusive of VAT and inclusive of travel and accommodation expenses "
     "within the Netherlands.")
para("For our privacy policy, please refer to our website: "
     "https://www.cushmanwakefield.com/en/emea-and-california-privacy-notice")
para("Thank you for your interest in our services. We hope that our proposal meets your expectations. "
     "Please do not hesitate to contact us if you have any questions or require additional information.")
para("If you agree with the content of this proposal and wish to commission these services, we kindly "
     "request that you return the signed proposal to us. Once approved and signed, we can start the "
     "work within two weeks.")

para()
# signature block
t4 = doc.add_table(rows=6, cols=2)
sig = [
    ("Kind regards,", "For approval:"),
    ("Cushman & Wakefield Netherlands B.V.", "Teledyne"),
    ("Project & Development Services", ""),
    ("i/o", "Date: ……… - ……… - ………"),
    ("Annelou de Groot", ""),
    ("Head of The Netherlands", "(Name + signature of authorised signatory)"),
]
for ri, (a, b) in enumerate(sig):
    set_cell(t4.rows[ri].cells[0], a, bold=(ri in (0, 1)))
    set_cell(t4.rows[ri].cells[1], b, bold=(ri in (0, 1)))

para()
para("Appendices:", bold=True, space_after=2)
bullet("DNR 2011")
bullet("C&W Capability Statement Consultancy & Design")

out = "/tmp/claude-0/-home-user-Solid-Base/19a65cb7-14af-5a33-bca2-1139c9f360ec/scratchpad/20260708 Teledyne - Proposal Project Plan - C&W PDS.docx"
doc.save(out)
print("saved:", out)
