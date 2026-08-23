---
type: audit
status: draft
date: 2026-08-23
scope: Bezzy Personal Assistant — full product gap analysis
---

# BEZZY PA — GAP ANALYSIS & PRODUCT READINESS AUDIT

> **Note on location:** this file lives in the git repository `sjbezemer-cmyk/solid-base`, in a newly created `PA/` folder — this repo had no `PA/` folder before this analysis. The **actual system of record for Bezzy PA** (policies, routines, family state, roadmap) is a *different* location: the `PA/` folder inside the **SJBrain Obsidian vault**, reached via the `SJBrain_MPC` MCP connector (Relay-synced, not git-versioned). Every `PA/...` path cited as a source in this document refers to that vault folder, not this git repo, unless explicitly marked "(this repo)". This distinction matters and is easy to conflate — flagged here once, up front.

---

## 1. EXECUTIVE SUMMARY

Bezzy PA is a real, partially-operational system, not a paper design. Four scheduled routines exist and are live-confirmed `enabled` with correct cron schedules as of this audit (2026-08-23, ~19:50 UTC): **Daily Briefing**, **PA Integrity Watch**, **Family Gmail Watch — Morning**, **Family Gmail Watch — Afternoon**. A real Family-State artifact (`Open-Loops.md`) contains genuine, non-fabricated family data with a timestamp attributing it to an actual Family Gmail Watch run (2026-08-20). The policy layer (`BEZZY.md`, approval gates, privacy boundaries, persona model) is well-specified and internally consistent.

