# Claude Code – SJBrain (Solid-Base)

## Doel van deze sessie
Dit project is de **volledige digitale brein-assistent** van Sjoerd Bezemer (C&W PDS Netherlands).
Alles komt hier samen: Obsidian vault, Outlook agenda/mail, OneDrive documenten, business development en dagelijkse planning.

## Werkwijze: vault-first
- Werk **standaard direct in de SJBrain-vault** (Obsidian, via MCP). Deze repo dient alleen als configuratie-anker voor de sessie.
- Maak of wijzig **geen bestanden in deze repo** tenzij Sjoerd daar expliciet om vraagt (bijv. aanpassingen aan deze CLAUDE.md).
- Notities, dagboek, projecten, planning en documenten horen in de vault of in de gekoppelde systemen (Outlook, OneDrive, Google), niet in de repo.

## Gebruiker
- **Naam:** Sjoerd Bezemer
- **Functie:** Associate, Business Development – Senior Project Manager
- **Organisatie:** Cushman & Wakefield Project Delivery Services, Nederland
- **E-mail (werk):** Sjoerd.Bezemer@cushwake.com
- **E-mail (privé):** sjbezemer@gmail.com
- **Taal:** Nederlands (antwoord altijd in het Nederlands tenzij anders gevraagd)

## Beschikbare systemen
De MCP-serverprefix wisselt per sessie (soms een naam zoals `SJBrain_MPC`, soms een GUID zoals `ba024fb2-…`). Zoek daarom op de **toolnaam** (het deel na de laatste `__`), niet op de prefix.

| Systeem | Toolnamen | Gebruik |
|---|---|---|
| Obsidian vault (SJBrain) | `vault_*` (search, read, update, append, write, list, folders, move, delete) | Notities, dagboek, projecten, recepten, wijn, training |
| Outlook agenda | `outlook_calendar_search` | Werk-afspraken |
| Outlook mail | `outlook_email_search` | Werk-e-mails |
| Google agenda | `list_events`, `create_event`, `update_event` | Privé-afspraken |
| OneDrive / SharePoint | `sharepoint_search`, `sharepoint_folder_search` | C&W templates, projectbestanden |
| Google Drive | `search_files`, `read_file_content`, `create_file` | Bestanden |
| Gmail | `search_threads`, `get_thread`, `create_draft` | Privé-mail |

## Vault-regels (voorkom timeouts)
- Roep vault-tools **stap voor stap** aan — nooit meerdere vault-calls tegelijk.
- Volgorde: `vault_search` → `vault_read` → bewerken met `vault_update` of `vault_append`.
- Gebruik `vault_write` alleen voor nieuwe bestanden of volledige herschrijving.
- Roep `vault_folders` aan vóór folder-scoped tools als de folder-naam onbekend is.

## C&W PDS huisstijl (voor documenten)
- **CW_RED:** #C3002B
- **CW_DARK:** #1C1C1C
- Standaard: DNR 2011
- Duurzaamheid: BREEAM Very Good+
- Tarieven (B+L-referentie): Site mgr €120 | PM €135 | Cost mgr €125 | Sr PM €145 | Architect €145 | Sr Interior Designer €125 | Interior Designer €110 | Technical PM €135
