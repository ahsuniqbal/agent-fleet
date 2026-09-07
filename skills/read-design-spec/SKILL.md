---
name: read-design-spec
description: Turn a module's design spec and canvas into an ordered frontend build plan, resolving every element against the existing component inventory before any code is written. Use at the start of stage M.6a, before build-component or compose-page.
---

# Read design spec

**Stage:** M.6a start · **Agent:** frontend-builder
**Reads:** `docs/modules/NN/design-spec.md`, the canvas, `docs/00-global/inventory.md`,
`docs/00-global/design-system.md`, `docs/modules/NN/spec.md` reuse plan
**Writes:** a build plan (working notes; no permanent document required)

## Read order matters

1. **`design-spec.md` first** — intent. Which elements are shared, extended, or new. What
   states exist. Which tokens apply. How data binds.
2. **Canvas second** — values. Exact composition, spacing, hierarchy.

Reversing this order produces a builder that reimplements a shared component because the canvas
showed pixels and the spec was never opened.

## Procedure

1. Read the spec's component inventory. For each element, resolve it against
   `inventory.md` **Components**:
   - **exists** → import it. Do not fork, do not copy, do not "adapt".
   - **exists but needs a variant** → add the variant to the shared component if it is general,
     or wrap it locally if it is specific to this module.
   - **new** → confirm the reuse plan actually said new. If the plan said reuse and you are
     about to build, stop and raise it.
2. Extract the full **state matrix**: every data-bound element × its states (default, loading,
   empty, no-results, error, partial, permission-denied). This matrix is your definition of done
   — not "the screen renders".
3. Extract the **token set** the module uses. Any token named in the spec that is not in the
   design system is a gap: raise it rather than inlining a value.
4. Extract the **data binding map** — which response field from `api-contract.md` populates
   which element. Cross-check against the contract now. A missing field found here is cheap; the
   same field found at integration costs an amendment.
5. Order the build: shared component extensions first, then module components, then pages. A
   page built before its components forces rework.
6. Note every **interaction rule** — confirmations, unsaved-change guards, optimistic updates,
   focus movement.

## Checklist

- [ ] Every element resolved to exists / extend / new
- [ ] Nothing marked new that the reuse plan said would be reused
- [ ] State matrix extracted and complete
- [ ] Every token in the spec exists in the design system
- [ ] Every bound field verified against the API contract
- [ ] Build ordered components before pages
- [ ] Interaction and accessibility rules noted
- [ ] Gaps raised rather than filled with assumptions

## Failure modes

- **Skipping to the canvas.** Produces duplicated components and missing states — the two things
  `drift-check` will find and force you to redo.
- **Silent gap-filling.** A token that does not exist, a field the contract does not return —
  both must be raised, not invented.
- **Building pages first.** Guarantees rework.
- **Treating "renders correctly" as done.** The state matrix is the definition of done.

## Handoff

`build-component`, then `compose-page`, then `wire-api-client` — though the client and mocks are
often generated first so components have something to develop against.
