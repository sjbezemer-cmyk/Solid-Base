# Claude Code – Projectinstructies (SJBrain / Solid-Base)

## Obsidian Vault (via Relay MCP)
- Vraag de vault **stap voor stap** (één call tegelijk), nooit meerdere vault-calls tegelijk — dit veroorzaakt een timeout.
- Gebruik `vault_search` eerst om een bestand te vinden, daarna `vault_read` voor de inhoud.
- Bij partiele bewerkingen: gebruik `vault_update` of `vault_append`, nooit `vault_write` op grote bestanden.

## Algemeen
- Gebruiker communiceert in het Nederlands; antwoord ook in het Nederlands tenzij anders gevraagd.
