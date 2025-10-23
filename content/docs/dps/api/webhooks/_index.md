---
title: Webhooks
weight: 3
---

## Overview

The National Library of Norway can send status updates directly to your systems via webhooks. This allows you to receive automatic notifications about status changes in submissions and disseminations without having to continuously poll our API.

This documentation describes how you as a partner can set up HTTP endpoints (webhooks) that we will call to deliver status messages.

**Purpose:**

- Notify about status changes in submissions
- Notify about completed disseminations
- Ensure secure and predictable delivery with clear contracts

## Technical Requirements

### Transport and Format

- **Protocol:** HTTPS (TLS 1.2+)
- **Method:** POST
- **Format:** JSON (`Content-Type: application/json; charset=utf-8`)
- **Authentication:** Bearer token (OAuth2 Client Credentials or static), or Basic auth over HTTPS
- **Response time:** Must respond within 5 seconds during normal operation
- **Certificate:** Must have valid TLS certificate

### Endpoint Setup

You must expose a publicly accessible URL, for example:

```http
POST https://partner.example.com/webhooks/status
```

**Recommendations:**

- Use IP allowlist (we can provide fixed outgoing IP addresses if needed)
- Implement logging for debugging
- Set up monitoring and alerting

## Message Format

### Headers

Each webhook request includes special headers:

```http
webhook-id: 74ea5da5-df40-47e9-9d44-4040b0c292fc
webhook-timestamp: 1757458468973
```

**Field descriptions:**

- `webhook-id`: Unique message ID that doesn't change on retry
- `webhook-timestamp`: Unix timestamp in milliseconds for when the message was sent

### Message Structure

All messages follow the same basic structure:

```json
{
  "type": "submission.preserved",
  "timestamp": "2025-08-26T14:39:53.344522+02:00",
  "data": {
    "contractId": "ef23",
    "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
    "archiveId": "68b803fb25d74833747835f7"
  }
}
```

**Field descriptions:**

