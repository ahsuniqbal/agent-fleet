# Design system — <product name>

Single source of visual truth. Everything downstream references token names from this file.

## Direction

What this product should feel like, and what visual decisions follow. Anchored to the audience
and the client's context.

## Themes

**Light / dark / both:** <decide now — retrofitting dark mode after four modules is expensive>

## Color

Semantic names, never literal ones. `--action-primary`, not `--blue-500`.

| Token | Light | Dark | Use |
|---|---|---|---|
| `--surface-base` | | | |
| `--surface-raised` | | | |
| `--surface-sunken` | | | |
| `--text-primary` | | | |
| `--text-secondary` | | | |
| `--text-disabled` | | | |
| `--border-subtle` | | | |
| `--border-strong` | | | |
| `--action-primary` | | | |
| `--action-primary-hover` | | | |
| `--action-secondary` | | | |

### Status

Each with foreground, background, and border.

| Status | fg | bg | border |
|---|---|---|---|
| success | | | |
| warning | | | |
| danger | | | |
| info | | | |

### Contrast

| Pair | Ratio | Passes AA |
|---|---|---|

## Typography

**Family:** · **Fallback stack:**

| Token | Size | Weight | Line height | Letter spacing | Use |
|---|---|---|---|---|---|
| `--type-display` | | | | | |
| `--type-h1` | | | | | |
| `--type-h2` | | | | | |
| `--type-h3` | | | | | |
| `--type-body` | | | | | |
| `--type-label` | | | | | |
| `--type-caption` | | | | | |
| `--type-code` | | | | | |

## Spacing

Base unit: <4px / 8px>

| Token | Value |
|---|---|
| `--space-2xs` | |
| `--space-xs` | |
| `--space-sm` | |
| `--space-md` | |
| `--space-lg` | |
| `--space-xl` | |
| `--space-2xl` | |

## Radius, border, elevation

| Token | Value |
|---|---|
| `--radius-sm` | |
| `--radius-md` | |
| `--radius-full` | |
| `--border-width` | |
| `--elevation-raised` | |
| `--elevation-overlay` | |

## Motion

| Token | Duration | Easing | Intent |
|---|---|---|---|
| `--motion-instant` | | | |
| `--motion-quick` | | | |
| `--motion-moderate` | | | |

**Reduced motion:** <behaviour when `prefers-reduced-motion` is set>

## Focus

Defined once here so no component invents its own.

`--focus-ring:` · offset: · applies to:

## Z-index layers

| Token | Value | Layer |
|---|---|---|
| `--z-dropdown` | | |
| `--z-sticky` | | |
| `--z-overlay` | | |
| `--z-modal` | | |
| `--z-toast` | | |

## Breakpoints

| Name | Min width | Layout intent |
|---|---|---|
