---
name: e2e-verify
description: Turn a module's BRD acceptance criteria into passing end-to-end tests, covering unhappy paths and permissions, and report results honestly. Use at stage M.7 after mocks are swapped for real calls. A module is done when every criterion passes, not when the screens render.
---

# E2E verify

**Stage:** M.7 · **Agent:** integrator
**Reads:** `docs/modules/NN/brd.md` acceptance criteria, `docs/modules/NN/api-contract.md`,
`CONVENTIONS.md`
**Writes:** end-to-end tests and a verification report

## The BRD is the test plan

Acceptance criteria were written in Given/When/Then at M.1 precisely so they could become tests
here. They are executable specification. Every criterion becomes at least one test.

If a criterion turns out to be untestable as written, that is a finding to report — not a
criterion to quietly skip.

## Coverage, in priority order

1. **Every acceptance criterion**, including the ones describing failures
2. **Permission matrix** — each role against each protected action, expecting both the allowed
   and denied outcomes
3. **Validation** — each field's rules from the BRD, rejected at the boundary
4. **Empty and first-run states** — before any data exists
5. **Error paths** — server error, network failure, timeout, conflict
6. **Edge cases from the BRD** — concurrency, limits, bulk partial failure, lifecycle
   transitions
7. **Critical journeys end to end** — the flows the client will demo

## Rules

1. **Test through the interface a user uses.** Reaching into internals proves less than it looks.
2. **Assert on user-visible outcomes**, not implementation detail. Tests coupled to markup
   structure break on every design tweak and teach the team to distrust the suite.
3. **Independent tests.** Each sets up its own state and cleans up. Order-dependent suites fail
   mysteriously in CI.
4. **No arbitrary waits.** Wait on conditions. Timing-based waits are the primary source of
   flakiness, and a flaky suite gets ignored, which is worse than having no suite.
5. **Use realistic fixtures** — the awkward data from `wire-api-client`, not tidy seed rows.
6. **Deterministic time.** Freeze or inject the clock for anything date-dependent.

## Reporting

Report honestly. State:

- which criteria pass
- which fail, with the actual output
- which could not be verified, and why

A green report covering a skipped check is worse than a red one, because it removes the chance
to fix the problem before the client finds it.

## Checklist

- [ ] Every acceptance criterion has at least one test
- [ ] Unhappy paths covered, not just happy paths
- [ ] Permission matrix tested per role, both allow and deny
- [ ] Validation rules tested at the boundary
- [ ] Empty and first-run states tested
- [ ] Error paths tested including network failure
- [ ] Tests are independent and self-cleaning
- [ ] No arbitrary waits
- [ ] Realistic fixtures used
- [ ] Time-dependent behaviour uses a controlled clock
- [ ] Suite passes repeatedly, not once
- [ ] Report states passes, failures with output, and anything unverified

## Failure modes

- **Happy path only.** Then the module ships with broken error handling.
- **Flaky tests.** They train everyone to ignore red, which defeats the whole exercise.
- **Testing implementation detail.** Breaks constantly, proves little.
- **Skipping permission tests.** The highest-risk area in most client work.
- **Reporting green over skipped checks.** Never do this.

## Handoff

`drift-check` and `/code-review` at M.8, then the human ships and demos.
