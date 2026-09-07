---
name: foundation-schema
description: Define the shared entities that multiple modules will reference — the global data model seed — derived from the module dependency graph. Use at stage F.5, after the architecture is approved and before the project skeleton.
---

# Foundation schema

**Stage:** F.5 · **Agent:** backend-builder
**Reads:** `docs/00-global/architecture.md`, `docs/00-global/module-map.md`, `CONVENTIONS.md`
**Writes:** `docs/00-global/data-model.md` (template: `templates/00-data-model.md`)

## What belongs here, and only this

An entity is global when **two or more modules in the queue reference it**. The module map's
dependency graph already tells you which — that is what it was built for.

Everything else stays module-owned and is defined at M.3 by `schema-design`.

## The asymmetry that justifies being slightly greedy here

Entities are the one exception to rule-of-two restraint. Refactoring a table across shipped
modules means data migration against real client data. Refactoring a component means editing
files. So: if the dependency graph shows a second module *will* reference an entity, define it
globally now, even though only module 1 uses it today.

Do not extend this licence to services, utilities, or components. Those still wait for the
second real use.

## Procedure

1. Walk the dependency graph. Every entity referenced by two or more modules is a candidate.
2. For each, define: purpose, columns with types and nullability, primary key, natural keys,
   relationships, indexes implied by known access patterns, and soft-delete or archival policy.
3. Decide **identity strategy once** for the whole product: UUID, ULID, or sequential integer.
   Mixed identity strategies are a permanent irritation.
4. Decide **timestamp convention once**: which columns, what timezone, stored how.
5. Decide **soft delete once**. Whether, and if so, the column and the query convention.
6. Decide **multi-tenancy once**, if applicable — column, schema, or database separation. This
   is nearly impossible to retrofit.
7. Decide **audit trail once** — which mutations are recorded, in what shape, where.
8. Name the owner module for each entity even though it is global — someone must own its shape.
9. Record every entity in `inventory.md` **Entities**, with its consumers.

## Checklist

- [ ] Every global entity is referenced by two or more modules in the queue
- [ ] No module-specific entity has crept in
- [ ] Identity strategy decided and applied uniformly
- [ ] Timestamp convention decided and applied uniformly
- [ ] Soft-delete policy decided
- [ ] Multi-tenancy decided, if applicable
- [ ] Audit approach decided
- [ ] Every entity has an owner module recorded
- [ ] Relationships have explicit cardinality and delete behaviour
- [ ] Indexes reflect the access patterns implied by the BRDs, not guesses
- [ ] Recorded in `inventory.md`

## Failure modes

- **Kitchen-sink user table.** Everything about a person crammed into one entity because it
  felt global. Profile, preferences, and role assignments are often separate.
- **Deferred multi-tenancy.** If the client might ever have a second tenant, decide now.
- **Delete behaviour left to the database default.** Cascade deletes discovered in production
  are a very bad day.
- **Module-specific entities promoted early.** If only one module in the queue references it,
  it is not global.

## Handoff

`project-skeleton` (F.6) sets up migrations against this. At M.3 `schema-design` references
these entities and never duplicates them.
