# Test environment — <product name>

Written by `project-skeleton` at F.6; updated whenever a module adds a role or seed data.
`qa-analyst` names users from here; `qa-tester` starts the app from this file alone. If a step
here does not work from a clean checkout, that is a defect in this file.

## Start

```bash
# install
# start database
# migrate
# seed
# start app
```

| Item | Value |
|---|---|
| Frontend URL | |
| API base URL | |
| Health check | |
| Reset to clean seed | |

## Roles and test users

One user per role, plus a second user in any role where ownership matters ("edit own" versus
"edit others"). Test credentials only — never real ones.

| Role | Email / username | Password | Notes |
|---|---|---|---|
| | | | |

## Getting an API token

```bash
# curl command that returns a token for a given user
```

## Seed data

What exists after seeding, so cases can rely on it.

| Entity | Records | Owned by | Added by module |
|---|---|---|---|

## Reaching non-default states

How a tester produces states without touching code — an empty account, a slow response, a
server error — or `not reachable` where there is no way.

| State | How |
|---|---|
| Empty / first run | |
| Slow network | browser throttling |
| Server error | |
