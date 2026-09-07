---
name: component-library
description: Build the primitive component set from the design tokens — roughly ten to twelve reusable building blocks with full variant, state, and accessibility coverage. Use at stage F.4, after the design system and before any module work. Primitives only, never domain components.
---

# Component library

**Stage:** F.4 · **Agents:** ux-engineer + frontend-builder
**Reads:** `docs/00-global/design-system.md`, `CONVENTIONS.md`
**Writes:** the shared component library in code, plus the **Components** section of
`docs/00-global/inventory.md`

## Primitives only

Build roughly these and stop:

button · icon button · text input · textarea · select · checkbox · radio · switch · form field
wrapper (label, hint, error) · modal / dialog · drawer · table · toast · tabs · nav shell ·
card · badge · avatar · spinner / skeleton · tooltip · dropdown menu · pagination control

**Do not build domain components.** No `InvoiceRow`, no `UserPicker`, no `BookingCalendar` —
however certain you are they will be needed. Rule of two governs: a component becomes shared
when a *second* module needs it, via `promote-shared`.

The cost asymmetry is the reason. An unbuilt component costs one module a little work. A
wrongly-guessed shared component costs every module that has to work around it.

## Every primitive ships complete

A primitive is not done when it renders. It is done when it covers:

- **Variants** the design system implies — sizes, emphasis levels, tones
- **States** — default, hover, focus-visible, active, disabled, loading, error, read-only
- **Accessibility** — correct semantic element or full ARIA, keyboard operation, focus
  management, screen-reader labelling, `aria-live` where content changes
- **Responsive behaviour** at every named breakpoint
- **Both themes**, if the design system defines dark
- **Reduced motion** honoured

## Procedure

1. Read the design system. Every value comes from a token — no exceptions, no "just this one".
2. Build each primitive against the checklist above.
3. Verify keyboard-only operation for every interactive primitive. Tab order, Escape, Enter,
   arrow keys where the pattern expects them, focus trap in modals and drawers, focus return on
   close.
4. Verify contrast for every state, not just default — disabled and hover are the usual failures.
5. Record each primitive in `inventory.md` **Components**: name, path, variants, states,
   one-line purpose.

## Checklist

- [ ] Zero hardcoded colors, spacing, radii, font sizes, or durations
- [ ] Every interactive primitive is keyboard operable
- [ ] Focus-visible uses the design system's defined treatment
- [ ] Modal and drawer trap focus and restore it on close
- [ ] Disabled states meet contrast requirements
- [ ] Loading states exist where an action can be async
- [ ] Form field wrapper handles label, hint, error, and required marking consistently
- [ ] Table has defined empty, loading, and error presentations
- [ ] Every primitive recorded in `inventory.md`
- [ ] No domain-specific component was built

## Failure modes

- **Anticipatory building.** The single most common and most costly error here.
- **Variant explosion.** Fifteen button variants means nobody knows which to use. Three or four
  emphasis levels and two or three sizes covers real products.
- **States as an afterthought.** A button without a loading state means every module invents
  its own spinner placement.
- **Unrecorded components.** A primitive missing from `inventory.md` will be rebuilt in module 3.

## Handoff

Foundation freezes after this. Module work at M.4 and M.6a builds on these primitives and must
check the inventory before creating anything new.
