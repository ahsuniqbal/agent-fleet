# Bugs — <NN> <module name>

The module's bug log. `qa-tester` opens, verifies, and reopens bugs at M.9; owners mark them
fixed with `fix-bugs`. `test-report.md` is the run log and cites these ids — the detail lives
here.

```
open ──(owner fixes)──► fixed ──(qa-tester retest)──► verified
                                     └──────────────► reopened ──► fixed …
```

Also: `invalid` (product-owner — the test case was wrong) and `deferred` (human only, at the
gate). An owner never moves their own bug to verified.

## Summary

| Bug | Title | Severity | Owner | Status | Found in run | Closed in run |
|---|---|---|---|---|---|---|
| BUG-<NN>-001 | | P0 | backend-developer | open | 1 | |

Gate: no P0 or P1 in `open`, `fixed`, or `reopened`. Three-run limit — past run 3, escalate.

---

### BUG-<NN>-001 — <what is wrong, stated as the observed behaviour> · P0

**Status:** open · **Owner:** frontend-developer / backend-developer / product-owner
**Cases:** TC-<NN>-0xx · **Found in:** run 1
**Repro:**
1.

**Expected:**
**Actual:**
**Evidence:** `qa-evidence/run-1/<TC-id>.png | .txt`

**Fix** — filled by the owner

- Cause:
- Change: local / structural —
- Commit:
- Test:

**History**
- run 1 — opened by qa-tester
