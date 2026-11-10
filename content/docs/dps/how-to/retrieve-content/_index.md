---
title: Request preserved content
weight: 3
aliases:
  - /docs/dps/api/dissemination/
---

This guide shows how to request delivery of content that has been preserved in DPS, and how to download it. Delivery is asynchronous: DPS verifies and prepares the content first, and notifies you when it is ready. Field names and statuses are listed in the [API reference](/docs/dps/reference/api/#disseminations).

## Before you start

- **Client credentials and an access token**, with a consumer role for the contract the content belongs to. See [Authentication & Authorization](/docs/dps/reference/api/#authentication--authorization).
- **The `archiveId`** of the content you want. It is sent in the `submission.preserved` webhook when the content is preserved.
- **A webhook endpoint** to receive the `dissemination.delivered` message with the download links. See [Receive notifications](/docs/dps/how-to/receive-notifications/).

## Steps

{{% steps %}}

### Request delivery

Create a dissemination with the `archiveId`. Use the default priority unless the need is urgent.

**Request**

```http
POST /dps-submission/v1/disseminations HTTP/1.1
Host: api.nb.no
Content-Type: application/json
Authorization: Bearer eyJhbGciOxxxxxxx

{
  "archiveId": "019e404e-60ab-7457-b7c9-94c453242c69",
  "priority": 50
}
```

**Response (201 Created)**

```json
{
  "disseminationId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
  "archiveId": "019e404e-60ab-7457-b7c9-94c453242c69",
  "clientId": "client-id",
  "contractId": "2d17",
  "objectId": "digifoto_5584a028-ba43-4ecb-bb67-7663cc802010",
  "sumSizeInBytes": 123456,
  "status": "RECEIVED",
  "priority": 50,
  "dateCreated": "2025-09-09T12:34:56.123456+01:00"
}
```

Store the `disseminationId` from the response. If a dissemination of the same content is already in progress, the API returns `409 Conflict`: fetch the existing dissemination instead of creating a new one.

### Wait for the content to be prepared

DPS retrieves the content from the repository, checks its integrity, and makes it available for download. This can take some time. When the content is ready, you receive a `dissemination.delivered` webhook message.

You can also follow the status by fetching the dissemination. Avoid tight polling; use exponential backoff.

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
  "archiveId": "019e404e-60ab-7457-b7c9-94c453242c69",
  "clientId": "client-id",
  "contractId": "2d17",
  "objectId": "digifoto_5584a028-ba43-4ecb-bb67-7663cc802010",
  "sumSizeInBytes": 123456,
  "status": "FIXITY_CHECK",
  "priority": 50,
  "dateCreated": "2025-09-09T12:34:56.123456+01:00"
}
```

### Download and verify the files

The [`dissemination.delivered`](/docs/dps/reference/api/#disseminationdelivered) message contains a `files` list. For each file, download it from `downloadURL` and compare it with `checksum`, using the algorithm given in `checksumAlgorithm`.

Download the files before the links expire (`expirationDate`). If the links expire, create a new dissemination request; each dissemination gets new links.

{{% /steps %}}

## Best practices

1. Reuse existing request if one is already in progress.
2. Use priority sparingly – reserve low values for urgent needs.
3. Store the `disseminationId` locally.
4. Handle 409 by fetching the existing dissemination instead of posting again.
5. Avoid tight polling; use exponential backoff.
6. Download the files before the links expire (`expirationDate` in the `dissemination.delivered` webhook). If the links expire, create a new dissemination request; each dissemination gets new links.

## Support

Contact the digital preservation team for questions or assistance.
