# API contract — <NN> <module name>

> **STATUS: DRAFT** — becomes `FROZEN — <date>` at the M.5 human gate.
>
> Once frozen, the frontend generates mocks from this document and the backend implements
> against it. **No silent changes.** Every change goes through `amend-contract` and is logged
> below.

## Conventions inherited

From `00-global/architecture.md` and the inventory's Patterns section. Not re-decided here.

| Concern | This product's rule |
|---|---|
| Base path | |
| Pagination | |
| Filter & sort params | |
| Error body shape | |
| Status code meanings | |
| Date / time encoding | |
| Money encoding | |
| Enum casing | |

## Reused endpoints

Existing endpoints serving this module's needs. Check the inventory before adding anything new.

| Endpoint | Owner module | Used for |
|---|---|---|

## Endpoints

### `METHOD /path`

**Purpose:** · **Authorization:** <explicit, even if "any authenticated user">

**Path parameters**

| Name | Type | Constraint |
|---|---|---|

**Query parameters**

| Name | Type | Required | Default | Constraint |
|---|---|---|---|---|

**Request body**

```json
```

**Success — `200`**

```json
```

**Errors**

| Status | Condition | Body |
|---|---|---|
| 400 | validation failure | identifies the failing field |
| 401 | | |
| 403 | | |
| 404 | | |
| 409 | | |
| 429 | | |
| 500 | | |

**Idempotency:** <for mutating endpoints>

**Example request / response** — mocks are generated from these, so make them realistic:
populated, multi-item, with optional fields both present and absent.

```json
```

## Traceability

**Design spec coverage** — every bound element reaches a response field

| Design element | Endpoint | Field |
|---|---|---|

**Acceptance criteria coverage** — including failures

| BRD criterion | Endpoint behaviour |
|---|---|

## Changelog

Appended only by `amend-contract`.

### <date> — <summary>
**Requested by:** · **Reason:** · **Type:** additive / modifying / removing
**Affects:** · **Both sides notified:** yes / no
