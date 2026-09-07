---
name: wire-api-client
description: Generate a typed API client and realistic mocks directly from the frozen API contract, so the frontend can be built and tested in parallel with the backend. Use during stage M.6a. The contract is the only source — never invent endpoints or fields.
---

# Wire API client

**Stage:** M.6a · **Agent:** frontend-builder
**Reads:** `docs/modules/NN/api-contract.md`, `docs/00-global/inventory.md`, `CONVENTIONS.md`
**Writes:** typed API client, request and response types, mock handlers, fixtures

## The contract is the only source

Every type, every path, every field comes from `api-contract.md`. If you need something the
contract does not provide, that is not a gap to fill locally — it is an amendment. Raise it so
`system-architect` runs `amend-contract`. A field invented here surfaces at M.7 as a mystery
mismatch and costs more to diagnose than to have raised.

## Procedure

1. **Reuse the existing client layer.** Check the inventory: base client, auth header handling,
   error normalisation, and retry policy already exist from earlier modules. Add this module's
   endpoints to that layer. Do not create a second HTTP client.
2. **Generate types** from the contract schemas. Optional versus required, nullable versus
   absent, and enum values must match the contract exactly — not "close enough".
3. **Normalise errors** through the existing shared handler so this module's error handling is
   identical to every previous module's.
4. **Build mocks** covering, per endpoint:
   - a realistic success response — populated, plausible, multi-item where the real thing would be
   - an **empty** result
   - a **paginated** result with more than one page, so pagination is actually exercised
   - each **error** the contract specifies: validation, unauthenticated, forbidden, not found,
     conflict, rate limit, server error
   - a **slow** response, so loading states are visible and testable
5. **Fixtures must be realistic.** Long names, missing optional fields, unicode, very large
   numbers, empty strings, dates across timezones. Sanitised fixtures hide the defects the UI
   will meet on day one.
6. **Mark the swap points** clearly so `integrator` can find every one of them at M.7.

## Checklist

- [ ] Every type derived from the contract, none invented
- [ ] Existing client layer reused, not replaced
- [ ] Error normalisation shared with earlier modules
- [ ] Mocks cover success, empty, multi-page, every specified error, and slow
- [ ] Fixtures include awkward realistic data
- [ ] Enum values match the contract exactly
- [ ] Date, time, and money encodings match the contract
- [ ] Swap points clearly marked
- [ ] Nothing outside the contract's surface is called

## Failure modes

- **Optimistic mocks.** Every response populated and fast means the empty, error, and loading
  states are never exercised and ship broken.
- **A second HTTP client.** Duplicated auth and error handling that then diverges.
- **Invented fields.** The defining failure of this stage. Raise instead.
- **Single-page mocks.** Pagination bugs surface in front of the client.
- **Enum drift.** `"active"` versus `"ACTIVE"` costs an afternoon at integration.

## Handoff

`integrator` at M.7 replaces mocks with real calls and reconciles any divergence against this
same contract.
