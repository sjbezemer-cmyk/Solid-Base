# Kioti 2 — PDF-offertes → Master calculatie

Workflow om de **Master_calculatie** Excel (C&W PDS) te voeden met PDF-offertes
en -opdrachten van leveranciers uit OneDrive.

## Analyse van de Master_calculatie (.xlsm)

| Tabblad | Functie |
|---|---|
| Toelichting | Handleiding + stappenplan |
| 1 \| Front cover | Voorblad (verwijst naar tabblad 2) |
| 2 \| Basic principles | Projectgegevens, m², uitgangspunten |
| 3 \| Summary sheet | Totalen per kostencode (100–800), €/m² |
| 4 \| Calculation | Het rekenhart: per post `C` omschrijving, `D` eenheid, `I` partij, `K` aantal, `L` €/eenheid |
| Input Procore budget | Export-laag richting Procore (PRM/RF-splitsing) |
| Measurement sheet | Meetstaten vloeren/wanden |
| Check quote amounts | SUMIF per partijnaam (kolom I) → vergelijk met offertetotaal |

Rekenmechaniek per regel: `M = K×L` (netto inkoop) en
`G = ROUND(K × CEILING(L×M7; afronding))` met `M7` = verborgen opslag
(10% inkoop × 4% onvoorzien ≈ **14,4%**) — kolom G is het klantbedrag,
kolom M het leveranciersbedrag. Er zit **geen VBA** in het bestand.

## Voeden met PDF-offertes — de aanpak

1. **Vind de PDF's**: OneDrive `SJB/Kioti 2/2.3 Aanbesteding & opdrachten/Opdrachten/`
   heeft per leverancier een map (01 SPIE, 02 4SUM, 03 Techno Project,
   04 Kampschreur, 06 Furniture, 07 Techno Telematica, 08 Bureau VanDerVorm,
   09 4all solutions, 10 Hoogwerf, McArt).
2. **Extraheer per PDF**: leverancier, offerte-/PO-nummer, regelomschrijvingen,
   bedragen **excl. btw**. De C&W-opdrachtbevestigingen ("25002 Kioti ... Opdracht ...")
   zijn leidend; offertes zonder opdracht worden gemarkeerd.
3. **Map naar kostencode**: HVAC→210, loodgieter→220, elektra→230,
   toegang/beveiliging→240, IT/data→250, brandveiligheid→260, vloer→311/314,
   wanden→322/323, meubilair→410, losse inrichting→420, AV→430, branding→450.
4. **Schrijf regels** in `4 | Calculation`: omschrijving, `post`, partijnaam,
   K=1, L=nettobedrag, opmerking met PO-/offertenummer.
5. **Check quote amounts**: partijnamen invullen → SUMIF laat per leverancier
   zien of het boek aansluit op de ontvangen offertes.

`build_kioti.py` voert dit uit: reset eerst alle testdata (K=0) en vult daarna
33 regels uit de Kioti 2-PDF's. Output: `output/Kioti 2 - Calculatie inkoop leveranciers.xlsx`.

## Resultaat (5-7-2026)

| Leverancier | Netto excl. btw | Bron |
|---|---:|---|
| Technoproject | € 98.137,00 | opdr. 2500212, 2500430 + **offerte** 1250355 (€18.347, nog geen opdracht) |
| BVDV | € 71.082,52 | opdr. 2500227/282/322/361/277 + 2600011 + **offerte** 202500273 (€2.225, nog geen opdracht) |
| 4Some | € 68.885,00 | opdr. 2500210, 2600012 |
| Techno Telematica | € 55.405,00 | opdr. 2500214, 2500323, 2500359, 2500428 |
| SPIE | € 53.494,74 | opdr. 2500211, 2500429, 2600008 |
| Kampschreur | € 7.136,39 | factuur 20251096 (PO 2500221, meerwerk) |
| McArt | € 3.299,49 | opdr. 2600083 |
| 4all Solutions | € 1.600,00 | opdr. 2500360 |
| Hoogwerf | € 614,81 | opdr. 2500467 |
| **Totaal** | **€ 359.654,95** | geautoriseerd budget: € 575.644 (v3, 30-5-2025) |

Met de verborgen opslag van 14,4% is het klantbedrag (kolom G / totaal O8) ± € 411.462.
