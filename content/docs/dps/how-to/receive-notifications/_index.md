---
title: Receive notifications
weight: 4
aliases:
  - /docs/dps/api/webhooks/
---

DPS can send notifications directly to your systems via webhooks when submissions or disseminations change status, so you do not have to poll the API. This guide shows how to set up an endpoint that receives and verifies these messages. The headers, message structure, and the fields of each message are listed in the [API reference](/docs/dps/reference/api/#webhooks).

When an event occurs in DPS:

1. DPS sends an **HTTP POST** request to the URL you have provided
2. The message contains information about the event in **JSON format**, according to *Standard Webhooks*[^1]
3. Your system receives the message, validates that it comes from DPS, and responds with **HTTP 200 OK**

## Before you start

- **An HTTPS endpoint** that DPS can reach, with a valid TLS certificate (TLS 1.2 or higher).
- **Contact with the digital preservation team.** The National Library currently registers all webhook endpoints manually in collaboration with each partner.

## Steps

{{% steps %}}

### Set up an endpoint

You must expose a publicly accessible URL that accepts HTTPS POST requests with JSON data, for example:

```http
https://partner.example.com/api/dps/webhook
```

**Recommendations:**

- Use an IP allowlist (we can provide fixed outgoing IPs if needed)
- Set up monitoring and alerting to ensure your service is operational
- Validate the signature for each message before processing

### Register the endpoint with the National Library

At this stage, the registration of the webhook URL and shared secret key is **handled manually by the National Library**. We coordinate setup and testing before production use. Contact the digital preservation team to register your endpoint.

### Verify the signature

The webhooks are signed to ensure authenticity and integrity. The receiver must validate the signature before processing the message. The signature is calculated from the `webhook-id` and `webhook-timestamp` headers and the raw request body.

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

>  **Tip:** Always verify the signature against the raw **request body**, not a re-serialized JSON structure.

### Respond to the message

The webhook receiver must:

- Respond with **HTTP 200 OK** or **204 No Content** within 10 seconds
- Return no or minimal body (DPS only cares about the status code)
- For 4xx/5xx or timeout, DPS will retry with exponential backoff

Because DPS retries, the same message can arrive more than once. Use `webhook-id` as a deduplication key.

### Handle the message

Use the `type` field to decide what to do:

- **`submission.preserved`:** the content is preserved. Store the `archiveId`; you need it to request the content later. You can now delete the source material.
- **`submission.rejected`:** the submission was rejected. The `reasons` list tells you what went wrong, and `filePath` points to the file when an error applies to a single file.
- **`dissemination.delivered`:** requested content is ready. Download the files before the links expire. See [Request preserved content](/docs/dps/how-to/retrieve-content/).

The fields of each message are listed under [Webhook events](/docs/dps/reference/api/#webhook-events).

{{% /steps %}}

## Troubleshooting

1. **Timeout:** Ensure the endpoint responds within the deadline
2. **Certificate Errors:** The TLS certificate must be valid and correctly configured
3. **Signature Errors:** Check that HMAC verification is implemented correctly
4. **Duplicates:** Implement deduplication based on `webhook-id`

## Support

For questions about webhook setup or if you experience issues, contact the digital preservation team at the National Library.

We can assist with:

- Testing the webhook endpoint
- Providing fixed IP addresses for allowlisting
- Troubleshooting delivery issues

[^1]: Standard Webhooks: [https://www.standardwebhooks.com](https://www.standardwebhooks.com)
