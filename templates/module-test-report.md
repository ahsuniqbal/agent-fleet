# Test report — <NN> <module name>

Written by `execute-tests` and `regression-suite` at M.9. Black-box only: browser for FE, HTTP
for API. Each retest is appended as a new run — earlier runs are never edited. This is the run
log; bug detail and status live in `bugs.md`, cited here by id.

**Verdict:** pass / fail · **Final run:** <N> · **Date:**

## Verdict summary

| Run | Date | Pass | Fail | Blocked | Skipped | Bugs opened | Verified | Reopened | Regression |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | — | — | green / red |

Pass requires: every P0 and P1 case passed, every P0 and P1 bug verified or deferred by the
human, regression green. Limit: three runs — past run 3, escalate.

## Environment

| Item | Value |
|---|---|
| Frontend URL | |
| API base URL | |
| Build / commit | |
| Seed | |
| Browser | |

---

## Run 1 — <date>

**Scope:** full — every case + regression suite
(Retest runs: fixed bugs' cases, last run's blocked cases, cases on the same screens / endpoints,
all P0 cases, full regression suite.)

### Results

| Case | Type | Priority | Result | Evidence / note |
|---|---|---|---|---|
| TC-<NN>-001 | FE | P0 | pass / fail / blocked / skipped | evidence path, or BUG id on fail |

### Regression

Earlier modules' cases from `00-global/regression-suite.md`.

| Case | Module | Type | Result | Evidence / note |
|---|---|---|---|---|

### Bug changes this run

| Bug | Change | Cases |
|---|---|---|
| BUG-<NN>-001 | opened / verified / reopened | |

### Flags

Structural fixes that need `drift-check` on the diff, environment problems, anything the human
should see before the next run.

---

## Not verified

Blocked and skipped cases with the reason, so nobody reads the verdict as wider than it is.

| Case | Result | Why |
|---|---|---|

## Added to regression suite

| Case | Title |
|---|---|
