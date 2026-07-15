# C&W PDS Pitch-Engine — HERBRUIKBARE TEMPLATES (3 prompts met variabelen)

Vul eerst de variabelentabel. Vervang daarna overal `{{VARIABELE}}` (of laat je editor het doen).
Dan heb je in 3 stappen een verzendklare pitch. Zie `README.md` voor de workflow.

## Variabelen (één keer invullen per pitch)
| Variabele | Betekenis | Voorbeeld (Corum) |
|---|---|---|
| `{{CLIENT}}` | Opdrachtgever | Corum A.M. |
| `{{CLIENT_PROFILE}}` | Type klant + context | Franse institutionele belegger, stuurt op afstand |
| `{{CLIENT_CONTACTS}}` | Contactpersonen | Dirk Hooiveld (Sr. Technical Manager), Marcus Dillon |
| `{{ASSET}}` | Gebouw/project | Westgate I |
| `{{ASSET_ADDRESS}}` | Adres | Thomas R. Malthusstraat 5, Amsterdam |
| `{{ASSET_SIZE}}` | Omvang | ± 27.000 m² |
| `{{TENANT}}` | Huurder | PwC |
| `{{OBJECTIVE}}` | Doel + hardheid | Paris Proof — harde contractuele verplichting, vast budget |
| `{{ADVISOR}}` | Technisch adviseur | M3E |
| `{{TECH_OPTIONS}}` | Scenario's (of "n.v.t.") | LT-WKO+klimaatplafonds vs. lucht-water WP+VRF |
| `{{CW_ROLE_MODEL}}` | Rol/teammodel C&W | twee-PM-model: Stakeholder Mgmt PM + Technical PM |
| `{{PHASING}}` | Fasering | Fase 0 → PM Preparation, PM Execution, Building Consultancy |
| `{{LESSON}}` | Les uit eerder project | Rotterdam: communicatie → huurdertevredenheid |
| `{{OPEN_QUESTIONS}}` | Openstaande vragen/slotvraag | Klant–huurder- en klant–adviseur-afspraken; NDA-first |
| `{{CLIENT_OWN_WORDS}}` | Letterlijke citaten uit je samenvattingsmail | zie Corum-voorbeeld |
| `{{GOLDEN_THREAD}}` | Kernmotief | CORUM DECIDES · C&W DELIVERS · PwC ALIGNED |
| `{{LANGUAGE}}` | Taal deck | Engels |
| `{{REFERENCE_DECK}}` | Bestaande C&W-deck als visuele referentie | CBOE pitch July 15 2026.pdf |
| `{{SLIDE_COUNT}}` | Aantal slides | 24 |

═══════════════════════════════════════════════════════════════════════
## TEMPLATE 1 — Fabel 5 (verhaal + copy → slide-voor-slide spec)
═══════════════════════════════════════════════════════════════════════
> Bijlagen meesturen: je samenvattingsmail aan {{CLIENT}}, de {{ADVISOR}}-notities, en optioneel een
> bestaande C&W-pitch als niveaureferentie.

Je bent een senior pitch-strateeg op MBB-niveau (McKinsey/BCG) én ervaren projectmanagement-adviseur in
commercieel vastgoed. Ik bereid een pitch voor van **Cushman & Wakefield (C&W) Project & Development
Services Netherlands** aan **{{CLIENT}}** ({{CLIENT_PROFILE}}; contacten: {{CLIENT_CONTACTS}}) voor het
**project management van {{OBJECTIVE}} van {{ASSET}} in {{ASSET_ADDRESS}}**.

**De één-zin-kernboodschap die door álles heen moet lopen:** *Maak C&W je single point of control — wij
**leveren** de volledige opgave én houden **huurder {{TENANT}} volledig op de hoogte en aligned**, zodat
{{CLIENT}} beslist en C&W levert.* Golden thread: **"{{GOLDEN_THREAD}}"**.

**Spiegel de eigen woorden van {{CLIENT}} (letterlijk uit mijn samenvattingsmail — gebruik deze frasen):**
{{CLIENT_OWN_WORDS}}

