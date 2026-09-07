# Global data model — <product name>

Shared entities only: those referenced by **two or more modules** in the build queue.
Module-owned tables live in each module's `data-model.md`.

## Conventions — decided once

| Decision | Choice |
|---|---|
| Identity strategy | UUID / ULID / sequential |
| Timestamp columns | |
| Timezone storage | |
| Soft delete | yes / no — column and query convention |
| Multi-tenancy | none / column / schema / database |
| Audit approach | which mutations, what shape, stored where |
| Naming | table and column casing |

Mixed identity or timestamp strategies are a permanent irritation. Multi-tenancy is nearly
impossible to retrofit.

## Entities

### `<table_name>`

**Owner module:** · **Referenced by:** · **Purpose:**

| Column | Type | Null | Default | Constraint | Notes |
|---|---|---|---|---|---|

**Primary key:** · **Natural key:**

**Relationships**

| Related | Cardinality | FK | ON DELETE |
|---|---|---|---|

**Indexes**

| Index | Columns | Justified by |
|---|---|---|

**States** — if the entity has a status

| From | To | Trigger | Enforced where |
|---|---|---|---|

**Retention:** how long rows live, what archives, what purges, what cascades

## Entity relationship diagram

```mermaid
erDiagram
```

## Deliberate denormalisation

| Table | Column | Reason | Access pattern it serves |
|---|---|---|---|
