# PROMPT 3 — Claude Design (STYLING-PASS, super gedetailleerd): CBOE look-and-feel over het wireframe

> **Wanneer:** NADAT het wireframe klaar is (Prompt 2). Dit is de tweede pass — je legt de C&W-huisstijl
> van de CBOE-deck als visuele skin over het goedgekeurde wireframe, zonder inhoud/volgorde te wijzigen.
>
> **Voeg in Claude Design deze twee bijlagen toe:**
> 1. het **goedgekeurde wireframe** (uit Prompt 2);
> 2. **`CBOE pitch July 15 2026.pdf`** (mail Ilse) — de **definitieve visuele referentie**.
>
> Plak daaronder alles vanaf de streep. Werk de slides in volgorde af; per slide staat exact welk
> CBOE-component erop moet.

---

## BRAND TOKENS — use these EXACTLY (colours as hex, fonts by name; do not approximate)
> Fill the `?`-values from the CBOE deck first (PowerPoint → Design → Variants → Colours/Fonts, or an
> eyedropper, or a brand-extractor on the PDF). See `STRATEGIE-look-and-feel-transfer.md`. Defaults below.
```
Colours
  --accent  #C3002B   (C&W red — CONFIRM against CBOE; alternative seen: #DE0025)
  --ink     #1C1C1C    --grey #7A7A7A   --panel #F3F3F3   --hair #E2E2E2   --white #FFFFFF
  --teal    #0093B2?   (only if CBOE uses it as a secondary accent)
Fonts (PowerPoint = C&W Office standard)
  Headings / section labels : Arial Bold
  Body                      : Arial Regular
Type scale
  H1 title 28–32pt · SECTION LABEL 10–11pt UPPERCASE tracked · body 10–11pt · caption 8pt
Style
  flat, high-contrast, generous whitespace · thin red section spine (left) · UPPERCASE red section label
  + sentence-case descriptor · statement slides on --ink/--accent
```
**Use the BRAND TOKENS above verbatim.** Anything not specified here, sample directly from the attached
CBOE deck. Where a token is given, match it exactly — never approximate a colour or substitute a font.

---

Apply the **exact visual look-and-feel of the attached "CBOE pitch July 15 2026.pdf"** (the C&W house style)
to the attached approved 24-slide wireframe for the **Cushman & Wakefield → Corum A.M. "Westgate I — Paris
Proof"** pitch. This is a **styling pass only**: keep the slide order, the content, the copy, the tables,
the diagrams and the deliberately white Team page unchanged. You are skinning the wireframe, not redesigning
it. Keep every placeholder marker visible ("€ [ • ]", "[ PHOTO ]", "[ GANTT ]", "[ ORG CHART ]").

═══════════════════════════════════════════════════════════════════════
## A. GLOBAL DESIGN SYSTEM (sample everything from the CBOE deck; do not invent)
═══════════════════════════════════════════════════════════════════════
- **Canvas:** 16:9. Consistent outer margins matching the CBOE deck. Visible, disciplined grid.
- **Colour tokens — sample directly from the CBOE PDF and reuse verbatim:**
  `--accent` (CBOE primary accent), `--ink` (dark charcoal text), `--panel` (light grey panel),
  `--line` (hairline rules), `--bg` (white). Do NOT use any colour absent from the CBOE deck.
  *Fallback only if the PDF is unavailable:* accent #C3002B, ink #1C1C1C, web-teal #0093B2, warm greys, white.
- **Type scale — match the CBOE families/weights:**
  H1 slide title (bold, large) · SECTION LABEL (uppercase, letter-spaced, small, accent) ·
  descriptor line (sentence case, medium grey) · body (regular) · caption/footnote (small grey).
- **Masthead:** every content slide, top-left: **"Cushman & Wakefield | Corum"**, with the slide number
  in the same position and format as the CBOE deck.
- **Footer:** thin, quiet, consistent — page number + section, as in the CBOE deck.
- **Accent discipline:** accent colour is for labels, key numbers, milestone markers, table header rows,
  statement slides and the golden-thread chip only. Everything else stays ink/grey on white.
