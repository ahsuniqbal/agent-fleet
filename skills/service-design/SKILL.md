---
name: service-design
description: Produce the global technical architecture for a product — services, boundaries, cross-cutting concerns, data flow, and recorded decisions with rationale. Use at stage F.2, after the module map is approved and before the design system or foundation schema.
---

# Service design

**Stage:** F.2 · **Agent:** system-architect
**Reads:** `docs/00-global/requirements.md`, `docs/00-global/module-map.md`, `CONVENTIONS.md`
**Writes:** `docs/00-global/architecture.md` (template: `templates/00-architecture.md`)

## Scope of this document

Global and cross-cutting only. Per-module technical detail belongs in `groom-module` at M.2.
If you find yourself designing an endpoint here, you have gone too deep.

## Procedure

1. **Restate the constraints** that drive architecture from the requirements: scale, latency,
   offline, compliance, data residency, integration deadlines. Architecture that does not
   trace to a constraint is decoration.
2. **Decide the shape.** Monolith, modular monolith, or services — and say why. For most
   client work a modular monolith is right; justify anything more elaborate against the actual
   constraints, not against imagined future scale.
3. **Define module boundaries in code**: how the module structure from `module-map.md` maps
   onto directories, packages, or deployables.
4. **Nominate cross-cutting concerns** and where each lives:
   authentication, authorization model, error handling, logging, audit trail, notifications,
   file upload and storage, background jobs, caching, feature flags, i18n, rate limiting.
   Each one gets an owner — foundation, a specific module, or a third-party service.
5. **Draw the data flow** for the two or three most important user journeys. Where does data
   enter, what transforms it, where does it rest.
6. **Name the integration points** with external systems: protocol, auth, failure behaviour,
   and who owns the other side.
7. **Record decisions with rationale.** Each: what was chosen, what was rejected, why, and what
   would make you revisit it.
8. **State the non-functional targets** concretely enough to test against.

## Checklist

- [ ] Every architectural choice traces to a stated constraint
- [ ] Module boundaries map onto a concrete code structure
- [ ] Every cross-cutting concern has a named owner
- [ ] Authorization *model* decided here — roles, scopes, or ownership-based
- [ ] Error shape decided here, once, for the whole product
- [ ] Pagination style decided here, once, for the whole product
- [ ] Integration points list failure behaviour, not just the happy path
- [ ] Every decision records what was rejected and why
- [ ] Nothing in this document is module-specific detail

## The two decisions that cost most if deferred

**Error shape** and **pagination style**. Both look like implementation details. Both get
re-invented independently by every module if not fixed here, and both are painful to unify
after four modules have shipped. Decide them now and record them in the inventory's
**Patterns** section so every later module inherits them.

## Failure modes

- **Speculative distribution** — services split for scale the client will never reach. Cost is
  paid immediately, benefit never arrives.
- **Cross-cutting concerns left implicit** — notifications, audit, and file upload are the
  usual casualties. Unassigned, they get built three times.
- **Decisions without rationale** — unrevisable six modules later.
- **Designing endpoints** — that is `api-contract` at M.5, per module.

## Handoff

Human approves. Then `design-system` (F.3) and `foundation-schema` (F.5) proceed as
independent chains.
