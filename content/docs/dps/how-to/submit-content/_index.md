---
title: Submit content for preservation
weight: 2
aliases:
  - /docs/dps/api/submission/
---

This guide shows how to submit content to DPS through the API: from a prepared Submission Information Package (SIP) to a preserved object. Field names, limits, and status codes are listed in the [submissions reference](/docs/dps/reference/api/#submissions).

## Before you start

- **Client credentials and an access token.** See [Authentication & Authorization](/docs/dps/reference/api/#authentication--authorization).
- **A contract ID (`contractId`)** for the agreement you submit under, and a producer role for that contract.
- **Content prepared as a SIP.** See [Prepare content for submission](/docs/dps/how-to/prepare-content/).

## Steps

{{% steps %}}

### Prepare the SIP

Package the content as a SIP, with an MD5 checksum for every file. See [Prepare content for submission](/docs/dps/how-to/prepare-content/). The files you register in the next steps are the files of the SIP, and their paths in the API mirror the package structure.

### Create a submission

A submission represents one information package. Create it with your identifier for the object (`objectId`) and the descriptive metadata. See [Metadata Requirements](/docs/dps/reference/descriptive-metadata/) for the metadata elements.

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
        "type": "person",
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
        "type": "person",
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
        "type": "korporasjon",
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
        "value": "swe"
      }
    ],
    "relation": [
      {
        "title": "Chronicles of Narnia",
        "lang": "eng",
        "type": "isPartOf"
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

Keep the `submissionId` from the response. You need it in the next steps.

### Register each file

Register every file in the SIP with its path in the package and its checksum. The response contains a pre-signed `uploadUrl` for the file.

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
  "s3ObjectKey": "examplebucket/myClientId/1234/8Z7x1T9rN0Xc2B5Yq4L3zP/representations/primary_20250217/data/ranablad_20250215.pdf",
  "checksum": "d41d8cd98f00b204e9800998ecf8427e",
  "isPackaged": false,
  "uploadUrl": "https://s3.nb.no/examplebucket/...&X-Amz-Signature=..."
}
```

### Upload the files

Upload the content of each file with HTTP PUT to its `uploadUrl`. The URL is valid for approximately one hour, and the content must have the same MD5 checksum as you registered.

```http
PUT {uploadUrl} HTTP/1.1
Content-Length: {file-size-in-bytes}

[FILE CONTENT]
```

If an upload fails or times out:

- Retry with the same `uploadUrl` if it has not expired.
- If it has expired, delete the file registration (`DELETE /v1/contracts/{contractId}/submissions/{submissionId}/files/{fileId}`) and register the file again to get a new URL.

{{% details title="Alternative upload for large files (files over 5 GiB)" closed="true" %}}

> [!NOTE]
> This functionality is primarily intended for internal use at the National Library, especially for large files, as pre-signed URLs only support files up to 5 GiB in size. Access to the S3 bucket used by the National Library for digital preservation can be obtained by contacting the Platform team.

The upload process follows these steps:
1. **Register a file** by sending a POST request to `/contracts/{contractId}/submissions/{submissionId}/files`
2. **Retrieve the s3ObjectKey** from the response
3. **Upload the file content** directly to S3, using `s3://{s3ObjectKey}` as the destination. The `s3ObjectKey` starts with the bucket name, followed by the object key.

We recommend using the AWS CLI for the upload. Documentation can be found here: https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html

Here is an example of how you can do this:
```shell
s3 cp path/to/my_big_movie_file.mov s3://examplebucket/clientId/contract/submissionId/path/to/my_big_movie_file.mov --endpoint-url=https://s3.nb.no
```

{{% /details %}}

### Add preservation events (optional)

If you have documented preservation events before submission, such as digitization or validation, add them now. Events can only be added before the submission is finalized. See [Add preservation events](/docs/dps/how-to/add-preservation-events/).

### Finalize the submission

When all files have been uploaded, finalize the submission. This starts the transfer to DPS, and no more files or events can be added.

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
      "s3ObjectKey": "examplebucket/myClientId/1234/8Z7x1T9rN0Xc2B5Yq4L3zP/representations/primary_20250217/data/ranablad_20250215.pdf",
      "checksum": "d41d8cd98f00b204e9800998ecf8427e",
      "isPackaged": false,
      "uploadUrl": "https://s3.nb.no/examplebucket/...&X-Amz-Signature=..."
    }
  ]
}
```

### Follow the status

The submission now moves through `PROCESSING` to either `PRESERVED` or `REJECTED`. Follow it by [receiving notifications](/docs/dps/how-to/receive-notifications/) or by fetching the submission. A `200 OK` from `finalize` only confirms that the upload is complete: the content of the files is validated after the transfer to DPS. When the submission is preserved, keep the `archiveId` from the `submission.preserved` message. It is the material's persistent identifier in DPS.

{{% /steps %}}

## Important information

1. **Always verify checksums before uploading.**
Verify that the files have the expected checksum before uploading them to DPS. The checksum confirms that the files are intact and have not been modified since the checksum was calculated.

2. **Perform thorough quality checks before submission.**
Once a submission has been verified and assigned the status `PRESERVED`, it cannot easily be deleted or withdrawn. It is therefore important to carefully review the material and ensure that the content, files, and metadata are accurate before the package is sent to the DPS.

3. **Use unique `objectId` values per contract and retain them.**
`objectId` is the link between the source system and DPS. It is returned in API responses and webhook events, allowing you to identify which object an event relates to. `objectId` cannot be changed.

4. **Provide rich metadata.**
High-quality and complete metadata improves searchability and helps ensure that the material can be identified and understood over time.

5. **Keep the `submissionId` and `archiveId`.**
- Keep the `submissionId` until you have received the `submission.preserved` message. The `submissionId` is used to look up the submission and for any necessary error handling or corrections.

- A `200 OK` response from `finalize` confirms that the upload has been completed. However, it does not mean that the SIP has been validated against the requirements for digital preservation. The API performs as much validation as possible before transfer, but validation of the file contents takes place only after the package has been transferred to DPS. If validation fails, you will receive a `submission.rejected` message.

- Keep the `archiveId`. This is the material's unique and persistent identifier in DPS.
  
6. **Do not delete the source material until you have received the `submission.preserved message`.**
`submission.preserved` confirms that the material has been preserved in DPS and has undergone the necessary validation and verification. Do not delete the source material until this message has been received.

## Support

For API support, please contact the Digital Preservation team.
