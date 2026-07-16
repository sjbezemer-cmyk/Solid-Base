# 24-slide narratief-template (vast) → vul met intake-variabelen → `slides.json`

De opbouw is altijd hetzelfde. Vul `{{variabelen}}` uit `intake.json`. Per slide staat het
**generator-type** (voor `slides.json`) en wat erin komt. Golden thread overal:
`{{golden_thread}}`. **Slide 21 (Team) blijft leeg.** Bedragen als `€ [ • ]`.

| # | type | Inhoud (action title = conclusie, niet onderwerp) |
|---|---|---|
| 1 | `cover` | "{{building}} — {{objective}}" · subtitle = single-point-of-control belofte · datum |
| 2 | `scqa` | Exec summary op zichzelf: Situation/Complication/Question({{main_question}})/Answer |
| 3 | `contents` | 6 secties (01–06) |
| 4 | `cards` | Situation — feiten {{building}}/{{tenant}}/{{client}} + "what this means" |
| 5 | `cards` | Complication — 3 krachten (huurder/levering/deadline) |
| 6 | `statement` | Governing answer: "Make C&W your single point of control" + triad |
| 7 | `cards` | Our answer — 3: {{tenant}} aware & aligned / organize works / control from afar |
| 8 | `cards` | Playing field — partijen; C&W als hub |
| 9 | `cards` | Two routes ({{advisor}}-scenario's) — vergelijking |
| 10 | `cards` | Deep dive 1 — deliver works, {{tenant}} fully aware & aligned (klant-eigen woorden) |
| 11 | `cards` | Deep dive 2 — organize the works ({{advisor}}-ontwerp → doel) |
| 12 | `cards` | Success factors (4) |
| 13 | `timeline` | The journey — vandaag → {{objective}} (indicatief) |
| 14 | `cards` | Engagement model — {{phasing}} |
| 15 | `timeline`/`table` | Planning (indicatief, te valideren met {{advisor}}) |
| 16 | `cards` | Organisation — {{team.model}}, de twee PM's als hart |
| 17 | `table` | Governance & decision rights (RACI) |
| 18 | `kpi` | Reporting — één pagina/maand |
| 19 | `table` | Risk — RAG; gekoppeld aan huurder/budget/deadline |
| 20 | `cards` | Why C&W (4) |
| 21 | `blank` | **TEAM — LEEG** |
| 22 | `cards` | Track record — referentiekaarten (`[ FOTO ]`, placeholders) |
| 23 | `fee` | Fee per fase (`€ [ • ]`) + rate card 2026 + assumptions (DNR 2011) |
| 24 | `closing` | Picture {{building}} in [jaar] + 5 next steps + contact |

**Vaste tekstpatronen**
- Golden thread: `{{CLIENT}} DECIDES · C&W DELIVERS · {{TENANT}} ALIGNED`.
- Spiegel `client_own_words` letterlijk (governance-frasen uit de samenvattingsmail).
- Beleggerstaal: asset value, tenant retention, de-risking, exit value.
- Rate card 2026 (excl. btw): PM €145 · Sr PM €155 · Cost €145 · Associate Director €175 · Partner €250
  (bevestig per pitch met Frank).

Zie `slides.example.json` voor het exacte JSON-formaat per type.
