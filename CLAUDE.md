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
| MarkItDown | `markitdown-mcp` | Documenten (PDF, Word, PowerPoint, Excel) omzetten naar Markdown vóór opslag in de vault |

## MarkItDown MCP-server
[MarkItDown](https://github.com/microsoft/markitdown) zet Office-documenten, PDF's en andere bestandsformaten om naar Markdown, zodat OneDrive/SharePoint-bijlagen direct bruikbaar zijn in de Obsidian vault.

- **Installatie:** `pip install markitdown-mcp` (wordt automatisch uitgevoerd door de `SessionStart`-hook in `.claude/hooks/session-start.sh`).
- **Starten:** `markitdown-mcp` (stdio) of `markitdown-mcp --http --host 127.0.0.1 --port 3001` (SSE/HTTP).
- **MCP-configuratie (voorbeeld):**
  ```json
  {
    "mcpServers": {
      "markitdown": {
        "command": "markitdown-mcp"
      }
    }
  }
  ```

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
