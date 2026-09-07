---
name: project-skeleton
description: Stand up the runnable project shell — repository layout, routing, database connection, migration runner, environment config, and CI — so the first module has somewhere to land. Use at stage F.6, the last step of foundation before module work begins.
---

# Project skeleton

**Stage:** F.6 · **Agent:** backend-builder
**Reads:** `CONVENTIONS.md`, `docs/00-global/architecture.md`, `docs/00-global/data-model.md`
**Writes:** the repository itself

## Rule

`CONVENTIONS.md` is authoritative. If it names a stack, use exactly that. If it names a
reference project, read it and mirror its structure. If a field says `TBD`, **ask** — do not
choose on the client's behalf and do not silently adopt a default. A skeleton built on a guessed
stack is expensive to unwind after module 1.

## What ships

1. **Repository layout** matching `CONVENTIONS.md`, with the module boundaries from
   `architecture.md` reflected in directories or packages.
2. **Runnable app shell** — starts, serves, renders a page, returns a health endpoint.
3. **Database connection** with pooling configured, plus the connection lifecycle.
4. **Migration runner** wired, with the foundation schema as migration 001.
5. **Environment configuration** — typed and validated at boot, failing loudly on a missing
   required variable. Include `.env.example` with every key and no secrets.
6. **Error handling middleware** implementing the error shape decided in `architecture.md`.
7. **Logging** with the decided format and levels, and request correlation ids.
8. **Auth shell** if the architecture calls for it — session or token plumbing, not module
   logic.
9. **Test harness** — unit and e2e runners configured, with one passing smoke test each so the
   wiring is proven.
10. **Linter and formatter** configured to `CONVENTIONS.md`, with a pre-commit path.
11. **CI** — install, lint, typecheck, test, build. Green on the first commit.
12. **README** — how to install, configure, run, migrate, test.

## Checklist

- [ ] `git clone` → documented setup steps → app runs. Verified, not assumed.
- [ ] Migrations run forward and roll back cleanly on a fresh database
- [ ] Missing required env var fails at boot with a clear message, not at first request
- [ ] `.env.example` complete, no real secrets committed
- [ ] Error middleware produces exactly the documented error shape
- [ ] Health endpoint returns dependency status, not just `200`
- [ ] CI green
- [ ] `.gitignore` covers env files, build output, dependencies, editor and OS files
- [ ] Smoke tests pass in both runners
- [ ] README lets someone else start from zero

## Failure modes

- **Guessed stack.** Ask instead. Every time.
- **Untested setup path.** Run the README steps yourself from a clean state.
- **Secrets committed.** Check before the first commit, not after.
- **Env validated lazily.** A missing key should stop boot, not surface as a null three screens
  into a demo.
- **CI added later.** It is cheapest now and never gets cheaper.

## Handoff

Foundation is frozen after this. Seed `docs/00-global/inventory.md` with the primitives from
F.4, the entities from F.5, and the patterns decided in `architecture.md` — pagination style,
error shape, logging, audit. Module 1 starts at M.0 by reading it.
