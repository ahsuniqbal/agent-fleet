---
description: Run Phase A — take a client brief through requirements, module decomposition, architecture, design system, primitives, foundation schema, and project skeleton.
---

Run **Phase A — Foundation** for this project. Once per project, before any module work.

Client input: $ARGUMENTS

## Before starting

1. Check `CONVENTIONS.md` at the plugin root or project root. If the stack fields say `TBD`,
   **ask the user** before F.6. Do not guess a stack.
2. Create `docs/00-global/` and `docs/modules/` if absent.
3. Copy the relevant files from `templates/` as each stage starts.

## Stages — stop at every gate

| Stage | Agent | Skill | Output |
|---|---|---|---|
| F.0 | `product-owner` | `requirements-intake` | `docs/00-global/requirements.md` |
| 🚦 | — | — | **STOP.** Present open questions. Wait for client answers. |
| F.1 | `product-owner` | `module-decomposition` | `docs/00-global/module-map.md` |
| 🚦 | — | — | **STOP.** Present the build queue with reasons. Wait for the user to approve or edit `order:`. |
| F.2 | `system-architect` | `service-design` | `docs/00-global/architecture.md` |
| F.3 | `ux-engineer` | `design-system` | `docs/00-global/design-system.md` |
| F.4 | `ux-engineer` + `frontend-builder` | `component-library` | primitives only |
| F.5 | `backend-builder` | `foundation-schema` | `docs/00-global/data-model.md` |
| F.6 | `backend-builder` | `project-skeleton` | repo, routing, CI, migration runner |
| 🚦 | — | — | **STOP.** Foundation frozen. |

F.3→F.4 and F.5→F.6 are independent chains and may run concurrently after F.2.

## Gates are hard stops

Do not continue past a 🚦 on your own judgment. A wrong module order or an unapproved
requirement set costs rework on every module that follows.

## On completion

Seed `docs/00-global/inventory.md` from `templates/00-inventory.md` with:

- the primitives built at F.4
- the entities defined at F.5
- the patterns decided at F.2 — pagination, error shape, logging, audit, date and money encoding

Then report: modules in the queue, what module 1 is, and what the user must decide before
`/module` runs.
