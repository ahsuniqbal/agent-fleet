---
name: compose-page
description: Assemble a module's screens from built components — routing, layout, data binding, state ownership, and the full set of page-level loading, empty, and error states. Use during stage M.6a after components exist.
---

# Compose page

**Stage:** M.6a · **Agent:** frontend-builder
**Reads:** `docs/modules/NN/design-spec.md`, the canvas, `docs/modules/NN/api-contract.md`,
`docs/00-global/inventory.md`, `CONVENTIONS.md`
**Writes:** module pages, routes, and page-level state

## Procedure

1. **Routing** per `CONVENTIONS.md` — paths, nesting, parameters, and route guards derived from
   the BRD's permission rules. A guard is not optional because the API also checks; both check.
2. **Layout** from the canvas, using the shared layout primitives and spacing tokens.
3. **State ownership** as decided in `spec.md`:
   - server data → the data-fetching layer named in conventions, never hand-rolled
   - filters, sorting, pagination, and tab selection → the URL, so state is shareable and
     survives reload
   - ephemeral UI state → local component state
   Deviating here is what makes module 5 behave differently from module 2.
4. **Page-level states** — the page has its own loading, empty, error, and permission-denied
   presentations, distinct from any individual component's. Follow the patterns in the inventory.
5. **Data binding** exactly as the design spec maps it, against the contract's schemas.
6. **Forms** — validation mirroring the BRD's rules, inline errors, submit disabled or busy
   during flight, server-side validation errors mapped back to the right fields, and an unsaved
   changes guard where the design spec calls for one.
7. **Destructive actions** — the confirmation pattern from the design spec, consistently.
8. **Accessibility at page level** — one `h1`, correct heading order, landmark regions, focus
   moved to the heading or main region on route change, page title updated.

## Checklist

- [ ] Routes match conventions; guards enforce BRD permissions
- [ ] Filters, sort, and pagination live in the URL
- [ ] Server state uses the conventional data layer
- [ ] Page-level loading, empty, no-results, error, and permission-denied states all present
- [ ] Every bound field verified against the contract
- [ ] Form validation mirrors the BRD rules
- [ ] Server validation errors map to specific fields
- [ ] Unsaved-changes guard where specified
- [ ] Destructive actions confirm consistently
- [ ] Heading order valid, one `h1`, landmarks correct
- [ ] Focus moves on route change; page title updates
- [ ] Responsive at every breakpoint
- [ ] No component logic leaked into the page that belongs in a component

## Failure modes

- **Filter state in component state.** Refresh loses it, links do not work, and the client
  notices immediately.
- **Missing page-level empty state.** Every list needs one.
- **Server errors as a generic toast.** The BRD specified per-error behaviour; implement it.
- **Route guards skipped** because the API enforces authorization. The user still sees a broken
  screen flash before the 403.
- **Focus not managed on navigation.** Screen reader users lose their place on every route change.

## Handoff

`wire-api-client` connects these to mocks generated from the contract. `integrator` swaps them
for real calls at M.7.
