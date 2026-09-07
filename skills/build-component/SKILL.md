---
name: build-component
description: Build the components a module needs, with full variant, state, and accessibility coverage, using only design tokens and reusing shared components rather than forking them. Use during stage M.6a after the build plan is made.
---

# Build component

**Stage:** M.6a · **Agent:** frontend-builder
**Reads:** the build plan, `docs/modules/NN/design-spec.md`, the canvas,
`docs/00-global/design-system.md`, `docs/00-global/inventory.md`, `CONVENTIONS.md`
**Writes:** module components; extensions to shared components where general

## Reuse first, every time

Before creating a file, check the inventory. If something close exists:

- **General need** → extend the shared component with a new variant or prop
- **Module-specific need** → compose the shared component, do not fork it
- **Genuinely different** → build new, and only if the reuse plan agreed

Forking a shared component is never correct. Two divergent copies of the same component is the
exact failure `drift-check` exists to catch, and it costs a refactor to unwind.

## Tokens only

No hardcoded colors, spacing, radii, font sizes, shadows, or durations. If the design spec names
a token that does not exist, raise it — `ux-engineer` adds it to the design system. Inlining the
value is how a design system dies.

## A component is done when every state works

From the state matrix: default, hover, focus-visible, active, disabled, loading, error,
read-only where applicable. For data-bound components also: empty, no-results, partial,
permission-denied.

"It renders with test data" is not done.

## Accessibility is part of building, not a later pass

- Correct semantic element, or complete ARIA if none fits
- Keyboard operable: tab order, Enter and Space where expected, Escape to dismiss, arrow keys
  for composite widgets
- Focus visible using the design system's treatment, never removed
- Labels associated with controls; errors linked via `aria-describedby`
- `aria-live` for content that updates without a navigation
- Focus managed on open and restored on close for anything overlaying

## Checklist

- [ ] Inventory checked before creating anything
- [ ] No shared component forked
- [ ] Zero hardcoded design values
- [ ] Every state from the matrix implemented
- [ ] Keyboard operable end to end
- [ ] Focus-visible present and correct
- [ ] Errors announced to assistive technology
- [ ] Responsive at every named breakpoint
- [ ] Both themes correct, if the product has both
- [ ] Reduced motion honoured
- [ ] Follows `CONVENTIONS.md` naming and file placement
- [ ] Props typed; no untyped escape hatches
- [ ] Long lists virtualised or paginated per the design spec, not rendered wholesale

## Failure modes

- **Forking instead of extending.** The costliest habit in this role.
- **One-off values "just for this screen".** They are never just for that screen.
- **States added later.** They are not; the module ships with loading spinners missing.
- **Accessibility as a cleanup pass.** It never happens, and retrofitting is harder than building
  it in.
- **Building something the reuse plan said to reuse.** Raise the conflict instead.

## Handoff

`compose-page` assembles these into screens. Anything built here that a later module will
plausibly need is a `promote-shared` candidate at M.8 — but only on second actual use.
