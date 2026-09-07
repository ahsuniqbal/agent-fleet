# BRD — <NN> <module name>

**Depends on modules:** · **Depended on by:**

## Purpose

What this module lets users do, and why it sits at this queue position.

## Users of this module

| Role | What they do here |
|---|---|

## Reuse awareness

Read from `00-global/inventory.md`. Features here resembling something already shipped:

| Feature here | Resembles | Module |
|---|---|---|

## Features

### F1 — <name>

**Story:** As a <role>, I want <goal>, so that <outcome>.

**Happy path**

1.

**Alternate flows**

**Validation**

| Field | Required | Format | Length | Range | Unique | Notes |
|---|---|---|---|---|---|---|

**Edge cases** — mark `n/a` explicitly where a dimension does not apply

| Dimension | Behaviour |
|---|---|
| Error states | |
| Empty state | |
| No-results state | |
| First run — no data yet | |
| Permissions per role | |
| Ownership — act on others' records? | |
| Concurrency — simultaneous edit | |
| Limits & quotas | |
| Data lifecycle — create/edit/delete/archive/restore/purge | |
| Bulk operations — select-all, partial failure | |
| Side effects — notifications, emails, webhooks, audit | |
| Time — timezone, scheduling, expiry, retention | |
| Search & filter — what is searchable, sort, pagination | |
| Import / export — formats, limits, malformed input | |
| Offline / interruption — lost connection, unsaved changes | |
| Localisation — language, currency, date, number, direction | |
| Accessibility — beyond design system baseline | |

**Acceptance criteria**

```
Given <precondition>
When <action>
Then <observable outcome>
```

Include the unhappy paths. These become the e2e suite at M.7.

## Permission matrix

| Action | Role A | Role B | Role C |
|---|---|---|---|
| view | | | |
| create | | | |
| edit own | | | |
| edit others | | | |
| delete | | | |
| export | | | |

No cell left blank. "Everyone" is a decision and gets written down.

## Out of scope for this module

## Open questions

| Question | Options | Implication |
|---|---|---|
