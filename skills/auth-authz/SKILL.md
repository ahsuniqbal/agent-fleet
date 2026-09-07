---
name: auth-authz
description: Implement and verify authorization for every endpoint in a module — per role, per action, per record ownership — mapping the BRD permission rules onto the global authorization model. Use during stage M.6b. No endpoint ships with an implicit authorization decision.
---

# Auth / authz

**Stage:** M.6b · **Agent:** backend-builder
**Reads:** `docs/modules/NN/brd.md` permissions, `docs/modules/NN/spec.md`,
`docs/modules/NN/api-contract.md`, `docs/00-global/architecture.md`, `docs/00-global/inventory.md`
**Writes:** authorization rules, policy checks, and their tests

## Every endpoint gets an explicit decision

Including the ones that look public. "Any authenticated user" is a decision and is written
down. An endpoint whose authorization is implicit is an endpoint nobody has thought about.

## Authentication versus authorization

- **Authentication** — who is this? Handled once, in the foundation. Do not re-implement it.
- **Authorization** — may they do this, to this record? Decided per endpoint, here.

## The three questions per endpoint

1. **Role** — which roles may call this at all?
2. **Ownership** — may a caller act on records they do not own? Most real defects live here.
   A correct role check with no ownership check means any user can read any other user's data
   by changing an id.
3. **State** — does the record's status permit this action? An approved invoice may not be
   editable regardless of role.

## Rules

1. **Enforce server-side, always.** The frontend hides controls for usability. That is not
   security and never was.
2. **Check in the handler**, not only in middleware or a route guard.
3. **Deny by default.** A new endpoint with no rule is unreachable, not open.
4. **Scope list queries at the database level.** Filter by what the caller may see in the query
   itself. Fetching everything and filtering in application code leaks through pagination
   counts and is slow.
5. **Do not leak existence.** If a caller may not see a record, `404` is usually the right answer
   rather than `403` — `403` confirms the record exists. Follow whatever the contract specifies,
   consistently.
6. **Reuse the global policy layer** from the inventory. A second authorization mechanism in
   module 4 is a security problem, not just an inconsistency.
7. **Test the negative cases.** Every rule needs a test proving the wrong role, the wrong owner,
   and the wrong record state are all rejected. Positive-only tests prove nothing about security.

## Checklist

- [ ] Every endpoint in the contract has an explicit, written authorization rule
- [ ] Every rule traces to a BRD permission statement
- [ ] Role, ownership, and record-state all considered per endpoint
- [ ] Checks are server-side and in the handler
- [ ] Deny by default
- [ ] List queries scoped in the database, not in memory
- [ ] Existence not leaked; behaviour matches the contract
- [ ] Global policy layer reused
- [ ] Negative tests for wrong role, wrong owner, wrong state
- [ ] Nested and related resources checked too — access to a parent does not imply access to
      every child
- [ ] Bulk operations authorized per item, not once for the batch

## Failure modes

- **Role checked, ownership not.** The most common real-world authorization defect.
- **Bulk endpoints authorized once.** A batch containing one forbidden id succeeds entirely.
- **Nested resources unchecked.** `/projects/1/documents/99` where document 99 belongs to
  project 2.
- **Filtering after fetching.** Leaks through counts, timing, and pagination metadata.
- **UI-only enforcement.** The API is the security boundary.
- **Positive tests only.** They pass whether or not the rule works.

## Handoff

`integrator` verifies permission-related acceptance criteria end to end at M.7. Record the
authorization pattern in the inventory at M.9 so later modules inherit it.
