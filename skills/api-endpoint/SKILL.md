---
name: api-endpoint
description: Implement a module's HTTP handlers exactly as the frozen API contract specifies — paths, schemas, status codes, error shapes, pagination, and idempotency. Use during stage M.6b after migrations. Never deviate from the contract silently.
---

# API endpoint

**Stage:** M.6b · **Agent:** backend-builder
**Reads:** `docs/modules/NN/api-contract.md`, `docs/modules/NN/data-model.md`,
`docs/00-global/inventory.md`, `CONVENTIONS.md`
**Writes:** route handlers, request validation, service layer, response serialisation

## The contract is law

The frontend is being built right now against mocks generated from that document. Every
deviation you make silently becomes a defect discovered at M.7 with no obvious cause.

When reality contradicts the contract — a field that cannot be computed efficiently, a status
code that does not fit, a shape that the data model cannot produce — **stop and raise it**.
`system-architect` runs `amend-contract`, the change is logged, and the frontend is told. That
round trip costs minutes. A silent divergence costs an afternoon of integration debugging.

## Procedure

1. **Reuse the existing layers.** The inventory lists shared services, validators, and
   middleware from earlier modules. Extend them; do not build a parallel set.
2. **Validate at the boundary.** Every request body, path parameter, and query parameter is
   validated against the contract schema before anything else runs. Reject unknown fields rather
   than ignoring them.
3. **Authorize explicitly** in every handler, per `auth-authz`. Never rely on a route guard
   alone, and never leave the decision implicit.
4. **Serialise to the contract shape.** Not the database row. An entity leaking columns the
   contract does not mention is both a contract violation and a data exposure risk.
5. **Errors in the global shape**, with the codes the contract specifies, and validation errors
   identifying the failing field.
6. **Pagination exactly as specified** — the same style, parameter names, and metadata as every
   other module.
7. **Transactions around multi-step writes.** Decide the boundary deliberately, per conventions.
8. **Idempotency** implemented where the contract specifies it.
9. **Query efficiently.** Watch for N+1 on any list endpoint — it is the standard defect here.
   Apply filters and pagination in the query, never in application memory.
10. **Emit the events** named in `spec.md`, with the documented payload.
11. **Audit** mutations per the global audit approach.

## Checklist

- [ ] Every path, method, and status code matches the contract exactly
- [ ] Response bodies match the contract schemas field for field
- [ ] No database column leaks that the contract does not declare
- [ ] Every input validated at the boundary; unknown fields rejected
- [ ] Every endpoint has an explicit authorization check
- [ ] Errors use the global shape and specified codes
- [ ] Validation errors identify the failing field
- [ ] Pagination matches the global pattern
- [ ] No N+1 queries on list endpoints
- [ ] Filtering, sorting, and pagination happen in the query
- [ ] Transactions wrap multi-step writes
- [ ] Idempotency implemented where specified
- [ ] Events emitted with documented payloads
- [ ] Mutations audited
- [ ] Existing shared services reused
- [ ] Every contract deviation went through `amend-contract`

## Failure modes

- **Silent contract deviation.** The one failure this whole pipeline is built to prevent.
- **Serialising the raw row.** Leaks columns and breaks the contract simultaneously.
- **N+1 on list endpoints.** Fine with seed data, unusable with the client's.
- **In-memory filtering.** Works until the table grows.
- **Authorization by route guard only.** Every handler decides for itself.

## Handoff

`auth-authz` verifies the authorization layer. `integrator` reconciles this against the frontend
and the contract at M.7.
