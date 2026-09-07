# Data model — <NN> <module name>

Module-owned tables only. Shared entities are referenced, never duplicated.

Written **before** the API contract, so response schemas are grounded in real tables.

## Referenced shared entities

| Entity | Owner | Used for | FK column here |
|---|---|---|---|

Never re-create these. Never shadow them with a near-copy. Extending one is an architecture
change — raise it.

## Owned tables

### `<table_name>`

**Purpose:**

| Column | Type | Null | Default | Constraint | BRD rule it enforces |
|---|---|---|---|---|---|

**Primary key:** · **Natural key:**

**Relationships**

| Related | Cardinality | FK | ON DELETE |
|---|---|---|---|

Never leave `ON DELETE` to a database default.

**Indexes**

| Index | Columns | Unique | Access pattern from the BRD |
|---|---|---|---|

**State transitions** — if the table has a status

| From | To | Trigger | Enforced where |
|---|---|---|---|

**Retention:** lifespan, archival, purge, cascade behaviour

## Conventions followed

Confirm each against `00-global/data-model.md`.

- [ ] Identity strategy
- [ ] Timestamp columns
- [ ] Soft delete
- [ ] Multi-tenancy column
- [ ] Audit approach
- [ ] Naming

## Deliberate denormalisation

| Table | Column | Reason | Access pattern it serves |
|---|---|---|---|

## Migration notes

Ordering constraints, dependencies on other modules' migrations, backfill needs.

## ERD

```mermaid
erDiagram
```