Toon: {{TENANT}} is een **partner die we aligned houden**, níet een probleem waar we {{CLIENT}} van
"afschermen".

**Harde feiten (moeten kloppen):**
- Gebouw: {{ASSET}}, {{ASSET_ADDRESS}}, {{ASSET_SIZE}}, verhuurd aan **{{TENANT}}**, gebouw in gebruik.
- Doel: {{OBJECTIVE}}.
- Technische scenario's van adviseur **{{ADVISOR}}**: {{TECH_OPTIONS}}.
- Rol C&W: project manager namens de eigenaar; **{{CW_ROLE_MODEL}}**.
- Fasering: {{PHASING}}. Klant beslist per fase.
- Les uit eerder project: {{LESSON}}. Daarom: huurdertevredenheid voorop, gefaseerd in een gebruikt
  gebouw, heldere governance, no surprises.
- Slotvraag / openstaande vragen aan {{CLIENT}}: {{OPEN_QUESTIONS}}.

**Wat ik van je wil — lever exact dit:**
1. Een **slide-voor-slide wireframe-spec** voor een deck van **{{SLIDE_COUNT}} slides**, in het
   **{{LANGUAGE}}**, met per slide: (a) een **action title** = de conclusie; (b) een korte
   **kicker/sectielabel**; (c) definitieve, wervende maar zakelijke **bodytekst/bullets** (meer tekst is
   goed); (d) een korte **layout-hint** (bv. "3 kolommen", "tijdlijn", "RACI-tabel").
2. Verhaallijn (chronologisch, pyramid principle): **Situation → Complication → Question → Answer (SCQA)**
   in een executive summary die op zichzelf staat; dan *What we take off your plate* met twee deep-dives:
   **"We deliver the works with {{TENANT}} fully aware and aligned"** en **"We organize the works"**; dan de
   *Journey* (tijdlijn vandaag → einddoel) met fasering en planning; dan *How we stay in control*
   (organisatie, governance/decision-rights, rapportage op afstand, risico als asset-value-bescherming); dan
   *Why C&W*, een **bewust WITTE teampagina**, track record; en tot slot fee (gefaseerd), de eindvisie en de
   concrete beslissing die we van {{CLIENT}} vragen.
3. Denk als een belegger: asset value, tenant retention, de-risking, exit value.
4. Alle bedragen als placeholders (`€ [ • ]`); markeer alles wat nog ingevuld moet worden.
5. **De teampagina blijft leeg** — alleen sectielabel "Team".

Output: één gestructureerd document, klaar als input voor een wireframe-tool. Geen opmaak-/kleuradvies.

═══════════════════════════════════════════════════════════════════════
## TEMPLATE 2 — Claude Design (ALLEEN wireframe)
═══════════════════════════════════════════════════════════════════════
> Bijlage meesturen: de slide-voor-slide spec uit Template 1.

Build a **low-fidelity WIREFRAME only** — not a finished, styled deck — for a 16:9 project-management pitch
from **Cushman & Wakefield** to **{{CLIENT}}** for the "{{ASSET}} — {{OBJECTIVE}}" assignment. Use the
attached slide-by-slide spec verbatim for structure and copy.

**This is explicitly a wireframe (blueprint), not a design:**
- Greyscale / blueprint look. Light-grey placeholder blocks with thin dashed outlines for every image, logo,
  chart, table and diagram, each labelled ("[ PHOTO ]", "[ ORG CHART ]", "[ GANTT ]", "[ RACI TABLE ]", …).
- Show real text (titles, kickers, body copy) so the narrative reads, but **no** finished design: no
  photography, polished icons, gradients or fine typography.
