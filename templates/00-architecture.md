# Architecture — <product name>

Global and cross-cutting only. Per-module technical detail lives in each module's `spec.md`.

## Driving constraints

| Constraint | Source | Architectural consequence |
|---|---|---|

Anything here that does not trace to a requirement is decoration.

## Shape

**Chosen:** monolith / modular monolith / services
**Rejected:** <alternatives>
**Why:** <against the actual constraints, not imagined future scale>

## Code structure

How `module-map.md` maps onto directories, packages, or deployables.

```
<tree>
```

## Cross-cutting concerns

| Concern | Owner | Approach |
|---|---|---|
| Authentication | | |
| Authorization model | | roles / scopes / ownership-based |
| Error handling | | |
| Logging | | |
| Audit trail | | |
| Notifications | | |
| File upload & storage | | |
| Background jobs | | |
| Caching | | |
| Feature flags | | |
| i18n | | |
| Rate limiting | | |

## Decided once, for the whole product

These get re-invented per module if not fixed here. Copy both into the inventory's Patterns
section.

**Error shape:**
```json
```

**Pagination:** cursor / offset — parameter names, metadata shape

**Filter & sort convention:**

**Status code meanings:**

**Date / time / money encoding:**

## Data flow

For the two or three most important journeys: where data enters, what transforms it, where it
rests.

## Integration points

| System | Protocol | Auth | Failure behaviour | Other side's owner |
|---|---|---|---|---|

## Decisions

### <decision>
**Chosen:** · **Rejected:** · **Why:** · **Revisit if:**

## Non-functional targets

Concrete enough to test against.
