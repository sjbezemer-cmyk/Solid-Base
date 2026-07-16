# cw-pitch-factory (skill)

Bouwt een C&W PDS-pitch van e-mails tot een Claude Design-pakket. Opbouw altijd hetzelfde; alleen
team, gebouw en hoofdvraag wisselen. Zie `SKILL.md` voor de stappen.

## Assets
| Bestand | Wat |
|---|---|
| `SKILL.md` | Het brein — de 6 stappen (intake → content → tokens → proof → handoff → vault) |
| `assets/intake-schema.json` | De variabelen (het enige dat wisselt) |
| `assets/narrative-template.md` | De vaste 24-slide ruggengraat → vul → `slides.json` |
| `assets/slides.example.json` | Voorbeeld-spec (Corum) + het JSON-formaat per slide-type |
| `assets/house-style-tokens.json` | Gemeten CBOE-huisstijl (navy/amber + fonts) |
| `assets/generate_proof.py` | **Parametrische generator**: slides.json + tokens → proof.pptx |
| `assets/render_pptx.py` | PIL-renderer = "ogen" (pptx → PNG, nooit blind bouwen) |
| `assets/sample_colours.py` | Kleuren pixel-exact uit een referentie-screenshot |
| `assets/brief-template.md` | De Claude Design go-brief (vul {{vars}}) |
| `assets/qa-checklist.md` | QA-gate vóór handoff |

## Snelstart (proof uit een spec)
```
python3 assets/generate_proof.py slides.json assets/house-style-tokens.json proof.pptx
python3 assets/render_pptx.py proof.pptx        # bekijk de PNG's
```

## Nieuw referentiedeck? (kleuren meten)
```
python3 assets/sample_colours.py slide.png                # palet-basis
python3 assets/sample_colours.py slide.png X1 Y1 X2 Y2    # accent (amber/rood) uit een crop
```
Fonts: bevestig in PowerPoint (Ontwerp → Varianten → Lettertypen).

## Principes
1. Referentie + tokens + "ogen" aan de vóórkant.
2. Content (Claude Code + Fabel) en visuele finish (Claude Design) strikt gescheiden — nooit het
   eind-design in code.
