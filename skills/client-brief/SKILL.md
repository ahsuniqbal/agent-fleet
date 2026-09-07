---
name: client-brief
description: Produce a client-facing document from internal artifacts — a scope proposal after decomposition, or a release note after a module ships. Use after F.1 or at stage M.9. Translates internal detail into something a non-technical client can act on.
---

# Client brief

**Stage:** after F.1, or M.9 · **Agent:** product-owner
**Reads:** `docs/00-global/module-map.md`, `docs/modules/NN/brd.md`,
`docs/modules/NN/summary.md`
**Writes:** a client-facing document (outside `docs/`, or wherever the client receives it)

## Two forms

| Form | When | Purpose |
|---|---|---|
| **Scope brief** | after F.1 | what will be built, in what order, and why that order |
| **Release note** | at M.9 | what shipped, what it does, what is next |

## Rules

1. **No internal jargon.** No module numbers as identifiers, no table names, no endpoint paths,
   no agent or stage names. The client cares about capabilities.
2. **Lead with what changes for their business**, not with what was implemented.
3. **Explain the sequencing** in a scope brief. Clients frequently want their favourite feature
   first; showing the dependency reasoning prevents that becoming a negotiation. "Invoicing needs
   customer records to exist first" is understood immediately.
4. **Be honest about what is not included.** Restate out-of-scope items plainly. This is the
   cheapest dispute prevention available.
5. **Surface open questions** the client still owes answers to, with what each one blocks.
6. **Do not over-promise on timing.** If dates appear, they carry their assumptions.
7. **Known limitations belong in the release note.** A limitation the client discovers alone
   costs trust; one you disclose costs a sentence.

## Scope brief contents

- What the product does, in one paragraph
- The capabilities being built, grouped as the client thinks about them
- Delivery sequence, with a plain-language reason per position
- What each stage lets them do when it lands
- Explicitly out of scope
- Open questions and what each blocks
- Assumptions the estimate rests on

## Release note contents

- What is now available, described by what the user can do
- How to reach it
- Known limitations, plainly stated
- What is coming next
- Anything you need from the client to proceed

## Checklist

- [ ] No internal terminology anywhere
- [ ] Capabilities described by user outcome
- [ ] Sequencing explained in business terms
- [ ] Out of scope explicit
- [ ] Open questions listed with what they block
- [ ] Known limitations disclosed
- [ ] Assumptions behind any dates stated
- [ ] Readable by someone with no technical background

## Failure modes

- **Internal language leaking through.** "Module 03" and "the contract" mean nothing to a client.
- **Feature lists instead of outcomes.** "Added filter dropdown" versus "find any invoice by
  status in one click".
- **Hidden limitations.** Always more expensive than disclosed ones.
- **Unqualified dates.** They become commitments the moment they are written down.
