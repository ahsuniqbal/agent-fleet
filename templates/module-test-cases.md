# Test cases — <NN> <module name>

Written by `write-test-cases` at M.6c, from the BRD, design spec, and frozen contract — never
from the build. Executed by `execute-tests` at M.9. Results go in `test-report.md`, not here.

**Sources:** `brd.md` · `design-spec.md` · `api-contract.md` (as of changelog entry: )

## Traceability matrix

Every source row has at least one case. A row with none is listed under open questions.

| Source id | Source | Requirement | Cases |
|---|---|---|---|
| AC-1 | BRD acceptance criteria | | |
| VAL-<field>-<rule> | BRD validation | | |
| EDGE-<feature>-<dimension> | BRD edge cases | | |
| PERM-<action>-<role> | BRD permission matrix | | |
| ERR-<endpoint>-<status> | Contract errors | | |
| STATE-<screen>-<state> | Design spec states | | |

## Summary

| Type | P0 | P1 | P2 | P3 | Total | Regression |
|---|---|---|---|---|---|---|
| FE | | | | | | |
| API | | | | | | |

## Test data

Users come from `00-global/test-env.md`. Fixtures this module's cases need:

| Fixture | Owner / role | State | Used by |
|---|---|---|---|

---

## FE cases

### TC-<NN>-001 — <one behaviour, stated as the outcome>

| Type | Priority | Role | Traces to | Regression |
|---|---|---|---|---|
| FE | P0 | | | yes / no |

**Preconditions:**
**Steps:**
1.

**Expected:** exact on-screen outcome — copy, state, what is enabled or hidden

---

## API cases

### TC-<NN>-0xx — <one behaviour>

| Type | Priority | Role | Traces to | Regression |
|---|---|---|---|---|
| API | P0 | | | yes / no |

**Preconditions:**
**Request:** `METHOD /path` · token: <role | none> · body:

```json
{}
```

**Expected:** status `` · body / error code · follow-up check if a write was refused

---

## Open questions

Sources that are silent or ambiguous. Not guessed — raised with `product-owner`.

| Source id | Question | Blocks cases |
|---|---|---|
