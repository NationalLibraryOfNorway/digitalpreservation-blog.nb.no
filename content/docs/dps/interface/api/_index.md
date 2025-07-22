---
title: Submission Service API
weight: 1
---


## Overview

The Digital Preservation Submission Service provides a RESTful API for managing digital submissions and their associated files. This service allows clients to create submissions, register files, upload content, and track the status of submissions throughout the digital preservation workflow.

This documentation complements the detailed API reference available through Swagger UI at https://digitalpreservation.no/swagger/.

## Authentication & Authorization

The API uses OAuth 2.0 with JWT tokens for authentication, specifically implementing the OAuth 2.0 Client Credentials Flow.

### OAuth 2.0 Client Credentials Flow

1. Your client application authenticates with the authorization server using its client ID and client secret
2. The authorization server validates these credentials and returns an access token
3. Your application includes this access token in the Authorization header of all API requests

Example token request:
```http
POST /authn/realms/dps/protocol/openid-connect/token HTTP/1.1
Host: www.nb.no
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id={your_client_id}
&client_secret={your_client_secret}
```

Example API request with token:
```http
GET /dps-submission/v1/contracts/{your_contract_id}/submissions/{your_submission_id} HTTP/1.1
Host: api.nb.no
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Role-Based Authorization

Access to endpoints is controlled by role-based authorization:

- Contract-specific roles (`{contractId}_R`, `{contractId}_W`) provide read and write access to resources under a specific contract
- The `DPS_SUBMISSION_HANDLER` role is required for internal status management operations

Your client application must request the access token, and the issued JWT will then contain your assigned roles.

## Resource Models

### Submission

A submission represents a package of files and metadata to be preserved.

**Key properties:**
- `contractId`: Contract identifier in Base16 format (4 characters)
- `submissionId`: Unique identifier for the submission in Base62 format (22 characters). The ID is case-sensitive
- `clientId`: Identifier of the client uploading the submission, extracted from the JWT token
- `objectId`: Client-provided identifier for the object
- `status`: Current status of the submission
- `priority`: Priority of the submission, used for processing order in DPS
- `metadata`: Dublin Core-based [metadata](metadata/) for the submission
- `sumSizeInBytes`: Total size of all files in the submission in bytes

### File

A file represents an individual digital asset within a submission.

**Key properties:**
- `contractId`: Contract identifier in Base16 format (4 characters)
- `submissionId`: Unique identifier in Base62 format (22 characters). The ID is case-sensitive
- `fileId`: Unique identifier in Base62 format (22 characters)
- `filePath`: Relative path of the file within the submission
- `s3ObjectKey`: The S3 object key where the file is stored internally
- `checksum`: MD5 checksum of the file content
- `isPackaged`: Indicates if the file is packaged (e.g., in a ZIP/TAR archive) and should be extracted during processing
- `uploadUrl`: Pre-signed URL for direct file upload to our S3 compatible storage

**File Size Limitations:**
- Maximum file size: 5 GB per file
- This limitation is due to constraints with Amazon S3 pre-signed URLs used for direct file uploads

## Submission Workflow

The complete submission process follows these steps:

1. **Create a submission** with metadata
2. **Register files** to get pre-signed upload URLs
3. **Upload files** to the provided URLs
4. **Finalize the submission** to initiate preservation processing
5. Track the **submission status** as it progresses through the preservation system (at a later stage we will support status updates)


### Example API Usage

**Register a new submission**

Request:
```http
POST /dps-submission/v1/contracts/1234/submissions HTTP/1.1
Host: api.nb.no
Content-Type: application/json
Authorization: Bearer eyJhbGciOxxxxxxx

{
  "objectId": "digavis_aabcc",
  "priority": 50,
  "metadata": {
    "type": "Artikkel",
    "identifier": [
      {
        "type": "URN",
        "value": "URN:NBN:no-nb_plfut_00001"
      }
    ],
    "title": {
      "value": "My Book Title",
      "lang": "eng"
    },
    "alternative": [
      {
        "type": "Original tittle",
        "value": "My Alternative Book Title",
        "lang": "eng"
      }
    ],
    "creator": [
      {
        "name": "Marek, Václav",
        "type": "Person",
        "role": "Fotograf",
        "authority": {
          "source": "Example authority",
          "code": "198097",
          "uri": "https://example.com/198097"
        }
      }
    ],
    "contributor": [
      {
        "name": "Nordmann, Ola",
        "type": "Person",
        "role": "Avbildet",
        "authority": {
          "source": "Example authority",
          "code": "198097",
          "uri": "https://example.com/198097"
        }
      }
    ],
    "publisher": [
      {
        "name": "Gyldendal",
        "type": "Organization",
        "authority": {
          "source": "Example authority",
          "code": "198097",
          "uri": "https://example.com/198097"
        }
      }
    ],
    "spatial": [
      {
        "name": "Mo i Rana",
        "type": "Place",
        "authority": {
          "source": "Example authority",
          "code": "198097",
          "uri": "https://example.com/198097"
        },
        "coordinateReferenceSystem": "EPSG:4326",
        "latitude": 67.2968,
        "longitude": 14.3974
      }
    ],
    "date": [
      {
        "type": "created",
        "value": "2023-10-27"
      }
    ],
    "language": [
      {
        "type": "Subtitles",
        "value": "Swedish",
        "lang": "eng"
      }
    ],
    "isPartOf": [
      {
        "value": "Chronicles of Narnia",
        "lang": "eng"
      }
    ],
    "provenance": [
      {
        "value": "The collection was donated to the National Library by Václav Marek 1979-05-12",
        "lang": "eng"
      }
    ],
    "subject": [
      {
        "lang": "nob",
        "value": "Norge"
      }
    ],
    "description": [
      {
        "lang": "nob",
        "value": "Norge"
      }
    ]
  }
}
```

Response:
```json
{
  "contractId": "1234",
  "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
  "objectId": "digavis_aabcc",
  "clientId": "myClientId",
  "status": "REGISTERED",
  "priority": 50
}
```

**Register a file for upload**

Request:
```http
POST /dps-submission/v1/contracts/1234/submissions/8Z7x1T9rN0Xc2B5Yq4L3zP/files HTTP/1.1
Host: api.nb.no
Content-Type: application/json
Authorization: Bearer eyJhbGciOxxxxxxx

