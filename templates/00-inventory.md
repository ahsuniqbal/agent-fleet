# Inventory — <product name>

**The reuse ledger. Every agent reads this at M.0, before doing anything.**

An index, not an archive. One line per item, pointing at the module summary for detail.
Keep under ~300 lines; past that, split into `00-global/inventory/` by category.

Updated by `close-module` at M.9 of every module.

---

## Components

Format: `` `Name` `` — module — capabilities | states | used by

- `Button` — foundation — variants: primary/secondary/ghost, sizes: sm/md/lg | states: default/hover/focus/active/disabled/loading | used by: all

## Entities

Format: `` `table` `` — owner — key fields | referenced by

- `users` — global — id, email, role | referenced by:

## Endpoints

Format: `METHOD /path` — module — behaviour

- `GET /users` — 01 — paginated, `?role=` filter

## Services / utils

Format: `` `name` `` — path — module — purpose

## Hooks / stores

Format: `` `name` `` — module — purpose

## Patterns

**Decided. Do not re-decide.** This section is what prevents a second pagination style in
module 5.

| Concern | Pattern |
|---|---|
| Pagination | |
| Error body shape | |
| Filter & sort params | |
| Loading state | |
| Empty state | |
| No-results state | |
| Error state | |
| Permission-denied state | |
| Form validation | |
| Destructive confirmation | |
| Optimistic updates | when allowed |
| Toast / notification | |
| Authorization checks | |
| Audit logging | |
| Date / money encoding | |

## Events

Format: `` `event.name` `` — emitter — payload

## Deferred / known gaps

Punted work, so the next module does not rediscover it.

| Item | Punted from | Revisit at | Note |
|---|---|---|---|
