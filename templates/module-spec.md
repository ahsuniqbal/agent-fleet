# Technical spec — <NN> <module name>

**Reads:** `brd.md`, `00-global/inventory.md`, `00-global/architecture.md`,
`00-global/data-model.md`

## Reuse plan

**Mandatory. Covers every capability the BRD requires, not just the interesting ones.**
Every `new` verdict carries a justification naming what you checked and why it does not fit.
A `new` row without justification is rejected at the human gate.

| Need | Verdict | Source | Justification if new |
|---|---|---|---|
| | reuse / extend / new | | |

## Entities

**Owned by this module**

| Entity | Purpose |
|---|---|

**Referenced** — reference, never duplicate

| Entity | Owner | Why needed |
|---|---|---|

Extending a shared entity is an architecture change. Raise it rather than deciding here.

## API surface

Resource level only. Full schemas come at M.5 once the data model and design spec exist.

| Resource | Operations | Notes |
|---|---|---|

## State ownership

| State | Lives in | Reason |
|---|---|---|
| Server data | | |
| Filters / sort / pagination | URL | shareable, survives reload |
| Ephemeral UI | local | |

## Background jobs

| Job | Trigger | Retry | On permanent failure |
|---|---|---|---|

## Events

| Event | Emitted / consumed | Payload |
|---|---|---|

## Module dependencies

**Upstream** — what this needs:
**Downstream** — what will need this (tells you what to keep stable):

## Permissions

BRD roles mapped onto the global authorization model. Any gap is a raised question, not a local
invention.

| Action | Rule | Role / ownership / state |
|---|---|---|

## Non-functionals

| Aspect | Target | Source |
|---|---|---|

## Test plan

| Layer | What | Fixtures needed |
|---|---|---|

## Rollout

Feature flag: · Migration ordering: · Backfill: · Sequencing constraints:

## Open technical questions

| Question | Options | Implication |
|---|---|---|
