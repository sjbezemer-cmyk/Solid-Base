---
type: audit
status: draft
date: 2026-08-23
scope: Bezzy PA — compact gap audit
---

# Bezzy PA — Gap Analysis

## 1. Executive Summary

Bezzy PA is real and partially operational, not a paper design. Vier PA-routines bestaan en zijn live bevestigd `enabled` met correct cron-schema (Daily Briefing, PA Integrity Watch, Family Gmail Watch AM/PM). Eén echt Family-State-artefact (`Open-Loops.md`, vault) bevat echte, niet-verzonnen data. De policy-laag (`BEZZY.md`) is helder en intern consistent. Maar: **uitvoeringsgeschiedenis van geen enkele trigger kon bevestigd worden** (`last_run` ontbreekt bij alle vier — dubbelzinnig per tool-semantiek, niet hetzelfde als "nooit gedraaid"), de **Google-connector is deze sessie niet geauthenticeerd**, 4 Google Cloud API's (Drive/People/Tasks/Chat) waren bij de laatste live-test uitgeschakeld, en de **Family Relay-isolatie is nooit technisch getest**. Status: **PARTIAL / EARLY OPERATIONAL.**

## 2. Current PA Status

| Laag | Status |
|---|---|
| Policy/scope-model (`BEZZY.md`) | DESIGN, intern consistent, actief onderhouden |
| Gmail/Calendar identiteit-scheiding | YELLOW — eerder deze sessie live bevestigd, vandaag niet herverifieerbaar (connector uit) |
| 4 kern-routines | YELLOW — config live bevestigd, executie UNKNOWN |
| Family Relay | YELLOW — bestaat live bevestigd, isolatie UNKNOWN |
| Google Workspace writes | CODE — tools bestaan, nooit getest (terecht, per policy) |

## 3. Capabilities

| Item | Status | Bewijs | Gap |
|---|---|---|---|
| Scope check PA/Family/Work | CODE | Family-Orchestrator.md §8.0 (referentie, zelf niet gelezen) | Niet live getest |
| UNKNOWN-discipline | YELLOW | 1 echte instantie in Open-Loops.md | Steekproef van 1 |
| Approval-gates externe comms/financieel | DESIGN | BEZZY.md §5 | Geen bewezen afleveringsmechanisme |
| Gmail read (Family) | YELLOW | Live geslaagd, vorige beurt; niet herverifieerd vandaag | Connector niet geauthenticeerd |
| Gmail write/send | CODE | Tools bestaan, nooit aangeroepen | — |
| Calendar read (multi-source) | YELLOW | 1 van 4 bronnen live bevestigd | Overige 3 bronnen ongetest |
| Calendar write | CODE | Tool bestaat; alleen ooit gebruikt voor bulk-import | Normale approval-flow nooit getest |
| Personal vs Family Gmail scheiding | GREEN | Code-verified (OAuth-laag) + live getest, beide mailboxen correct gescheiden | — |
| Family Relay isolatie | BLOCKED | Relay bestaat live bevestigd; grens niet testbaar deze sessie | Sessie gebonden aan Family relay nodig |
| Family-State / Open Loops | YELLOW | Echt bestand, echte data, 3 dagen oud | Automatiseringsbewijs onvolledig |
| Drive/Docs/Sheets/Slides/Forms | RED | Drive live gefaald: API uitgeschakeld (project 283055709294) | Google Cloud-actie nodig |
| Contacts/Tasks/Chat | BLOCKED | Live gefaald: API's uitgeschakeld | Google Cloud-actie nodig |
| Daily Briefing | YELLOW | Trigger enabled, correct schema | Executie onbevestigd |
| PA Integrity Watch | YELLOW | Trigger enabled, correct schema | Executie onbevestigd; "no repair" is prompt-only |
| WhatsApp | RED | Expliciet "bewust uitgesteld" | Niet gestart |
| SJBrain als single source of truth | GREEN | Vault-reads/writes werken aantoonbaar, structureel | — |

## 4. Routines

