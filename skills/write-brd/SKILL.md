---
name: write-brd
description: Write a detailed business requirements document for one module — features, user stories, every edge case, permissions, validation rules, and Given/When/Then acceptance criteria. Use at stage M.1, the first step of every module loop, before any technical grooming.
---

# Write BRD

**Stage:** M.1 · **Agent:** product-owner
**Reads:** `docs/00-global/inventory.md`, `docs/00-global/requirements.md`,
`docs/00-global/module-map.md`
**Writes:** `docs/modules/NN-<name>/brd.md` (template: `templates/module-brd.md`)

This is where edge cases get found. Every edge case not found here is found by the client, in
production, at the worst possible moment.

## The edge case checklist — work every line

For each feature in the module:

| Dimension | Ask |
|---|---|
| **Happy path** | The intended flow, start to finish |
| **Alternate flows** | Legitimate variations — different roles, different entry points |
| **Validation** | Every field: required, format, length, range, uniqueness, allowed characters |
| **Error states** | What the user sees when each thing fails, and what they can do next |
| **Empty states** | Nothing yet, nothing matching the filter, nothing they have access to |
| **First run** | The very first time, before any data exists |
| **Permissions** | Per role: who can see, create, edit, delete, export, approve |
| **Ownership** | Can a user act on records they did not create? |
| **Concurrency** | Two users edit the same record simultaneously — who wins, what does the loser see |
| **Limits and quotas** | Maximum items, file sizes, request rates, and the message at the limit |
| **Data lifecycle** | Create, edit, delete, archive, restore, permanent purge — which exist, who can, what cascades |
| **Bulk operations** | Select-all semantics, partial failure behaviour |
| **Side effects** | Notifications, emails, webhooks, audit entries triggered by each action |
| **Time** | Timezones, scheduling, expiry, retention |
| **Search and filter** | What is searchable, how results sort, what pagination the user sees |
| **Import and export** | Formats, size limits, malformed input handling |
| **Offline and interruption** | Lost connection mid-action, unsaved changes on navigation |
| **Localisation** | Languages, currencies, date formats, number formats, text direction |
| **Accessibility** | Any obligation beyond the baseline the design system already provides |

Not every dimension applies to every feature. The ones that do not apply are written down as
"not applicable" — an unanswered dimension is different from an inapplicable one.

## Reuse awareness

Read the inventory before writing. If a feature in this module resembles something already
shipped, say so explicitly: "same pattern as the list view in module 02". This is what lets
`groom-module` produce a real reuse plan instead of rediscovering everything from scratch.

## Acceptance criteria

Every feature ends with Given/When/Then criteria, including the unhappy paths. These become the
e2e suite at M.7 — they are executable specification, not description.

```
Given a user with the "viewer" role
When they open an invoice they do not own
Then they see the invoice in read-only form with no edit controls
```

If you cannot write a testable criterion for a requirement, it is not ready to build.

## Checklist

- [ ] Every feature has a user story with a role and a goal
- [ ] Every edge case dimension addressed or explicitly marked not applicable
- [ ] Permissions specified per role, per action — no implicit "everyone"
- [ ] Every field has validation rules
- [ ] Every error has user-facing wording, or a note that it needs copy
- [ ] Every list has an empty state and a no-results state
- [ ] Acceptance criteria in Given/When/Then, covering unhappy paths
- [ ] Out of scope for this module stated explicitly
- [ ] Dependencies on other modules named
- [ ] Similarities to already-shipped features flagged for reuse
- [ ] Open questions listed with implications

## Failure modes

- **Happy path only.** The most common failure, and the reason modules slip late.
- **Permissions as an afterthought.** Retrofitting authorization is expensive and dangerous.
- **"The system should handle errors gracefully."** Not a requirement. Name the errors.
- **Missing empty states.** Every list needs one, and the client always notices.
- **Untestable criteria.** If the integrator cannot turn it into a test, rewrite it.

## Handoff

Client approves scope and acceptance criteria. Then `groom-module` at M.2.
