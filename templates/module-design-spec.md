# Design spec — <NN> <module name>

Machine-readable handoff to `frontend-builder`. Pairs with the canvas: **spec first for intent,
canvas second for values.**

Every value is a token name from `00-global/design-system.md`. If a token is missing, add it
there first — never inline a value here.

## Screens

| Screen | Route | Purpose |
|---|---|---|

## Component inventory

Mark every element. This is what `read-design-spec` builds the plan from.

| Screen | Element | Verdict | Source |
|---|---|---|---|
| | | shared / extend / new | `Name` — module |

Must agree with the reuse plan in `spec.md`.

## States

Every data-bound element gets a full row. The happy path alone is not a design.

| Element | Default | Loading | Empty | No results | Error | Partial | Permission denied |
|---|---|---|---|---|---|---|---|

Interaction states for controls: hover, focus-visible, active, disabled.

## Data binding

What the builder would otherwise guess.

| Element | Source endpoint | Response field | Transform |
|---|---|---|---|

## Responsive behaviour

| Breakpoint | Layout | Reflows | Collapses | Hidden | Scrolls |
|---|---|---|---|---|---|

## Interaction rules

| Trigger | Behaviour |
|---|---|
| Submit | |
| Validation failure | |
| Destructive action | confirmation pattern |
| Navigate with unsaved changes | |
| Optimistic update | allowed on which actions |
| Success feedback | |

## Copy

Real microcopy. Placeholders ship to production more often than anyone admits.

| Location | Text |
|---|---|
| Page titles | |
| Labels | |
| Hints | |
| Empty state | |
| No results | |
| Error messages | |
| Confirmations | |
| Buttons | |

## New tokens required

Added to `00-global/design-system.md` before this spec references them.

| Token | Value | Reason |
|---|---|---|

## Accessibility

Beyond the primitives' baseline.

| Concern | Requirement |
|---|---|
| Heading order | |
| Landmarks | |
| Live regions | |
| Focus on route change | |
| Focus on modal open / close | |

## Canvas

**File:** · **Artboards:**
