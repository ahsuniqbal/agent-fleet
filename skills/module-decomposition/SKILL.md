---
name: module-decomposition
description: Break a product's requirements into modules, build the entity-dependency graph between them, and emit an ordered build queue with a reason for each position. Use at stage F.1, after requirements intake and before any architecture work.
---

# Module decomposition

**Stage:** F.1 · **Agent:** product-owner
**Reads:** `docs/00-global/requirements.md`
**Writes:** `docs/00-global/module-map.md` (template: `templates/00-module-map.md`)

This document is the spine of the whole project. Modules ship one at a time in the order this
file specifies, so a bad ordering costs rework on every module after it.

## What a module is

**A module is something you could demo to the client on its own.**

Too small and orchestration overhead exceeds the work. Too big and there is no incremental
ship, no early feedback, and no useful reuse ledger. A module is a vertical slice — UI, API,
and data together — not a horizontal layer.

## Procedure

1. **List candidate modules** from the requirements. Group by user-facing capability, not by
   technical layer. "Invoicing" is a module. "The database" is not.
2. **Name the entities** each module owns and each module references. Ownership means: this
   module creates the table and defines its shape.
3. **Build the dependency graph.** Module A depends on module B when A references an entity B
   owns, calls an endpoint B provides, or consumes an event B emits.
4. **Topologically sort.** A module that owns an entity ships before any module referencing it.
5. **Break tie positions** in this order:
   1. fewest dependencies
   2. largest shared surface area — modules that many others depend on go earlier
   3. highest client-demo value — early demos protect the relationship
6. **Break cycles** by extracting the shared entity up to `00-global/data-model.md` and
   removing the edge. Record that you did this and why.
7. **Write one line of reasoning per queue position.** The human will disagree with some of
   them and needs to see the logic to override it.
8. **Emit an explicit `order:` list** the human can edit directly.

## Do not hardcode any module into first position

Auth frequently lands first because most entities reference a user — but that is a *derived*
result, not an assumption. Some products have no auth module at all: internal tools behind a
VPN, public sites, embedded widgets. Let the graph decide.

## Checklist

- [ ] Every requirement maps to exactly one module, or is explicitly out of scope
- [ ] Every module could be demoed alone
- [ ] Each module lists entities owned and entities referenced
- [ ] Dependency graph is acyclic, or cycles are broken with recorded justification
- [ ] Queue is topologically valid
- [ ] Every position has a one-line reason
- [ ] `order:` list is present and editable
- [ ] Cross-cutting concerns (auth, notifications, audit, file upload) are identified as
      either their own module or a foundation concern — never left implicit inside one module

## Failure modes

- **Horizontal modules** — "backend", "frontend", "admin panel". These cannot be demoed as a
  slice and destroy the whole model.
- **A module that depends on everything** — usually a dashboard or reporting module. It belongs
  at the end of the queue, not the start, however visible it is.
- **Hidden cross-cutting concerns** — notifications built inside module 3 and then needed by
  modules 5, 6, and 7. Catch these now and either promote them to foundation or give them an
  early queue position.
- **A module with no owned entities** — it is probably a feature of another module, not a
  module.

## Handoff

The human reviews and edits `order:`. Once approved, `system-architect` runs `service-design`.
