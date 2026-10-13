---
name: write-test-cases
description: Turn one module's BRD, design spec, and frozen API contract into detailed, traceable test cases for both the UI and the API — happy paths, every edge case, validation, and the full permission matrix. Use at stage M.6c, in parallel with the developers, after the contract is frozen. Produces the document qa-tester executes at M.9.
---

# Write test cases

**Stage:** M.6c ⟂ · **Agent:** qa-analyst
**Reads:** `docs/00-global/inventory.md`, `docs/00-global/requirements.md`,
`docs/00-global/test-env.md`, `docs/00-global/regression-suite.md`, `docs/modules/NN/brd.md`,
`docs/modules/NN/design-spec.md`, `docs/modules/NN/api-contract.md`
**Writes:** `docs/modules/NN/test-cases.md` (template: `templates/module-test-cases.md`)

## Why now

The contract froze at M.5, so every input this skill needs exists. Writing in parallel with
M.6a and M.6b means the cases are ready the moment the module reaches QA, and — more
importantly — they are written before anyone has seen the build, so they describe the
requirement rather than the implementation.

## Sources, and what each yields

| Source | Becomes |
|---|---|
| BRD acceptance criteria | at least one case each, FE and/or API |
| BRD validation table | one case per rule per field, at the boundary and just past it |
| BRD edge case table | one case per non-`n/a` row |
| BRD permission matrix | one case per cell — FE (control visible/hidden) **and** API (allowed/refused) |
| Design spec states | loading, empty, no-results, error, permission-denied — each reached and checked |
| Design spec copy | exact on-screen text for labels, errors, empty states |
| Contract endpoints | success shape, every listed error, pagination, auth missing, wrong owner |
| Inventory patterns | assertions that this module follows the established treatment |

## Procedure

1. **Build the traceability matrix first.** List every acceptance criterion, validation rule,
   edge case row, and permission cell with an id. Cases are written to fill it.
2. **Write FE cases** per feature: preconditions, role, numbered steps through the UI, test
   data, and the exact expected outcome on screen.
3. **Write API cases** per endpoint: method, path, role/token, request body, expected status,
   and expected response body or error shape from the contract.
4. **Write the permission cases** from the matrix, both layers.
5. **Write negative and boundary cases**: empty input, max length, max+1, wrong type, duplicate,
   another user's id, expired or missing token, concurrent edit where the BRD specifies it.
6. **Assign priority**:
   - **P0** — a core journey or a security/permission rule; failure blocks release
   - **P1** — a feature does not work as specified; failure blocks release
   - **P2** — a secondary path or an edge case with a workaround
   - **P3** — cosmetic or copy
7. **Mark regression candidates.** Set `Regression: yes` on the P0 cases that prove the module
   still works — usually one per critical journey and one per permission boundary. These are
   what `regression-suite` will carry forward for every later module.
8. **Check the matrix.** Every row has at least one case. Any row you could not cover goes to
   open questions with the reason.

## Case format

```markdown
### TC-03-014 — Viewer cannot delete an invoice (API)

| Type | Priority | Role | Traces to | Regression |
|---|---|---|---|---|
| API | P0 | viewer | BRD perm: delete × viewer; contract `DELETE /invoices/{id}` 403 | yes |

**Preconditions:** invoice `INV-1` exists, owned by `admin@test`
**Steps:**
1. `DELETE /api/invoices/{INV-1.id}` with the viewer token
**Expected:** `403`, body matches the contract error shape with code `FORBIDDEN`; a follow-up
`GET` still returns the invoice
```

Ids are `TC-<module NN>-<sequence>`, never reused, so a report or a bug can cite them forever.

## Rules

1. **Expected results are exact.** "Shows an error" is not a result. The message, the status
   code, the field highlighted.
2. **One behaviour per case.** A case that checks five things fails without saying which.
3. **Steps are executable by someone who has never seen the app.**
4. **Never take expected behaviour from the code.** Only from the BRD, design spec, and contract.
5. **Never invent an expected result** the sources do not give. Raise it.
6. **Test data is named**, using the users from `test-env.md` and fixtures listed in the case.

## Checklist

- [ ] Traceability matrix complete; every acceptance criterion covered
- [ ] Every validation rule covered at the boundary
- [ ] Every non-`n/a` edge case row covered
- [ ] Every permission matrix cell covered at both FE and API
- [ ] Every contract error response covered
- [ ] Loading, empty, no-results, error, and permission-denied states covered
- [ ] Every case has type, priority, role, source, preconditions, steps, exact expected result
- [ ] Regression candidates marked
- [ ] Gaps recorded as open questions, not guessed

## Failure modes

- **Happy path only.** Most defects live in the unhappy paths the BRD spent pages on.
- **UI-only permissions.** A hidden button proves nothing about the endpoint behind it.
- **Vague expected results.** They turn every run into a judgement call.
- **Cases written from the build.** They only confirm what was built, right or wrong.
- **Every case marked regression.** The suite becomes too slow to run on every module.

## Handoff

The cases sit ready while M.6, M.7, and M.8 complete. `qa-tester` executes them at M.9 with
`execute-tests`. If an amendment to the contract lands during M.6, update the affected API
cases before M.9.
