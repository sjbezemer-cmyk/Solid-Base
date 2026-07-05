---
name: offerte
description: Voeg een PDF-offerte, opdrachtbevestiging of factuur toe aan een projectcalculatie (Master_calculatie Excel). Gebruik bij "voeg offerte toe", "verwerk deze PDF in de calculatie", "nieuwe opdracht voor project X", of bij het aanmaken van een nieuw calculatieproject.
---

# Offerte toevoegen aan projectcalculatie

Je verwerkt PDF-offertes/opdrachten/facturen van leveranciers in de projectcalculatie
(gebaseerd op het C&W Master_calculatie-template). Antwoord altijd in het Nederlands.

## Stappen

1. **Bepaal het project.** Draai `python3 calculatie/tools/calc_tool.py list`.
   Noemt Sjoerd geen project, kies dan het meest waarschijnlijke en zeg dat erbij.
   Nieuw project: `python3 calculatie/tools/calc_tool.py init "Naam" [--m2 ...] [--locatie "..."]`.

2. **Haal de PDF op.** Bronnen, in volgorde van waarschijnlijkheid:
   - Upload in het gesprek (pad staat in de melding).
   - OneDrive via Microsoft 365 MCP: `sharepoint_search` (folderName = projectmap,
     fileType pdf) en dan `read_resource` met de gevonden URI. Projectmappen volgen
     het patroon `SJB/<project>/2.3 Aanbesteding & opdrachten/Opdrachten/<leverancier>/`.
   - Bijlage in Outlook-mail (`outlook_email_search`).

3. **Extraheer uit de PDF-tekst:**
   - leverancier, offerte-/PO-/factuurnummer, datum;
   - type: `opdracht` (C&W-opdrachtbevestiging = leidend), `offerte` (nog geen
     opdracht) of `factuur` (alleen meerwerk dat nergens anders staat);
   - regels met bedragen **netto excl. btw**. Grote posten apart houden, kleine
     samenvoegen tot één logische regel per discipline.
   - **Dubbelcheck**: dekt een opdracht een eerdere offerte, verwerk dan alléén de
     opdracht. Het register (`calculatie/projecten/<slug>/register.json`) toont wat
     al verwerkt is; het tool weigert dubbele referenties automatisch.

4. **Map elke regel naar een kostencode:**

   | Code | Inhoud | Code | Inhoud |
   |---|---|---|---|
   | 110 | bouwplaats/begeleiding | 311-314 | vloerafwerking |
   | 120 | sloopwerk | 321-323 | wanden (MS/systeem/deuren) |
   | 131-135 | divers bouwkundig, trap, entree, keuken | 330 | wandafwerking/schilderwerk |
   | 141-143 | sanitair, douche, berging | 340 | plafond |
   | 210 | HVAC/klimaat | 350 | verlichting |
   | 220 | loodgieter | 360 | zonwering |
   | 230 | elektra | 370 | maatwerkmeubilair |
   | 240 | toegang & beveiliging | 410 | los meubilair |
   | 250 | IT/data | 420 | losse inrichting |
   | 260 | brandveiligheid | 430 | AV |
   |  |  | 440 | akoestiek |
   |  |  | 450 | branding/signing |
   |  |  | 510-530, 610-620, 710-730 | overig, PM, onvoorzien/opslag/verzekering |

5. **Voeg toe.** Schrijf een JSON-bestand in de scratchpad (formaat: zie docstring
   van `calculatie/tools/calc_tool.py`) en draai:
   `python3 calculatie/tools/calc_tool.py add <slug> --json <bestand>`

6. **Rapporteer en bewaar.** Draai `status <slug>`, meld per leverancier het totaal
   en welke offertes nog geen opdracht hebben. Commit en push daarna:
   bestand `calculatie/projecten/<slug>/` + registerwijziging, commitbericht
   `"<project>: <leverancier> <type> <referentie> (EUR <bedrag>)"`.

7. **Sync naar SJBrain (verplichte slotstap).** Werk de projectnotitie in de
   Obsidian vault bij (`vault_write`/`vault_update`, folder `Projects`, pad
   `/<project>/<slug>-calculatie-inkoop.md`): tabel totalen per leverancier,
   totaalbedrag, datum, en de lijst offertes zonder opdracht. Bestaat de notitie
   nog niet, maak hem dan aan naar het voorbeeld van
   `Projects/Kioti/kioti-2-calculatie-inkoop.md`.

## Batchverwerking (hele projectmap)

Vraagt Sjoerd om een hele OneDrive-map te verwerken: zoek alle PDF's in de map
(`sharepoint_search`, pagineer!), lees ze één voor één, sla documenten over die al
in het register staan, en verwerk de rest volgens bovenstaande stappen. Meld aan het
eind een tabel: verwerkt / overgeslagen (duplicaat) / genegeerd (geen offerte, bijv.
leveringsvoorwaarden of tekeningen).

## Regels

- Bedragen altijd **netto excl. btw**; bij twijfel de PDF-totaalregel aanhouden.
- Nooit bedragen verzinnen: staat een bedrag niet leesbaar in de PDF, vraag het.
- Het Excel-bestand nooit met de hand bewerken — altijd via `calc_tool.py`, anders
  klopt het register niet meer.
- Kolom G in de Excel bevat de verborgen opslag (±14,4%); het leveranciersbedrag
  staat in kolom M. Rapporteer aan Sjoerd altijd de netto-inkoopbedragen (M).
