---
title: Application Programming Interface
weight: 1
---


## Overview

The Digital Preservation services at the National Library of Norway provide a RESTful API for managing the submission and dissemination of digital objects. This allows clients to integrate their systems with our preservation workflows.

This documentation provides a high-level overview of the available APIs. For complete technical details, please refer to our [Swagger UI](https://digitalpreservation.no/swagger/).

The following services are available:
- [**Submission Service API**](submission/): For submitting digital objects for preservation.
- [**Dissemination Service API**](dissemination/): For requesting preserved digital objects.
- [**Webhooks**](webhooks/): For receiving automatic status updates in your systems.

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


When an error occurs, the API returns a JSON response with an `error` object containing:
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "A descriptive error message",
    "details": "Additional details about the error"
  }
}
```


## Support

For API support, please contact the Digital Preservation team.

## API Reference

For complete API details including endpoints, parameters, request/response schemas, and status codes, please refer to the [Swagger documentation](https://digitalpreservation.no/swagger/).
