---
description: Close a shipped module — write its summary and fold everything reusable into the global inventory index.
argument-hint: [module name or number, or blank for the most recently shipped]
---

Close module: $ARGUMENTS

Blank means the most recently shipped module in `docs/00-global/module-map.md`.

Use the `reviewer` agent with the `close-module` skill.

## What this produces

| File | Role | Read when |
|---|---|---|
| `docs/modules/NN/summary.md` | **detail** — why, how, caveats | on demand |
| `docs/00-global/inventory.md` | **index** — one line per item | at M.0, every module, by every agent |
| `docs/00-global/CHANGELOG.md` | promotions and global changes | when tracing history |

## Must be captured

- Every reusable component, service, hook, entity, endpoint, and event
- **Patterns** established that later modules must follow — the section that prevents a second
  pagination style
- Promotions from `promote-shared`, with consumer lists
- `accept` verdicts from `drift-check`, with justifications, so nobody re-raises them
- Contract amendments and what caused them
- Known limitations and deferred items, with a revisit point

## Hygiene

- Index entries are **one line**, pointing at the summary for detail
- Update consumer lists on **existing** entries, not only new ones — the rule of two cannot be
  evaluated otherwise
- Keep `inventory.md` under ~300 lines; past that, split into `00-global/inventory/` by category

## Why this stage is not optional

The next module's agents start at M.0 by reading the inventory. An unwritten summary means the
next module rebuilds what this one already has, and the ledger quietly stops being true.

## On completion

Report what was added to the inventory, and name the next module in the queue.
