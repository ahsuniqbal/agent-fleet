---
name: groom-module
description: Turn one module's BRD into a detailed technical spec, including the mandatory reuse plan that classifies every capability as reuse, extend, or new against the global inventory. Use at stage M.2, after the client approves the BRD and before schema or design work.
---

# Groom module

**Stage:** M.2 · **Agent:** system-architect
**Reads:** `docs/00-global/inventory.md`, `docs/modules/NN/brd.md`,
`docs/00-global/architecture.md`, `docs/00-global/data-model.md`, `CONVENTIONS.md`
**Writes:** `docs/modules/NN/spec.md` (template: `templates/module-spec.md`)

## The reuse plan is the point of this stage

Everything else here is ordinary technical grooming. The reuse plan is what stops a serial
pipeline from producing seven applications wearing a trench coat.

Every capability the BRD requires is classified against the inventory:

```markdown
## Reuse plan

| Need | Verdict | Source | Justification if new |
|---|---|---|---|
| user picker | reuse | `UserSelect` — modules/01 | |
| line-item table | extend | `DataTable` + editable cells | |
| paginated list endpoint | reuse | cursor pattern — inventory Patterns | |
| tax calculation | new | — | no monetary rule engine exists; tax rules are jurisdiction-specific and used nowhere else |
```

Rules:

- The table covers **every** capability, not the interesting ones.
- Every **new** row carries a justification naming what you checked and why it does not fit.
- A **new** row without justification is rejected at the human gate.
- If the BRD flagged a similarity to a shipped feature, the table must address it.

## The rest of the grooming

1. **Entities touched** — split into owned by this module vs referenced from global or another
   module. Reference, never duplicate. If you need to *extend* a shared entity, that is an
   architecture change: raise it rather than deciding here.
2. **API surface** — the endpoints this module will expose, at resource level. Full schemas
   come at M.5 once the data model and design spec exist.
3. **State ownership** — what lives on the server, what lives in client state, what lives in
   the URL. Decide once here or every screen decides differently.
4. **Background jobs** — what runs async, on what trigger, with what retry and failure
   behaviour.
5. **Events** — emitted and consumed. Name them so later modules can subscribe.
6. **Module dependencies** — upstream (what this needs) and downstream (what will need this).
   Downstream matters: it tells you what to make stable.
7. **Permissions model** — map the BRD's per-role rules onto the architecture's authorization
   model. Any gap is a raised question, not a local invention.
8. **Non-functionals** — expected volumes, response time targets, any limits from the BRD.
9. **Test plan** — what gets unit tested, what gets e2e tested, what fixtures are needed.
10. **Rollout** — feature flag, migration ordering, backfill, and whether anything must ship in
    a particular sequence.
11. **Open technical questions** — with options and implications, for the human gate.

## Checklist

- [ ] Reuse plan covers every capability in the BRD
- [ ] Every "new" verdict is justified against something you actually checked
- [ ] Entities split into owned vs referenced, with no duplication of a shared entity
- [ ] Every BRD acceptance criterion is technically addressed by something in this spec
- [ ] Permissions mapped onto the global authorization model
- [ ] State ownership decided
- [ ] Events named
- [ ] Downstream dependents identified
- [ ] Existing patterns from the inventory adopted, not re-decided
- [ ] Open questions carry options and implications

## Failure modes

- **Reuse plan written after the design.** Then it rationalises what was already built. Write it
  first; it is meant to constrain.
- **"New" as the default verdict.** If most rows are new by module 4, the inventory is not being
  read. That is the system failing.
- **Re-deciding settled patterns.** Pagination and error shape were decided at F.2. Adopt them.
- **Silently extending a shared entity.** Raise it — it affects every other consumer.
- **Grooming that skips the unhappy paths in the BRD.** The edge cases were found at M.1
  precisely so they could be designed for here.

## Handoff

Human approves the spec and challenges every "new". Then M.3 `schema-design` and M.4
`design-direction` proceed — they are independent and both feed M.5.
