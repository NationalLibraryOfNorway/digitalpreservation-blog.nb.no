---
title: Dissemination Service
weight: 2
---

## Overview

The Dissemination Service lets clients request delivery of archived and preserved packages (AIPs). When a dissemination request is submitted, an integrity (fixity) check and required preparation are performed before the content is made available through a presigned URL that is returned via a webhook.

This documentation complements the detailed API reference available through Swagger UI at https://digitalpreservation.no/swagger/.

For general information on authentication and authorization, please refer to the main [API documentation](../).

## Workflow

1. Client sends dissemination request with `archiveId` (and optional `priority`).
2. Service validates (authorization, AIP exists, preserved status, duplicate check).
3. Background process runs integrity check and prepares data.
4. The object becomes available via a presigned URL delivered on a webhook.
5. Client may fetch status by polling on `disseminationId`.


## Endpoints

| Method | Path | Description |
| ------ | ---- | ----------- |
| POST | `/v1/disseminations` | Create new dissemination |
| GET | `/v1/disseminations/{disseminationId}` | Fetch dissemination |


## Example API Usage

### Create Dissemination


**Request**

```http
POST /dps-submission/v1/disseminations HTTP/1.1
Host: api.nb.no
Content-Type: application/json
Authorization: Bearer eyJhbGciOxxxxxxx

{
  "archiveId": "68cd11bce080fe9cdf1dac1d",
  "priority": 50
}
```

**Response (201 Created)**

```json
{
  "disseminationId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
  "archiveId": "68d3a83aa0be2b1d75eeef77",
  "clientId": "client-id",
  "contractId": "2d17",
  "objectId": "digifoto_5584a028-ba43-4ecb-bb67-7663cc802010",
  "sumSizeInBytes": 123456,
  "status": "RECEIVED",
  "priority": 50,
  "dateCreated": "2025-09-09T12:34:56.123456+01:00"
}
```


### Get Dissemination

**Request**

```http
GET /dps-submission/v1/disseminations/8Z7x1T9rN0Xc2B5Yq4L3zP HTTP/1.1
Host: api.nb.no
Content-Type: application/json
Authorization: Bearer eyJhbGciOxxxxxxx
```

**Response (200 OK)**

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
