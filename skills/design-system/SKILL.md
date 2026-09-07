---
name: design-system
description: Establish the product's design tokens — color, typography, spacing, radius, elevation, motion — as the single source of visual truth before any component or screen is designed. Use at stage F.3, after the architecture is set and before the component library.
---

# Design system

**Stage:** F.3 · **Agent:** ux-engineer
**Reads:** `docs/00-global/requirements.md`, `docs/00-global/architecture.md`, any client brand
material
**Writes:** `docs/00-global/design-system.md` (template: `templates/00-design-system.md`)

Load the `frontend-design` skill alongside this one for aesthetic direction.

## Why tokens first

Every hardcoded value in the final codebase traces back to a token that did not exist when
someone needed it. Define the scale before anything consumes it.

## Procedure

1. **Establish direction** before values: what should this product feel like, and what visual
   decisions follow from that? Anchor it to the audience and the client's context, not to a
   generic default.
2. **Color.** Define semantic tokens, not just a palette:
   surface levels, text levels, border levels, primary/secondary action, and the full status
   set (success, warning, danger, info) each with foreground, background, and border variants.
   Check contrast ratios — WCAG AA minimum for text.
3. **Both themes.** Decide now whether the product is light, dark, or both. Retrofitting dark
   mode after four modules is expensive. If both, every token is defined in both.
4. **Typography.** A scale, not ad-hoc sizes. Family, weights, sizes, line heights, letter
   spacing. Name by role — display, heading levels, body, label, caption, code.
5. **Spacing.** One scale, consistently applied. A 4px or 8px base is conventional and worth
   sticking to.
6. **Radius, border width, elevation.** Small named scales.
7. **Motion.** Durations and easing curves, named by intent — instant, quick, moderate,
   deliberate. Plus the reduced-motion behaviour.
8. **Breakpoints.** Named, with the layout intent at each.
9. **Z-index scale.** Named layers. Ad-hoc z-index values are a guaranteed later bug.

## Checklist

- [ ] Every token has a semantic name, not a literal one (`--surface-raised`, not `--gray-100`)
- [ ] Status colors cover foreground, background, and border
- [ ] Text contrast meets WCAG AA against every surface it can sit on
- [ ] Dark theme decided explicitly, and defined if in scope
- [ ] Type scale is a scale, with line heights
- [ ] One spacing scale, no exceptions
- [ ] Motion includes a reduced-motion answer
- [ ] Focus-visible treatment is defined here, once
- [ ] Z-index layers named
- [ ] Breakpoints named with layout intent

## Failure modes

- **Literal names.** `--blue-500` forces every consumer to know what blue means. `--action-primary`
  survives a rebrand.
- **Palette without semantics.** Twelve colors and no rule for which to use where produces
  twelve inconsistent screens.
- **Dark mode deferred.** Decide now even if the answer is "light only" — that answer is what
  stops someone half-implementing it in module 5.
- **No focus treatment.** Then every component invents its own, and accessibility fails audit.

## Handoff

`component-library` (F.4) consumes these tokens. Every later `design-direction` at M.4
references token names from this file and adds new tokens here rather than inlining values.
