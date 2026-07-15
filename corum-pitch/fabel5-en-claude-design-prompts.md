# Twee prompts: eerst Fabel 5, daarna Claude Design (alleen wireframe)

Werkwijze:
1. **Stap 1 — Fabel 5.** Plak Prompt A in Fabel 5. Voeg als context toe: `wireframe-outline.md`,
   de M3E-samenvattingen en (optioneel) de ESA-pitch als stijl-/niveaureferentie. Fabel 5
   levert een aangescherpte, definitieve **slide-voor-slide wireframe-spec** (alleen tekst/structuur).
2. **Stap 2 — Claude Design.** Plak Prompt B + de output van Fabel 5 in Claude Design. Claude
   Design levert **alleen een wireframe** (low-fidelity, grijze blokken) — nog geen afgewerkt ontwerp.

---

## PROMPT A — voor Fabel 5 (scherpstellen van verhaal + copy)

> Je bent een senior pitch-strateeg op MBB-niveau (denk McKinsey/BCG) én ervaren project­management-
> adviseur in vastgoed. Ik bereid een pitch voor van **Cushman & Wakefield (C&W) PDS Netherlands**
> aan **Corum A.M.** (Franse institutionele vastgoedbelegger; contact: Dirk Hooiveld, Marcus Dillon)
> voor het **project management van de "Paris Proof"-verduurzaming van Westgate I** in Amsterdam.
>
> **De één-zin-kernboodschap die door álles heen moet lopen:** *Maak C&W je single point of control
> in Nederland — wij managen PwC namens Corum én organiseren de volledige verduurzaming, zodat
> Corum beslist en C&W levert.* ("CORUM DECIDES · C&W DELIVERS")
>
> **Harde feiten (moeten kloppen):**
> - Gebouw: Westgate I, Thomas R. Malthusstraat 5, 1066 JR Amsterdam, ± 27.000 m², volledig verhuurd
>   aan **PwC**, gebouw volledig in gebruik.
> - Doel: technisch verduurzamen tot **Paris Proof — een harde contractuele verplichting** met vast budget.
> - Twee technische scenario's van adviseur **M3E** (9 feb 2026): (1) VOORKEUR = laagtemperatuur-WKO +
>   klimaatplafonds, volledige vervanging gasinstallatie, energiecentrale in kelder, gefaseerd per
>   verdieping, toekomstvast; (2) ALTERNATIEF = lucht-water warmtepomp + behoud VAV-inductie + VRF-
>   naregeling + nieuw DX-blok, minder ingrepen maar restlevensduur VAV ± 6–9 jaar → tweede ingreep later.
> - Rol C&W: project manager namens de eigenaar; **twee-PM-model** — een Stakeholder Management PM
>   (huurderrelatie, communicatie, besluitvorming) en een Technical PM (techniek, directievoering,
>   afstemming M3E, tender & uitvoering).
> - Gefaseerde opdracht: Fase 0 voorbereidende opdracht → daarna 3 losse opdrachten (PM Preparation,
>   PM Execution, Building Consultancy/kwaliteitsinspecties). Corum beslist per fase.
> - Les uit eerder Corum-project (Rotterdam): gebrekkige communicatie → huurderontevredenheid. Daarom:
>   huurdertevredenheid voorop, gefaseerd in een gebruikt gebouw, heldere governance, no surprises.
> - Vervolg: NDA via Dentons; daarna inzicht in Corum–PwC-overeenkomst en Corum–M3E-afspraken.
>
> **Wat ik van je wil (lever exact dit):**
> 1. Een **slide-voor-slide wireframe-spec** voor een deck van ± 22–24 slides, in het **Engels**, met
>    per slide: (a) een **action title** = de conclusie, niet het onderwerp; (b) een korte **kicker/sectie­label**;
>    (c) de **bodytekst/bullets** in definitieve, wervende maar zakelijke copy; (d) een korte **layout-hint**
>    (bijv. "3 kolommen", "tijdlijn", "RACI-tabel"). Meer tekst is goed — dit is inhoudelijk, geen tagline-deck.
> 2. Volg deze verhaallijn (chronologisch, pyramid principle): **Situation → Complication → Question →
>    Answer (SCQA)** in een executive summary die op zichzelf staat; dan *What we take off your plate*
>    met twee expliciete deep-dives ("We manage PwC for you" en "We organize the works"); dan de
>    *Journey* (tijdlijn vandaag → Paris Proof) met fasering en planning; dan *How we stay in control*
>    (organisatie, governance/decision rights, rapportage, risico als asset-value-bescherming); dan
>    *Why C&W*, **een bewust WITTE teampagina**, track record; en tot slot fee (gefaseerd), 2030-visie
>    en de concrete beslissing die we van Corum vragen.
> 3. Denk als een belegger: gebruik taal als asset value, tenant retention, de-risking, exit value.
> 4. Houd alle bedragen als placeholders (`€ [ • ]`) en markeer alles wat nog ingevuld moet worden.
> 5. **De teampagina blijft leeg** — alleen sectielabel "Team", verder niets.
>
> Output: één gestructureerd document, klaar om als input aan een wireframe-tool te geven. Geen opmaak-
> of kleuradvies — puur verhaal, titels en copy.

---

## PROMPT B — voor Claude Design (ALLEEN een wireframe)

> Build a **low-fidelity WIREFRAME only** — not a finished, styled deck — for a 16:9 project-management
> pitch from **Cushman & Wakefield** to **Corum A.M.** for the "Westgate I — Paris Proof" sustainability
> upgrade in Amsterdam. Use the attached slide-by-slide spec verbatim for structure and copy.
>
> **This is explicitly a wireframe:**
> - Greyscale / blueprint look. Light-grey placeholder blocks with thin dashed outlines for every image,
>   logo, chart, table and diagram. Label each placeholder ("[ PHOTO ]", "[ ORG CHART ]", "[ GANTT ]",
>   "[ LOGO ]").
> - Show real text (titles, kickers, body copy from the spec) so the narrative is readable, but do **not**
>   apply finished visual design: no photography, no polished icons, no gradients, no fine typography work.
> - One thin **red (#C3002B) accent** is allowed as a wireframe marker for section spine, milestones and
>   the recurring footer badge "CORUM DECIDES · C&W DELIVERS"; everything else stays greyscale.
> - Keep every layout hint from the spec (columns, timeline, RACI table, phase cards, SCQA blocks).
> - Consistent margins and a visible grid; page numbers and the footer "CUSHMAN & WAKEFIELD | CORUM A.M."
> - **Slide "Team" must be left blank on purpose** — only the small "Team" section label, nothing else.
> - Keep all placeholder markers ("€ [ • ]", "[ PHOTO ]") visible and easy to find.
>
> Deliver the wireframe as editable slides (real text boxes and placeholder shapes), one per spec slide,
> in the same order. Do not proceed to a high-fidelity design — wireframe only.