- `type` (string): Event type (see [Event Types](#event-types))
- `timestamp` (string): ISO 8601 timestamp with timezone for status change
- `data` (object): Event-specific data

**Future compatibility:**
We may add new, non-required fields. Your endpoint should ignore unknown fields to remain compatible with future versions.

## Event Types

### Submission Events

The following event types are sent for submissions:

- `submission.validating` - Submission is being validated
- `submission.queued` - Submission queued for processing
- `submission.processing` - Archive object being processed by DPS
- `submission.archiving` - Archive object being sent to storage
- `submission.preserved` - Archive object verified and preserved
- `submission.rejected` - Error during validation, archive object rejected

**Example submission message:**

```json
{
  "type": "submission.preserved",
  "timestamp": "2025-08-26T14:39:53.344522+02:00",
  "data": {
    "contractId": "ef23",
    "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
    "archiveId": "68b803fb25d74833747835f7"
  }
}
```

### Dissemination Events

For disseminations, the following event type is sent:

- `dissemination.delivered` - Dissemination is ready for download

**Example dissemination message:**

```json
{
  "type": "dissemination.delivered",
  "timestamp": "2025-10-15T12:18:42.315+02:00",
  "data": {
    "archiveId": "68ee1917e2768fd730076661",
    "disseminationId": "0pS8bYb6KmJoRvBtZ3Qxd1",
    "objectId": "5280df44-d34e-4195-ac6f-ee96fe0e01d4",
    "clientId": "client-id",
    "contractId": "ef23",
    "sumSizeInBytes": 215040,
    "files": [
      {
        "downloadURL": "https://s3.nb.no/bucket/0pS8bYb6KmJoRvBtZ3Qxd1/68ee1917e2768fd730076661/metadata.tar",
        "filename": "metadata.tar",
        "filesize": 163840,
        "expirationDate": "2025-10-16T12:18:41.919934218+02:00",
        "checksum": "43943b08cbfc1748abe7b30e2ffc9963",
        "checksumAlgorithm": "MD5"
      },
      {
        "downloadURL": "https://s3.nb.no/bucket/0pS8bYb6KmJoRvBtZ3Qxd1/68ee1917e2768fd730076661/primary_20251014.tar",
        "filename": "primary_20251014.tar",
        "filesize": 51200,
        "expirationDate": "2025-10-16T12:18:41.934462292+02:00",
        "checksum": "ae393a24d6e5c0f4e0bc6d544be56570",
        "checksumAlgorithm": "MD5"
      }
    ]
  }
}
```

We can agree on which event types should send notifications based on your needs.

## Authentication

### Bearer Token (recommended)

We support two types of Bearer token authentication:

#### OAuth2 Client Credentials

1. We send POST request to your token endpoint with `grant_type=client_credentials`
2. We receive an `access_token` (JWT or opaque)
3. For each webhook call we send the header:

   ```http
   Authorization: Bearer <access_token>
   ```

4. We automatically refresh tokens upon expiry. On 401 Unauthorized we fetch a new token and retry.

#### Static API Token

You can issue a long, random API token that we send in the header:

```http
Authorization: Bearer <API_token>
```

### Basic Authentication

Alternatively, you can require HTTP Basic over HTTPS:

```http
Authorization: Basic <base64(username:password)>
```

**Important:** Basic auth is only used over secure TLS connection.

### Additional Measures

- **IP allowlist:** You can restrict traffic to our outgoing IP addresses
- **Rate limiting:** Implement protection against too many requests

## Response Requirements

Your endpoint must respond with appropriate HTTP status codes:

### Success

- `200 OK` or `204 No Content` – Message received and stored/processing started

### Client Errors (4xx)

- `401 Unauthorized` – Invalid authentication
- `403 Forbidden` – Missing access
- `404 Not Found` – Endpoint not found
- `422 Unprocessable Entity` – Invalid message format

### Server Errors (5xx)

- `500 Internal Server Error` – Temporary error on your side
- `502 Bad Gateway` – Gateway error
- `503 Service Unavailable` – Service unavailable

**Important:** On 4xx errors we consider the message permanently failed and don't retry. On 5xx errors we implement retry logic.

Response body is optional and ignored.

## Idempotency and Re-delivery

### Duplicate Handling

- We may send the same message multiple times due to network errors or other issues
- Use `webhook-id` from the header as deduplication key
- Implement idempotent processing (no side effects on repeated processing)

### Retry Strategy

On non-success (non-2xx status) we retry with exponential backoff:

**Backoff sequence:**
30s → 1m → 2m → 4m → 8m → 16m → 32m → 1h → 2h → 4h → 8h → 16h → then daily

**Maximum duration:** 5 days total retry period

After maximum time window the event is marked as undelivered. We may optionally send a manual report about failed deliveries.

## Implementation Example

Here's a simple example of how you can implement a webhook endpoint:

```python
from flask import Flask, request, jsonify
import hashlib
import hmac

app = Flask(__name__)

# Storage for duplicate checking (use database in production)
processed_webhooks = set()

@app.route('/webhooks/status', methods=['POST'])
def handle_webhook():
    # Get webhook ID for duplicate checking
    webhook_id = request.headers.get('webhook-id')
    
    if webhook_id in processed_webhooks:
        # Already processed - return success without action
        return '', 204
    
    # Validate authentication
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return {'error': 'Missing or invalid authorization'}, 401
    
    try:
        # Parse JSON content
        data = request.get_json()
        
        # Process message based on type
        if data['type'] == 'submission.preserved':
            handle_submission_preserved(data)
        elif data['type'] == 'dissemination.delivered':
            handle_dissemination_delivered(data)
        else:
            # Unknown type - ignore for future compatibility
            print(f"Unknown webhook type: {data['type']}")
        
        # Mark as processed
        processed_webhooks.add(webhook_id)
        
        return '', 200
        
    except Exception as e:
        # Log error
        print(f"Error processing webhook: {e}")
        return {'error': 'Internal server error'}, 500

def handle_submission_preserved(data):
    # Your logic for submission events
    submission_id = data['data']['submissionId']
    print(f"Submission {submission_id} is now preserved!")

def handle_dissemination_delivered(data):
    # Your logic for dissemination events
    dissemination_id = data['data']['disseminationId']
    print(f"Dissemination {dissemination_id} is ready for download!")
```

## Troubleshooting

### Common Issues

1. **Timeout errors:** Ensure endpoint responds within 5 seconds
2. **Certificate errors:** Verify TLS certificate is valid and properly configured
3. **Authentication errors:** Check that Bearer token or Basic auth is correctly implemented
4. **Duplicates:** Implement deduplication based on `webhook-id`

## Support

For questions about webhook setup or problems with deliveries, contact the digital preservation team at the National Library of Norway.

We can also help with:

- Testing your webhook endpoint
- Provide fixed IP addresses for allowlisting
- Troubleshooting delivery issues
