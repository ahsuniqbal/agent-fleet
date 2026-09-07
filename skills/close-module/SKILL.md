---
name: close-module
description: Close a shipped module by writing its summary and folding everything reusable into the global inventory index, so the next module's agents know what already exists. Use at stage M.9, the final step of every module loop. The mechanism that makes serial delivery accumulate instead of repeat.
---

# Close module

**Stage:** M.9 · **Agent:** reviewer
**Reads:** everything the module produced, `drift-check` verdicts, promotions
**Writes:** `docs/modules/NN/summary.md` (template: `templates/module-summary.md`),
`docs/00-global/inventory.md`, `docs/00-global/CHANGELOG.md`

## Index and detail, kept separate

Two artifacts with different jobs:

| File | Job | Read when |
|---|---|---|
| `00-global/inventory.md` | **index** — one line per item | at M.0, by every agent, every module |
| `modules/NN/summary.md` | **detail** — why, how, caveats | on demand, when the index points there |

If only summaries existed, module 7's agents would have to read and synthesise six documents —
expensive and lossy. If only an index existed, the reasoning behind each entry would be gone.

## What goes into the inventory

Update every section the module touched:

- **Components** — name, path, owning module, variants, states, current consumers
- **Entities** — name, owner, key fields, relationships, referencing modules
- **Endpoints** — method, path, purpose, owning module, notable behaviour
- **Services / utils** — name, path, purpose
- **Hooks / stores** — name, purpose, owning module
- **Patterns** — anything decided in this module that later modules must follow. This is the
  section that prevents a second pagination style.
- **Events** — name, emitter, payload shape
- **Deferred / known gaps** — what was punted, and where it should be revisited. Without this,
  the next module rediscovers the same gap from scratch.

Entry format — one line, scannable:

```markdown
- `DataTable` — modules/02 — sortable, paginated, row-select | states: loading/empty/error | used by: 02, 04
```

## What goes into the summary

Detail the index cannot carry: what was built and why, decisions taken and rejected, deviations
from the spec with reasons, `accept` verdicts from drift-check with their justifications,
contract amendments and what caused them, known limitations, performance notes, and anything the
next module should know before touching this code.

## Hygiene

Keep `inventory.md` under roughly **300 lines**. Past that, split into
`00-global/inventory/` by category and keep a short top-level index.

An index that stops being scannable stops being read, and an unread ledger means the whole
system fails quietly — every module rebuilding what already exists while the documents claim
otherwise.

## Checklist

- [ ] Every reusable component, service, hook, entity, and endpoint recorded
- [ ] Patterns section updated with anything later modules must follow
- [ ] Events recorded with payload shapes
- [ ] Promotions from `promote-shared` reflected, with consumer lists
- [ ] Deferred items and known gaps recorded with a suggested revisit point
- [ ] `accept` verdicts carried into the summary with justifications
- [ ] Contract amendments summarised
- [ ] Entries are one line each and point at the summary for detail
- [ ] `CHANGELOG.md` updated with promotions and global changes
- [ ] Inventory still under the line budget, or split
- [ ] Consumer lists updated on existing entries, not only new ones

## Failure modes

- **Recording only new things.** Existing entries need their consumer lists updated, or the
  rule of two cannot be evaluated next time.
- **Detail in the index.** It grows, stops being scannable, stops being read.
- **Omitting the Patterns section.** The most valuable part — it is what stops re-deciding.
- **Skipping deferred items.** The next module rediscovers the same gap and re-litigates it.
- **Closing without the summary.** The reasoning is gone within a week.

## Handoff

Next module in the queue starts at M.0 by reading the inventory you just wrote. That read is the
entire payoff of this stage.
