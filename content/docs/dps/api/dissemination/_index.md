---
title: Dissemination Service API
weight: 2
---

## Overview

The Dissemination Service lets clients request delivery of archived and preserved packages (AIPs). When a dissemination request is submitted, an integrity (fixity) check and required preparation are performed before the content is made available through a presigned URL that is returned via a webhook.

This documentation supplements the detailed API specification available in Swagger at <https://digitalpreservation.no/swagger/>

For authentication and role details, see the Submission Service API documentation.

## Resource Model: Dissemination

A dissemination represents a request to deliver an already preserved object.

**Key properties:**

- `disseminationId`: Unique Base62 ID (22 characters, case-sensitive)
- `archiveId`: Internal archive ID (AIP identifier)
- `clientId`: Requesting client
- `contractId`: Contract association
- `objectId`: Object identifier
- `sumSizeInBytes`: Total size
- `status`: Current status
- `priority`: Priority (integer; lower = faster scheduling)
- `dateCreated`: Timestamp (RFC 3339)

## Workflow

1. Client sends dissemination request with `archiveId` (and optional `priority`).
2. Service validates (authorization, AIP exists, preserved status, duplicate check).
3. Background process runs integrity check and prepares data.
4. The object becomes available via a presigned URL delivered on a webhook.
5. Client may fetch status by polling on `disseminationId`.

### Internal Process (NiFi)

Internal components (NiFi) coordinate technical steps:

1. Fetch next request (`GET /v1/disseminations/next`).
2. Resolve file locations from LocationDB.
3. Retrieve files from HPSS / other archival storage layer.
4. Verify checksum (fixity).
5. Write files (or consolidated package) to S3.
6. Generate presigned URLs via API.
7. Finalize (set disseminated and expose links).
8. Send notification (success or failure).

## Endpoints

| Method | Path | Description | Role |
| ------ | ---- | ----------- | ----- |
| POST | `/v1/disseminations` | Create new dissemination | `{contractId}_R` |
| GET | `/v1/disseminations/{disseminationId}` | Fetch dissemination | `{contractId}_R` |

## Create Dissemination

`POST /v1/disseminations`

### Request (body)

```json
{
  "archiveId": "68cd11bce080fe9cdf1dac1d",
  "priority": 50
}
```

### Response (201 Created)

```json
{
  "disseminationId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
  "archiveId": "68d3a83aa0be2b1d75eeef77",
  "clientId": "client-id",
  "contractId": "2d17",
  "objectId": "digifoto_5584a028-ba43-4ecb-bb67-7663cc802010",
  "sumSizeInBytes": 123456,
  "status": "FIXITY_CHECK",
  "priority": 50,
  "dateCreated": "2025-09-09T12:34:56.123456+01:00"
}
```

### Errors (creation)

- `400 Bad Request` – Invalid input
- `401 Unauthorized` – Missing / invalid token
- `403 Forbidden` – Missing required role
- `404 AIP not found` – Unknown `archiveId`
- `409 Conflict` – Dissemination already in progress for the same `archiveId` and client
- `422 Unprocessable Entity` – AIP exists but is not preserved / not ready

## Get Dissemination

`GET /v1/disseminations/{disseminationId}`

### Response (200)

```json
{
  "disseminationId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
  "archiveId": "68d3a83aa0be2b1d75eeef77",
  "clientId": "client-id",
  "contractId": "2d17",
  "objectId": "digifoto_5584a028-ba43-4ecb-bb67-7663cc802010",
  "sumSizeInBytes": 123456,
  "status": "FIXITY_CHECK",
  "priority": 50,
  "dateCreated": "2025-09-09T12:34:56.123456+01:00"
}
```

### Errors (retrieval)

- `401 Unauthorized`
- `403 Forbidden`
- `404 Dissemination not found`

## Status Flow

Preliminary statuses (may be extended):

1. `RECEIVED` – Received
2. `QUEUED` – Placed in queue
3. `DOWNLOADING_FROM_REPOSITORY` – Downloading from repository
4. `FIXITY_CHECK` – Integrity verification
5. `UPLOADING_TO_S3` – Uploading to S3
6. `DISSEMINATED` – Delivered
7. `FAILED` – Failed
8. `REJECTED` – Rejected

## Best Practices

1. Reuse existing request if one is already in progress.
2. Use priority sparingly – reserve elevated urgency for critical needs.
3. Poll using exponential backoff.
4. Store the `disseminationId` locally.
5. Handle 409 by fetching the existing dissemination instead of posting again.
6. Avoid tight polling; use exponential backoff.
7. Reuse download links until they expire; regenerate only when necessary.

## Support

Contact the digital preservation team for questions or assistance.

## API Reference

See Swagger: <https://digitalpreservation.no/swagger/> for full schemas and future endpoints.
