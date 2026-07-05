# Claude Code – SJBrain (Solid-Base)

## Doel van deze sessie
Dit project is de **volledige digitale brein-assistent** van Sjoerd Bezemer (C&W PDS Netherlands).
Alles komt hier samen: Obsidian vault, Outlook agenda/mail, OneDrive documenten, business development en dagelijkse planning.

## Gebruiker
- **Naam:** Sjoerd Bezemer
- **Functie:** Associate, Business Development – Senior Project Manager
- **Organisatie:** Cushman & Wakefield Project Delivery Services, Nederland
- **E-mail (werk):** Sjoerd.Bezemer@cushwake.com
- **E-mail (privé):** sjbezemer@gmail.com
- **Taal:** Nederlands (antwoord altijd in het Nederlands tenzij anders gevraagd)

## Beschikbare systemen
| Systeem | MCP / tool | Gebruik |
|---|---|---|
| Obsidian vault (SJBrain) | `mcp__ba024fb2__vault_*` | Notities, dagboek, projecten, recepten, wijn, training |
| Outlook agenda | `mcp__969bfc01__outlook_calendar_search` | Werk-afspraken |
| Outlook mail | `mcp__969bfc01__outlook_email_search` | Werk-e-mails |
| Google agenda | `mcp__b8c8676b__list_events` | Privé-afspraken |
| OneDrive / SharePoint | `mcp__969bfc01__sharepoint_*` | C&W templates, projectbestanden |
| Google Drive | `mcp__958235f6__*` | Bestanden |
| Gmail | `mcp__e5548b38__*` | Privé-mail |

## SJBrain is de bron van waarheid (ALTIJD toepassen)
Claude Code werkt **altijd vanuit het SJBrain** (Obsidian vault via `mcp__SJBrain_MPC__vault_*`):
1. **Begin van elke taak:** zoek eerst in de vault naar bestaande context (`vault_search` op project-/onderwerpnaam, o.a. in `Projects`, `Skills`, `Context`). Gebruik wat er staat; vraag niet naar dingen die al in het brein staan.
2. **Einde van elke substantiële taak:** schrijf het resultaat terug naar de vault — projectresultaten in `Projects/<project>/`, nieuwe werkwijzen/routines in `Skills/`. Werk bestaande notities bij in plaats van duplicaten te maken.
3. **Rolverdeling:** de vault is de leesbare waarheid (wat & waarom, voor Sjoerd), de Solid-Base repo is de werkende waarheid (tools, templates, data). Houd beide in sync.
4. Kleine vragen of opzoekacties hoeven géén vault-notitie; alleen werk met blijvende waarde.

## Vault-regels (voorkom timeouts)
- Roep vault-tools **stap voor stap** aan — nooit meerdere vault-calls tegelijk.
- Volgorde: `vault_search` → `vault_read` → bewerken met `vault_update` of `vault_append`.
- Gebruik `vault_write` alleen voor nieuwe bestanden of volledige herschrijving.
- Roep `vault_folders` aan vóór folder-scoped tools als de folder-naam onbekend is.

## Projectcalculaties (offertes → Excel)
- Workflow en tooling: zie `calculatie/README.md`; het proces zelf zit in de skill `/offerte`.
- Leeg C&W-template: `calculatie/template/Master_calculatie_LEEG.xlsx`. Per project een map onder `calculatie/projecten/<slug>/` met `calculatie.xlsx` + `register.json`.
- PDF-offertes/opdrachten **altijd** verwerken via `python3 calculatie/tools/calc_tool.py add <slug> --json ...` — nooit de Excel handmatig bewerken (register = audittrail + dedupe).
- Bedragen netto excl. btw rapporteren (kolom M); kolom G bevat de verborgen opslag (±14,4%).
- Na elke verwerking: commit + push.

## C&W PDS huisstijl (voor documenten)
- **CW_RED:** #C3002B
- **CW_DARK:** #1C1C1C
- Standaard: DNR 2011
- Duurzaamheid: BREEAM Very Good+
- Tarieven (B+L-referentie): Site mgr €120 | PM €135 | Cost mgr €125 | Sr PM €145 | Architect €145 | Sr Interior Designer €125 | Interior Designer €110 | Technical PM €135
