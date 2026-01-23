---
title: Submission Service
weight: 1
---

## Overview

The Submission Service API allows clients to submit digital objects for long-term preservation. For general information on authentication and authorization, please refer to the main [API documentation](../).

This documentation complements the detailed API reference available through Swagger UI at https://digitalpreservation.no/swagger/.

For general information on authentication and authorization, please refer to the main [API documentation](../).

**File Size Limitations:**
- Maximum file size: 5 GB per file
- This limitation is due to constraints with S3 pre-signed URLs used for direct file uploads

## Workflow

The complete submission process follows these steps:

1. **Create a submission** with metadata
2. **Register files** to get pre-signed upload URLs
3. **Upload files** to the provided URLs
4. **Finalize the submission** to initiate preservation processing
5. Track the **submission status** as it progresses through the preservation system (at a later stage we will support status updates)


## Example API Usage

### Register a new submission

`POST /v1/contracts/{contractId}/submissions`

**Request**
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
        "type": "Original title",
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

**Response (201 Created)**

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

### Register a file for upload

The `isPackaged` field indicates whether files are packaged temporarily for transmission purposes only. These files are packed to facilitate transfer and will be unpacked by the preservation flow.

**Request**
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

**Response**
```json
{
  "fileId": "1M0x4T9rN8Xc7B2Yq5L3zK",
  "filePath": "representations/primary_20250217/data/ranablad_20250215.pdf",
  "s3ObjectKey": "bucket/myClientId/1234/8Z7x1T9rN0Xc2B5Yq4L3zP/representations/primary_20250217/data/ranablad_20250215.pdf",
  "checksum": "d41d8cd98f00b204e9800998ecf8427e",
  "isPackaged": false,
  "uploadUrl": "https://s3.nb.no/examplebucket/...&X-Amz-Signature=..."
}
```

### Finalize the submission after upload

**Request**
```http
POST /dps-submission/v1/contracts/1234/submissions/8Z7x1T9rN0Xc2B5Yq4L3zP/finalize HTTP/1.1
Host: api.nb.no
Authorization: Bearer eyJhbGciOxxxxxxx
```

**Response**
```json
{
  "contractId": "1234",
  "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
  "objectId": "digavis_aabcc",
  "clientId": "myClientId",
  "status": "UPLOAD_COMPLETED",
  "priority": 50,
  "sumSizeInBytes": 12345678,
  "files": [
    {
      "fileId": "1M0x4T9rN8Xc7B2Yq5L3zK",
      "filePath": "representations/primary_20250217/data/ranablad_20250215.pdf",
      "s3ObjectKey": "myClientId/1234/8Z7x1T9rN0Xc2B5Yq4L3zP/representations/primary_20250217/data/ranablad_20250215.pdf",
      "checksum": "d41d8cd98f00b204e9800998ecf8427e",
      "isPackaged": false,
      "uploadUrl": "https://s3.nb.no/examplebucket/...&X-Amz-Signature=..."
    }
  ]
}
```

## File Upload

The upload process follows these steps:

1. **Register a file** by sending a POST request to `/contracts/{contractId}/submissions/{submissionId}/files`
2. **Retrieve the pre-signed URL** from the response. The field is called `uploadUrl`, and it is valid for approximately 1 hour.
3. **Upload the file content** directly to S3 using HTTP PUT to the specified URL.

### Uploading a file using a pre-signed URL

```http
PUT {uploadUrl} HTTP/1.1
Content-Length: {file-size-in-bytes}

[FILE CONTENT]
```

{{% details title="Alternative upload for large files (files over 5 GiB)" closed="true" %}}

> [!NOTE]
> This functionality is primarily intended for internal use at the National Library, especially for large files, as pre-signed URLs only support files up to 5 GiB in size. Access to the S3 bucket used by the National Library for digital preservation can be obtained by contacting the Platform team.

The upload process follows these steps:
1. **Register a file** by sending a POST request to `/contracts/{contractId}/submissions/{submissionId}/files`
2. **Retrieve the s3ObjectKey** from the response
3. **Upload the file content** directly to S3 using the s3ObjectKey as the object key

We recommend using the AWS CLI for the upload. Documentation can be found here: https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html

Here is an example of how you can do this:
```shell
s3 cp path/to/my_big_movie_file.mov s3://examplebucket/clientId/contract/submissionId/path/to/my_big_movie_file.mov --endpoint-url=https://s3.nb.no
```

{{% /details %}}

### Upload Requirements
- The file must be uploaded via the provided pre-signed URL
- The file content must have the same MD5 checksum as specified during registration

### Handling Upload Failures

If an upload fails or times out:
1. You can retry the upload using the same pre-signed URL if it hasn't expired
2. If the URL has expired, delete the file registration and register it again to get a new URL

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
