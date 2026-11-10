---
title: Application Programming Interface
weight: 1
aliases:
  - /docs/dps/api/
---


## Overview

The Digital Preservation services at the National Library of Norway provide a RESTful API for managing the submission and dissemination of digital objects. This allows clients to integrate their systems with our preservation workflows.

This documentation provides a high-level overview of the available APIs. For complete technical details, please refer to our [Swagger UI](https://digitalpreservation.no/swagger/).

The machine-readable OpenAPI specification (JSON) is available at <https://api.nb.no/dps-submission/v1/api-docs>.

The API lets you:
- [**Submit content for preservation**](../../how-to/submit-content/): submit digital objects for preservation.
- [**Add preservation events**](../../how-to/add-preservation-events/): add preservation events to a submission.
- [**Request preserved content**](../../how-to/retrieve-content/): request preserved digital objects.
- [**Receive notifications**](../../how-to/receive-notifications/): get automatic status updates in your systems through webhooks.

This page also lists the endpoints, request fields, and status lifecycles for [submissions](#submissions) and [disseminations](#disseminations).

## Authentication & Authorization

The API uses OAuth 2.0 with JWT tokens for authentication, specifically implementing the OAuth 2.0 Client Credentials flow.
The services are designed for system-to-system communication and do not support user-based authentication flows (e.g., the Authorization Code flow).

### OAuth 2.0 Client Credentials Flow

1. Your client application authenticates with the authorization server using its client ID and client secret.
2. The authorization server validates these credentials and returns an access token.
3. Your application includes this access token in the `Authorization` header of all API requests.

All API communication is handled via `https://api.nb.no`, while authentication requests are sent to `https://www.nb.no/authn/realms/dps/protocol/openid-connect/token`.

**Example token request:**
```http
POST /authn/realms/dps/protocol/openid-connect/token HTTP/1.1
Host: www.nb.no
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id={your_client_id}
&client_secret={your_client_secret}
```

**Example API request with token:**
```http
GET /dps-submission/v1/contracts/{your_contract_id}/submissions/{your_submission_id} HTTP/1.1
Host: api.nb.no
Authorization: Bearer {access_token}
```

### Role-Based Authorization

Access to endpoints is controlled by role-based authorization. Your client application must request an access token, and the issued JWT will contain your assigned roles.

- Contract-specific roles (`{contractId}_R`, `{contractId}_W`) provide read and write access to resources under a specific contract.
- The `DPS_SUBMISSION_HANDLER` role is required for internal status management operations.


## Error Handling
The API uses standard HTTP status codes to indicate the success or failure of requests:
- `200 OK` - Request was successful
- `201 Created` - Resource was successfully created
- `400 Bad Request` - Invalid request parameters or payload
- `401 Unauthorized` - Authentication failed or token is missing/invalid
- `403 Forbidden` - Access token is valid but lacks required roles
- `404 Not Found` - Resource not found
- `409 Conflict` - Duplicate/concurrent request
- `422 Unprocessable Entity` – Resource exists but is not preserved / not ready
- `500 Internal Server Error` - An unexpected error occurred on the server
- `502 Bad Gateway` - A service the API depends on failed


Error responses follow [RFC 9457 Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457) and are returned with the media type `application/problem+json`:
```json
{
  "type": "https://digitalpreservation.no/problems/submission-not-found",
  "title": "Submission Not Found",
  "status": 404,
  "detail": "Submission with ID 7mVKGHwOA6w2Ot8feF9fIU was not found",
  "instance": "/v1/contracts/4eaf/submissions/7mVKGHwOA6w2Ot8feF9fIU",
  "timestamp": "2025-10-14T10:03:00.123Z",
  "errorCategory": "NOT_FOUND"
}
```

| Field              | Description                                                                                                                                                        |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`             | URI that identifies the problem type                                                                                                                               |
| `title`            | Short, human-readable summary of the problem type                                                                                                                  |
| `status`           | HTTP status code                                                                                                                                                   |
| `detail`           | Human-readable explanation of this occurrence of the problem                                                                                                       |
| `instance`         | URI that identifies this occurrence of the problem                                                                                                                 |
| `timestamp`        | When the error occurred (ISO 8601)                                                                                                                                 |
| `errorCategory`    | One of `NOT_FOUND`, `CONFLICT`, `VALIDATION_ERROR`, `BUSINESS_RULE_VIOLATION`, `AUTHORIZATION_ERROR`, `INTERNAL_ERROR`, `EXTERNAL_SERVICE_ERROR`                   |
| `validationErrors` | Only for validation errors: an object that maps each invalid field to a list of messages                                                                           |
| `currentStatus`    | Only for errors caused by the resource's state: the current status of the resource                                                                                 |


## Submissions

Endpoints for submitting content. For a step-by-step walkthrough, see [Submit content for preservation](/docs/dps/how-to/submit-content/). All paths are relative to `https://api.nb.no/dps-submission`.

### Submission endpoints

| Method | Path                                                                   | Description                       |
|--------|------------------------------------------------------------------------|-----------------------------------|
| POST   | `/v1/contracts/{contractId}/submissions`                               | Create submission                 |
| GET    | `/v1/contracts/{contractId}/submissions`                               | List submissions for the contract |
| GET    | `/v1/contracts/{contractId}/submissions/{submissionId}`                | Fetch submission                  |
| DELETE | `/v1/contracts/{contractId}/submissions/{submissionId}`                | Delete submission                 |
| POST   | `/v1/contracts/{contractId}/submissions/{submissionId}/files`          | Register file and get upload URL  |
| GET    | `/v1/contracts/{contractId}/submissions/{submissionId}/files/{fileId}` | Fetch file                        |
| DELETE | `/v1/contracts/{contractId}/submissions/{submissionId}/files/{fileId}` | Delete file                       |
| POST   | `/v1/contracts/{contractId}/submissions/{submissionId}/finalize`       | Finalize submission               |
| POST   | `/v1/contracts/{contractId}/submissions/{submissionId}/events`         | Submit event, see [Preservation events](/docs/dps/reference/preservation-events/) |
| GET    | `/v1/contracts/{contractId}/submissions/{submissionId}/events`         | Fetch events                      |

- **List submissions:** Ordered by creation date and paginated with `page` (zero-based, default `0`) and `size` (default `10`). Filter with `objectId` and/or `archiveId` (exact match; multiple filters are combined with AND). If nothing matches, the response is an empty page.
- **Fetch submission:** Use the `include` query parameter to add related data to the response: `FILES` (registered files), `DESCRIPTIVE_METADATA` (the metadata from the request) and `EVENTS` (preservation events), e.g. `?include=FILES&include=EVENTS`.
- **Delete submission:** Only allowed while the submission has the status `REGISTERED` and has no registered files. Delete the files first; a submission that still has files returns `409 Conflict`.
- **Delete file:** Only allowed while the submission has the status `REGISTERED`; otherwise the API returns `409 Conflict`. By default only the file registration is deleted. Add `deleteFromS3=true` to also delete the uploaded file from S3.
- **Finalize submission:** The submission must have at least one registered, non-empty file, and every registered file must be in S3; otherwise the API returns `422 Unprocessable Entity`. A submission can only be finalized once; a second call returns `409 Conflict`.
- **Submit event:** Only allowed while the submission has the status `REGISTERED`. A successful request returns `204 No Content`.

### Submission request fields

#### Create submission

| Field      | Type    | Required | Description |
|------------|---------|----------|-------------|
| `objectId` | string  | Yes      | The client's identifier for the submission object – typically an ID from the source system (e.g. a database ID or URN fragment). Links DPS events such as webhooks back to the object in your system. Must be unique per contract (the combination of `contractId` + `objectId` must be unique). Cannot be changed after the submission has been delivered to DPS. Must be 3–200 characters and may only contain `a-z`, `A-Z`, `0-9`, `-` and `_`. |
| `priority` | integer | No       | Priority for processing in the queue. Valid values: `1` (highest) to `100` (lowest). Default is `50` (normal priority), which is what should be used in most cases. Values above `50` indicate lower priority and are used e.g. for re-archiving. |
| `metadata` | object  | Yes      | Descriptive metadata about the content. See [Metadata Requirements](/docs/dps/reference/descriptive-metadata/) for the available elements. |

#### Register file

| Field        | Type    | Required | Description |
|--------------|---------|----------|-------------|
| `filePath`   | string  | Yes      | Relative path of the file within the submission. Must be unique within the submission, at most 900 characters, may only contain `a-z`, `A-Z`, `0-9`, `-`, `_`, `.`, `(`, `)` and `/`, and cannot start with `/` or `.`. |
| `checksum`   | string  | Yes      | MD5 checksum of the file as 32 lowercase hexadecimal characters. |
| `isPackaged` | boolean | No       | Whether the file is packaged temporarily for transfer only (for example as TAR or ZIP). Such files are unpacked by the preservation flow. Default is `false`. |

The response contains the `fileId`, the `s3ObjectKey`, and an `uploadUrl` for uploading the file content.

### Submission limits

| Limit | Value |
|-------|-------|
| Maximum file size for upload through a pre-signed URL | 5 GiB per file |
| Validity of a pre-signed upload URL (`uploadUrl`) | Approximately 1 hour |
| Checksum algorithm | MD5 |

The file size limit is due to constraints in S3 pre-signed URLs. Larger files can be uploaded directly to S3 using the `s3ObjectKey`; this is primarily intended for internal use at the National Library.

### Submission status lifecycle

A submission progresses through the following statuses:

1. `REGISTERED` - Initial state when a submission is created
2. `UPLOAD_COMPLETED` - All files have been uploaded and the submission has been finalized
3. `PROCESSING` - The submission is being transferred to, validated and archived in the preservation system
4. `PRESERVED` - The submission has been successfully preserved
5. `REJECTED` - The submission has been rejected due to validation errors or other issues

Changes to `PRESERVED` and `REJECTED` are also sent as [webhook](/docs/dps/how-to/receive-notifications/) messages (`submission.preserved` and `submission.rejected`).

## Disseminations

Endpoints for requesting delivery of preserved content. For a step-by-step walkthrough, see [Request preserved content](/docs/dps/how-to/retrieve-content/). All paths are relative to `https://api.nb.no/dps-submission`.

### Dissemination endpoints

| Method | Path                                   | Description              |
|--------|----------------------------------------|--------------------------|
| POST   | `/v1/disseminations`                   | Create new dissemination |
| GET    | `/v1/disseminations/{disseminationId}` | Fetch dissemination      |

- **Create dissemination:** The API checks that the client is authorized, that the package exists and is preserved, and that the request is not a duplicate. If a dissemination is already in progress, the API returns `409 Conflict`. Preparation then runs in the background, and the result is delivered through the `dissemination.delivered` [webhook](/docs/dps/how-to/receive-notifications/).

### Dissemination request fields

| Field       | Type    | Required | Description |
|-------------|---------|----------|-------------|
| `archiveId` | string  | Yes      | Unique identifier for the archive object in DPS to be disseminated. Received via the `submission.preserved` webhook. |
| `priority`  | integer | No       | Priority for processing in the queue. Valid values: `1` (highest) to `100` (lowest). Default is `50` (normal priority). |

### Dissemination status lifecycle

Preliminary statuses (may be extended):

1. `RECEIVED` – Received
2. `QUEUED` – Placed in queue
3. `DOWNLOADING_FROM_REPOSITORY` – Downloading from repository
4. `FIXITY_CHECK` – Integrity verification
5. `UPLOADING_TO_S3` – Uploading to S3
6. `DISSEMINATED` – Delivered
7. `FAILED` – Failed
8. `REJECTED` – Rejected

The download links in the `dissemination.delivered` webhook expire at the time given in `expirationDate`. Each new dissemination gets new links.

## Support

For API support, please contact the Digital Preservation team.

## API Reference

For complete API details including endpoints, parameters, request/response schemas, and status codes, please refer to the [Swagger documentation](https://digitalpreservation.no/swagger/).
