---
name: promote-shared
description: Move a component, service, hook, or utility into the shared layer when a second module needs it — generalising it, refactoring the original consumer, and recording the move. Use at stage M.8 after drift-check issues a promote verdict. Never promote on first use.
---

# Promote shared

**Stage:** M.8 · **Agents:** frontend-builder or backend-builder
**Reads:** `drift-check` verdicts, `docs/00-global/inventory.md`, `CONVENTIONS.md`
**Writes:** the shared library, refactored consumers, `inventory.md`, `00-global/CHANGELOG.md`

## The rule of two

Nothing becomes shared on first use. A second real consumer triggers promotion.

The reason is cost asymmetry: an abstraction built for one known use and one imagined use is
usually shaped wrong, and every later consumer pays for that shape. Two real uses show you
which parts genuinely vary.

**The exception is entities.** Those go global as soon as `groom-module` sees a queued module
that will reference them, because migrating a table across shipped modules means moving real
client data, while moving a component means editing files.

## Procedure

1. **Confirm two real consumers.** Not one real and one anticipated.
2. **Find the true variation.** Compare both uses and identify precisely what differs. That
   difference becomes the API — a prop, a parameter, a slot. Everything identical stays fixed.
3. **Generalise minimally.** Do not add options neither consumer needs. A shared component with
   speculative flexibility is worse than two local copies.
4. **Move it** to the shared location per `CONVENTIONS.md`.
5. **Refactor the first consumer.** This step is not optional. Leaving the original in place
   creates exactly the duplication the promotion was meant to remove, plus a shared copy nobody
   uses.
6. **Refactor the second consumer** to use it too.
7. **Verify both** still behave identically — the original module's tests must still pass.
8. **Record it** in `inventory.md` with its consumers, and log the move in
   `00-global/CHANGELOG.md` with the date and reason.

## Checklist

- [ ] Two genuine consumers, both existing today
- [ ] Variation points identified from real differences, not imagination
- [ ] Generalisation is minimal
- [ ] Moved to the conventional shared location
- [ ] **First consumer refactored** to use the shared version
- [ ] Second consumer uses it
- [ ] Original module's tests still pass
- [ ] No behaviour changed for either consumer
- [ ] Recorded in `inventory.md` with consumers listed
- [ ] Logged in `CHANGELOG.md` with date and reason
- [ ] Both themes, all states, and accessibility preserved through the move

## Failure modes

- **Promoting on one use.** Produces a wrongly-shaped abstraction that every later module fights.
- **Not refactoring the original.** The single most common failure: now there are two
  implementations *and* a shared one.
- **Over-generalising.** Ten props for two consumers means nobody can tell what the component
  actually does.
- **Behaviour drift during the move.** The first module was working; keep it working.
- **Promoting without recording.** An unlisted shared component gets rebuilt in module 6.

## Handoff

`close-module` folds the promotion into the module summary and the inventory index.
