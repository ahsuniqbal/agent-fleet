---
description: Run Phase B for one module — BRD, technical grooming, schema, design, frozen contract, parallel build and test design, integration, review, and QA.
argument-hint: [module name or number, or blank for next in queue]
---

Run **Phase B — the module loop** for: $ARGUMENTS

Blank means the next unshipped module in `docs/00-global/module-map.md`'s `order:` list.

## M.0 — mandatory preamble

Read `docs/00-global/inventory.md` **first**. Every agent in this loop reads it before acting.
Then read `CONVENTIONS.md`, `docs/00-global/architecture.md`, `design-system.md`, and
`data-model.md`.

Skipping this is how the same component gets built twice.

## Stages — stop at every gate

| Stage | Agent | Skill | Output |
|---|---|---|---|
| M.1 | `product-owner` | `write-brd` | `docs/modules/NN-<name>/brd.md` |
| 🚦 | — | — | **STOP.** Client approves scope and acceptance criteria. |
| M.2 | `system-architect` | `groom-module` | `spec.md` with a complete reuse plan |
| 🚦 | — | — | **STOP.** User approves. Challenge every `new` verdict. |
| M.3 | `backend-developer` | `schema-design` | `data-model.md` |
| M.4 | `ux-engineer` | `design-direction` | `design-spec.md` + canvas |
| 🚦 | — | — | **STOP.** User and client review the canvas. |
| M.5 | `system-architect` | `api-contract` | `api-contract.md` |
| 🚦 | — | — | **STOP. CONTRACT FROZEN.** This gate is what makes M.6 safe. |
| M.6a ⟂ | `frontend-developer` | `read-design-spec`, `build-component`, `compose-page`, `wire-api-client` | UI against mocks |
| M.6b ⟂ | `backend-developer` | `migrations`, `api-endpoint`, `auth-authz` | migrations, endpoints, authz |
| M.6c ⟂ | `qa-analyst` | `write-test-cases` | `test-cases.md` — FE and API |
| M.7 | `api-integrator` | `swap-mocks`, `e2e-verify` | real wiring, passing e2e |
| M.8 | `code-reviewer` | `drift-check` + `/code-review` | verdicts; `promote-shared` where flagged |
| M.9 ↺ | `qa-tester` ⇄ owners | `execute-tests`, `regression-suite`, `fix-bugs` | `test-report.md`, `bugs.md` — loop below |
| 🚦 | — | — | **STOP.** QA verdict pass. User ships and demos. |

M.3 and M.4 are independent and both feed M.5. Launch M.6a, M.6b, and M.6c concurrently — that
is the only parallelism in this pipeline, and the frozen contract is what makes it safe.

## M.9 — the QA loop

1. **Run 1.** `qa-tester` runs every case and the regression suite, writes run 1 in
   `test-report.md`, and files each defect in `bugs.md` as `open` with an owner.
2. **Pass?** Stop here and go to the gate.
3. **Fix round.** Launch each owner with `fix-bugs` on their own bugs, concurrently —
   `frontend-developer`, `backend-developer`, and `product-owner` for BRD conflicts. Each fix
   ships with a reproducing automated test and a fix note; status becomes `fixed`.
4. **Structural fix?** If any fix note says `structural`, `code-reviewer` runs `drift-check` on
   the fix diff before the retest.
5. **Retest.** `qa-tester` appends the next run — fixed bugs' cases, blocked cases, cases on the
   same screens and endpoints, all P0 cases, the full regression suite — and moves each bug to
   `verified` or `reopened`.
6. **Repeat from 2**, to a maximum of **three runs**. If run 3 still has an open or reopened P0
   or P1, stop and escalate to the user with the open bugs and their reopen history.

The gate opens only on a pass verdict — every P0 and P1 bug verified, or deferred by the user
with a reason recorded in the bug; regression green.

## Rules that hold during this loop

1. **The contract is law after M.5.** A developer blocked by it triggers `amend-contract` — never
   a local workaround, never a translation shim.
2. **The reuse plan is binding.** Building something the plan said to reuse is a conflict to
   raise, not a decision to make.
3. **Tokens only.** No hardcoded design values anywhere.
4. **Every state.** Loading, empty, no-results, error, permission-denied. "It renders" is not
   done.
5. **QA is black box.** `qa-tester` never reads or edits application code. The M.7 e2e suite
   stays in the codebase as a separate, automated net.

## On completion

Run `/close` to write the module summary and update the inventory. Do not start the next module
before that runs — the next module's agents depend on it.
