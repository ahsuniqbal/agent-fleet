---
description: Run Phase B for one module — BRD, technical grooming, schema, design, frozen contract, parallel build, integration, and review.
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
| M.3 | `backend-builder` | `schema-design` | `data-model.md` |
| M.4 | `ux-engineer` | `design-direction` | `design-spec.md` + canvas |
| 🚦 | — | — | **STOP.** User and client review the canvas. |
| M.5 | `system-architect` | `api-contract` | `api-contract.md` |
| 🚦 | — | — | **STOP. CONTRACT FROZEN.** This gate is what makes M.6 safe. |
| M.6a ⟂ | `frontend-builder` | `read-design-spec`, `build-component`, `compose-page`, `wire-api-client` | UI against mocks |
| M.6b ⟂ | `backend-builder` | `migrations`, `api-endpoint`, `auth-authz` | migrations, endpoints, authz |
| M.7 | `integrator` | `swap-mocks`, `e2e-verify` | real wiring, passing e2e |
| M.8 | `reviewer` | `drift-check` + `/code-review` | verdicts; `promote-shared` where flagged |
| 🚦 | — | — | **STOP.** User ships and demos. |

M.3 and M.4 are independent and both feed M.5. Launch M.6a and M.6b concurrently — that is the
only parallelism in this pipeline, and the frozen contract is what makes it safe.

## Rules that hold during this loop

1. **The contract is law after M.5.** A builder blocked by it triggers `amend-contract` — never
   a local workaround, never a translation shim.
2. **The reuse plan is binding.** Building something the plan said to reuse is a conflict to
   raise, not a decision to make.
3. **Tokens only.** No hardcoded design values anywhere.
4. **Every state.** Loading, empty, no-results, error, permission-denied. "It renders" is not
   done.

## On completion

Run `/close` to write the module summary and update the inventory. Do not start the next module
before that runs — the next module's agents depend on it.
