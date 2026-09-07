---
name: api-contract
description: Author the frozen API contract for one module — endpoints, request and response schemas, errors, pagination, and authorization — grounded in the module data model and the fields the design spec actually needs. Use at stage M.5. This document is what allows the frontend and backend to build in parallel.
---

# API contract

**Stage:** M.5 · **Agent:** system-architect
**Reads:** `docs/modules/NN/spec.md`, `docs/modules/NN/data-model.md`,
`docs/modules/NN/design-spec.md`, `docs/00-global/inventory.md`, `CONVENTIONS.md`
**Writes:** `docs/modules/NN/api-contract.md` (template: `templates/module-api-contract.md`)

## Why this stage sits where it does

It reads the **data model** so schemas describe fields that actually exist. It reads the
**design spec** so endpoints return the fields the screens actually need. Written before
either, it would be a guess that both builders then work around.

Once frozen, both builders start. The frontend generates mocks from this document; the backend
implements against it. That parallelism is the only parallelism in the pipeline, and this
document is what makes it safe.

## Procedure

1. **Check the inventory Endpoints section first.** If an endpoint already exists that serves
   this need, reuse it. Do not create `GET /api/module3/users`.
2. **Adopt the global patterns** from `architecture.md` and the inventory: pagination style and
   parameter names, error body shape, filter and sort conventions, status code meanings,
   date and money encoding. Do not re-decide these per module.
3. For every endpoint specify: method, path, purpose, authorization requirement, path and query
   parameters with types and constraints, request body schema, success response schema with
   status code, every error response with status and body, pagination shape where applicable,
   and idempotency behaviour for anything that mutates.
4. **Trace every field in the design spec** to a response field. Any element the design binds
   to must be reachable. Missing fields discovered at integration are the single most common
   cause of contract amendments.
5. **Trace every acceptance criterion** in the BRD to the endpoints that satisfy it, including
   the unhappy paths — an authorization failure needs a specified response, not an
   implementation accident.
6. **Specify errors exhaustively.** Validation failure shape including which field failed,
   authentication failure, authorization failure, not found, conflict, rate limit, and server
   error. The frontend builds error states from this list.
7. **Include realistic examples** for every request and response. Examples are what mocks are
   generated from, so a sloppy example produces a sloppy mock and a surprise at integration.
8. **Open a changelog section** in the document, empty at freeze. `amend-contract` appends to it.

## Checklist

- [ ] Existing endpoints reused where applicable
- [ ] Global pagination, error, and filter conventions followed exactly
- [ ] Every endpoint has an explicit authorization requirement, including "any authenticated user"
- [ ] Every design-spec element traces to a response field
- [ ] Every BRD acceptance criterion, including failures, traces to an endpoint behaviour
- [ ] Every error case specified with status and body
- [ ] Validation errors identify the failing field
- [ ] Mutating endpoints state their idempotency behaviour
- [ ] Realistic examples for every request and response
- [ ] Dates, times, timezones, money, and enums have stated encodings
- [ ] Empty changelog section present
- [ ] Marked **FROZEN** with a date once the human approves

## Failure modes

- **Written before the design spec.** Then screens need fields nobody exposed.
- **Vague error handling.** "Returns 4xx on error" leaves the frontend inventing error states
  that will not match reality.
- **Optimistic examples.** Empty arrays, null-free objects, and single-page results produce
  mocks that hide every case the UI will actually meet.
- **Unstated encodings.** Money as float, dates without timezone — both cause real defects.
- **Silent drift after freeze.** Any change goes through `amend-contract`, always.

## Handoff

Human freezes. Then M.6a and M.6b start in parallel. Any blocker on either side routes to
`amend-contract` — never to a local workaround.