- **Golden-thread chip (C11):** appears on **every content slide except the cover (1), the white Team page
  (21) and the closing contact slide (24)** — on slide 24 the full-width contact bar is the brand element.
- **Icons/dividers:** simple line style, matching the CBOE deck.

═══════════════════════════════════════════════════════════════════════
## B. COMPONENT LIBRARY (define once, reuse by reference below)
═══════════════════════════════════════════════════════════════════════
- **C1 — Masthead** — running header "Cushman & Wakefield | Corum" + slide no.
- **C2 — Section header** — UPPERCASE label + one sentence-case descriptor beneath (CBOE signature).
- **C3 — Statement slide** — full-bleed accent/ink background, large minimal type, short triad line.
- **C4 — Value triple** — three equal pillars in a row with icon + heading + supporting line.
- **C5 — Numbered journey** — numbered steps grouped into phases with durations + decision gates.
- **C6 — Card row** — 2/3/4/5 equal cards, accent header bar, title + bullets/body.
- **C7 — Data table** — accent header row, hairline rules, generous padding; RAG dots red/amber/green.
- **C8 — Node diagram** — clean nodes + connectors, C&W as the highlighted hub.
- **C9 — Comparison panels** — two side-by-side panels with contrasting header treatment.
- **C10 — Case card** — image block + short project descriptor ("A sneak preview of C&W projects" style).
- **C11 — Golden-thread chip** — small accent chip: "CORUM DECIDES · C&W DELIVERS · PwC ALIGNED".
- **C12 — Contact block** — CBOE contact-page style (name, role, mobile, email).

═══════════════════════════════════════════════════════════════════════
## C. SLIDE-BY-SLIDE STYLING (all 24 — keep copy/structure; apply the named components)
═══════════════════════════════════════════════════════════════════════

**1 — Cover.** CBOE cover style: full-bleed hero photo of Westgate I with a subtle dark gradient for legible
white type. Title "WESTGATE I — PARIS PROOF"; accent sub-line "Your single point of control — delivering
Paris Proof with tenant PwC fully aware and aligned"; small line "Project Management Proposal · Corum A.M. ·
July 2026". Thin accent rule under the hero. C&W logo top-right or bottom-right per CBOE. No masthead here.

**2 — Executive summary (SCQA).** C1 + C2 (label "EXECUTIVE SUMMARY" + the action title as descriptor).
Render the four SCQA rows as a vertical stack: left ink/accent tab (SITUATION / COMPLICATION / QUESTION /
ANSWER) + light panel body; give QUESTION and ANSWER the accent tab so they pop. C11 in the footer. This
slide must read as the whole argument on one page.

**3 — Contents.** C1 + C2 ("CONTENTS" + "How this proposal is built"). Six numbered blocks (01–06) as a
clean CBOE index row/grid: big accent number, uppercase title, one grey descriptor line. No chrome overload.

**4 — Situation.** C1 + C2. Left: four fact rows (label + value) with hairline dividers (CBOE table calm).
Right: an accent-tinted "WHAT THIS MEANS FOR CORUM" panel (the three-assets-at-stake list). Keep it airy.

**5 — Complication.** C1 + C2. Use C6 (three cards) for the three forces, each with an accent header bar
("01 THE TENANT RISK", etc.), an italic accent sub-line, and body. Bottom: one ink strapline (the
"compound vs. controlled" sentence). C11.

**6 — Governing answer.** C3 statement slide (full accent or ink background). Big: "Make Cushman & Wakefield
your single point of control." Supporting paragraph in lighter weight. Add the CBOE-style triad line
**"One programme. One accountable partner. PwC aligned."** and the C11 chip styled prominently (this
statement slide keeps the chip, but drops the C1 masthead and C2 header). A breather slide.

