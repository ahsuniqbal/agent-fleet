---
name: schema-design
description: Design the tables this module owns, referencing shared global entities without duplicating them. Use at stage M.3, after the module spec is approved. Produces the module data model that the API contract is grounded in.
---

# Schema design

**Stage:** M.3 · **Agent:** backend-builder
**Reads:** `docs/00-global/inventory.md`, `docs/00-global/data-model.md`,
`docs/modules/NN/spec.md`, `docs/modules/NN/brd.md`, `CONVENTIONS.md`
**Writes:** `docs/modules/NN/data-model.md` (template: `templates/module-data-model.md`)

Note the ordering: this runs **before** the API contract. The contract author needs real tables
so the response schemas are grounded in what actually exists rather than invented.

## Owned versus referenced

The spec already split these. Honour it:

- **Owned** — this module creates the table and defines its shape. Design it here.
- **Referenced** — defined in `00-global/data-model.md` or another module. Add a foreign key.
  Never re-create it, never shadow it with a near-copy.

If an owned table starts looking like a variant of a shared entity, stop. That is a signal for
the architect, not a table to write.

## Procedure

1. Derive entities from the BRD's nouns and the spec's owned-entity list.
2. Normalise to third normal form by default. Denormalise only with a recorded reason —
   a measured access pattern, not a hunch.
3. For every column: type, nullability, default, and the constraint that enforces the BRD's
   validation rule. Validation lives in the database as well as the application; the
   application can be bypassed.
4. Follow the global conventions without deviation: identity strategy, timestamps, soft delete,
   multi-tenancy column, audit approach.
5. Relationships: cardinality, and explicit `ON DELETE` behaviour for every foreign key.
   Never leave delete behaviour to a default.
6. Indexes derived from the actual access patterns in the BRD — the filters, sorts, and lookups
   the screens perform. Include the foreign keys that will be joined. Note uniqueness
   constraints, including partial and composite ones.
7. State transitions: if an entity has a status, enumerate the legal transitions and where they
   are enforced.
8. Retention: how long rows live, what archives, what purges, what cascades.

## Checklist

- [ ] Every owned table traces to the spec's owned-entity list
- [ ] No shared entity duplicated or shadowed
- [ ] Every BRD validation rule has a database constraint where expressible
- [ ] Every foreign key has explicit `ON DELETE` behaviour
- [ ] Identity, timestamp, soft-delete, and tenancy conventions followed exactly
- [ ] Indexes justified by a named access pattern from the BRD
- [ ] Unique constraints cover the BRD's uniqueness requirements
- [ ] Status fields have enumerated legal transitions
- [ ] Denormalisation, if any, has a recorded reason
- [ ] Nothing here contradicts `00-global/data-model.md`

## Failure modes

- **Shadow entities.** `module_users`, `customer_profile` sitting alongside a global `users`.
  The most damaging error available at this stage.
- **Validation only in the application.** The API is not the only writer — migrations, scripts,
  and support tooling all reach the database.
- **Default delete behaviour.** Discovered when a cascade removes six months of records.
- **Indexes by superstition.** Index what the screens actually query.
- **Missing state machine.** Statuses without enumerated transitions become invalid states in
  production.

## Handoff

`api-contract` at M.5 reads this alongside the design spec. `migrations` at M.6b implements it.
