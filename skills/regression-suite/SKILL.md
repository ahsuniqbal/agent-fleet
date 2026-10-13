---
name: regression-suite
description: Run every earlier module's regression cases against the current build to prove the new module broke nothing, then add this module's verified regression cases to the global suite. Use at stage M.9 alongside execute-tests. Keeps a serial pipeline from silently breaking shipped modules.
---

# Regression suite

**Stage:** M.9 · **Agent:** qa-tester
**Reads:** `docs/00-global/regression-suite.md`, `docs/00-global/test-env.md`,
`docs/modules/NN/test-cases.md`
**Writes:** the regression section of `docs/modules/NN/test-report.md`,
`docs/00-global/regression-suite.md` (template: `templates/00-regression-suite.md`)

## Why

Every module touches shared code — promoted components, shared entities, the auth layer. A
module that passes its own cases can still break module 2's checkout. In a serial pipeline
nobody looks at module 2 again unless something makes them.

## The suite is an index

`regression-suite.md` holds one line per case: id, module, type, title, and the path to the
module's `test-cases.md` where the full steps live. Steps are never copied into the suite — a
copy drifts from its source.

## Procedure

1. **Run the suite before adding to it.** Execute every listed case from earlier modules, FE
   and API, exactly as `execute-tests` does. Record results in this module's report under
   **Regression**.
2. **A regression fail is a bug in this module**, filed in this module's `bugs.md`, not in the
   old one — the old module passed when it shipped. Owner is whoever changed the shared thing;
   cite the case's original module.
3. **After this module's verdict is pass**, append the cases its `test-cases.md` marks
   `Regression: yes`. Only verified cases enter the suite.
4. **Retire with a reason.** When a later module deliberately changes old behaviour, the case is
   updated or retired in the suite with the module and reason that changed it — never silently
   deleted.

## Keep it runnable

The suite is run on every module, so it must stay small enough to run on every module. Target
roughly **10 cases per module**, all P0. When a module wants more, pick the ones that guard a
journey or a permission boundary. A suite too slow to run gets skipped, and a skipped suite
protects nothing.

## Checklist

- [ ] Every existing suite case executed and recorded in this module's report
- [ ] Every regression fail filed in this module's `bugs.md`
- [ ] This module's cases added only after its verdict is pass
- [ ] Entries are one line each, pointing at the source `test-cases.md`
- [ ] Retired or changed cases record the module and reason
- [ ] Suite size still reasonable to run every module

## Failure modes

- **Skipping the suite because "nothing shared changed".** That is exactly what it checks.
- **Adding unverified cases.** The suite then fails on day one and gets ignored.
- **Copying steps into the suite.** The copy drifts; the source is updated and the suite is not.
- **Deleting a failing case.** That is hiding a regression.

## Handoff

`close-module` at M.10 records the QA outcome and regression additions in the module summary.
