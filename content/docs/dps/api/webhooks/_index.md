---
title: Webhooks
weight: 3
---

# Webhooks from Digital Preservation System (DPS)

The National Library of Norway can send event notifications directly to your systems via webhooks.  
DPS uses **Standard Webhooks**[^1] for format and signing, allowing notifications to be securely validated and automatically processed.

This enables you to receive automatic messages when submissions or disseminations change status – without having to poll our API continuously.

To receive these notifications, you must have an **endpoint (a URL)** that can accept **HTTPS POST** requests with **JSON data** from DPS.  
Currently, the National Library manually registers all webhook endpoints in collaboration with each partner.

---

## Purpose

- Notify about status changes in submissions
- Notify about completed disseminations
- Ensure secure and predictable delivery with clear contracts

---

## How it works

When an event occurs in DPS:

1. DPS sends an **HTTP POST** request to the URL you have provided
2. The message contains information about the event in **JSON format**, according to *Standard Webhooks*
3. Your system receives the message, validates that it comes from DPS, and responds with **HTTP 200 OK**

## Technical Requirements

### Transport and Format

| Property           | Requirement                                    |
|--------------------|------------------------------------------------|
| **Protocol**       | HTTPS (TLS 1.2 or higher)                      |
| **Method**         | POST                                           |
| **Content-Type**   | `application/json`                             |
| **Authentication** | HMAC signature in header (`webhook-signature`) |
| **Response Time**  | Maximum 10 seconds                             |
| **Certificate**    | Valid TLS certificate required                 |

### Endpoint Setup

You must expose a publicly accessible URL, for example:

```http
POST https://partner.example.com/api/dps/webhook
```

**Recommendations:**

- Use an IP allowlist (we can provide fixed outgoing IPs if needed)
- Set up monitoring and alerting to ensure your service is operational
- Validate the signature for each message before processing

---

## HTTP Headers (Standard Webhooks Format)

All messages are sent with the following headers:

```
webhook-id: <unique id>
webhook-timestamp: <unix seconds>
webhook-signature: v1,<base64-signature>
```

| Header              | Description                                                                            |
|---------------------|----------------------------------------------------------------------------------------|
| `webhook-id`        | Unique ID for the message (same ID used for retries – use as deduplication key)        |
| `webhook-timestamp` | UNIX time in seconds; use a time window (±5–10 min) to reject old messages             |
| `webhook-signature` | HMAC-SHA256 of `id + "." + timestamp + "." + raw request body`, signed with shared key |

>  **Tip:** Always verify the signature against the raw **request body**, not a re-serialized JSON structure.

---

## Responding to the Message

The webhook receiver must:

- Respond with **HTTP 200 OK** within 10 seconds
- Return no or minimal body (DPS only cares about the status code)
- For 4xx/5xx or timeout, DPS will retry with exponential backoff

---

## Common JSON Structure

All webhook messages follow the same structure ("envelope"):

```json
{
  "type": "<event type>",
  "timestamp": "2025-09-10T00:08:11.407000+02:00",
  "data": {}
}
```

| Field       | Type   | Description                                                                                   |
|-------------|--------|-----------------------------------------------------------------------------------------------|
| `type`      | string | Event type (see below)                                                                        |
| `timestamp` | string | Timestamp when the event occurred, in RFC3339/ISO 8601 format with explicit offset or UTC (Z) |
| `data`      | object | Event-specific fields                                                                         |

---

## Events

DPS currently supports the following events.

---

### `submission.preserved`

Webhook sent when a SIP submission is preserved and stored permanently.

**Example**
```json
{
  "type": "submission.preserved",
  "timestamp": "2025-09-10T00:08:11.407000+02:00",
  "data": {
    "contractId": "ef23",
    "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
    "archiveId": "68b803fb25d74833747835f7"
  }
}
```

| Field          | Type   | Description                                                          |
|----------------|--------|----------------------------------------------------------------------|
| `contractId`   | string | Identifier for the contract or agreement the submission is linked to |
| `submissionId` | string | Unique identifier for the SIP submission                             |
| `archiveId`    | string | Unique identifier for the archive object in DPS                      |

---

### `submission.rejected`

Webhook sent when a SIP submission is rejected during validation or processing.

**Example**
```json
{
  "type": "submission.rejected",
  "timestamp": "2025-09-10T00:08:11.407000+02:00",
  "data": {
    "contractId": "ef23",
    "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
    "archiveId": "68b803fb25d74833747835f7",
    "reasons": [
      {
        "code": "METADATA_SCHEMA_INVALID",
        "message": "Descriptive metadata did not validate against the required profile."
      },
      {
        "code": "FILE_CHECKSUM_MISMATCH",
        "message": "Checksum mismatch.",
        "filePath": "objects/issue_1942_05.pdf"
      }
    ]
  }
}
```