| Name | Trigger | Purpose | Status |
|---|---|---|---|
| Bezzy — Daily Briefing | `trig_01Dd4oa1RpNos187jZszK53t`, cron `30 5 * * *` | Combineert Gmail+Calendar+SJBrain tot dagbriefing | YELLOW |
| Bezzy — Family Gmail Watch — Morning | `trig_01B8mpvfiLoH8zJpxHwAL5HD`, cron `0 5 * * *` | Leest bezzy.pa@gmail.com, classificeert, voedt Open Loops | YELLOW |
| Bezzy — Family Gmail Watch — Afternoon | `trig_014ndvJHF3r5b9t3rEYgg5Ai`, cron `0 14 * * *` | Idem, middagronde, geen dubbele rapportage | YELLOW |
| Bezzy — PA Integrity Watch | `trig_01EXquJC8kFXzJjvc39s5oKb`, cron `0 5 * * 1,3,5` | Detecteert schade aan PA/**, nooit repareren | YELLOW |

## 5. Loops

| Name | Input → Process → Output | Status |
|---|---|---|
| Family Gmail Watch loop | Gmail → change detection → relevance/priority → Open-Loops.md → Daily Briefing | YELLOW — dedup is expliciet niet code-backed, leunt op LLM die eigen vorige output teruglees |
| PA Integrity Watch loop | Vault → detect → verify → report → stop | YELLOW — geen technische restrictie op schrijftools gevonden, alleen instructie |
| Daily Briefing loop | Gmail-watch-output + Calendar + SJBrain → briefing | YELLOW — de expliciete end-to-end-test die de vault zelf voorschrijft is nooit gedraaid |
| Open Loop lifecycle | Action Required ↔ Waiting For ↔ Later ↔ Completed | YELLOW — 1 echte overgang waargenomen |

## 6. Triggers

| Name | Schedule | Enabled | Status |
|---|---|---|---|
| Bezzy — Daily Briefing | 07:30 CEST dagelijks | true (live geverifieerd) | last_run: afwezig — UNKNOWN of ooit gevuurd |
| Bezzy — Family Gmail Watch — Morning | 07:00 CEST dagelijks | true | last_run: afwezig |
| Bezzy — Family Gmail Watch — Afternoon | 16:00 CEST dagelijks | true | last_run: afwezig |
| Bezzy — PA Integrity Watch | 07:00 CEST ma/wo/vr | true | last_run: afwezig |

Trigger-tooling was deze sessie beschikbaar en is gebruikt (`list_triggers`, live). Alle vier bestaan, staan aan, hebben een correct cron-schema. **Executiegeschiedenis: UNKNOWN** — `last_run` ontbreekt bij alle vier, en dat betekent per de tool-semantiek "nooit gevuurd" ÓF "sessie-gebonden routine, niet zo bijgehouden" — niet te onderscheiden vanuit deze data alleen. Bekend, onopgelost: cron staat vast in UTC, niet DST-veilig (schuift 1 uur na eind oktober 2026).

## 7. Skills

Geen losstaand Bezzy-PA-skillbestand gevonden. Twee gerelateerde oppervlakken bestaan (Claude Code `morning`-skill; vault `Skills/`-map) maar geen van beide is een Bezzy-PA-specifiek, herbruikbaar skill-artefact — de mail-triage-logica zit inline in het trigger-systeemprompt zelf.

## 8. MCP Status

| Groep | Geïmplementeerd | Exposed | Authentiek getest | Daadwerkelijk bruikbaar |
|---|---|---|---|---|
| Gmail | ✅ 28 tools | ✅ | ✅ (vorige beurt) | ❓ connector nu niet geauthenticeerd |
| Calendar | ✅ 9 tools | ✅ | ✅ (vorige beurt) | ❓ idem |
| Drive | ✅ 20 tools | ✅ | ✅ (token geldig) | ❌ API uitgeschakeld |
| Docs/Sheets/Slides/Forms | ✅ 37 tools | ✅ | — | ❌/UNKNOWN — geblokkeerd door Drive of geen object-ID |
| Contacts | ✅ 7 tools | ✅ | ✅ | ❌ API uitgeschakeld |
| Tasks | ✅ ~5 tools | ✅ | ✅ | ❌ API uitgeschakeld |
| Chat | ✅ ~8 tools | ✅ | ✅ | ❌ API uitgeschakeld |
| Other (Apps Script, Custom Search, debug) | ✅ ~13 tools | ✅ | gedeeltelijk | Custom Search faalt op ontbrekende `GOOGLE_PSE_API_KEY`; debug-tools code-verified, geen risico |

"Tool bestaat" ≠ "tool werkt": van 121 tools hebben alleen Gmail en Calendar ooit een echte, geslaagde Google API-respons opgeleverd.

## 9. Family / Relay Boundaries

Live bevestigd (`vault_relays`): 2 relays — SJBrain Relay (actief in deze sessie) en Bezzy Family Relay (bestaat, niet gebonden aan deze sessie).

| Boundary | Technisch afgedwongen? | Status |
|---|---|---|
| Personal vs Family Gmail | ✅ Ja (OAuth-laag, code-verified + live getest) | GREEN — enige boundary die dit dubbel heeft |
| Family Relay isolatie (PA/** onbereikbaar vanuit Family-sessie) | UNKNOWN — nooit getest, niet testbaar deze sessie | BLOCKED |
| Juliette-toegang | Niet aanwezig | Bevestigd afwezig, conform opdracht |
| C&W-content nooit naar Family | Niet getest | UNKNOWN |

## 10. Gaps

### CRITICAL
| Gap | Waarom nodig | Dependency | Next action | Status |
|---|---|---|---|---|
| Google-connector niet geauthenticeerd | Blokkeert alle verdere live Google-tests | claude.ai connector-instellingen | Gebruiker zet connector aan in dit gesprek | OPEN |
| Google Cloud API's uitgeschakeld (Drive/People/Tasks/Chat) | Blokkeert Drive/Contacts/Tasks/Chat en alles wat daarvan afhangt | Google Cloud Console, project 283055709294 | Gebruiker schakelt API's in | OPEN |
| Trigger-executiegeschiedenis onbevestigd | Onbekend of PA daadwerkelijk ooit gedraaid heeft | Observatie na natuurlijke firing, of platform-uitleg over `last_run`-semantiek | Wachten/opnieuw checken | OPEN |

### IMPORTANT
| Gap | Waarom nodig | Dependency | Next action | Status |
|---|---|---|---|---|
| Family Relay-isolatie nooit getest | Blokkeert Harry/Juliette en alle Family-only automatisering | Sessie gebonden aan Family relay | Ontwerpbeslissing + test | OPEN |
| Geen bewezen approval-afleveringsmechanisme | Schrijfacties zijn policy-gated maar het "hoe" ontbreekt | Ontwerpbeslissing | Specificeren vóór Gmail-send/Calendar-write echt getest wordt | OPEN |
| DST-onveilige cron's | Schema's verschuiven na eind oktober 2026 | Handmatige cron-correctie | Niet urgent, wel onopgelost | OPEN |

### FUTURE
| Gap | Waarom nodig | Dependency | Next action | Status |
|---|---|---|---|---|
| Persistente dedup voor Open Loops | Huidige dedup leunt op LLM die eigen output teruglees | — | Ontwerp later | OPEN |
| Harry/Juliette-rollout | Volgende laag na Family-boundary-validatie | Family Relay-isolatie bewezen | Wachten op CRITICAL/IMPORTANT | GEBLOKKEERD-BY-DESIGN |
| WhatsApp-integratie | Bewust uitgesteld | — | Niet gestart | GEPARKEERD |

## 11. Blockers

1. **Google-connector niet geauthenticeerd in deze sessie** — blokkeert alle Google-live-tests.
2. **4 Google Cloud API's uitgeschakeld** (Drive/People/Tasks/Chat, project 283055709294) — blokkeert het grootste deel van de MCP-capability-matrix.
3. **Family Relay-isolatie nooit technisch getest** — blokkeert alle Family-only uitbreiding.

## 12. Full PA Acceptance Criteria

- [ ] Core PA operationeel (scope-check, UNKNOWN-discipline, approval-gates bewezen, niet alleen gedocumenteerd)
- [ ] Google MCP geauthenticeerd en live geverifieerd in dezelfde sessie
- [ ] Gmail, Calendar, Drive, Docs/Sheets/Slides, Contacts, Tasks, Chat leveren allemaal echte data op
- [ ] Daily Briefing minstens 1x bevestigd uitgevoerd (`last_run` gevuld)
- [ ] Family Gmail Watch (AM+PM) minstens 1x bevestigd uitgevoerd
- [ ] PA Integrity Watch minstens 1x bevestigd uitgevoerd
- [ ] Open Loop-management heeft een dedup-mechanisme onafhankelijk van LLM-geheugen
- [ ] Family Relay-isolatie technisch getest vanuit een echte Family-gebonden sessie
- [ ] Approval-mechanisme voor externe/financiële acties concreet bewezen, niet alleen beleid
- [ ] Eén echte schrijfactie (Gmail-send of Calendar-create) via de normale approval-flow uitgevoerd en correct verlopen
- [ ] Cron-schema's DST-veilig of automatisch gecorrigeerd
- [ ] UNKNOWN-discipline consistent aangetoond over meerdere runs (nu: steekproef van 1)
- [ ] `debug_docs_runtime_info`/`debug_table_structure` bewust aan- of uitgezet (nu: geen beslissing genomen)

## 13. Recommended Next Steps

1. Gebruiker zet de Bezzy Google MPC-connector aan in dit specifieke gesprek.
2. Gebruiker bevestigt/schakelt de 4 Google Cloud API's in (project 283055709294).
3. Daarna: herhaal de live Gmail/Calendar/Drive/Contacts/Tasks/Chat-tests, en observeer of een trigger natuurlijk vuurt om `last_run` te kunnen aflezen.

## 14. Evidence / Unknowns

**Bewijs (deze sessie, live):** `vault_relays` (2 relays), `vault_folders`, `vault_list` op `PA` (26 items), `vault_read` op `Status.md`, `BEZZY.md`, `BEZZY-Golden-Rules.md`, `Open-Loops.md`, `BEZZY-ROADMAP.md`, `list_triggers` (12 triggers totaal, 4 Bezzy-relevant, volledige JSON vastgelegd).
**Bewijs (eerder deze conversatie, live, niet herhaald):** Gmail/Calendar live-tests geslaagd; Drive/Contacts/Tasks/Chat/Custom Search live-tests gefaald met concrete foutmeldingen; code-review van `bezzy-google-mcp` (OAuth-isolatie, SSRF-bescherming, 1 dependency-kwetsbaarheid gevonden en gefixt op ongemergde branch).
**Onbekend/onverifieerbaar:** trigger-executiegeschiedenis; huidige Google Cloud API-status (niet vandaag herverifieerd); of Family Relay-isolatie standhoudt; of "no repair" bij PA Integrity Watch technisch of alleen instructie-matig is; inhoud van overige Family-State-bestanden en Backup/-documenten (bestaan bevestigd, inhoud niet gelezen).
