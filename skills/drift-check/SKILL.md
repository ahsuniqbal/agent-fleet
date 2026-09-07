---
name: drift-check
description: Audit a finished module for consistency against the global inventory, design system, and conventions established by earlier modules — duplicated components, hardcoded values, diverging patterns, shadowed entities. Use at stage M.8, alongside /code-review. Guards against a serial pipeline producing several different applications.
---

# Drift check

**Stage:** M.8 · **Agent:** reviewer
**Reads:** the finished module, `docs/00-global/inventory.md`,
`docs/00-global/design-system.md`, `docs/00-global/data-model.md`, `CONVENTIONS.md`,
`docs/modules/NN/spec.md` reuse plan
**Writes:** verdicts of **promote**, **refactor**, or **accept**

## This is not a bug hunt

`/code-review` handles correctness. You handle **consistency**. Nothing else in a serial
pipeline forces module 7 to resemble module 1. Left unchecked, the result is a codebase that
reads like several different applications stitched together.

## What to scan for

| Category | Look for |
|---|---|
| **Component duplication** | A new component doing what an inventory component already does. Check by behaviour, not name — `ItemList` and `RecordTable` can be the same thing. |
| **Hardcoded values** | Any color, spacing, radius, font size, shadow, or duration not coming from a token |
| **Endpoint convention drift** | Pagination style, error shape, filter parameter naming, status code usage differing from earlier modules |
| **Entity shadowing** | A module table duplicating or near-copying a shared entity |
| **Service duplication** | A backend util or service doing what an inventory service already does |
| **State pattern drift** | Loading, empty, error, and permission-denied treatments differing from the established patterns |
| **Reuse plan violations** | Anything the plan said to reuse that was built instead |
| **Naming drift** | File, component, route, column, or event naming departing from conventions |
| **Auth pattern drift** | A second authorization mechanism, or checks placed differently |
| **Client layer drift** | A second HTTP client, a second error normaliser |

## Verdicts

- **promote** — a rule-of-two hit: a second module now needs this. Hand to `promote-shared`.
- **refactor** — real drift with no upside. Must be fixed before shipping: hardcoded values,
  duplicated components, convention violations.
- **accept** — a deliberate, justified difference. Record the justification in the module summary
  so the next reviewer does not re-raise it.

## Procedure

1. Read the reuse plan first. It is the module's own statement of intent — deviations from it
   are the highest-signal findings available.
2. Grep for raw design values across the module's files.
3. Inventory every component the module created and compare each by behaviour against the
   existing library.
4. Compare every new endpoint's shape against the patterns section of the inventory.
5. Compare new tables against the global data model.
6. Compare loading, empty, and error treatments against earlier modules.
7. Produce the verdict list, most consequential first.

## Checklist

- [ ] Reuse plan compared against what was actually built
- [ ] No raw design values anywhere in the module
- [ ] Every new component checked by behaviour against the library
- [ ] Endpoint conventions match earlier modules
- [ ] No shadowed entities
- [ ] No duplicated services or clients
- [ ] State treatments consistent
- [ ] Naming consistent
- [ ] Authorization uses the single global mechanism
- [ ] Every finding has a verdict; every **accept** has a recorded justification

## Failure modes

- **Matching on names.** Duplicates usually have different names. Compare what things do.
- **Accepting drift to avoid rework.** It compounds — module 8 will copy module 7.
- **Promoting on first use.** Rule of two exists because anticipated abstractions are usually
  wrong.
- **Turning into a code review.** Correctness is `/code-review`'s job; stay on consistency.

## Handoff

`promote-shared` executes the promotions. Then the human ships and `close-module` records
everything in the ledger.
