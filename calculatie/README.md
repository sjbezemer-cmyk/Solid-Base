# Calculatie — PDF-offertes → Master calculatie, per project

Volledig geautomatiseerde route om per project PDF-offertes/opdrachten van
leveranciers te verwerken in de C&W Master_calculatie Excel.

## De route

```
PDF (upload / OneDrive / mail)
        │  1. Claude leest de PDF (MCP of upload)
        ▼
extractie: leverancier, referentie, regels excl. btw
        │  2. mapping naar kostencodes (110–730)
        ▼
calc_tool.py add  ──►  projecten/<slug>/calculatie.xlsx   (regels + formules)
        │              projecten/<slug>/register.json     (dedupe + audittrail)
        ▼
status-rapport per leverancier  →  commit + push
```

In een Claude Code-sessie is dit één zin: *"voeg deze offerte toe aan kioti-2"*
of */offerte* — de skill in `.claude/skills/offerte/` stuurt het proces.

## Structuur

```
calculatie/
├── template/Master_calculatie_LEEG.xlsx   # het lege template (bron van elk project)
├── tools/calc_tool.py                     # init / add / status / list
└── projecten/
    └── kioti-2/
        ├── calculatie.xlsx                # het gevulde werkboek
        └── register.json                  # verwerkte documenten (dedupe-sleutel:
                                           #  leverancier + referentie)
```

## Commando's

```bash
python3 calculatie/tools/calc_tool.py list                        # alle projecten
python3 calculatie/tools/calc_tool.py init "Naam" --m2 445        # nieuw project
python3 calculatie/tools/calc_tool.py add kioti-2 --json o.json   # document toevoegen
python3 calculatie/tools/calc_tool.py status kioti-2              # totalen + open offertes
```

Het JSON-formaat voor `add` staat in de docstring van `calc_tool.py`.

## Waarom dit werkt

- **Het lege template staat in de repo** — elk project start identiek, formules en
  opslagen (kolom G = klantbedrag met ±14,4% opslag, kolom M = netto inkoop) blijven intact.
- **Claude doet het slimme werk** (PDF lezen, bedragen herkennen, kostencode kiezen);
  het script doet het deterministische werk (rijen schrijven, formules, dedupe, totalen).
- **Register.json is de audittrail**: hetzelfde document twee keer aanbieden wordt
  geweigerd, en je ziet altijd welke offertes nog geen opdracht zijn geworden.
- **Alles in git**: elke toegevoegde offerte is een commit, dus elke stand van de
  calculatie is terug te halen.

## Optioneel: volautomatische bewaking

Per project kan een terugkerende routine worden aangezet die de OneDrive-map
`SJB/<project>/2.3 Aanbesteding & opdrachten/Opdrachten/` periodiek scant,
nieuwe PDF's tegen het register houdt en ze automatisch verwerkt + pusht.
Vraag Claude: *"zet een dagelijkse offertecheck aan voor project X"*.