- One thin **red (#C3002B) accent** as a wireframe marker only: left section spine, milestone diamonds, and
  the recurring footer badge **"{{GOLDEN_THREAD}}"**. Everything else greyscale.
- Keep every layout hint from the spec (SCQA blocks, columns, phase cards, timeline, RACI table, comparison
  panels).
- Consistent margins and a visible grid; page numbers and the footer "CUSHMAN & WAKEFIELD | {{CLIENT}}".
- The **golden-thread badge** appears on every content slide **except the cover, the white Team page and the
  closing contact slide**.
- **The "Team" slide is deliberately blank** — only the small "Team" section label, nothing else.
- Keep all placeholder markers ("€ [ • ]", "[ PHOTO ]") visible.

Deliver editable slides (real text boxes and placeholder shapes), one per spec slide, same order. Do **not**
proceed to high-fidelity design — wireframe only.

═══════════════════════════════════════════════════════════════════════
## TEMPLATE 3 — Claude Design (STYLING-PASS: C&W look-and-feel)
═══════════════════════════════════════════════════════════════════════
> Bijlagen meesturen: (1) het goedgekeurde wireframe, (2) **{{REFERENCE_DECK}}** als visuele referentie.

Apply the **exact visual look-and-feel of the attached {{REFERENCE_DECK}}** (the C&W house style) to the
attached approved {{SLIDE_COUNT}}-slide wireframe for the **Cushman & Wakefield → {{CLIENT}} "{{ASSET}} —
{{OBJECTIVE}}"** pitch. This is a **styling pass only**: keep slide order, content, copy, tables, diagrams
and the deliberately white Team page unchanged. Keep every placeholder marker visible.

**Global design system (sample from {{REFERENCE_DECK}}; do not invent):** 16:9, disciplined grid; colour
tokens sampled from the reference deck; matching type scale (bold H1, uppercase accent section label +
sentence-case descriptor, body, caption); masthead "Cushman & Wakefield | {{CLIENT}}" + slide number
top-left; quiet footer; accent used only for labels, key numbers, milestones, table headers, statement
slides and the golden-thread chip.

**Reusable components (define once, apply throughout):** C1 masthead · C2 section label + descriptor ·
C3 statement slide (short triad) · C4 value-triple · C5 numbered journey (phases + durations + decision
gates) · C6 card row (2–5 up) · C7 data table (accent header, RAG dots) · C8 node/org diagram (C&W as hub) ·
C9 comparison panels · C10 case card ("A sneak preview of C&W projects") · C11 golden-thread chip
"{{GOLDEN_THREAD}}" · C12 contact block.

**Apply by slide archetype** (map onto whatever the wireframe contains):
- **Cover** → hero photo of {{ASSET}}, title, accent sub-line, date; no masthead.
- **Executive summary** → C2 + SCQA stack (accent tabs on Question/Answer).
- **Contents** → numbered index (01…) in C&W index style.
- **Situation / Complication** → C2 + fact rows / C6 cards.
- **Governing answer & closing vision** → C3 statement slides with the triad
  "One programme. One accountable partner. {{TENANT}} aligned."
- **What we take off your plate** → C6 three cards ({{TENANT}} aware & aligned / organize the works /
  control from afar).
- **Stakeholder map & organisation** → C8 with C&W as the accent hub; the two PM boxes as the heart.
- **Two scenarios** → C9 comparison panels.
- **Deep dives** → intro paragraph + C6 blocks / C5 numbered steps; pull the client's own confidence phrase
  out as an accent highlight.
- **Journey & planning** → C5 numbered journey + a clean quarter-column Gantt with accent milestones.
- **Governance / risk / fee** → C7 tables (RACI, RAG risk, phased fee + rate card).
- **Why C&W / track record** → C6 cards / C10 case cards with "Project & Development Services" footer.
- **Team** → **LEAVE BLANK / WHITE.** Only the "Team" label. Do not apply the team grid yet.
- **Closing** → C3 vision band + numbered decision steps + full-width C12 contact bar.

**Golden-thread chip (C11):** on every content slide except the cover, the white Team page and the closing
contact slide.

**Do NOT:** reorder/add/remove slides; rewrite copy; populate the Team page; use colours/fonts absent from
{{REFERENCE_DECK}}; turn placeholders into invented content.

**Output:** a styled, presentation-ready **PPTX** in C&W house style, same {{SLIDE_COUNT}}-slide structure,
editable, all placeholders intact, Team page white.
