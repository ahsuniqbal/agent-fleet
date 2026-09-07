---
name: design-direction
description: Produce a module's design — a visual canvas for human and client review, plus a machine-readable design spec that the frontend builder implements from. Use at stage M.4, after the module spec is approved. Always emits both artifacts.
---

# Design direction

**Stage:** M.4 · **Agent:** ux-engineer
**Reads:** `docs/00-global/inventory.md`, `docs/00-global/design-system.md`,
`docs/modules/NN/brd.md`, `docs/modules/NN/spec.md`
**Writes:** canvas artboards (via the `design` skill) **and**
`docs/modules/NN/design-spec.md` (template: `templates/module-design-spec.md`)

Load `frontend-design` alongside this skill. Load `dataviz` before designing any chart.

## Two artifacts, both required

| Artifact | For | Carries |
|---|---|---|
| Canvas | you and the client | composition, spacing, hierarchy — visual truth |
| `design-spec.md` | the frontend builder | token names, component inventory, states, breakpoints, data binding, interaction rules |

Canvas alone makes the builder guess token names and miss every non-default state. Spec alone
cannot convey layout economically. The builder reads the spec first for intent, then the canvas
for values.

## Check the inventory before designing anything

The **Components** and **Patterns** sections tell you what exists. Designing a second date
picker, a second empty state treatment, or a second pagination control is the most expensive
mistake available in this role — it costs a build, a drift-check, a refactor, and a promotion.

The spec's reuse plan already committed to specific components. Design with those.

## What the design spec must contain

1. **Screen inventory** — every screen and modal, with its route and purpose.
2. **Component inventory per screen** — for each element, whether it is an existing shared
   component, an extension of one, or new to this module. Mark them explicitly; this is what
   `read-design-spec` uses to plan the build.
3. **Every state, for every data-bound element**: default, loading, empty, no-results, error,
   partial, permission-denied. Plus the interaction states for controls: hover, focus-visible,
   active, disabled.
4. **Token references** — never raw values. If a needed token does not exist, add it to
   `00-global/design-system.md` first, then reference it here.
5. **Responsive behaviour** at each named breakpoint — what reflows, what collapses, what hides,
   what becomes scrollable.
6. **Data binding** — which field of which API response populates which element. This is what
   stops the builder from guessing.
7. **Interaction rules** — what happens on submit, on validation failure, on destructive action,
   on navigation with unsaved changes. Confirmation patterns. Optimistic update decisions.
8. **Copy** — real microcopy for labels, empty states, errors, and confirmations. Placeholder
   copy ships to production more often than anyone admits.
9. **Accessibility notes** beyond the primitives' baseline: heading order, landmark structure,
   live regions, focus movement on route and modal changes.

## Checklist

- [ ] Inventory checked; reuse plan honoured
- [ ] Every screen in the BRD has a design
- [ ] Every state from the BRD's edge case list is designed, not just the happy path
- [ ] Every value is a token reference
- [ ] New tokens added to the design system, not inlined
- [ ] Each element marked shared / extended / new
- [ ] Responsive behaviour at every breakpoint
- [ ] Data binding maps to the module's actual API surface
- [ ] Real copy, no lorem, no placeholders
- [ ] Destructive actions have a defined confirmation pattern
- [ ] Focus and live-region behaviour specified
- [ ] Canvas and spec agree with each other

## Failure modes

- **Canvas without spec.** Guaranteed token invention and missing states downstream.
- **Happy path only.** The BRD listed the edge cases at M.1 so they could be designed here.
- **Raw values in the spec.** They become hardcoded values in the codebase, then drift-check
  findings, then refactors.
- **Redesigning an existing pattern.** Two empty state treatments in one product is drift.
- **Placeholder copy.** It ships.

## Handoff

Human and client review the canvas. Then `api-contract` at M.5 reads this spec to ensure
endpoints return the fields these screens actually need.
