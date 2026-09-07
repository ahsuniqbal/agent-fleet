---
name: migrations
description: Write reversible, safe database migrations from a module's data model, separating schema changes from backfills and planning for real client data. Use during stage M.6b before implementing endpoints.
---

# Migrations

**Stage:** M.6b · **Agent:** backend-builder
**Reads:** `docs/modules/NN/data-model.md`, `docs/00-global/data-model.md`, `CONVENTIONS.md`
**Writes:** migration files

## Assume real data

By module 3, the client has data in this database. Every migration runs against it. Write each
one as though a rollback at 2am is a live possibility, because occasionally it is.

## Rules

1. **Forward and rollback.** Every migration has both. A rollback that loses data is documented
   as such, loudly, in the migration itself.
2. **Schema and data are separate migrations.** Adding a column is one migration; populating it
   is another. Mixed, they cannot be rolled back independently and a failed backfill takes the
   schema change with it.
3. **Additive first.** To change a column: add the new one, backfill, switch the application to
   read it, then drop the old one in a *later* release. Never rename in place on a table with
   real data and a running application.
4. **Nullable, then constrained.** Add a non-null column as nullable with no default, backfill,
   then add the constraint. Adding non-null with a default to a large table can lock it.
5. **Index creation must not block.** Use the concurrent or online path your database provides.
6. **Batch backfills.** Never a single statement over a large table — it holds locks and can
   time out halfway with no clean recovery.
7. **Idempotent where possible.** A migration that partly ran should be safely re-runnable.
8. **No application logic in migrations.** They must run correctly against any version of the
   application code.
9. **Order matters.** Foreign keys after their referenced tables. State it explicitly if this
   module's migrations must run after another module's.

## Checklist

- [ ] Every migration has a tested rollback
- [ ] Destructive rollbacks documented in the file itself
- [ ] Schema and backfill separated
- [ ] No in-place rename on a populated table
- [ ] Non-null columns added in the nullable-backfill-constrain sequence
- [ ] Indexes created without blocking writes
- [ ] Backfills batched
- [ ] Foreign keys declare `ON DELETE` behaviour matching the data model
- [ ] Constraints match the BRD validation rules
- [ ] Migration order and cross-module dependencies stated
- [ ] Tested forward and back on a database seeded with realistic volume
- [ ] Matches `data-model.md` exactly — no undocumented columns

## Failure modes

- **Untested rollback.** Discovered when it is needed.
- **Combined schema and backfill.** The failure mode that turns a small problem into an outage.
- **`ALTER TABLE ... SET NOT NULL` on a large table.** Table lock, timeout, blocked application.
- **Blocking index creation.** Same outcome.
- **Silent divergence from the data model.** The contract and the design were built against that
  document; the database must match it.
- **Migrations that import application code.** They break when the code changes and old
  migrations re-run on a fresh environment.

## Handoff

`api-endpoint` implements handlers against this schema. `integrator` runs migrations as part of
end-to-end verification at M.7.
