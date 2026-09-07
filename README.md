# agent-fleet

A delivery pipeline as a Claude Code plugin. Seven role agents, twenty-six skills, and a
document spine that carries a client brief from first call to shipped modules.

Built around one constraint: **modules ship one at a time, in dependency order.** Throughput
is not the goal — consistency is. Module 7 must look like module 1.

## Pipeline reference

[pipeline.html](pipeline.html) is the whole pipeline on one page — flow diagram, all sixteen
stages, the eight human gates, the agent roster, and the skill index. Open it locally, or read
the published copy:

<https://claude.ai/code/artifact/0e8c2e69-1f67-41a9-ad11-c3d8046f0f47>

To update the published page after editing `pipeline.html`, republish it to that same URL rather
than as a new artifact — publishing without the URL creates a separate page and the link above
goes stale.

## Install

```bash
claude
/plugin marketplace add ~/Documents/Projects/agent-fleet
/plugin install agent-fleet@agent-fleet
```

Iterate in place — edits to this repo are picked up without reinstalling.

## The document spine

Agents have no memory between runs. Everything a human colleague would carry in their head
lives in files. Every stage reads the previous document and writes the next.

```
docs/
  00-global/
    requirements.md     whole product, one truth
    module-map.md       modules, dependency graph, ordered build queue
    architecture.md     services, boundaries, cross-cutting concerns
    design-system.md    tokens
    data-model.md       shared entities only
    inventory.md        THE REUSE LEDGER — read at the start of every module
    CHANGELOG.md        what got promoted to shared, and when
  modules/
    01-<name>/
      brd.md            business requirements, edge cases, acceptance criteria
      spec.md           technical grooming + mandatory reuse plan
      design-spec.md    tokens, component inventory, states, breakpoints
      data-model.md     module-owned tables only
      api-contract.md   frozen before build starts
      summary.md        written at close, feeds the inventory
```

Templates for all of these are in [templates/](templates/).

## Phase A — Foundation, once per project

| Stage | Agent | Skill | Output |
|---|---|---|---|
| F.0 | product-owner | `requirements-intake` | `00-global/requirements.md` |
| F.1 | product-owner | `module-decomposition` | `00-global/module-map.md` |
| F.2 | system-architect | `service-design` | `00-global/architecture.md` |
| F.3 | ux-engineer | `design-system` | `00-global/design-system.md` |
| F.4 | ux-engineer + frontend-builder | `component-library` | primitives only |
| F.5 | backend-builder | `foundation-schema` | `00-global/data-model.md` |
| F.6 | backend-builder | `project-skeleton` | repo, routing, CI, migration runner |

Human gates: client agrees scope after F.0; you approve build order after F.1; you freeze the
foundation after F.4/F.6.

## Phase B — Module loop, repeated in queue order

| Stage | Agent | Skill |
|---|---|---|
| M.0 | *all* | read `00-global/inventory.md` |
| M.1 | product-owner | `write-brd` |
| M.2 | system-architect | `groom-module` |
| M.3 | backend-builder | `schema-design` |
| M.4 | ux-engineer | `design-direction` |
| M.5 | system-architect | `api-contract` → **freeze** |
| M.6a | frontend-builder | `read-design-spec`, `build-component`, `compose-page`, `wire-api-client` |
| M.6b | backend-builder | `migrations`, `api-endpoint`, `auth-authz` |
| M.7 | integrator | `swap-mocks`, `e2e-verify` |
| M.8 | reviewer | `drift-check` + `/code-review` |
| M.9 | reviewer | `close-module` |

M.6a and M.6b run in parallel. That is the only parallelism in the pipeline, and the frozen
contract at M.5 is what makes it safe.

## The three rules

1. **M.0 preamble.** Every agent reads `inventory.md` before doing anything. No exceptions.
2. **Reuse plan is mandatory** in `spec.md`. Anything marked *new* carries a justification.
   This is where reuse is enforced, not suggested.
3. **Rule of two.** Nothing becomes shared on first use. Second consumer triggers
   `promote-shared`. The exception is entities — those go global the moment `groom-module`
   sees a queued module that will reference them, because refactoring a table across shipped
   modules is expensive and refactoring a component is not.

## Agents

| Agent | Model | Owns |
|---|---|---|
| `product-owner` | opus | Business truth: requirements → modules → BRDs |
| `system-architect` | opus | Technical boundaries and contracts |
| `ux-engineer` | opus | Design system and per-module design intent |
| `frontend-builder` | sonnet | UI implementation against mocks |
| `backend-builder` | sonnet | Data and API implementation |
| `integrator` | sonnet | Mocks → real, end-to-end verification |
| `reviewer` | opus | Cross-module consistency and the reuse ledger |

## Commands

- `/foundation` — run Phase A
- `/module <name>` — run Phase B for the next module in the queue
- `/close` — close the current module and update the ledger

## Before first use

Fill in [CONVENTIONS.md](CONVENTIONS.md). Agents read it before writing code, and any field
left as `TBD` becomes a question they must ask instead of a guess they will get wrong.