{
  "filePath": "representations/primary_20250217/data/ranablad_20250215.pdf",
  "checksum": "d41d8cd98f00b204e9800998ecf8427e",
  "isPackaged": false
}
```

Response:
```json
{
  "fileId": "1M0x4T9rN8Xc7B2Yq5L3zK",
  "filePath": "representations/primary_20250217/data/ranablad_20250215.pdf",
  "checksum": "d41d8cd98f00b204e9800998ecf8427e",
  "isPackaged": false,  
  "uploadUrl": "https://.../upload/42?token=..."
}
```

**Finalize the submission after upload**

Request:
```http
POST /dps-submission/v1/contracts/1234/submissions/8Z7x1T9rN0Xc2B5Yq4L3zP/finalize HTTP/1.1
Host: api.nb.no
Authorization: Bearer eyJhbGciOxxxxxxx
```

Response:
```json
{
  "contractId": "1234",
  "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
  "objectId": "digavis_aabcc",
  "clientId": "myClientId",
  "status": "REGISTERED",
  "priority": 50,
  "sumSizeInBytes": 12345678,
  "files": [
    {
      "fileId": "1M0x4T9rN8Xc7B2Yq5L3zK",
      "filePath": "representations/primary_20250217/data/ranablad_20250215.pdf",
      "s3ObjectKey": "myClientId/1234/8Z7x1T9rN0Xc2B5Yq4L3zP/representations/primary_20250217/data/ranablad_20250215.pdf",
      "checksum": "d41d8cd98f00b204e9800998ecf8427e",
      "isPackaged": false,
      "uploadUrl": "https://.../upload/42?token=..."
    }
  ]
}
```




## File Upload Process

The file upload process in the Digital Preservation Submission Service follows these steps:

1. **Register a file** by making a POST request to `/contracts/{contractId}/submissions/{submissionId}/files` with file metadata
2. **Receive a pre-signed URL** in the response, which is valid for a limited time (typically 1 hour)
3. **Upload the file content** directly to our S3 compatible storage using the pre-signed URL with an HTTP PUT request

### Pre-signed URL Usage

The pre-signed URL allows for secure direct uploads to S3 without requiring credentials:

```http
PUT {pre-signed-url} HTTP/1.1
Content-Length: {file-size}

[FILE CONTENT]
```

### Upload Requirements
- The file must be uploaded using the pre-signed URL provided during registration
- The file content must generate the same MD5 checksum provided during registration

### Handling Upload Failures

If an upload fails or times out:
1. You can retry the upload using the same pre-signed URL if it hasn't expired
2. If the URL has expired, you must delete the file registration and register it again to get a new URL

## Status Lifecycle

A submission progresses through the following statuses:

1. `REGISTERED` - Initial state when a submission is created
2. `UPLOAD_COMPLETED` - All files have been uploaded and the submission has been finalized
3. `TRANSFERRING` - The submission is being transferred from S3 Storage to the preservation system
4. `VALIDATING` - The submission is being validated for integrity and completeness
5. `ARCHIVING` - The submission is being archived in the preservation system
6. `PRESERVED` - The submission has been successfully preserved
7. `REJECTED` - The submission has been rejected due to validation errors or other issues

## Best Practices

1. **Always verify checksums** before uploading files to ensure data integrity
2. **Use unique objectIds** within each contract to avoid conflicts
3. **Include comprehensive metadata** to enhance discoverability and preservation
4. **Implement proper error handling** in your client application

## Support

For API support, please contact the Digital Preservation team.

## API Reference

For complete API details including endpoints, parameters, request/response schemas, and status codes, please refer to the [Swagger documentation](https://digitalpreservation.no/swagger/).