**7 — Our answer (three columns).** C1 + C2. C6 with three cards: **"PwC FULLY AWARE & ALIGNED"**,
**"WE ORGANIZE THE SUSTAINABILITY WORKS"**, **"WE KEEP YOU IN CONTROL FROM AFAR"**. Give card 1 and card 3
the accent header, card 2 the ink header (rhythm). Bottom ink strapline. C11.

**8 — Playing field.** C1 + C2. C8 node diagram: Corum, PwC, M3E, Contractor as nodes; **C&W as the accent
hub in the centre** with connectors to all four. Left: a small "THE PARTIES" legend list. Keep whitespace.

**9 — Two routes (M3E).** C1 + C2. C9 two comparison panels: PREFERRED (accent header) vs. ALTERNATIVE (ink
header), bulleted. Bottom: accent-tinted banner — "C&W makes the choice decision-ready… phased, floor-by-
floor, tenant-first." Add a tiny source note "Based on M3E scenario notes, 9 Feb 2026". C11.

**10 — Deep dive 1: deliver with PwC aware & aligned.** C1 + C2 (label "DEEP DIVE 1 OF 2"). Intro paragraph
across the top. Then C6 as a 2×2 of four blocks: ONE FAMILIAR INTERFACE · ACTIVELY INVOLVED IN DECISIONS ·
CONTINUOUS INSIGHT & TIMELY NOTICE · FULL CONFIDENCE, PROTECTED VALUE. Pull the phrase "PwC experiences full
confidence that the project is under control" out as an accent highlight. C11.

**11 — Deep dive 2: organize the works.** C1 + C2 ("DEEP DIVE 2 OF 2"). Intro paragraph, then C5-lite: five
numbered steps in a row — SCOPE → TENDER → BUILD → COMMISSION → PARIS PROOF — with accent numbers and
connecting arrows (mirror the CBOE journey styling). Bottom ink strapline about one accountable owner. C11.

**12 — Success factors.** C1 + C2. Style as C4 value-pillars extended to four (or a 2×2 of C6 cards):
TENANT SATISFACTION FIRST · PHASED DELIVERY IN A LIVE BUILDING · CLEAR GOVERNANCE & DECISION RIGHTS ·
NO SURPRISES. Each with a simple line icon in accent. C11.

**13 — The journey.** C1 + C2 ("THE JOURNEY" + "From today to Paris Proof…"). This is the hero **C5**: a
horizontal numbered timeline with accent milestone diamonds — TODAY → MOBILISE → DECIDE → TENDER → BUILD →
PARIS PROOF, alternating labels above/below the line, each with date + one line. Add a discreet footnote:
"Indicative — to be validated with M3E design planning & the Paris Proof deadline". C11.

**14 — Engagement model.** C1 + C2. C6 four phase-cards with arrows (Phase 0 accent-highlighted): PHASE 0
PREPARATORY · PHASE 1 PM PREPARATION · PHASE 2 PM EXECUTION · PHASE 3 BUILDING CONSULTANCY. Bottom accent-
tint banner: "Each phase is a separate assignment… you decide, phase by phase." Mirror the CBOE phase-bar
look (e.g. "| 16W", "| 20W") by showing indicative durations on each card. C11.

**15 — Planning.** C1 + C2. Style the indicative Gantt as a clean CBOE schedule: quarter columns
(Q3 2026 → 2029), grey task bars, **accent bars/diamonds for C&W-owned milestones**, a small legend
"■ accent = decision / milestone owned by C&W", and the footnote about validation. Keep it uncluttered. C11.

**16 — Organisation (two-PM).** C1 + C2. C8 org chart: Corum + PwC on top; **the two PM boxes (Stakeholder
Management PM, Technical PM) as the accent heart**; M3E + Contractor below; connectors. Bottom ink strapline
"one guards the relationship, one guards the technique". C11.

**17 — Governance & decision rights.** C1 + C2. C7 table (RACI): columns DECISION AREA · CORUM · C&W ·
PwC/M3E · SITS WITH; accent header row; emphasise the CORUM "DECIDE" and C&W "MANAGE/DIRECT" cells in accent.
Below: the italic line about the full team being personally introduced at the outset. C11.

