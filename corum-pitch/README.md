# C&W PDS Pitch-Engine — 3-prompt workflow (herbruikbaar)

Een vaste, herbruikbare manier om van ruwe input (mail aan de klant, adviseursnotities, een bestaande
C&W-deck) naar een verzendklare pitch te komen — op MBB-niveau en in C&W-huisstijl. Ontwikkeld voor de
**Corum / Westgate I "Paris Proof"**-pitch, maar bewust zo opgezet dat je hem **elke keer** kunt inzetten.

## De 3 stappen
1. **Prompt 1 → Fabel 5** — verhaal + copy aanscherpen tot een slide-voor-slide **spec** (SCQA, action titles).
2. **Prompt 2 → Claude Design** — van die spec **alleen een wireframe** (grijs, low-fidelity).
3. **Prompt 3 → Claude Design** — CBOE **look-and-feel** als styling-pass over het goedgekeurde wireframe.

> Waarom deze volgorde: eerst **inhoud/structuur**, dan **visuele skin**. Het model ontwerpt niet voordat de
> boodschap staat; je kunt de wireframe eerst met Frank/klant-oog checken; de huisstijl wordt een
> herbruikbare thema-laag.

## Bestanden
| Bestand | Wat |
|---|---|
| `prompt-1-fabel5.md` | Prompt 1 — Corum-versie (ingevuld) |
| `prompt-2-claude-design.md` | Prompt 2 — Corum-versie (wireframe) |
| `prompt-3-claude-design-styling.md` | Prompt 3 — Corum-versie (super gedetailleerd, per slide) |
| `TEMPLATE-prompts-reusable.md` | **De 3 prompts met `{{variabelen}}` — voor élke volgende pitch** |
| `wireframe-outline.md` | Structuur + de 3 verbeterrondes + slide-overzicht |
| `Corum-Westgate-I-Pitch-Wireframe.pptx` | Het wireframe (24 slides, teampagina wit) |
| `build_wireframe_v2.py` | Generator van het wireframe |

## Herbruik-checklist (voor de volgende pitch)
1. **Verzamel input:** je samenvattingsmail aan de klant, de adviseursnotities, en een bestaande
   C&W-deck als visuele referentie (bv. de CBOE-deck).
2. **Vul de variabelen** in `TEMPLATE-prompts-reusable.md` (tabel bovenaan).
3. **Prompt 1 in Fabel 5** (met de bronbestanden als context) → slide-voor-slide spec.
4. **Prompt 2 in Claude Design** (met de spec) → wireframe. Review met Frank/klant-oog.
5. **Prompt 3 in Claude Design** (met wireframe + de referentie-C&W-deck) → gestylede deck.
6. **Vul de placeholders** (fee, referenties, team), laat tekenen, verstuur.

## Vaste principes (blijven altijd gelijk — dít maakt het "C&W-grade")
- **SCQA** executive summary die op zichzelf staat (antwoord eerst / pyramid principle).
- **Action titles**: elke slidetitel is de conclusie, niet het onderwerp.
- **Golden thread** als terugkerende chip: `KLANT DECIDES · C&W DELIVERS · HUURDER ALIGNED`
  (op elke content-slide, behalve cover, teampagina en slotslide).
- **Teampagina bewust wit** tot het team bevestigd is.
- **CBOE-huisstijl** als visuele referentie (masthead, sectielabel + descriptor, statement-slides,
  numbered journey, cost-structure tabellen, case-cards).
- **Beleggerstaal**: asset value, tenant retention, de-risking, exit value.
- **Placeholders zichtbaar** (`€ [ • ]`, `[ FOTO ]`) tot ze definitief ingevuld worden.
