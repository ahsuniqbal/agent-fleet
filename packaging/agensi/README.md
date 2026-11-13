# agent-fleet

A serial, module-by-module software delivery pipeline for AI coding agents. Nine role
definitions, thirty-three skills, and a document spine that carries a client brief from first
call to shipped modules.

Built around one constraint: **modules ship one at a time, in dependency order.** Throughput is
not the goal — consistency is. Module 7 must look like module 1.

## Where to start

| You want to | Use the skill |
|---|---|
| Start a new project from a client brief | `agent-fleet-foundation` |
| Build the next module end to end | `agent-fleet-module` |
| Close a shipped module and update the inventory | `agent-fleet-close` |
| Run one stage on its own | the stage skill, e.g. `write-brd`, `api-contract`, `drift-check` |

The three orchestrator skills walk the stages in order and stop at every human gate.

## What is in this pack

| Path | What it is |
|---|---|
| `skills/` | One folder per skill. Each `SKILL.md` names its stage and its role. |
| `agents/` | Role definitions — product-owner, system-architect, ux-engineer, frontend-developer, backend-developer, api-integrator, code-reviewer, qa-analyst, qa-tester. |
| `templates/` | The document spine. Skills copy from here into your project's `docs/`. |
| `CONVENTIONS.md` | Stack and project conventions. Fill in the `TBD` fields before stage F.6. |

## Roles

Every skill names the role that runs it. Before starting a skill, the agent reads
`agents/<role>.md` and works as that role. If your tool can launch subagents, launch one per
role with that file as its instructions — this keeps each role's context separate and lets
stage M.6 run the frontend, backend, and test-design branches in parallel.

## Source

The same pipeline ships as a Claude Code plugin, with installed subagents and slash commands:
https://github.com/ahsuniqbal/agent-fleet
