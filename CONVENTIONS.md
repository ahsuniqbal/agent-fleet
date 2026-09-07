# Conventions

Every agent in this fleet reads this file before writing code. Fill it in per project (or
keep a filled copy at the fleet level if your stack is consistent across clients).

If a field says `TBD`, agents must ask rather than guess.

## Stack

| Layer | Choice |
|---|---|
| Frontend framework | TBD |
| Language / typing | TBD |
| Styling | TBD |
| Component state | TBD |
| Server state / data fetching | TBD |
| Routing | TBD |
| Backend runtime | TBD |
| Backend framework | TBD |
| Database | TBD |
| ORM / query layer | TBD |
| Migrations tool | TBD |
| Auth | TBD |
| Background jobs | TBD |
| File storage | TBD |
| Hosting | TBD |
| Unit test runner | TBD |
| E2E test runner | TBD |
| Linter / formatter | TBD |
| Package manager | TBD |

## Repository layout

```
TBD — paste the tree of a reference project here.
Agents mirror this exactly rather than inventing structure.
```

## Naming

- Files: TBD
- Components: TBD
- Hooks / composables: TBD
- Database tables: TBD
- Database columns: TBD
- API routes: TBD
- Env vars: TBD

## API conventions

- Base path: TBD
- Pagination: TBD (cursor vs offset, param names)
- Filtering / sorting params: TBD
- Error body shape: TBD
- Status codes for validation / authz / not-found: TBD
- Idempotency: TBD
- Versioning: TBD

## Frontend conventions

- Loading state pattern: TBD
- Empty state pattern: TBD
- Error state pattern: TBD
- Form validation: TBD
- Toast / notification: TBD
- Optimistic updates — when allowed: TBD

## Backend conventions

- Validation layer: TBD
- Authorization check placement: TBD
- Transaction boundaries: TBD
- Logging: TBD
- Audit trail: TBD

## Testing

- What must have tests: TBD
- What is exempt: TBD
- Fixture / factory pattern: TBD

## Git

- Branch naming: TBD
- Commit message format: TBD
- PR template: TBD

## Reference project

Path or URL to a repo agents should read for idiom when this file is ambiguous:

`TBD`
