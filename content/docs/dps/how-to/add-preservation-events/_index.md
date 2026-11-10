---
title: Add preservation events to a submission
linkTitle: Add preservation events
weight: 2
---

This guide shows how to choose which events to document for your workflow, and how to submit them through the API as part of a submission. For what events are and why they matter, see [Preservation events](/docs/dps/understanding/metadata-management/preservation-events/). For the meaning and allowed values of each element, see the [preservation events reference](/docs/dps/reference/preservation-events/).

## Before you start

- You need a submission with the status `REGISTERED`. See [Submit content for preservation](/docs/dps/how-to/submit-content/).
- Events can only be submitted before the submission is finalized. Submit all events first, then finalize.

## Event types you can submit

The API accepts the following values for `eventType`. Requests with other values are rejected. The [preservation events reference](/docs/dps/reference/preservation-events/) describes each type with guidelines and examples. It also covers event types that DPS records itself, which cannot be submitted. The [Swagger documentation](/swagger/) is the authoritative source for the values the API accepts.

- [`capture`](/docs/dps/reference/preservation-events/#capture)
- [`creation`](/docs/dps/reference/preservation-events/#creation)
- [`filename change`](/docs/dps/reference/preservation-events/#filename-change)
- [`fixity check`](/docs/dps/reference/preservation-events/#fixity-check)
- [`imaging`](/docs/dps/reference/preservation-events/#imaging)
- [`information package creation`](/docs/dps/reference/preservation-events/#information-package-creation)
- [`message digest calculation`](/docs/dps/reference/preservation-events/#message-digest-calculation)
- [`metadata extraction`](/docs/dps/reference/preservation-events/#metadata-extraction)
- [`migration`](/docs/dps/reference/preservation-events/#migration)
- [`transfer`](/docs/dps/reference/preservation-events/#transfer)
- [`validation`](/docs/dps/reference/preservation-events/#validation)
- [`virus check`](/docs/dps/reference/preservation-events/#virus-check)

## Choose which events to document

This guidance is based on the National Library's internal workflows and may not cover all types of preservation processes. Feedback on improvements, clarifications, and additional use cases is welcome.


### Digitization of physical sources

**Minimum:**

- **Creation or Imaging (use one of these):** Documents when the file(s) are actually created.<br>
**Creation** is used when digital files are created through digitization or production processes, such as document scanning, audio digitization, or transfer of video content from an analog source.<br>
**Imaging** is used when a complete disk image (bit-for-bit copy) of a physical storage medium is created, such as a hard drive, floppy disk, CD, or memory card. Imaging captures the entire medium, including the file system structure, metadata, unallocated space, and any deleted data. 
- **Message Digest Calculation:** Creation of checksums. It is generally not necessary to document checksum verification immediately after the checksums have been generated. Verification before transfer to the next stage is recommended, but no separate event needs to be recorded for this activity. 
- **Information Package Creation:** Creation of a SIP. Document the applicable packaging standard (e.g., E-ARK). 


**May Be Relevant:**

- **Validation:** Validation of file quality and/or format against a specified standard. 
- **Metadata Extraction:** Extraction of technical, administrative, and/or descriptive metadata from files. The extracted information should either be documented in "outcomeDetail" or result in a new file that is included in the preservation package. 


### Born-Digital Material

**Minimum:**

- **Transfer:** Transfer from the producer/depositor to an internal processing workflow or staging area.
- **Message Digest Calculation or Fixity Check:** If files are delivered with checksums, these must be verified. If no checksums are provided, checksums must be generated.
- **Information Package Creation:** Creation of a SIP. Document the applicable packaging standard (e.g., E-ARK).

**May Be Relevant:**

- **Virus Check:** Create a single event covering all files in the package. Any issues or anomalies should be documented at the file level.
- **Validation:** Validation of file quality and/or format against a specified standard.
- **Metadata Extraction:** Extraction of technical, administrative, and/or descriptive metadata from files. The extracted information should either be documented in "outcomeDetail" or result in a new file that is included in the preservation package.
- **Filename Change:** If file names are changed after receipt of the files.
- **Migration:** If file formats are changed.


### Transfer of Material from a previous Storage System to the DPS

**Minimum:**

- **Transfer:** Transfer from the previous storage system.
- **Fixity Check or Message Digest Calculation:** Verification of existing checksums. If the material does not include checksums, new checksums must be generated.
- **Information Package Creation:** Creation of a SIP. Document the applicable packaging standard (e.g., E-ARK). This event is only relevant when preservation packages are modified.

Note: A single Transfer event may include checksum verification as part of the transfer process, for example: transfer from system X to system Y with checksum verification performed during transfer.


**May Be Relevant:**

- **Creation:** If the creation of the files has not already been documented and the relevant information is available. 
- **Filename Change:** If file names are changed after transfer from the previous storage system.
- **Migration:** If file formats are changed.


### Web Harvesting (Web Archive)

**Minimum:**

- **Capture:** The actual web harvesting or crawl process.
- **Creation:** If new files are created as part of the harvesting process, for example WARC files.
- **Message Digest Calculation:** Generation of checksums. It is generally not necessary to document checksum verification immediately after the checksums have been generated. Verification before transfer to the next stage is recommended, but no separate event needs to be recorded for this activity.
- **Information Package Creation:** Creation of a SIP. Document the applicable packaging standard (e.g., E-ARK).


**May Be Relevant:**

- **Validation:** Validation of file quality and/or format against a specified standard.
- **Virus Check:** Create a single event covering all files in the package. Any issues or anomalies should be documented at the file level.
- **Metadata Extraction:** Extraction of technical, administrative, and/or descriptive metadata from files. The extracted information should either be documented in "outcomeDetail" or result in a new file that is included in the preservation package.

## Linking events to an object

Events are submitted via the API:

`POST /v1/contracts/{contractId}/submissions/{submissionId}/events`

An event is always linked to a submission, which represents an Intellectual Entity (IE).

Events can only be submitted while the submission has the status `REGISTERED`, that is, before the submission is finalized. A successful request returns `204 No Content`. The field `isUserInitiated` is set to `true` automatically for events submitted through the API and does not need to be included.

Submitted events can be retrieved with `GET /v1/contracts/{contractId}/submissions/{submissionId}/events`.

### Level and reference to file

Events are always linked to a submission (IE). They can apply to the entire information package (IE level) or to a specific file (file level).

This is controlled by `fileRef`:

- Without `fileRef` → the event applies to the entire information package (IE)
- With `fileRef` → the event applies to a specific file

`fileRef` identifies the file using `relativePath`:

- The reference is based on the file's relative path within the information package
- `fileId` is generated internally in DPS and must not be provided in the API call
- Only one `fileRef` can be specified per event

**Example (file level):**

```json
{
  "fileRef": {
    "relativePath": "representations/rep-images/data/DSC_0456.JPG"
  }
}
```

In this example, the event applies to the file `DSC_0456.JPG` in the representation `rep-images`.

## JSON payload structure

An event is submitted as a single JSON object. The fields describing the action itself and its result are at the top level. The actor that performed the action is described in the `agent` object.

`fileRef` is optional and is only used when the event applies to a specific file. If `fileRef` is not specified, the event applies to the entire information package (IE level).

**Simplified structure:**

```json
{
  "agent": {
    "agentName": "...",
    "agentType": "...",
    "agentVersion": "...",
    "agentNote": "..."
  },
  "eventDateTime": "...",
  "eventType": "...",
  "eventDetail": "...",
  "fileRef": {
    "relativePath": "..."
  },
  "outcome": "...",
  "outcomeDetail": "..."
}
```

Events can be registered at both package level and file level. As a general rule, events should be linked to the package level, the Intellectual Entity (IE), where possible. This is to avoid large numbers of events that essentially convey the same information. It is possible to associate events with individual files when there is a need to document file-level actions. The most important consideration is to be deliberate about what is documented, why it is documented, and at which level.

For Norwegian submitters it is recommended that events are written in Norwegian whenever possible. In general the events should be formulated with future management and use in mind, so that the information remains as clear and verifiable as possible over time.

For technical documentation of submissions in API and event formatting see: [Swagger DPS Submission Service API](https://digitalpreservation.no/swagger/)

The machine-readable OpenAPI specification (JSON) is available at <https://api.nb.no/dps-submission/v1/api-docs>. Events are described by the `SubmitEventDto` schema.