However: **execution history could not be confirmed via the trigger API itself** (`last_run` is absent for all four Bezzy triggers — which per the tool's own semantics can mean "never fired" *or* "session-bound, not tracked this way"; this is genuinely ambiguous, not resolved here). The **Google Workspace MCP connector (`Bezzy_Google_MPC`) is currently unauthenticated** in this session and could not be live-tested today. Four Google Cloud APIs (Drive, People, Tasks, Chat) were confirmed disabled as of the last successful live test (this same conversation, several turns ago) and their current state is unknown. The **Bezzy Family Relay exists** (confirmed live: `cc0c201b-1369-4ccc-9c9a-94ab38b30bb1`) but its **security isolation boundary has never been technically tested** — the vault's own roadmap explicitly marks the routines that depend on that boundary as `BLOCKED`.

**Overall PA status: PARTIAL / EARLY OPERATIONAL.** The foundational architecture is real and largely sound; the "does it actually work end-to-end, unattended, safely" question remains genuinely open on several fronts. See §17 (Full PA acceptance checklist) — most boxes are unchecked, honestly.

---

## 2. CURRENT PA STATUS

Policy and scope model: **DOCUMENTED**, internally consistent, actively maintained (`BEZZY.md`, v1, 14 Aug 2026). Calendar/Gmail identity separation (`bezzy.pa@gmail.com` vs `sjbezemer@gmail.com`): **DOCUMENTED as resolved**, **LIVE VERIFIED** for Gmail+Calendar in this conversation at an earlier turn (both returned real, correctly-scoped data), **NOT RE-VERIFIED today** (connector currently unauthenticated). Four routines: **LIVE VERIFIED** to exist, be enabled, and have correct schedules; **execution history UNKNOWN**. Family Relay: **LIVE VERIFIED to exist as a distinct relay**; **isolation boundary NOT LIVE TESTABLE** with tools available in this session. Google Workspace write capabilities (Gmail send, Calendar write, Drive/Docs/Sheets/Slides write): **CODE VERIFIED to exist as tools**, **DOCUMENTED as approval-gated**, **not runtime tested** (correctly — this task and the underlying policy both prohibit unapproved write testing).

---

## 3. EVIDENCE METHODOLOGY

Evidence hierarchy used throughout (as specified in the task):

| Level | Meaning | Used how here |
|---|---|---|
| 1 — LIVE RUNTIME | Actual tool call / trigger data obtained in this session | `list_triggers` output (this turn), `vault_*` reads (this turn), Gmail/Calendar/Drive/Contacts/Tasks/Chat live test results (this conversation, timestamped) |
| 2 — CODE | Current implementation inspected | `bezzy-google-mcp` source (auth flow, session isolation, SSRF, scopes) |
| 3 — CONFIG | Current environment/deployment state | Railway env vars, OAuth discovery metadata |
| 4 — DOCUMENTATION | Specs, policy docs, roadmap | `BEZZY.md`, `BEZZY-Golden-Rules.md`, `BEZZY-ROADMAP.md`, `Status.md` |
| 5 — PREVIOUS REPORTS | Historical audit reports | Explicitly **not used as evidence** here; not re-cited |

Every claim below is tagged with its level. Where Level-4 documents assert something is `ACTIVE` or `resolved`, that assertion is treated as a *lead*, and independently checked where tooling allowed it this session. Where it could not be checked, it is marked `UNKNOWN` or `NOT RE-VERIFIED`, not silently accepted.

---

## 4. CAPABILITY INVENTORY

Status legend: 🟢 GREEN (implemented + operationally verified) · 🟡 YELLOW (implemented, partially verified) · 🔵 BLUE (implemented in code, not runtime verified) · ⚪ GREY (documented/design only) · 🔴 RED (missing/non-functional) · 🚧 BLOCKED · ❓ UNKNOWN

| Cat | Capability | Intended behaviour | Status | Evidence |
|---|---|---|---|---|
| A. Core PA | Scope check before persona selection | Determine PA/Family/Work scope before acting | 🔵 | L4 (`Family-Orchestrator.md` §8.0, cited but not itself read this session) |
| A. Core PA | UNKNOWN discipline | Never guess; return UNKNOWN when data is missing/conflicting | 🟡 | L4 design rule + L1 concrete instance found in `Open-Loops.md` ("UNKNOWN: of Arielle op 26-08 voor beide kinderen is") — one real, correctly-applied instance seen |
| B. Communication | Gmail read (Family) | Read `bezzy.pa@gmail.com` | 🟡 | L1, but from an earlier turn this conversation, not re-verified today (connector currently unauthenticated) |
| B. Communication | Gmail write/send/draft (Family) | Draft/send external comms, approval-gated | 🔵 | L2 (tools exist: `send_gmail_message`, `draft_gmail_message`, `modify_gmail_message_labels`) — never invoked, per policy |
| B. Communication | WhatsApp integration | — | 🔴 | L4 explicit: "Nog niet gebouwd (bewust uitgesteld)" |
| C. Calendar | Multi-source calendar read | 4 sources: cw-outlook, sjbezemer-gcal, bezzy-gcal, family-gcal | 🟡 | L1 `bezzy-gcal` read confirmed (earlier turn); other 3 sources not tested this session |
| C. Calendar | Calendar write (Family) | Create/modify events, approval-gated | 🔵 | L2 tools exist (`manage_event`); L4 documented as never yet exercised through the normal approval flow |
| D. Tasks | Google Tasks read/write | — | 🚧 | L1: Tasks API confirmed **disabled** on the Google Cloud project (earlier turn, live 403) |
| E. Documents (Docs) | Read/write Google Docs | — | 🚧 | L1: blocked upstream of testing — Drive API (needed for discovery) confirmed disabled |
| F. Drive | List/search/read files | — | 🔴 (live-failed) | L1: `Google Drive API is not enabled for your project (283055709294)` — real error, captured verbatim earlier this conversation |
| G. Sheets | Read/write spreadsheets | — | 🚧 | Same upstream Drive-API blocker |
| H. Slides | Read/write presentations | — | ❓ | Never reached an object ID to test; API-enablement status unknown |
| I. Forms | Read/write forms | — | ❓ | Same |
| J. Contacts | Read Google Contacts | — | 🔴 (live-failed) | L1: People API confirmed disabled, live 403 |
| K. Family | Family-State tracking (Open Loops, Today, This-Week, Upcoming, Household, Financials, Activities) | Vault-based family state | 🟡 | L1: `Open-Loops.md` read this session, real content, dated 2026-08-20; other Family-State files not read this session (existence confirmed via `vault_list`, contents not verified) |
| K. Family | Family Relay isolation | Family data physically/logically separated from PA/Work | 🚧 | L1: relay exists (`vault_relays` confirmed two relays); boundary itself **NOT LIVE TESTABLE** with tools in this session |
| L. Personal | Personal Gmail/Calendar kept separate from Family | Never treat `sjbezemer@gmail.com` as Family inbox | 🟡 | L1 earlier this session: the two Gmail connectors independently returned different, correctly-scoped mailboxes |
| M. Work/C&W | C&W Outlook read for availability only, content never exposed to Family | — | ❓ | Not tested this session; Microsoft 365 connector was connected but not exercised for this purpose |
| N. Daily Briefing | Combine sources into a daily summary for Sjoerd | — | 🟡 | L1: trigger exists, enabled, correct schedule (`30 5 * * *`); **no confirmed execution** (`last_run` absent) |
| O. Open Loops | Track action-required / waiting-for / later / completed | — | 🟢 (as data structure) / 🟡 (as automated loop) | L1: real file with real, well-classified entries exists; automation that maintains it (Family Gmail Watch) has unconfirmed execution history |
| P. Proactive assistance | Anticipate, early-warning, pattern detection | — | ⚪ | L4 only (`BEZZY-Golden-Rules.md`) — explicitly marked a *vision* document, not active policy |
| Q. Memory/Context | SJBrain as single source of truth | — | 🟢 | L1: extensively confirmed across this whole conversation — vault reads/writes work, are real, are structured |
| R. Automation | Scheduled routines (crons) | — | 🟡 | L1: 4 relevant triggers exist and are enabled; execution proof incomplete |
| S. Safety/Authority | Approval gates on external comms, financial actions, shared-info changes | — | 🟡 | L4 explicit policy (`BEZZY.md` §5); technically enforced only insofar as no write tool has ever been invoked — see §12 |
| T. Integrity/Monitoring | PA Integrity Watch (detect-only, no repair) | — | 🟡 | L1: trigger exists, enabled, correct schedule; execution unconfirmed; "no repair" is prompt-enforced, not code-enforced |
| U. Future/Planned | Harry (Juliette persona), couple coordination, financial routines, household routines | — | ⚪ | L4 only — explicitly gated behind Family Relay boundary validation (roadmap §10), which itself is unverified |

---

## 5. MCP INVENTORY

The Google Workspace MCP (`Bezzy_Google_MPC`, deployed on Railway, code in `sjbezemer-cmyk/bezzy-google-mcp`) exposes **121 tools** across Gmail, Drive, Docs, Sheets, Slides, Forms, Calendar, Contacts, Tasks, Chat, Apps Script and Custom Search (L2/L3: tool catalogue observed directly via this session's own tool announcements + prior code review of the repo).

Distinguishing IMPLEMENTED / EXPOSED / AUTHENTICATED / RUNTIME VERIFIED / ACTUALLY USABLE, per tool category, as of the most recent test data available (earlier this same conversation) and current session state:

| Category | Implemented | Exposed to Claude | Authenticated (last known) | Runtime verified | Actually usable **right now** |
|---|---|---|---|---|---|
| Gmail | ✅ (28 tools) | ✅ | ✅ (earlier turn) | ✅ (list_gmail_labels, search_gmail_messages both succeeded) | ❓ — connector currently shows "requires authentication" this session |
| Calendar | ✅ (9 tools) | ✅ | ✅ (earlier turn, account = `bezzy.pa@gmail.com`) | ✅ (list_calendars succeeded) | ❓ — same |
| Drive | ✅ (20 tools) | ✅ | ✅ (token valid) | ❌ FAILED — live 403, Drive API disabled on Google Cloud project `283055709294` | ❌ |
| Docs/Sheets/Slides/Forms | ✅ (37 tools combined) | ✅ | — | ❌ blocked upstream (Drive-dependent discovery) or NOT TESTED (no object ID) | ❌ |
| Contacts | ✅ (7 tools) | ✅ | ✅ | ❌ FAILED — People API disabled | ❌ |
| Tasks | ✅ (~5 tools) | ✅ | ✅ | ❌ FAILED — Tasks API disabled | ❌ |
| Chat | ✅ (~8 tools) | ✅ | ✅ | ❌ FAILED — Chat API disabled | ❌ |
| Custom Search | ✅ (2 tools) | ✅ | N/A (API-key based, not OAuth) | ❌ FAILED — `GOOGLE_PSE_API_KEY` not set on Railway | ❌ |
| Apps Script | ✅ (~9 tools) | ✅ | — | NOT TESTED | ❓ |
| Admin/debug (`debug_docs_runtime_info`, `debug_table_structure`) | ✅ (2 tools) | ✅ | — | CODE VERIFIED only (read-only, operate within caller's own auth scope, no elevated access) | 🔵 |

**Key distinction the task asked for explicitly:** "tool exists" ≠ "tool works." Of 121 implemented+exposed tools, only Gmail (partial) and Calendar (partial) categories have ever returned a real, successful Google API response in this project's history. The rest are either confirmed broken (disabled API) or genuinely untested.

Security posture of the MCP itself (CODE VERIFIED, from direct source inspection this project): cross-user credential isolation is explicit and robust (`auth/oauth21_session_store.py` — mismatched token/session → logged `SECURITY VIOLATION`, access denied); SSRF protection present and unit-tested (`core/http_utils.resolve_and_validate_host`); no secrets found in git history; one dependency vulnerability (`click` PYSEC-2026-2132) found and patched (branch `claude/security-review-fixes`, not yet merged to `main`).

---

## 6. ROUTINE INVENTORY

**LIVE VERIFIED this session** via `list_triggers` (2026-08-23, ~19:50 UTC). All four exist, all `enabled: true`.

| Routine | Trigger ID | Cron (UTC) | Local time (CEST) | next_run_at | last_run | Status |
|---|---|---|---|---|---|---|
| Bezzy — Daily Briefing | `trig_01Dd4oa1RpNos187jZszK53t` | `30 5 * * *` | 07:30 daily | 2026-08-24T05:30:19Z | absent | Enabled, schedule correct. *Note: the vault's own roadmap doc (dated 17–18 Aug) claimed this trigger had no cron/next_run_at and "never fires" — that claim does not match this live check; either it was fixed since, or the doc was wrong. Flagged, not silently resolved either way.* |
| Bezzy — PA Integrity Watch | `trig_01EXquJC8kFXzJjvc39s5oKb` | `0 5 * * 1,3,5` | 07:00 Mon/Wed/Fri | 2026-08-24T05:01:36Z | absent | Enabled, schedule correct |
| Bezzy — Family Gmail Watch — Morning | `trig_01B8mpvfiLoH8zJpxHwAL5HD` | `0 5 * * *` | 07:00 daily | 2026-08-24T05:06:07Z | absent | Enabled, schedule correct |
| Bezzy — Family Gmail Watch — Afternoon | `trig_014ndvJHF3r5b9t3rEYgg5Ai` | `0 14 * * *` | 16:00 daily | 2026-08-24T14:07:28Z | absent | Enabled, schedule correct |

Purpose/output/authority summary per routine (from `BEZZY-ROADMAP.md`, L4, cross-checked against real output where possible):

- **Family Gmail Watch (AM+PM):** reads `bezzy.pa@gmail.com` only; classifies into ACTION REQUIRED / REPLY REQUIRED / DEADLINE / CALENDAR RELEVANT / FAMILY INFORMATION / OPEN LOOP / WAITING FOR / FYI / NOISE; writes to `Open-Loops.md`; feeds the 07:30 Daily Briefing. Authority: read/classify/signal only — **may not** send, reply, delete, archive, move, or change calendar. Real output artifact exists and matches this spec (§ below).
- **Daily Briefing:** aggregates Gmail-watch output + Calendar + SJBrain context into a briefing for Sjoerd/Floor. Read-only.
- **PA Integrity Watch:** detects anomalies in `PA/**`. Flow `DETECT → VERIFY → REPORT → STOP`. Explicitly forbidden from repairing, deleting, or modifying anything.

Real evidence of at least one execution: `Family-State/Open-Loops.md` (vault) is dated "Laatste update: 2026-08-20 (Family Gmail Watch middagrun)" and contains specific, non-generic family data (an Essent account email, an OV-chipkaart collection notice, a childcare-coordination thread with Juliette, one correctly-applied UNKNOWN flag). Consistent with a real run around 2026-08-20 — see §8 (Trigger Inventory) for why this can't be tied conclusively to the trigger API's own execution record.

---

## 7. LOOP INVENTORY

| Loop | Source → Detect → Classify → State → Surface → Dedup → Resolve | Completeness | Technically enforced? |
|---|---|---|---|
| Family Gmail Watch loop | `GMAIL WATCH → CHANGE DETECTION → RELEVANCE → PRIORITY → STATE (Open-Loops.md) → 07:30 Daily Briefing` | Partially complete: state file is real (L1), classification categories well-defined (L4), dedup mechanism **explicitly documented as not code-backed** ("Geen persistent tracking beschikbaar → rapporteer die beperking; geen nieuwe database bouwen") | **Prompt-enforced only.** No dedicated dedup data structure or code found; relies on the LLM re-reading its own prior markdown output each run. |
| PA Integrity Watch loop | `DETECT → VERIFY → REPORT → STOP` | Simple, designed, schedule-verified live; no evidence found of an actual anomaly-detection mechanism beyond "read the vault and use judgment" | **Prompt-enforced.** "No repair" is an instruction in the trigger's own system prompt (confirmed present, see §8), not a verified technical restriction on which tools that session actually has access to. |
| Daily Briefing loop | Aggregates Gmail-watch output + Calendar + SJBrain context → single briefing | Designed, scheduled; the exact end-to-end test the vault's own `Status.md` proposes ("Floor, wat moet ik vandaag weten?") is explicitly recorded there as *not yet run* | Prompt-enforced |
| Open Loop lifecycle (Action Required → Waiting For → Later → Completed) | Manual-ish state machine maintained by whichever routine writes to `Open-Loops.md` | One real transition observed (an item moved from "Waiting For" toward resolution, tracked across dated entries) | Prompt-enforced |

No loop in this system has independent, code-level state (a database, a processed-message-ID table, etc.) — **every loop's "memory" is the markdown file it last wrote**, re-read at the start of the next run. Simple and auditable, but has no independent enforcement backstop if a future run's prompt is subtly wrong.

---

## 8. TRIGGER INVENTORY

Full account has **12 triggers total** (LIVE VERIFIED, `list_triggers`, this session). **4 are Bezzy-PA-scoped**, detailed in §6. The remaining 8 belong to other systems and are out of scope for this audit, listed for completeness only: `weekly-vault-optimizer`, `RVS Playbook` (×2), `Email backlog`, `SJB Prive e-mail Thur`, `SJB Prive e-mail Ma`, `C&W Work e-mail 24H`, `SJBrain Vault Operator`.

**On `last_run` being absent for all 4 Bezzy-PA triggers:** per the tool's own documented semantics, an absent `last_run` means "no run has been recorded — **either it never fired, or it's a routine that wakes its own bound session**, in which case run history isn't tracked this way." Genuinely ambiguous from the API alone. **TRIGGER CONFIGURATION: LIVE VERIFIED. TRIGGER EXECUTION HISTORY: UNKNOWN** — not assumed either way.

**Each Bezzy trigger carries its own inline system prompt** (confirmed present in the raw `list_triggers` output, not just referenced from the vault) that: (a) treats the session as fresh with no memory of prior runs, instructing it to re-read everything it needs from the vault; (b) for the two Gmail-Watch triggers, mandates a live Gmail-identity check as STEP 0 before reading any mail (never trust connector naming alone); (c) restates the authority/privacy boundaries inline rather than relying solely on the vault being read correctly. This is a real, verified design choice — each trigger fails safe (reports a blocked/misconfigured state) rather than silently acting against the wrong account, *by design*, though the actual fail-safe behavior itself was not observed firing this session.

**Cross-check against the vault's own documentation:** `BEZZY-ROADMAP.md` (dated 17–18 Aug) claims the Daily Briefing trigger exists as a record with no `cron_expression` and a zero-value `next_run_at`, i.e. that it "never fires on its own." This session's live `list_triggers` call shows the opposite: a valid `30 5 * * *` cron and a correct future `next_run_at`. This discrepancy is reported, not resolved — either the underlying issue was fixed after the doc was last updated, or something else changed. Treat the vault claim as stale rather than current.

**Known, self-acknowledged, unresolved gap (from the routines' own spec):** all four crons are fixed in UTC and do not auto-adjust for the late-October 2026 DST changeover — after that, all four will fire one hour off local time until manually corrected.

**Tooling note:** a *different* attempt to call `list_triggers` earlier today, in a different task within this same conversation, was refused with "requires approval." This attempt succeeded. The reason for the different outcome is unexplained and not investigated further here.

---

## 9. SKILL INVENTORY

Two distinct "skill" surfaces exist and should not be conflated:

**A. Claude Code skills (this environment's own skill system)** — includes `morning` (renders/sets up the morning brief as an HTML artifact — related to but **not the same mechanism** as the vault-triggered "Bezzy — Daily Briefing" routine), plus work-oriented skills (`cw-offerte-intake`, `cw-project-dossier`, `rvs-longlist-miner`) unrelated to Family PA.

**B. Vault `Skills/` folder content** (L1, read earlier this conversation) — includes `Vault-Operator/` (a separate, actively-running agent with 90+ dated daily logs through 2026-08-10, its own task-list and archive — **a distinct system from Bezzy PA**, worth not conflating), `os-mcp/setup-runbook.md`, and several work-skill subfolders (`cw-offerte-intake`, `cw-project-dossier`, `linkedin-writer`, `newsletter-writer`).

Dependency chain for the one skill genuinely part of Bezzy PA (Family Gmail Watch's mail-triage behaviour): not a discrete "skill" file — it is inline instruction text embedded directly in the trigger's own system prompt (§8), not a separately-invokable, reusable skill artifact. **No dedicated Bezzy-PA skill file was found in the vault's `Skills/` folder** — a gap, not a confirmed non-existence beyond this session's search depth.

---

## 10. GOOGLE WORKSPACE STATUS

| Service | API enabled? | OAuth scope available? | Tools implemented? | Tools exposed? | Auth verified? | Runtime tested? | Blocker type |
|---|---|---|---|---|---|---|---|
| Gmail | ✅ (live-confirmed working) | ✅ | ✅ | ✅ | ✅ (earlier turn) | ✅ PASS | — |
| Calendar | ✅ (live-confirmed working) | ✅ | ✅ | ✅ | ✅ (earlier turn) | ✅ PASS | — |
| Drive | ❌ live-confirmed disabled | ✅ (advertised) | ✅ | ✅ | ✅ (token valid) | ❌ FAILED | **GOOGLE CLOUD CONFIGURATION** |
| People/Contacts | ❌ live-confirmed disabled | ✅ | ✅ | ✅ | ✅ | ❌ FAILED | **GOOGLE CLOUD CONFIGURATION** |
| Tasks | ❌ live-confirmed disabled | ✅ | ✅ | ✅ | ✅ | ❌ FAILED | **GOOGLE CLOUD CONFIGURATION** |
| Chat | ❌ live-confirmed disabled | ✅ | ✅ | ✅ | ✅ | ❌ FAILED | **GOOGLE CLOUD CONFIGURATION** |
| Docs/Sheets/Slides/Forms | ❓ unknown | ✅ (advertised) | ✅ | ✅ | — | NOT TESTED (no reachable object ID; Drive discovery broken) | Depends on Drive fix first |
| Custom Search | N/A (API key based) | N/A | ✅ | ✅ | ❌ | ❌ FAILED | **TOOLING/DEPLOYMENT CONFIGURATION** — `GOOGLE_PSE_API_KEY` missing on Railway, explicitly not an OAuth or code problem |

Google Cloud project: `283055709294`. Enablement links were provided in an earlier turn of this conversation; **current enablement state is not re-verified today** because the connector itself requires re-authentication in this session.

---

## 11. RELAY / FAMILY BOUNDARY STATUS

**LIVE VERIFIED (`vault_relays`, this session):**
```
* SJBrain Relay — d6923d02-947d-4771-bd9d-80b5f89f6ce3   (active binding for this MCP session)
  Bezzy Family Relay — cc0c201b-1369-4ccc-9c9a-94ab38b30bb1
```
The Family Relay **exists** as a distinct relay — real, not aspirational. This session's `SJBrain_MPC` connector is bound to the *SJBrain* relay, not the Family relay, so this session cannot browse Family-relay content directly (consistent with intended isolation, though that consistency could equally be an artifact of binding rather than proof of an enforced boundary).

| Boundary | Technically enforced? | Prompt/doc enforced? | Notes |
|---|---|---|---|
| PA/** stays Sjoerd-only, never exposed to Family | UNKNOWN — NOT LIVE TESTABLE this session | ✅ documented repeatedly | No tool available in this session to attempt (and explicitly instructed not to attempt) a cross-boundary read |
| Family Relay isolation (a Family-scoped session cannot reach `PA/**`, `Personal/**`, etc.) | **NOT LIVE TESTABLE** — no credential/binding for the Family Relay in this session, by design | ✅ documented as the explicit precondition for unlocking Harry/Juliette routines | The vault's own roadmap independently reaches the same conclusion — several Family routines marked `BLOCKED` pending exactly this validation |
| Juliette access | Not present | N/A | Confirmed absent — no Juliette persona/account found anywhere in this reconnaissance |
| Personal Gmail vs Family Gmail | ✅ **technically enforced at the OAuth/session layer** (code-verified: distinct credentials, distinct connectors, `SECURITY VIOLATION` logging on mismatch) | ✅ also documented | The one boundary in this audit that is both code-verified *and* live-tested successfully |
| C&W (work) content never leaking into Family | UNKNOWN — not tested this session | ✅ documented | — |

**Bottom line:** exactly one boundary (Personal vs. Family Gmail identity) is both documented *and* technically enforced *and* live-tested. Every other boundary here is real only in the sense that it is consistently documented — none of the rest has been technically tested this session, and the biggest one (Family Relay isolation) has, per the vault's own record, never been validated at all.

---

## 12. SAFETY / AUTHORITY STATUS

The intended distinction — INFORMATION → RECOMMENDATION → SIGNAL → ACTION → EXTERNAL ACTION → APPROVAL → REPAIR — is **clearly and consistently documented** (`BEZZY.md` §5, `BEZZY-ROADMAP.md` §12, each routine's own "Authority" section).

Enforcement mechanism found: **PROMPT ENFORCED, not technically enforced**, for every PA-level authority rule examined (approval gates, no-repair, scope separation at the PA/Family boundary). The one exception is the Google OAuth session-isolation layer, which **is** technically enforced (code-verified) — but that protects *which Google account* a call can reach, not *whether* the PA is allowed to write to the vault or send an email.

**UNKNOWN discipline** — the one behavioural claim checkable against a real artifact: confirmed once, correctly applied, in `Open-Loops.md` ("UNKNOWN: of Arielle op 26-08 voor beide kinderen is"). One real, positive data point — not proof of consistent behaviour across many runs.

**No evidence found, in either direction, of a technical guard** that would stop a misconfigured or misbehaving future run from, say, sending an email from `bezzy.pa@gmail.com` — the write-capable Gmail tools exist and are exposed to the same connector that reads it; nothing observed this session removes them from a given trigger's tool access. Flagged as the single most important open question in this audit — not because misbehaviour has happened, but because the system's safety currently rests entirely on every future prompt being written correctly, with no independent backstop found.

---

## 13. MASTER GAP MATRIX

| Capability | Intended | Implemented | Runtime Verified | Technically Enforced | Dependencies | Status | Gap |
|---|---|---|---|---|---|---|---|
| Family Gmail read | ✅ | ✅ | ✅ (earlier turn) | ✅ (OAuth layer) | Bezzy_Google_MPC auth | 🟡 | Re-auth needed in this session |
| Family Calendar read | ✅ | ✅ | ✅ (earlier turn) | ✅ | same | 🟡 | same |
| Drive/Docs/Sheets/Slides/Forms | ✅ | ✅ | ❌ | N/A | Google Cloud API enablement | 🚧 | Enable 4–8 APIs (project 283055709294) |
| Contacts/Tasks/Chat | ✅ | ✅ | ❌ | N/A | same | 🚧 | same |
| Custom Search | ✅ | ✅ | ❌ | N/A | `GOOGLE_PSE_API_KEY` on Railway | 🚧 | Set env var, or accept as out of scope |
| Family Relay isolation | ✅ | 🔵 (relay exists) | ❌ | ❓ | Family-bound session/credential | 🚧 | Needs a session actually bound to the Family relay to test |
| Gmail write/send (approval-gated) | ✅ | ✅ (tools exist) | ❌ (correctly untested) | ❌ | Approval-flow implementation | ⚪ | The approval mechanism itself is not evidenced anywhere found this session |
| Calendar write (approval-gated) | ✅ | ✅ | ❌ (only used once, for the bulk import) | ❌ | same | ⚪ | same |
| Daily Briefing end-to-end | ✅ | ✅ (trigger) | ❌ unconfirmed | N/A | — | 🟡 | The vault's own `Status.md` names this exact missing test |
| Open Loops automation | ✅ | ✅ (partial) | 🟡 (one dated artifact, ambiguous mechanism) | ❌ (no dedup DB) | — | 🟡 | Dedup relies on the LLM re-reading its own output |
| PA Integrity Watch | ✅ | ✅ (trigger) | ❌ unconfirmed | ❌ (no-repair is prompt only) | — | 🟡 | — |
| Harry/Juliette persona & routines | ✅ (planned) | ⚪ | ❌ | N/A | Family Relay boundary validation | ⚪ | Explicitly gated by the still-unvalidated boundary above |
| WhatsApp integration | planned (future) | ❌ | ❌ | N/A | — | 🔴 | Not started, deliberately deferred |
| DST-safe scheduling | implied | ❌ | ❌ | N/A | Manual cron correction after Oct 2026 | 🔴 | Self-acknowledged, unresolved |

---

## 14. MISSING CAPABILITIES

- Full Docs/Sheets/Slides/Forms read/write (blocked upstream of Drive).
- A persistent (non-LLM-memory) dedup mechanism for Open Loops.
- A concrete, evidenced approval-delivery mechanism for writes (how a draft actually reaches Sjoerd/Juliette for yes/no).
- Any technical (not just documented) enforcement of the PA/Family/Work scope boundaries beyond the one OAuth-layer exception.
- A tested Family Relay isolation boundary.
- Harry (Juliette persona) and all downstream Family-only routines — correctly not started, gated on the above.
- WhatsApp integration — deliberately deferred, not evaluated further here.
- DST-safe cron scheduling.
- Confirmed execution history for all 4 core triggers.

---

## 15. BLOCKERS

| # | Blocker | Blocks | Who can resolve | Type |
|---|---|---|---|---|
| 1 | `Bezzy_Google_MPC` connector unauthenticated in this session | All further live Google Workspace testing | User (claude.ai connector settings) | Session/auth |
| 2 | `last_run` absent for all 4 Bezzy triggers, ambiguous per tool semantics | Confirming any routine has ever executed | Nobody, this turn — needs either a natural firing + recheck, or a direct answer from the platform on the field's semantics for session-bound routines | Tooling/observability |
| 3 | Drive, People, Tasks, Chat APIs disabled on Google Cloud project `283055709294` (last confirmed several turns ago, not re-verified today) | Drive/Docs/Sheets/Slides/Forms/Contacts/Tasks/Chat testing | User (Google Cloud Console) | External configuration |
| 4 | Family Relay isolation never technically tested | Harry/Juliette rollout, all Family-only automation beyond Gmail Watch | User/architecture decision — needs a session actually bound to the Family relay | Architecture/testing gap |
| 5 | No evidenced approval-delivery mechanism for writes | Any real Gmail-send or Calendar-write through the "normal" flow | Design decision needed, then implementation | Design gap |

---

## 16. PRIORITIZED ROADMAP

Built from the actual dependency chain found in this audit:

**P0 — critical blockers to a functioning PA**
1. Restore `Bezzy_Google_MPC` authentication in-session (user action).
2. Confirm trigger execution history one way or the other (observation, or a direct platform answer on `last_run` semantics for session-bound routines).
3. Enable the disabled Google Cloud APIs — Drive, People, Tasks, Chat at minimum (user action, Cloud Console).

**P1 — required for a production-grade PA**
4. Technically test Family Relay isolation from an actual Family-bound session.
5. Run the one missing end-to-end test the vault itself names: "Floor, wat moet ik vandaag weten?" (read-only, once auth is restored).
6. Design and evidence a concrete approval-delivery mechanism for writes.
7. Fix DST-unsafe cron scheduling (low urgency until late October 2026, but currently silently wrong-by-design after that date).

**P2 — important improvements**
8. Build a persistent dedup mechanism for Open Loops, instead of relying on the LLM re-reading its last markdown output.
9. Fix or deliberately deprioritize Custom Search (`GOOGLE_PSE_API_KEY` missing).
10. Merge the already-fixed `click` dependency vulnerability from `claude/security-review-fixes` into `main` (safe, tested, just needs a merge decision).

**P3 — future enhancements**
11. Harry/Juliette persona rollout (correctly gated behind P1 item 4).
12. WhatsApp integration (deliberately deferred).
13. Financial routines, household routines, work/RFP routines (all `FUTURE` per the vault's own roadmap, none started).

Dependency-ordered execution:

**STEP A** Restore connector auth → **STEP B** Google Cloud API enablement → **STEP C** Confirm trigger execution history → **STEP D** Run the named end-to-end judgment test → **STEP E** Design the approval mechanism → **STEP F** Exercise one real write through the normal approval flow → **STEP G** Technically test Family Relay isolation → **STEP H** DST-safe scheduling fix (independent, can happen any time) → **STEP I** Persistent dedup for Open Loops (hardening) → **STEP J** Full PA acceptance re-audit against §17.

This is deliberately *not* "build more routines." Per the vault's own `Status.md`: *"Niet verder bouwen aan de architectuur totdat één echte end-to-end test is gedaan."* This audit independently arrives at the same conclusion from the evidence gathered, not by trusting that sentence at face value.

---

## 17. FULL PA ACCEPTANCE CRITERIA

Derived only from what this audit actually found in the architecture, specs, routines and code — nothing invented.

**FULL PA =**

- [ ] All four core triggers have at least one **confirmed** execution visible via `list_triggers` `last_run`, not just a correct schedule.
- [ ] The end-to-end judgment test ("Floor, wat moet ik vandaag weten?") has been run live and independently reviewed for correct scope/privacy/UNKNOWN behaviour.
- [ ] Gmail, Calendar, Drive, Docs/Sheets/Slides, Contacts, Tasks and Chat all return real data in the same session (currently: 2 of 9 categories ever confirmed working).
- [ ] Family Relay isolation has been technically tested from an actual Family-bound session, not just documented.
- [ ] A concrete, evidenced approval mechanism exists for external communication and financial actions.
- [ ] At least one write action (Gmail send, Calendar create) has been exercised through the *normal* approval-gated flow and produced correct, auditable behaviour.
- [ ] Cron schedules are DST-safe or have a documented, automated correction mechanism.
- [ ] Open Loops has a dedup mechanism that does not depend solely on the LLM re-reading its own prior output.
- [ ] `debug_docs_runtime_info` / `debug_table_structure` are deliberately kept or deliberately disabled via `--disabled-tools`.
- [ ] The `click` security fix is merged (or a deliberate decision is recorded not to).
- [ ] Harry (Juliette persona) exists and operates strictly within Family scope, gated on the Relay-isolation item above.

**None of these boxes can honestly be checked today.** The last two are small and mechanical; everything else needs either a live test this audit could not perform, or a design decision not yet made.

---

## 18. EVIDENCE APPENDIX

- `vault_relays` (SJBrain_MPC, this session): 2 relays — SJBrain Relay (active), Bezzy Family Relay.
- `vault_folders` (SJBrain_MPC, this session): `PA`, `Gezin`, `Context`, `Daily`, `Intelligence`, `Personal`, `Projects`, `RVS`, `Resources`, `CW-Archief`, `Shared Files (root)`, `Skills`, `audits`.
- `vault_list` on `PA` (this session): 26 items including `Status.md`, `BEZZY-ROADMAP.md`, `CLAUDE.md`, `Policies/BEZZY.md`, `Policies/BEZZY-Golden-Rules.md`, `Policies/Calendar-Sources.md`, `Policies/Persona-Registry.md`, `Agents/Family-Orchestrator.md`, `Family-State/*` (7 files), `Backup/*` (6 files).
- `vault_read` this session, full content reviewed: `Status.md`, `Policies/BEZZY-Golden-Rules.md`, `Policies/BEZZY.md`, `Family-State/Open-Loops.md`, `BEZZY-ROADMAP.md`.
- `list_triggers` (this session): 12 total triggers on the account; full JSON captured for the 4 Bezzy-PA-relevant ones (IDs, cron, enabled, next_run_at, last_run — see §6, §8).
- Google Workspace live test results (earlier this same conversation, timestamped): `list_gmail_labels` PASS, `search_gmail_messages` PASS, `list_calendars` PASS (account `bezzy.pa@gmail.com`), `list_drive_items` FAILED (Drive API disabled), `list_spreadsheets` FAILED, `search_docs` FAILED, `list_contacts` FAILED (People API disabled), `list_task_lists` FAILED (Tasks API disabled), `list_spaces` FAILED (Chat API disabled), `get_search_engine_info` FAILED (missing `GOOGLE_PSE_API_KEY`).
- `bezzy-google-mcp` source code review (this conversation, earlier turns): `auth/oauth21_session_store.py`, `auth/credential_store.py`, `auth/mcp_session_middleware.py`, `core/http_utils.py`, `main.py` bind-host logic — full pytest suite (1620 passed, 2 skipped), ruff clean, `pip-audit` (1 vuln found and fixed on branch `claude/security-review-fixes`, not merged).

---

## 19. UNKNOWNS / UNVERIFIED ITEMS

- Whether any of the 4 core Bezzy triggers has ever actually fired (`last_run` absent; ambiguous per tool semantics).
- Current Google Cloud API enablement state for `283055709294` (last checked several turns ago in this conversation, not today).
- Whether the Family Relay isolation boundary actually holds under test — never tested, by anyone, per all evidence found.
- Whether PA Integrity Watch's "no repair" rule is backed by an actual tool restriction or is instruction-only.
- What mechanism (if any) currently delivers an approval request to Sjoerd/Juliette and captures their response.
- Contents of `Family-State/Activities.md`, `Financials.md`, `Household.md`, `This-Week.md`, `Today.md`, `Upcoming.md` — existence confirmed, contents not read this session.
- Full contents of `Agents/Family-Orchestrator.md`, `Policies/Persona-Registry.md`, `Policies/Calendar-Sources.md`, `Backup/ARCHITECTURE.md`, `Backup/RELAY-ARCHITECTURE.md`, `Backup/BEHAVIOUR.md` — referenced repeatedly by other documents, not independently read this session.
- Whether the discrepancy between the vault's claim ("Daily Briefing trigger never fires") and this session's live check (trigger has a valid cron and next_run_at) reflects a genuine fix since the doc was written, or a different underlying issue.
- Docs/Sheets/Slides/Forms API enablement state specifically (never tested, blocked upstream by Drive).
