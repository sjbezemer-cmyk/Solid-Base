# Strategie — CBOE look-and-feel (fonts + kleuren) overzetten naar de Corum-pitch

Doel: de Corum-pitch dezelfde **fonts en kleuren** (en algehele look-and-feel) geven als de CBOE-deck,
via een **prompt** die je in Claude Design (of Fabel) draait — betrouwbaar en herbruikbaar.

## Kerninzicht (uit online research)
"Match de bijgevoegde deck" alleen werkt slecht: AI-designtools **samplen kleuren/fonts inconsistent**.
De robuuste, herhaalbare industrie-aanpak is **"design tokens first"**:
1. **Extraheer** de merk-tokens (kleuren-hex, fontnamen, type-scale, spacing) uit de referentie.
2. **Zet dat tokenblok letterlijk bovenaan de prompt** (een mini-`DESIGN.md` / "prompt-fragment").
3. **Voeg de referentie-deck als bijlage toe** voor lay-out/gevoel.
→ Tokens = deterministische kleur/font-match · bijlage = lay-out & sfeer.

Bronnen bevestigen: sla kleuren/typografie/spacing op als gestructureerd bestand en laat de AI daaruit
putten voor consistente output; vertaal tokens naar een herbruikbaar promptfragment
("Brand palette: … Typography: … Style: …") dat je vóór elke opdracht plakt.

## Stap 1 — Haal de EXACTE CBOE-tokens op (kies één; ~2 min)
1. **Uit de PPTX-thema (beste):** open `CBOE pitch July 2026.pptx` in PowerPoint →
   tab **Ontwerp/Design → Varianten → Kleuren → Kleuren aanpassen** = exacte thema-hex;
   **Lettertypen** = kop- en bodyfont. (Of **Beeld → Diamodel** voor themakleuren/fonts.)
2. **Pipet:** voeg een vorm in → Opvulling → **Pipet** over het CBOE-rood/charcoal/grijs → "Meer kleuren" toont hex.
3. **Automatische extractor:** upload de CBOE-**PDF** naar een brand-extractor (StyleExtract, Brandparser,
   Brandfetch, dembrandt) → krijg een `DESIGN.md`/token-JSON met kleuren + fonts.

## Stap 2 — Het tokenblok (GEMETEN uit de CBOE-slides, 16 jul 2026)
Pixel-exact gesampled uit screenshots van de CBOE-pitch (twee overeenkomende samples per kleur).
**De echte CBOE-look is navy + amber + wit — NIET rood/charcoal.**
```
BRAND TOKENS — CBOE / Cushman & Wakefield (gemeten)
Colours
  --navy    #1F1942   PRIMAIR donker — achtergronden, cards, koppen & body op licht
  --amber   #F4B634   ACCENT — sectielabels, titels, pull-quotes, data, kerncijfers
  --white   #FFFFFF   lichte achtergronden en tekst op navy
  --cream   #F4EFE6   subtiel warm off-white paneel
  --grey    #6B6467   captions / secundaire tekst
Fonts
  Sectielabels / titels / body : Arial   (sectielabel = Arial Bold, HOOFDLETTERS, amber)
  Taglines & pull-quotes       : serif — Chronicle Display italic (fallback Georgia), meestal amber
Type scale
  H1/titel 26–32pt · SECTIELABEL 12–13pt HOOFDLETTERS bold amber · descriptor 14–16pt navy ·
  body 9–11pt · caption 8pt
Stijl
  Navy + amber + wit, editorial, veel witruimte. Amber HOOFDLETTER-sectielabel met navy sentence-case
  descriptor eronder. Statement-slides & cards in navy met witte tekst; amber voor de kernregel.
  Korte taglines in serif italic ("Better never settles"). Header linksboven "Cushman & Wakefield | [klant]".
```

## Stap 3 — Zet het tokenblok bovenaan de styling-prompt
Prepend dit boven `prompt-3-claude-design-styling.md`, met deze regel eronder:
> "Gebruik de BRAND TOKENS hierboven **exact** (kleuren-hex en fontnamen letterlijk — niet benaderen).
> Alles wat hier niet is gespecificeerd, sample je uit de bijgevoegde CBOE-deck. Bijlagen: (1) het
> goedgekeurde wireframe, (2) `CBOE pitch July 15 2026.pdf`."

Zo krijg je: **deterministische kleur/font-match** (uit tokens) + **lay-out/sfeer** (uit de bijlage).

## Waarom dit beter is dan mijn eerdere code-poging
- Code-opmaak (python-pptx) heeft geen design-engine → houterig, en ik kon de CBOE-tokens niet uit het
  binaire bestand halen. Claude Design mét exacte tokens + de PDF geeft echt design.
- Het tokenblok is **herbruikbaar** voor elke volgende C&W-pitch (staat ook in de reusable template).

## Bronnen
- Cushman & Wakefield Brand Guidelines (Chronicle/Gotham; **Arial voor Microsoft**; rood + grijs) — brandcolorcode.com, scribd brand guidelines
- COLOURlovers: C&W-rood #DE0025
- MindStudio — "Design Tokens with AI Agents" (tokens-JSON → consistente AI-output)
- StyleExtract / Brandparser / Ad Legends Visual DNA / dembrandt — brand-token-extractie uit URL/bestand
