# RUN-SHEET — Corum pitch doorlopen (Fabel + Claude Code)

> Start hier. Alles staat in deze map (`corum-pitch/`). Zie ook `README.md`.
> Golden thread: **CORUM DECIDES · C&W DELIVERS · PwC ALIGNED**.

## Stap 0 — keuzes (STATUS 16 jul)
1. **Taal deck:** ✅ Engels (blijft).
2. **Fee:** ✅ per-fase bedragen als placeholders; **rate card slide 23 gevuld** met actuele 2026 C&W PDS-tarieven (PM €145 · Sr PM €155 · Cost €145 · Associate Director €175 · Partner €250, excl. btw).
3. **Referenties (slide 22):** ✅ placeholders laten; jij levert later 3–4 projecten.
4. **Planning:** ✅ indicatief houden (2026→2029, "te valideren met M3E"). ⏳ **ACTIE:** M3E-uitvoeringsplanning / jaartallen opvragen bij Björn van der Lande (M3E) — zit niet in onze systemen; daarna journey (13) + planning (15) bijwerken.

## Route A — Snel (als copy al goed is)
Bestaand `Corum-Westgate-I-Pitch-Wireframe.pptx` → direct **Prompt 3** (`prompt-3-claude-design-styling.md`)
in Claude Design, met `CBOE pitch July 15 2026.pdf` erbij. Klaar in 1 stap.

## Route B — Volledig (copy nog aanscherpen)
1. **Fabel 5 — `prompt-1-fabel5.md`** (+ `wireframe-outline.md`, M3E-notities, optioneel CBOE-deck)
   → slide-voor-slide spec. Check: SCQA · action titles · 2 deep-dives · teampagina leeg · golden thread.
2. **Claude Code/Design — `prompt-2-claude-design.md`** (+ de spec) → grijs wireframe.
   Alternatief: Claude Code draait `python3 build_wireframe_v2.py` (regenereert het wireframe).
   Check: 24 slides · teampagina wit · chip op juiste slides · placeholders zichtbaar.
3. **Review** wireframe (Frank/klant-oog).
4. **Claude Design — `prompt-3-claude-design-styling.md`** (+ wireframe + **CBOE-PDF**) → gestyled deck.
   Check: CBOE-look · structuur ongewijzigd · teampagina wit · placeholders intact.

## Afronden
Placeholders vullen (fee, referenties, team) → laten tekenen → versturen aan **Dirk Hooiveld + Marcus
Dillon**, opvolgafspraak plannen. NDA via Dentons; daarna Corum–PwC- en Corum–M3E-info verwerken.

## Voor de Claude Code-sessie
- Branch: `claude/corum-pitch-wireframe-6g356g`. Deck + prompts + generator staan in `corum-pitch/`.
- Wireframe regenereren: `python3 corum-pitch/build_wireframe_v2.py` (vanuit repo-root).
- Herbruikbaar voor volgende pitches: `TEMPLATE-prompts-reusable.md` (3 prompts met `{{variabelen}}`).
