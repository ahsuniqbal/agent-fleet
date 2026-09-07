---
name: swap-mocks
description: Reconcile the frontend, the backend, and the frozen contract, then replace mocks with real API calls. Use at stage M.7 when both build branches are complete. Reconciliation comes before wiring — divergences are the real output of this stage.
---

# Swap mocks

**Stage:** M.7 · **Agent:** integrator
**Reads:** `docs/modules/NN/api-contract.md` including its changelog, the frontend client and
mocks, the backend handlers, `CONVENTIONS.md`
**Writes:** real API wiring; divergence findings

## Reconcile before you wire

Do not swap a single mock until you have diffed all three:

1. What the **contract** specifies
2. What the **backend** actually returns
3. What the **frontend** actually expects

The changelog is the first place to look — amendments are where divergence concentrates,
especially if one side resumed work before being notified.

For each divergence, decide and record:

| Finding | Resolution |
|---|---|
| Backend does not match the contract | Backend fixes it |
| Frontend does not match the contract | Frontend fixes it |
| Contract itself is wrong | `system-architect` runs `amend-contract`, then both align |

**Never add a translation shim in the client.** A shim hides the drift, leaves the contract
wrong for whoever reads it next, and guarantees the next module repeats the mistake.

## What to check, field by field

- Field names and casing
- Types — especially numbers arriving as strings, and money encodings
- Nullability — a field the contract says is required arriving as null
- Enum values, exactly
- Date, time, and timezone encoding
- Pagination metadata shape and parameter names
- Error body shape for **every** specified error, not just validation
- Status codes, including the authorization failures
- Empty results — an empty array versus null versus an absent key

## Then wire

1. Replace mocks at the marked swap points. Remove the mock layer from the runtime path but
   keep fixtures for tests.
2. Exercise every state against the real backend: loading, empty, no-results, error,
   permission-denied. Loading states in particular were only ever seen against artificial
   latency.
3. Verify authorization end to end — sign in as each role and confirm the BRD's rules hold in
   the real system.
4. Check performance with realistic data volume, not seed data. List endpoints are where N+1
   surfaces.

## Checklist

- [ ] All three sources diffed before wiring
- [ ] Contract changelog reviewed
- [ ] Every divergence resolved by fixing a side or amending the contract
- [ ] No translation shims added
- [ ] Every swap point replaced
- [ ] Every state exercised against the real backend
- [ ] Every error path produces the designed UI, not a generic failure
- [ ] Authorization verified per role, in the running system
- [ ] Tested with realistic data volume
- [ ] Fixtures retained for tests

## Failure modes

- **Wiring first, reconciling never.** Divergences become mysterious runtime bugs.
- **Shimming.** The tempting shortcut that compounds across modules.
- **Only testing the happy path after swapping.** Error states were built against mocks and are
  often the thing that breaks.
- **Seed-data-only testing.** Real volume exposes different defects.
- **Leaving the mock layer in the runtime path.** It gets used accidentally later.

## Handoff

`e2e-verify` turns the BRD acceptance criteria into passing tests.
