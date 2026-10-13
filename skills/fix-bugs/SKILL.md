---
name: fix-bugs
description: Fix the QA bugs assigned to you in a module's bug log — reproduce, fix at the root, add an automated test that reproduces the bug, and mark it fixed for qa-tester to verify. Use at stage M.9 between QA runs, by frontend-developer or backend-developer, and by product-owner for bugs that are really BRD conflicts. Never verifies or closes a bug.
---

# Fix bugs

**Stage:** M.9 ↺ · **Agents:** frontend-developer, backend-developer, product-owner
**Reads:** `docs/modules/NN/bugs.md`, the cited cases in `test-cases.md`, the cited evidence in
`qa-evidence/`, `api-contract.md`, `CONVENTIONS.md`
**Writes:** the fix, an automated test, and the bug's status and history in `bugs.md`

## Scope

Take only the bugs where **Owner** is you and **Status** is `open` or `reopened`. Work them in
severity order, P0 first. A bug that turns out to belong to the other side is reassigned with a
reason in its history — not fixed across the boundary.

## Procedure — developers

1. **Reproduce first**, from the bug's repro steps and evidence. If you cannot reproduce it, do
   not mark it fixed — add what you tried to the history and leave it for the next run.
2. **Find the root cause.** The failing case is a symptom. Fix where the defect is, not where it
   showed — a missing authorization check is fixed in the authorization layer, not by hiding a
   button.
3. **Stay inside the contract.** If the fix needs the contract to change, it is an
   `amend-contract`, not a bug fix.
4. **Write the automated test first** that reproduces the bug — unit, integration, or e2e,
   whichever is closest to the defect — watch it fail, then fix until it passes. This is what
   stops the same bug returning after QA has moved on.
5. **Check the neighbours.** Same screen, same endpoint, same validation on other fields. One
   missing check is often several.
6. **Mark it fixed** in `bugs.md`:

   ```markdown
   **Status:** fixed

   **Fix**
   - Cause: authorization check missing on DELETE; only the UI hid the button
   - Change: added ownership check in the invoice policy; local change
   - Commit: a1b2c3d
   - Test: `invoices.policy.test.ts › viewer cannot delete`

   **History**
   - run 1 — opened by qa-tester
   - after run 1 — fixed by backend-developer
   ```

   **Change** says `local` or `structural`. Structural means the fix moved or reshaped something
   shared — `qa-tester` flags it so `code-reviewer` runs `drift-check` on the diff.

## Procedure — product-owner

A bug owned by `product-owner` means the test case and the BRD disagree, or the BRD is silent.

- **The build is right and the test case is wrong** → status `invalid`, with the reason;
  `qa-analyst` corrects the case.
- **The test case is right** → the BRD is clarified, and the bug is reassigned to the developer
  who must change the build.
- **The scope itself is in question** → stop and raise it with the human; that is a client
  decision.

## Rules

1. **Never move a bug to verified.** Only `qa-tester` does that, from a passing run.
2. **Never edit `test-report.md` or the evidence.** They are the record of what QA observed.
3. **Never weaken a test case to make it pass.** Disagreement goes through `product-owner`.
4. **One commit per bug** where practical, cited in the bug, so a reopen can be traced.

## Checklist

- [ ] Only my `open` and `reopened` bugs taken, P0 first
- [ ] Each reproduced before fixing
- [ ] Root cause fixed, not the symptom
- [ ] Automated test added that failed before the fix and passes after
- [ ] Neighbouring cases checked
- [ ] Contract untouched, or `amend-contract` raised
- [ ] Fix note with cause, change (local / structural), commit, and test
- [ ] Status set to `fixed` and a history line added

## Failure modes

- **Fixing the symptom.** Hiding the button leaves the endpoint open, and the API case reopens it.
- **No reproducing test.** The bug comes back two modules later and nobody notices until QA.
- **Marking fixed without reproducing.** The next run reopens it and a run is wasted.
- **Closing your own bug.** The lifecycle exists so the person who found it confirms it.

## Handoff

When every assigned bug is `fixed`, `invalid`, or reassigned, `qa-tester` runs `execute-tests`
again as the next run.
