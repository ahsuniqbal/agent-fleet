---
name: amend-contract
description: Change a frozen API contract safely when a builder hits a genuine blocker — assess impact, log the amendment, and notify both sides. Use during stage M.6 whenever the frontend or backend cannot proceed within the contract as written. The only sanctioned way to change a frozen contract.
---

# Amend contract

**Stage:** M.6, on demand · **Agent:** system-architect
**Reads:** the blocker, `docs/modules/NN/api-contract.md`, `docs/modules/NN/data-model.md`,
`docs/modules/NN/design-spec.md`
**Writes:** the amendment plus a changelog entry in `api-contract.md`

## Why this exists

A frozen contract lets two builders work in parallel. The freeze is only credible if there is a
sanctioned way to change it. Without one, builders work around the contract locally, both sides
drift, and integration becomes archaeology.

**Any contract change goes through here. There are no small exceptions.**

## Procedure

1. **State the blocker precisely.** What was attempted, what the contract says, why it cannot be
   satisfied. "It would be easier this way" is not a blocker — it is a preference, and the answer
   is no. Real blockers: the data model cannot produce the field; the design needs data no
   endpoint exposes; the specified status code is wrong for the semantics; a field's type cannot
   represent real values.
2. **Consider the alternatives before amending.** Can the existing contract satisfy the need with
   a different call pattern? Is the *design* wrong rather than the contract? Is the *data model*
   the thing that should change? Amending is the last option, not the first.
3. **Assess blast radius.** Which endpoints, which screens, which mocks, which already-written
   code on both sides. Does anything already merged depend on the current shape? Does another
   module consume this endpoint?
4. **Classify the change:**
   - **Additive** — new optional field, new endpoint. Low risk. The frontend can ignore it.
   - **Modifying** — changed type, renamed field, changed status code. Both sides must change
     together.
   - **Removing** — dropped field or endpoint. Highest risk; confirm nothing depends on it.
5. **Write the changelog entry** in `api-contract.md`:

   ```markdown
   ## Changelog

   ### 2026-09-07 — added `invoice.taxBreakdown`
   **Requested by:** frontend-builder
   **Reason:** design spec binds per-line tax; the contract only exposed a total
   **Type:** additive
   **Affects:** GET /invoices/{id}, GET /invoices — mocks and the invoice detail screen
   **Both sides notified:** yes
   ```

6. **Update the contract body** and its examples. Stale examples produce stale mocks.
7. **Notify both builders explicitly**, naming what changed and what each must do.
8. **Re-freeze** with a new date.

## Checklist

- [ ] Blocker is a real impossibility, not a preference
- [ ] Alternatives considered and recorded
- [ ] Blast radius assessed on both sides, and across modules
- [ ] Change classified additive / modifying / removing
- [ ] Contract body updated
- [ ] **Examples updated** — mocks are generated from them
- [ ] Changelog entry complete
- [ ] Both builders notified, with their specific action
- [ ] Re-frozen with a new date

## Failure modes

- **Amending for convenience.** The freeze stops meaning anything.
- **Updating the body but not the examples.** Mocks stay wrong and the bug surfaces at M.7.
- **Notifying one side.** Guarantees the mismatch you were trying to prevent.
- **No changelog entry.** Nobody can reconstruct why the contract looks like this six months on.
- **Amending when the design or data model is the real problem.** Fix the actual cause.

## Handoff

Both builders resume against the amended contract. `integrator` reads the changelog at M.7 —
amendments are the first place to look for divergence.
