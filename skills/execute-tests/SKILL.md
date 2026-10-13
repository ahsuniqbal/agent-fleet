---
name: execute-tests
description: Execute one module's test cases as black-box QA against the running application — FE cases in a real browser, API cases as raw HTTP requests — write the module's test report, and file and verify bugs in the module's bug log — retesting until pass or the three-run limit. Use at stage M.9, after review and before close. Never reads or edits application code.
---

# Execute tests

**Stage:** M.9 · **Agent:** qa-tester
**Reads:** `docs/00-global/test-env.md`, `docs/modules/NN/test-cases.md`,
`docs/modules/NN/api-contract.md`, `docs/modules/NN/bugs.md` on a retest
**Writes:** `docs/modules/NN/test-report.md` (template: `templates/module-test-report.md`),
`docs/modules/NN/bugs.md` (template: `templates/module-bugs.md`),
`docs/modules/NN/qa-evidence/`

## Two files, two jobs

| File | Job | Who writes |
|---|---|---|
| `test-report.md` | **log** — what each run executed and observed. Append-only. | `qa-tester` only |
| `bugs.md` | **state** — each defect and where it is in its lifecycle | `qa-tester` opens, verifies, reopens; the owner marks fixed |

The report cites bug ids; the bug cites cases and evidence. Neither copies the other.

## Black box

This stage verifies the module the way the client will meet it. The source is not opened, the
database is not consulted, and the code is not changed. The M.7 e2e suite already lives in the
codebase; this is an independent check by someone who did not build the thing.

## Setup

1. Start and seed the application exactly as `test-env.md` describes. If that fails, stop — an
   environment that cannot be reproduced from the document is itself a finding.
2. Confirm every role in `test-env.md` can sign in, and capture an API token per role.
3. Confirm the browser tools respond. If they do not, stop and report it; do not fall back to
   marking FE cases from API results.

## Evidence layout

Evidence lives inside the module folder, next to the report that cites it:

```
docs/modules/NN-<name>/
  test-cases.md
  test-report.md
  bugs.md
  qa-evidence/
    run-1/
      TC-03-004.png          FE — screenshot
      TC-03-014.txt          API — full request and response
    run-2/
```

One folder per run, one file per case named by its id. Paths in the report and in `bugs.md` are
relative to the module folder, so `qa-evidence/run-1/TC-03-014.txt`. Earlier runs' folders are never touched.

## Executing FE cases

- Drive the browser through the steps exactly as written, as the role the case names.
- Read what is on screen and compare with the expected result word for word where copy is
  specified.
- Reach the non-default states the case asks for — empty, error, slow — through the means the
  case gives, not by editing code.
- Screenshot every fail, and the final state of every P0 pass.

## Executing API cases

- Send the request with `curl`, with the named role's token, or none when the case says so.
- Compare status, body shape, and error code with the expected result.
- Record the full request and response for every fail.
- Where the case says to, follow up with a read to prove a refused write left no change.

## Results

Each case gets exactly one result:

- **pass** — observed matches expected
- **fail** — it does not; becomes a bug
- **blocked** — could not be executed (environment, missing data, a preceding fail); says why
- **skipped** — not run; says why, and a skipped P0 or P1 means the verdict cannot be pass

## Bugs

Every failure is filed in `bugs.md`. One bug per distinct defect, not per failed case — five
cases failing on the same missing validation are one bug citing five cases.

```markdown
### BUG-03-002 — Viewer can delete invoices through the API · P0

**Status:** open · **Owner:** backend-developer · **Cases:** TC-03-014, TC-03-015
**Found in:** run 1
**Repro:**
1. Sign in as `viewer@test`
2. `DELETE /api/invoices/{id}` for an invoice owned by `admin@test`
**Expected:** `403 FORBIDDEN`, invoice unchanged
**Actual:** `204`, invoice gone
**Evidence:** `qa-evidence/run-1/TC-03-014.txt`

**History**
- run 1 — opened by qa-tester
```

