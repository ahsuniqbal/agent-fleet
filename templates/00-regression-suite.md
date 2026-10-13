# Regression suite — <product name>

**Run in full by `qa-tester` at M.9 of every module, before that module's cases are added.**

An index, not a copy. One line per case; the steps live in the source module's
`test-cases.md`. Only cases that passed when their module shipped are listed.

Maintained by `regression-suite` at M.9. Target roughly 10 P0 cases per module — a suite too
slow to run every module gets skipped.

Format: `TC-id` — module — FE/API — title — `docs/modules/NN-<name>/test-cases.md`

---

## 01 — <module name>

- `TC-01-003` — 01 — FE — Admin creates an invoice end to end — `docs/modules/01-invoices/test-cases.md`

## Retired / changed

Never silently deleted.

| Case | Changed by module | Change | Reason |
|---|---|---|---|
