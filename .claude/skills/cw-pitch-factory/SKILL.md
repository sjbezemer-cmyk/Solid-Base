---
name: cw-pitch-factory
description: >
  Bouwt een Cushman & Wakefield PDS-pitch/voorstel van e-mails tot een kant-en-klaar
  Claude Design-pakket. Gebruik deze skill wanneer Sjoerd vraagt om "een pitch / voorstel /
  offerte-deck te maken/starten" voor een klant of gebouw, of "start de pitch factory".
  De opbouw is altijd hetzelfde (24-slide narratief, SCQA, golden thread, CBOE-huisstijl);
  alleen klant, gebouw, hoofdvraag, team, adviseur+scenario's, fee en referenties wisselen.
license: Proprietary — C&W intern.
---

# C&W Pitch Factory

Van e-mails → content → gemeten huisstijl → proof → **Claude Design-pakket**. Twee principes:
1. **Referentie + tokens + "ogen" aan de vóórkant** (meet kleuren/fonts vóór je style).
2. **Content (Claude Code + Fabel) en visuele finish (Claude Design) strikt gescheiden** — maak nooit
   het eind-design in code; de generator levert alleen een *proof*.

Alle assets staan in `assets/` (paden hieronder zijn relatief aan deze skill-map).

## Stappen

### 1 · INTAKE  (Opus)
- Lees de bronnen met de beschikbare MCP-tools:
  - **Outlook**: `outlook_email_search` + `read_resource` — zoek de **samenvattingsmail aan de klant**
    (het gespreksverslag), adviseursnotities en updates.
  - **Vault**: `vault_search`/`vault_read` — bestaande projectnotitie.
  - **Referentiedeck**: een bestaande C&W-pitch (bv. CBOE) als huisstijl-referentie.
- Vul **`assets/intake-schema.json`** → `intake.json`. Toon een korte samenvatting en vraag **alleen de
  ontbrekende** variabelen (klant, gebouw, hoofdvraag, team, adviseur+scenario's, fee-basis, referenties, taal).
- Extraheer **letterlijke sleutelzinnen** uit de samenvattingsmail (`client_own_words`) — die verwerken we in het deck.

### 2 · CONTENT  (Opus → optioneel Fabel 5)
- Vul **`assets/narrative-template.md`** met de intake-variabelen → een `slides.json` in het formaat van
  **`assets/slides.example.json`** (types: cover · scqa · contents · cards · statement · table · kpi ·
  timeline · fee · blank · closing).
- Regels: **SCQA**-executive summary die op zichzelf staat · **action titles** (titel = conclusie) ·
  golden thread · twee deep-dives (huurder aligned + werken organiseren) · **teampagina blijft leeg** ·
  bedragen als `€ [ • ]`. Meer tekst is goed.
- Wil je copy-finesse: draai Fabel 5 op de teksten vóór je `slides.json` finaliseert.

### 3 · BRAND TOKENS  (Opus)
- Laad **`assets/house-style-tokens.json`** (CBOE navy/amber al gemeten). Bij een **nieuw** referentiedeck:
  vraag 1 screenshot van een slide → **sample de kleuren pixel-exact** (PIL, zie `assets/sample_colours.py`),
  en vraag de **fonts** uit het PPTX-thema (Ontwerp → Varianten → Lettertypen). Werk de tokens bij.

### 4 · PROOF + PAKKET  (Opus)
- Bouw de proof: `python3 assets/generate_proof.py slides.json assets/house-style-tokens.json proof.pptx`
- **Render en kijk** (nooit blind): `python3 assets/render_pptx.py proof.pptx` → controleer visueel.
- **QA-gate**: loop `assets/qa-checklist.md` af; los alles op vóór handoff.
- Genereer de **`assets/brief-template.md`** ingevuld → `CLAUDE-DESIGN-BRIEF.md` (tokens + layoutsysteem +
  per-slide + regels).

### 5 · HANDOFF  (mens → Claude Design)
- Lever het pakket + attach-lijst: **`slides.json`/`spec.md`** (copy) · **referentiedeck-PDF** (visueel/fonts) ·
  **proof.pptx** (kleur/layout-proof) · **CLAUDE-DESIGN-BRIEF.md** (plakken). Bevestig eerst de fonts.

### 6 · VAULT  (Opus)
- Leg status, `intake.json` en tokens vast in de vault (`Projects/CW/...`), gekoppeld aan
  `Resources/CW-huisstijl-en-pitch-referentie.md` en `Resources/CW-pitch-factory-proces-en-skill.md`.

## Vaste 24-slide ruggengraat (zie `assets/narrative-template.md`)
Cover · Exec summary (SCQA) · Contents · Situation · Complication · Governing answer · Our answer ·
Playing field · Two routes (adviseur) · Deep dive 1 (huurder aligned) · Deep dive 2 (werken organiseren) ·
Success factors · The journey · Engagement model · Planning · Organisation · Governance · Reporting · Risk ·
Why C&W · **Team (LEEG)** · Track record · Fee · The decision (2030 + next steps).

## Do / Don't
- **Do**: meet tokens vóór styling · render elke proof · houd placeholders zichtbaar · teampagina wit.
- **Don't**: het eind-design in code afmaken · kleuren/fonts benaderen · slides herordenen of copy herschrijven bij styling.