- **Owner** is `frontend-developer`, `backend-developer`, or `product-owner` when the test case
  and the BRD turn out to disagree. If you cannot tell FE from BE from the outside — the UI
  shows a wrong value and the API response is right, it is FE; the API response is wrong, it is
  BE — say what you observed and pick by that rule.
- **Severity** follows the case's priority unless the failure is worse than the case
  anticipated.
- A regression failure is filed here too, against this module, citing the original module's
  case.

## Bug lifecycle

```
open ──(owner fixes)──► fixed ──(qa-tester retest)──► verified
                                     └──────────────► reopened ──(owner fixes)──► fixed …
```

| Transition | Who | Requires |
|---|---|---|
| → **open** | qa-tester | repro, expected, actual, evidence |
| open / reopened → **fixed** | owner (`fix-bugs`) | fix note, commit, and the automated test that reproduces the bug |
| fixed → **verified** | qa-tester | every cited case passes in the retest run |
| fixed → **reopened** | qa-tester | new evidence from the retest run |
| any → **deferred** | human only, at the gate | the reason, recorded in the bug |
| open → **invalid** | product-owner | test case was wrong; `qa-analyst` corrects it |

Only `qa-tester` moves a bug to verified or reopened. An owner never closes their own bug.
Every transition adds a line to the bug's **History**.

## Retest

After the owners' `fix-bugs` round, run again as **Run N+1**, appended to the report with its
own evidence folder. The retest scope is:

1. every case cited by a bug now in **fixed**
2. every case that was **blocked** last run
3. cases exercising the same screen or endpoint as each fix
4. all of this module's **P0** cases
5. the full regression suite (`regression-suite`)

Then move each fixed bug to verified or reopened. Any new failure is a new bug.

If a fix note says the change was structural rather than local, flag it in the run so
`code-reviewer` runs `drift-check` on the fix diff before the gate.

## Three-run limit

Run 1 plus at most two retests. If after **run 3** any P0 or P1 bug is still open or reopened,
stop the loop and escalate to the human with: the open bugs, how many times each was reopened,
and what the fix notes claimed. Repeated reopening is a signal the problem is in the BRD, the
contract, or the design — not something another run will fix.

## Verdict

- **Pass** — every P0 and P1 case passed, every P0 and P1 bug verified (or deferred by the
  human), regression green
- **Fail** — anything else

The verdict is not a negotiation. Deferring a P1 is a human decision recorded at the gate, not
a downgrade made here.

## Checklist

- [ ] Environment started from `test-env.md` alone
- [ ] Every case has exactly one result
- [ ] Every fail has evidence and a bug in `bugs.md`
- [ ] Every blocked and skipped case says why
- [ ] Bugs deduplicated, each with status, owner, severity, repro, expected, actual, history
- [ ] Every fixed bug moved to verified or reopened in the retest
- [ ] Escalated to the human if run 3 still has open P0 or P1
- [ ] Retests appended as new runs, earlier runs untouched
- [ ] Regression suite run (`regression-suite`)
- [ ] Verdict stated, consistent with the counts

## Failure modes

- **Reading the code to explain a failure.** That is the developer's job; report what you saw.
- **Fixing it yourself.** The fix bypasses review and the bug never reaches the ledger.
- **Passing on a near-match.** Wrong copy, wrong status code, wrong shape is a fail.
- **Overwriting the first run.** The history of what broke is how the next module learns.
- **Green over skipped.** Never.
- **Verifying on the owner's word.** A bug is verified by a passing case, not a fix note.
- **A fourth run.** Past three, the loop is hiding a problem upstream; escalate.

## Handoff

On **fail**, owners run `fix-bugs` against `bugs.md`, then this skill runs again — up to run 3.
On **pass**, `regression-suite` adds this module's regression cases, the human ships and demos,
and `close-module` records the QA outcome at M.10.
