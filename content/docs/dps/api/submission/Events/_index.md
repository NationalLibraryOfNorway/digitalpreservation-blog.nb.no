---
title: Events/preservation metadata
weight: 2
draft: false
---



In digital preservation, an “event” documents an action or occurrence that has affected a digital object, such as creation, migration, validation, or transfer. Events are considered important preservation metadata, as they provide traceability and evidence of what has been done to the object throughout its entire lifecycle.

The event and agent model used here is based on the [PREMIS data model](https://www.loc.gov/standards/premis/) for preservation metadata.

Providing events is not mandatory, but we recommend doing so whenever such information is available. Events submitted through the API are preserved in the same way as events recorded internally within the preservation environment (DPS). This makes it easier to get an overview of all events associated with an object when it is delivered.

Preservation metadata can be provided in two ways: through the API or as files included in the Submission Information Package (SIP). We recommend submitting preservation metadata through the API. Events submitted through the API are also accessible via the API, while metadata provided as files in the SIP are preserved as part of the package. If practical or technical constraints prevent you from submitting metadata through the API, we still recommend including it in the SIP rather than leaving it out. The SIP may also contain other types of preservation metadata than those described on this page. See more under [metadata primer](/docs/dps/sip/metadata/) and [requirements for SIP structure](/docs/dps/sip/structure-requirements/). Information relating directly to provenance may be included under [metadata](/docs/dps/api/submission/metadata/).



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

# Use of event elements


**The following elements are permitted:**

**Agent (`agent`):**\*
- **agentName**\*
- **agentType**\*
- **agentVersion**
- **agentNote**

**Event (top level):**
- **eventDateTime**\*
- **eventType**\*
- **eventDetail**
- **fileRef** (with **relativePath**\* when `fileRef` is used)
- **outcome**\*
- **outcomeDetail**

Elements marked with \* are required.

## How to use Event Elements:

## Agent:
The Agent describes the actor (who or what) that performed the action. This may be software, an organization, or a person. The information should be sufficiently precise to identify which actor and configuration was used.


### AgentName
The name of the actor that performed the action. The name must be unique and used consistently.

**Examples:**
- "Apache NiFi"
- "Nasjonalbiblioteket – Team Digital Preservation"
- "Ola Nordmann"
- "JHOVE"


### AgentType
Specifies the type of actor that performed the action. Values are taken from the [Library of Congress vocabulary for agentType](https://id.loc.gov/vocabulary/preservation/agentType.html).

**Allowed values:**
- "software"
- "organization"
- "person"
- "hardware"



### AgentVersion
The version or revision of the agent. This field is **only** relevant for software and hardware agents. AgentVersion is used to ensure traceability and reproducibility, as different versions of the same tool may produce different results.

**Examples:**
- "1.15.0"
- "3.2"
- "1.11.0; DROID_SignatureFile_V116.xml; container-signature-20231127.xml"



### AgentNote
Additional information about the agent that performed the action. This element documents characteristics, context, or configuration of the agent itself — not what the agent did in a specific event.

**This may include:**
- What the agent is and what it does in general.
- How the agent is configured or installed.
- Operational context or responsibility.
  
**Examples:**
- "File format identification tool using PRONOM signatures. Installed with signature set v95 for PDF, TIFF, JPEG, and XML formats." 
- "Dataflow automation tool that enables the design and management of complex data pipelines." 
- "Custom installation with PDF, TIFF and JPEG modules enabled. Running under Java 17 runtime environment."
- "Institution with formal responsibility for digital preservation, ingest, and long-term management of archival materials."

> [!NOTE]
> Use consistent wording in agentNote when describing the same agent.



## Event:
The Event describes the action performed on the object.


### EventDateTime
The date and time when the event occurred. Must be expressed according to the ISO 8601 standard, including time zone.

**Example:**
- "2026-02-23T10:45:00+01:00"



### EventType
Specifies the type of action performed. This element describes the kind of process the event represents.
The value must be a controlled and consistently used term — see list of allowed event types below.



### EventDetail
A precise description of what was done in the event. The description should indicate which operation was performed, on which object, and where applicable, which method, standard, or process was used.

**Examples:**
- "MD5 checksum generated." 
- "Migrated from TIFF to JPEG2000."
- "Validated against PDF/A-2b standard."


### Outcome
The overall result of the event. This element indicates whether the event was completed as expected, failed, or was completed with deviations. The value should be used consistently for equivalent events. Values are taken from the [Library of Congress vocabulary for eventOutcome](https://id.loc.gov/vocabulary/preservation/eventOutcome.html).

**Allowed values:**
- "success" – the event succeeded in having its intended result.
- "warning" – a warning was generated by the event, indicating that it needs to be evaluated. This also includes partial success, for example a validation reporting a breach of a SHOULD requirement.
- "fail" – the event did not succeed in producing the intended result.


### OutcomeDetail

This element is only used when additional information about the outcome needs to be documented. In many cases, it is sufficient to use the "Outcome"-element (success, warning, fail).
"OutcomeDetail" is a concrete and precise description of the result of the event.
This field should be used when the result contains information relevant for further use, control, or documentation.
This element documents what was actually achieved or which deviations were identified. The description should be concise and clear.

**Examples:**
- "Identified as fmt/353 (TIFF 6.0)."
- "The package was validated against the profiles E-ARK-SIP-v2-2-0, NB-SIP-STRUCTURE-1.0, and NB-SIP-MOVINGIMAGES-PROFILE-1.0, resulting in one warning: CSIPSTR13 the representation folder primary_20250325 is missing the metadata subfolder (SHOULD requirement). Processing continued."


# Event-types

The National Library bases its work on the [Library of Congress](https://www.loc.gov/) list of [EventTypes](https://id.loc.gov/vocabulary/preservation/eventType.html). This list has been narrowed down, and the use of the different types has been specified to suit our needs and preservation environments. Event types other than those specified in the list below are not approved in the API.


## EventTypes


### Capture

| Name 	        | **capture** 	                                                                                                                                                                                  |
|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description 	 | The process whereby an agent (organization, team, role, system, service, or automated process) actively acquires an object through mechanisms other than transfer from the creator or donor. Retrieval of existing digital data. |
| Scope	        | IE, File 	                                                                                                                                                                                     |


**Guidelines for use:**
- Used for capture of websites during crawling functions of a repository.

**Example:**
```json
{
  "agent": {
    "agentName": "Heritrix Web Crawler",
    "agentType": "software",
    "agentVersion": "3.5.0",
    "agentNote": "Used for web archiving to capture websites; HTML, images, scripts, and linked resources."
  },
  "eventDateTime": "2026-02-03T07:14:01.716+01:00",
  "eventType": "capture",
  "eventDetail": "Captured the website https://example.org; including all pages, images, PDFs, and linked resources, according to the scheduled web archiving crawl.",
  "outcome": "success",
  "outcomeDetail": "Total pages captured: 234; total data size: 1.2 GB; all URLs successfully archived in WARC format."
}



### Creation 


| Name         | **creation**                          |
|:-------------|:--------------------------------------|
| Description  | The process of creating a new object. A new file or digital object is created, for example through digitization. |
| Scope        | IE, File                              |


**Guidelines for use:**
- Used to document the creation of a digital object.
-	Used to document the origin of the file or Intellectual Entity, describes the method and process of creating the file/IE. See also eventType "imaging".


**Example:**
```json
{
  "agent": {
    "agentName": "Pyramix",
    "agentType": "software",
    "agentVersion": "15.0.8",
    "agentNote": "Software for recording, editing, mixing, and mastering audio."
  },
  "eventDateTime": "2026-02-03T08:02:17.304+01:00",
  "eventType": "creation",
  "eventDetail": "Digitization of a physical carrier, 1/4-inch audio tape, to WAV/BWF using Pyramix and an A/D converter. Recording performed in real time from an analog source via an external converter. Verified recording quality.",
  "outcome": "success"
}
```


### Filename change 


| Name        | **filename change**              |
|:------------|:---------------------------------|
| Description | The process of modifying a filename. |
| Scope       | File                             |


**Guidelines for use:**
-	Used when changing the filename of a digitally created file.
- Documents a complete or partial change to the original filename, for example to remove prohibited characters or spaces, comply with the current filename standard, or correct errors in the filename.

**Example:**
```json
{
  "agent": {
    "agentName": "Apache NiFi",
    "agentType": "software",
    "agentVersion": "2.4.0",
    "agentNote": "Dataflow automation tool that enables the design and management of complex data pipelines."
  },
  "eventDateTime": "2026-02-03T10:47:29.332+01:00",
  "eventType": "filename change",
  "eventDetail": "The filename was changed from NN_TR_2011_01_31_18_40.mp4 to NRK_TR_2011_01_31_18_40.mp4 to comply with the current filename standard. The filename prefix indicates the radio channel from which the file originates. The original prefix, NN, was incorrect and was replaced with NRK.",
  "fileRef": {
    "relativePath": "representations/primary_20250325/data/NRK_TR_2011_01_31_18_40.mp4"
  },
  "outcome": "success"
}
```


 ### Fixity check 


 | Name 	        | **fixity check** 	                                                               |
|:--------------|:---------------------------------------------------------------------------------|
| Description 	 | The process of verifying that an object has not been altered by checking its checksum(s).	 |
| Scope 	       | IE, File 	                                                                       |


**Guidelines for use:**
-	Used to verify that a digital object has not been altered by checking and comparing its checksum against a previously recorded checksum.
- The event should be associated with the IE whenever possible. It should only be associated with an individual file when deviations need to be documented.
- Will most likely contain the results of the "message digest calculation" event.
- Particularly important when checksums are received from external sources.


**Example:**
```json
{
  "agent": {
    "agentName": "md5sum (GNU coreutils)",
    "agentType": "software",
    "agentVersion": "8.32",
    "agentNote": "Tool used to calculate and verify checksums to control data integrity over time."
  },
  "eventDateTime": "2026-02-03T12:05:48.210+01:00",
  "eventType": "fixity check",
  "eventDetail": "MD5 checksums were verified against previously registered values for all files in the package.",
  "outcome": "success"
}
```


 ### Imaging 


 | Name 	        | **imaging** 	                                                                |
|:--------------|:-----------------------------------------------------------------------------|
| Description 	 | The process of extracting a disk image from a physical information carrier.	 |
| Scope 	       | IE 	                                                                         |


**Guidelines for use:**
-	Used to document the process of creating an exact digital copy (disk image) of a storage medium, including all files, metadata, file system structure, and sometimes also free space and deleted data.
-	As a general rule, this event should be used instead of the creation event, rather than in addition to it. However, in some cases, it may be relevant to use both events.

**Example:**

```json
{
  "agent": {
    "agentName": "GNU ddrescue",
    "agentType": "software",
    "agentVersion": "1.27",
    "agentNote": "Tool used to create bit-for-bit disk images from physical storage media."
  },
  "eventDateTime": "2026-02-03T09:00:00+01:00",
  "eventType": "imaging",
  "eventDetail": "Created a bit-for-bit disk image from an external hard drive. The disk image includes the file system structure and associated metadata from the original media.",
  "outcome": "success"
}
```

### Information package creation

 | Name 	        | **information package creation** 	                                         |
|:--------------|:-----------------------------------------------------------------------------|
| Description 	 | The process of generating an Information Package (SIP, AIP or DIP).	 |
| Scope 	       | IE 	                                                                         |

**Guidelines for use:**
- Used when a SIP, AIP or DIP is created as a new information package, including the establishment of package structure, metadata, and associated files in accordance with the applicable packaging standard (e.g. E-ARK). 
- Should not be used for simple copying or transfer of existing packages without changes to package structure or metadata.
- If the SIP Generator developed by the National Library is used without modification, use the agent from the first example.

**Example:**

```json
{
  "agent": {
    "agentName": "nifi-nb-eark-nar.EarkSIPGenerator",
    "agentType": "software",
    "agentVersion": "1.0.11",
    "agentNote": "Apache NiFi processor developed by the National Library for creating E-ARK SIPs. Uses commons-ip, a Java library for the creation and management of E-ARK information packages."
  },
  "eventDateTime": "2026-02-03T16:42:15+01:00",
  "eventType": "information package creation",
  "eventDetail": "Created a SIP in accordance with the National Library's Profile SIP 1.0.",
  "outcome": "success"
}
```

```json
{
  "agent": {
    "agentName": "org.roda-community:commons-ip2",
    "agentType": "software",
    "agentVersion": "2.12.0",
    "agentNote": "Java library for the creation and management of E-ARK information packages."
  },
  "eventDateTime": "2026-02-03T16:58:03+01:00",
  "eventType": "information package creation",
  "eventDetail": "Creation of an E-ARK SIP in accordance with the E-ARK Common Specification (CSIP) V.2.2.0, E-ARK SIP V.2.2.0, and the National Library of Norway specifications SIP 1.0 (E-ARK).",
  "outcome": "success"
}
```


### Message digest calculation 


 | Name 	        | **message digest calculation** 	                            |
|:--------------|:------------------------------------------------------------|
| Description 	 | The process by which a message digest ("hash") is created.	 |
| Scope 	       | IE, File	                                                   |


**Guidelines for use:**
-	Used when generating new checksums. If checksums are generated locally, there is no need to use the "fixity check" event in addition to the "message digest calculation" event. See also EventType "fixity check".
- The "fixity check" event documents the verification of checksum(s).
- The event should be associated with the IE whenever possible. If deviations need to be documented, they should be associated with the relevant file.


**Example:**
```json
{
  "agent": {
    "agentName": "md5sum (GNU coreutils)",
    "agentType": "software",
    "agentVersion": "8.32",
    "agentNote": "Tool used to calculate and verify checksums to control data integrity over time."
  },
  "eventDateTime": "2026-02-03T13:36:42.455+01:00",
  "eventType": "message digest calculation",
  "eventDetail": "Calculated MD5 checksum for all the files in the package.",
  "outcome": "success"
}
```


### Metadata extraction 


| Name        | **metadata extraction**                                                                             |
|:------------|:----------------------------------------------------------------------------------------------------|
| Description | Extraction of metadata from an object. This includes technical, administrative and descriptive metadata. |
| Scope       | File                                                                                                |


**Guidelines for use:**
- Used when metadata is extracted from a file.
- The derived metadata must reference the source file in `"fileRef"`. 
- If the extraction results in one or more metadata files, `"outcomeDetail"` must include a reference (relative file path) to the extracted/generated metadata file(s).


**Examples:**

Example of metadata extraction documented in outcomeDetail:

```json
{
  "agent": {
    "agentName": "ExifTool",
    "agentType": "software",
    "agentVersion": "12.60",
    "agentNote": "Extracts technical metadata from files."
  },
  "eventDateTime": "2026-02-19T11:45:32.123+01:00",
  "eventType": "metadata extraction",
  "eventDetail": "Extracted technical metadata from image file.",
  "fileRef": {
    "relativePath": "representations/rep-images_20230908/data/DSC_0456.JPG"
  },
  "outcome": "success",
  "outcomeDetail": "Image: format JPEG, resolution 8256x5504 pixels, 24-bit color; Camera: Nikon D850; Lens: 24-70mm f/2.8; Exposure: 1/125 sec at f/8; ISO: 100; File size: 18.2 MB."
}
```

Example of metadata extraction stored as a separate file: 

```json
{
  "agent": {
    "agentName": "Audioinspector",
    "agentType": "software",
    "agentVersion": "5.5",
    "agentNote": "A software tool for automated analysis, quality assessment, and metadata management of audio files."
  },
  "eventDateTime": "2026-02-11T12:01:08Z",
  "eventType": "metadata extraction",
  "eventDetail": "The WAV file was analyzed for quality control and documentation.",
  "fileRef": {
    "relativePath": "representations/primary_20250325/data/something.wav"
  },
  "outcome": "success",
  "outcomeDetail": "An XML metadata file was created, containing detailed analysis results: representations/primary_20250325/metadata/technical/audioinspector/metadata.xml"
}
```


### Migration


| Name        | **migration**                               |
|:------------|:--------------------------------------------|
| Description | Conversion to a new file format.            |
| Scope       | IE, File                                    |


**Guidelines for use:**

- Used when one or more files are converted to a different file format.
- The event should be associated with the Intellectual Entity (IE) whenever possible, for example, if the files have been converted in the same way to the same format. 
-	Migration events should always create a new file(s) or package. 
- Relevant parameters describing the migration process should be documented in `eventDetail`.
- The migrated file(s) must reference the source file in `fileRef` when single files are migrated (when the event is not associated with IE).
-  `outcomeDetail` must include a reference (relative file path) to the migrated file(s).


**Example:**
```json
{
  "agent": {
    "agentName": "FFmpeg",
    "agentType": "software",
    "agentVersion": "6.0",
    "agentNote": "Media conversion and encoding of AV files."
  },
  "eventDateTime": "2026-02-03T15:09:55.774+01:00",
  "eventType": "migration",
  "eventDetail": "Batch migration of all MOV files in the package (25 files) to MXF/Op1a format with lossless JPEG2000 video codec and 24-bit PCM audio codec. Parameters used: command=ffmpeg -i input.mov -c:v jpeg2000 -pred dwt53 -c:a pcm_s24le output.mxf; container=MXF/Op1a; videoCodec=JPEG2000 (lossless, dwt53); audioCodec=PCM 24-bit; integrityChecked=yes",
  "outcome": "success",
  "outcomeDetail": "Resulting MXF files stored in representations/primary_20250325/data/."
}
```


### Transfer 


| Name        | **transfer**                                                                    |
|:------------|:--------------------------------------------------------------------------------|
| Description | The process of transferring metadata and/or digital object(s) between systems.  |
| Scope       | IE                                                                              |


**Guidelines for use:**
- Used for transfer of material between systems or organisational contexts, for example from a producer to a preservation system or between storage environments. Should not be used for internal workflows or internal processing steps.
- Do not use the transfer event for transfer of material into DPS (submission via API), the system automatically creates an event when the material is received.


**Example:**
```json
{
  "agent": {
    "agentName": "Apache NiFi",
    "agentType": "software",
    "agentVersion": "2.4.0",
    "agentNote": "Dataflow automation tool that enables the design and management of complex data pipelines."
  },
  "eventDateTime": "2026-02-18T14:02:33+01:00",
  "eventType": "transfer",
  "eventDetail": "Transferred package from preservation storage Oracle HSM (SAM-FS) to local workspace for further processing; source checksums were verified with md5sum (GNU coreutils) during upload.",
  "outcome": "success"
}
```


### Validation 


| Name        | **validation**                  |
|:------------|:--------------------------------|
| Description | Validation against a standard.  |
| Scope       | IE, File                        |


**Guidelines for use:**

- Used when a package or file is checked to verify that it complies with a specific standard, profile, specification, or other defined requirements.
-	The object being validated may be an individual file or an Intellectual Entity (IE). Whenever possible, the event should be associated with the IE, for example when multiple files are validated in the same way using the same tool, or when the structure of the package is validated as a whole. The event should also specify what the validation was performed against, such as a standard, profile, specification, or other defined requirements.
- It may be appropriate to create a single event covering the entire validation process, and instead describe which tools are used in the different steps, rather than creating multiple events for multiple validations.


**Examples:**
```json
{
  "agent": {
    "agentName": "JHOVE",
    "agentType": "software",
    "agentVersion": "1.32.1",
    "agentNote": "Tool used for identification, validation and characterisation of digital objects."
  },
  "eventDateTime": "2026-02-03T17:30:39.662+01:00",
  "eventType": "validation",
  "eventDetail": "Validated all PDF files in the package (35 files) using JHOVE to verify that they comply with the PDF 1.7 specifications.",
  "outcome": "success"
}
```
```json
{
  "agent": {
    "agentName": "Apache NiFi",
    "agentType": "software",
    "agentVersion": "2.4.0",
    "agentNote": "Dataflow automation tool that enables the design and management of complex data pipelines."
  },
  "eventDateTime": "2026-02-03T17:41:12.508+01:00",
  "eventType": "validation",
  "eventDetail": "Validated E-ARK SIP using DPS Validation workflow v.a00f683: nifi-nb-eark-nar.EarkSIPValidator 1.0.7; org.roda-community:commons-ip2 2.12.0. Validated against profiles E-ARK-SIP-v2-2-0, NB-SIP-STRUCTURE-1.0 and NB-SIP-MOVINGIMAGES-PROFILE-1.0.",
  "outcome": "success"
}
```

Example of a validation with deviations that did not stop processing:

```json
{
  "agent": {
    "agentName": "Apache NiFi",
    "agentType": "software",
    "agentVersion": "2.4.0",
    "agentNote": "Dataflow automation tool that enables the design and management of complex data pipelines."
  },
  "eventDateTime": "2026-02-03T17:48:05.219+01:00",
  "eventType": "validation",
  "eventDetail": "Validated E-ARK SIP using DPS Validation workflow v.a00f683: nifi-nb-eark-nar.EarkSIPValidator 1.0.7; org.roda-community:commons-ip2 2.12.0.",
  "outcome": "warning",
  "outcomeDetail": "Validated against profiles E-ARK-SIP-v2-2-0 and NB-SIP-STRUCTURE-1.0 with one warning: CSIPSTR13 – the representation folder primary_20250325 has no metadata subfolder (SHOULD requirement). Processing continued."
}
```


### Virus check 


 | Name	         | **virus check** 	                                        |
|:--------------|:---------------------------------------------------------|
| Description 	 | The process of scanning a file for malicious programs. 	 |
| Scope 	       | IE, File	                                                |


**Guidelines for use:**
-	The event should be linked to the IE where possible. Linked to the File only when it is necessary to document discrepancies.
- If a virus or other malicious software is found, `outcome` must be `fail`. Link the event to the affected file with `fileRef`, and describe the finding in `outcomeDetail`.
 

**Examples:**
```json
{
  "agent": {
    "agentName": "ClamAV",
    "agentType": "software",
    "agentVersion": "1.4.2",
    "agentNote": "Antivirus software used to detect malicious software. Virus signatures: daily.cvd, version 27890; main.cvd, version 12345."
  },
  "eventDateTime": "2026-02-03T18:27:53.842+01:00",
  "eventType": "virus check",
  "eventDetail": "All files in the package were scanned for viruses and other malicious software prior to further processing.",
  "outcome": "success"
}
```
```json
{
  "agent": {
    "agentName": "ClamAV",
    "agentType": "software",
    "agentVersion": "1.4.2",
    "agentNote": "Antivirus program used to detect malicious software."
  },
  "eventDateTime": "2026-02-03T08:51:40.127+01:00",
  "eventType": "virus check",
  "eventDetail": "The file was scanned for viruses and other malicious software prior to transfer.",
  "fileRef": {
    "relativePath": "representations/primary_20250325/data/file_2026.xml"
  },
  "outcome": "fail",
  "outcomeDetail": "Detected the signature Win.Trojan.MacroVirus-12345."
}
```



## Guidance for use of event types in different data flows

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