| Field          | Type   | Description                                                                                                                                                        |
|----------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `contractId`   | string | Identifier for the contract or agreement the submission is linked to                                                                                               |
| `submissionId` | string | Unique identifier for the SIP submission                                                                                                                           |
| `archiveId`    | string | Unique identifier for the archive object in DPS                                                                                                                    |
| `reasons`      | array  | List of reasons for rejection. At least one entry.                                                                                                                 |
| → `code`       | string | Machine-readable error code identifying the type of error. Stable over time                                                                                        |
| → `message`    | string | Human-readable description of the error                                                                                                                            |
| → `filePath`   | string | Relative path to the file the error pertains to, if the error can be linked to a specific file. If this field is missing, the error applies to the entire package. |

---

### `dissemination.delivered`

Webhook sent when a delivery package (DIP) is made available for download.

**Example**
```json
{
  "type": "dissemination.delivered",
  "timestamp": "2025-10-02T09:18:01.160+02:00",
  "data": {
    "archiveId": "68d3a838a0be2b1d75eeef75",
    "disseminationId": "5MfwdzCjkYW4c79MYorXy9",
    "objectId": "digifoto_ae0690eb-22bf-4996-a6a0-9273b7cd9256",
    "clientId": "kulturit",
    "contractId": "2d17",
    "sumSizeInBytes": "1",
    "files": [
      {
        "downloadURL": "https://minio.dev.nb.no/submission-service-stage/dissemination/5MfwdzCjkYW4c79MYorXy9/68d3a838a0be2b1d75eeef75/primary_20250325.tar?...",
        "filename": "primary_20250325.tar",
        "filesize": 3481600,
        "expirationDate": "2025-10-03T09:18:01.023897767+02:00",
        "checksum": "ae958c69059974c63980035882d2178c",
        "checksumAlgorithm": "MD5"
      }
    ]
  }
}
```

| Field                  | Type      | Description                                                                |
|------------------------|-----------|----------------------------------------------------------------------------|
| `archiveId`            | string    | Unique identifier for the archive object in DPS                            |
| `disseminationId`      | string    | Unique identifier for the delivery package                                 |
| `objectId`             | string    | Object identifier from the depositor                                       |
| `clientId`             | string    | Recipient                                                                  |
| `contractId`           | string    | Identifier for the contract or agreement the delivery package is linked to |
| `sumSizeInBytes`       | integer   | Total size in bytes                                                        |
| `files`                | array     | List of files in the package                                               |
| → `downloadURL`        | uri       | Pre-signed download URL                                                    |
| → `filename`           | string    | File name                                                                  |
| → `filesize`           | integer   | File size in bytes                                                         |
| → `expirationDate`     | date-time | Expiration date for the URL                                                |
| → `checksum`           | string    | Checksum                                                                   |
| → `checksumAlgorithm`  | enum      | Algorithm used for checksum                                                |

---

## Signature Verification

The webhooks are signed to ensure authenticity and integrity.  
The receiver must validate the signature before processing the message.

**Pseudocode:**

```text
raw = read_raw_body()
id = header["webhook-id"]
ts = header["webhook-timestamp"]
sig_header = header["webhook-signature"]   # may contain multiple (v1,<b64>)

base = id + "." + ts + "." + raw
calc = base64(hmac_sha256(secret, base))

# Accept if one v1 signature in the header matches calc (constant-time comparison)
# Reject if |now - ts| > tolerance window (replay protection)
# Parse JSON after successful verification
```

---

## Responses, Retries, and Error Handling

- **Success:** `200 OK` or `204 No Content` – message received
- **Client Error (4xx):** considered permanent; DPS will not retry
- **Server Error (5xx):** DPS will retry with exponential backoff (up to 5 days total)
- **Timeout:** considered an error, and DPS will retry with exponential backoff (up to 5 days total)
- **Deduplication:** Use `webhook-id` as an idempotency key

---

## Troubleshooting

### Common Issues

1. **Timeout:** Ensure the endpoint responds within the deadline
2. **Certificate Errors:** The TLS certificate must be valid and correctly configured
3. **Signature Errors:** Check that HMAC verification is implemented correctly
4. **Duplicates:** Implement deduplication based on `webhook-id`

---

## Configuration and Support

At this stage, the registration of the webhook URL and shared secret key is **handled manually by the National Library**.  
We coordinate setup and testing before production use.

For questions about webhook setup or if you experience issues, contact the digital preservation team at the National Library.

We can assist with:

- Testing the webhook endpoint
- Providing fixed IP addresses for allowlisting
- Troubleshooting delivery issues

---

## Summary

| Property       | Value                                                 |
|----------------|-------------------------------------------------------|
| Transport      | HTTPS                                                 |
| Method         | POST                                                  |
| Content Type   | `application/json`                                    |
| Standard       | [Standard Webhooks](https://www.standardwebhooks.com) |
| Authentication | HMAC signature (`webhook-signature`)                  |
| Response       | `200 OK` within 10 seconds                            |
| Retries        | Yes (exponential backoff, up to 5 days total)         |
| Configuration  | Handled manually by NB                                |



[^1]: Standard Webhooks: [https://www.standardwebhooks.com](https://www.standardwebhooks.com)