**18 — Reporting.** C1 + C2 ("REPORTING" + "You stay fully in control from Paris — on one page a month").
Left: the four questions (schedule/budget/PwC/decisions) as a tidy list. Right: a CBOE-style dashboard
mock-up — a 2×3 grid of metric tiles (SCHEDULE, BUDGET, TENANT (PwC), RISK, DECISIONS DUE, PROGRESS) each
with a RAG dot placeholder. Keep "[ dashboard mock-up ]" visible. C11.

**19 — Risk.** C1 + C2 ("RISK" + "We manage risk as asset-value protection…"). C7 table: # · RISK ·
THREATENS · MITIGATION · OWNER · RAG. Accent header; **RAG dots red/amber/green**; THREATENS column in accent
(Tenancy/Budget/Deadline). Footnote: "Illustrative — full register produced in Phase 0". C11.

**20 — Why C&W.** C1 + C2. C6 2×2 cards: WE SPEAK INVESTOR · WE MANAGE CORPORATE OCCUPIERS · WE ARE ONE
INTEGRATED PARTNER · WE ARE LOCAL, FOR A REMOTE OWNER. Echo CBOE's "single point of accountability" language
visually (accent keyword highlights). C11.

**21 — Team.** **LEAVE BLANK / WHITE ON PURPOSE.** Only the small section label "05 — TEAM" in the margin
and the page number. No masthead body, no photos, no placeholders, no filler. (Do NOT apply the CBOE team
grid here — it stays empty by design; the grid will be added later when the team is confirmed.)

**22 — Track record.** C1 + C2 ("…we have done exactly this…"). C10 case cards ×4: image block + REFERENCE n
+ short descriptor (size · C&W role · outcome: tenant retained, on time, on budget), CBOE "A sneak preview of
C&W projects" styling with a "Project & Development Services" style footer label. Keep "[ FOTO ]" markers. C11.

**23 — Fee.** C1 + C2 ("FEE" + "A fee structured as a phased investment…"). Left: C7 fee table per phase
(Phase 0–3) with "€ [ • ]" amounts and accent totals. Right: an accent-tinted "RATE CARD (REFERENCE)" panel
(the hourly rates) mirroring the CBOE cost-structure page. Bottom: a white "WHY THIS STRUCTURE WORKS FOR
CORUM" panel with the assumptions/exclusions (DNR 2011). Keep all "€ [ • ]" and "XX" markers. C11.

**24 — 2030 vision + the decision.** Hybrid: top third = C3 statement band ("Picture Westgate I in 2030" +
vision paragraph on ink/accent). Bottom two-thirds = "THE DECISION WE ASK YOU TO MAKE NOW" as five numbered
steps (accent number chips), ending in a full-width accent C12 contact bar (Sjoerd Bezemer + Frank Okker).
This is the emotional close — make it confident and clean.

═══════════════════════════════════════════════════════════════════════
## D. DO NOT
═══════════════════════════════════════════════════════════════════════
- Do not reorder, add or remove slides; do not rewrite copy; do not populate the Team page.
- Do not use colours, fonts or effects that are not present in the CBOE deck.
- Do not convert placeholders into invented content — keep "€ [ • ]", "[ FOTO ]", "[ GANTT ]", "XX" visible.
- Masthead (C1) and section header (C2) appear on every content slide except the cover (1), the two
  statement slides (6, 24) and the white Team page (21). The golden-thread chip (C11) appears on every
  content slide except the cover (1), the white Team page (21) and the closing contact slide (24).
  Do not drop these elements anywhere else.

═══════════════════════════════════════════════════════════════════════
## E. OUTPUT
═══════════════════════════════════════════════════════════════════════
A fully styled, presentation-ready **PPTX** in C&W CBOE house style — same 24-slide structure and order as
the wireframe, editable (real text boxes and shapes), all placeholder markers intact, and the Team page left
deliberately white. Deliver all 24 slides in one deck.
