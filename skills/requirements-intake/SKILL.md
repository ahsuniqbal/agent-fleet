---
name: requirements-intake
description: Turn a client conversation, transcript, brief, or notes into a structured product requirements document with explicit assumptions, open questions, and out-of-scope items. Use at stage F.0, at the very start of a project, before any decomposition or technical work.
---

# Requirements intake

**Stage:** F.0 · **Agent:** product-owner
**Reads:** client call notes, transcript, brief, existing docs
**Writes:** `docs/00-global/requirements.md` (template: `templates/00-requirements.md`)

## The one thing that goes wrong

Confident invention. Clients speak in fragments and the temptation is to smooth them into a
coherent document by filling gaps. Every gap you fill silently becomes a decision nobody
approved, discovered at delivery.

So: three buckets, always visible and never merged.

| Bucket | Meaning |
|---|---|
| **Stated** | The client said this. Quote or paraphrase closely. |
| **Assumed** | You inferred it. Reasonable, but unconfirmed — flagged for correction. |
| **Open** | Genuinely unknown. Needs the client to answer before it can move. |

## Procedure

1. Extract every stated requirement. Do not editorialise, do not reorder into your preferred
   structure yet.
2. Identify the **business goal** behind the request — what changes for the client's business
   if this ships? A requirements doc without this cannot support scope trade-offs later.
3. Identify **who uses it**: every user type, their goal, their frequency of use, their
   technical comfort. Roles discovered late rewrite the permission model.
4. Capture **constraints** as constraints, never as solutions. "Must work on site with no
   signal" — not "use IndexedDB".
5. List **assumptions** explicitly, each one testable by a yes/no question to the client.
6. List **open questions**, each with the candidate answers and what each one implies for
   scope, cost, or timeline. An open question without implications is not decision-ready.
7. Write **out of scope** explicitly. This section prevents more disputes than any other.
8. Note **existing systems** to integrate with, and who owns them.
9. Note **non-functionals** the client actually cares about: expected users, data volumes,
   uptime expectations, compliance, data residency, languages, accessibility obligations.

## Checklist before you hand it over

- [ ] Business goal stated in one sentence
- [ ] Every user role listed with their primary goal
- [ ] Every stated requirement traceable to something the client actually said
- [ ] Assumptions section is non-empty (if it is empty, you invented instead of flagged)
- [ ] Every open question carries options and implications
- [ ] Out of scope is explicit and specific
- [ ] Non-functionals captured, or explicitly marked as not discussed
- [ ] Existing systems and their owners listed
- [ ] No technology named anywhere in the document

## Failure modes

- **Empty assumptions section** — means gaps were filled silently. Re-read and find them.
- **Technology in the requirements** — a business document that names a database has skipped
  a stage and pre-empted the architect.
- **Untestable requirements** — "the system should be fast" is not a requirement. Either get a
  number or move it to open questions.
- **Requirements that are really features of a solution the client already imagined** —
  separate the underlying need from their proposed implementation, and record both.

## Handoff

The human takes open questions to the client. Do not proceed to `module-decomposition` until
questions that affect module boundaries are answered — a wrong boundary is expensive to undo
once modules start shipping.
