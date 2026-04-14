---
title: Events/preservation metadata
weight: 2
draft: false
---

> ⚠️ **These pages is under construction** ⚠️


In digital preservation, an “event” documents an action or occurrence that has affected a digital object, such as creation, migration, validation, or transfer. Events are considered important preservation metadata, as they provide traceability and evidence of what has been done to the object throughout its entire lifecycle.

The event and agent model used here is based on the [PREMIS data model](https://www.loc.gov/standards/premis/) for preservation metadata.

Submitting events is not mandatory, but we recommend doing so when such information is available. Events added through the API will be preserved in a dedicated event database, just like events that occur within the preservation environment (DPS). When disseminated, this provides a clearer overview of all events associated with an object.

Preservation metadata can also be submitted as files in the information package (SIP). The difference is that events registered via the API are stored in a searchable event database, whereas files in the SIP are preserved as part of the package without becoming searchable in the same way. We therefore prefer that preservation metadata is submitted via the API. If this is not possible for practical or technical reasons, it is still better to include the information in the SIP than to leave it out. See more under [metadata primer](/docs/dps/sip/1.0/metadata/) and [requirements for SIP structure](/docs/dps/sip/1.0/structure-requirements/). Information relating directly to provenance may be included under [metadata](/docs/dps/api/submission/metadata/).

## Linking events to an object

Events are submitted via the API:

`POST /v1/contracts/{contractId}/submissions/{submissionId}/events`

An event is always linked to a submission, which represents an Intellectual Entity (IE).

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
  "event": {
    "fileRef": {
      "relativePath": "representations/rep-images/data/DSC_0456.JPG"
    }
  }
}
```

In this example, the event applies to the file `DSC_0456.JPG` in the representation `rep-images`.

## JSON payload structure

An event is submitted as a JSON structure with two main elements:

- `agent` – describes the actor that performed the action
- `event` – describes the action itself and its result

`fileRef` is optional and is only used when the event applies to a specific file. If `fileRef` is not specified, the event applies to the entire information package (IE level).

**Simplified structure:**

```json
{
  "agent": {
    "agentName": "...",
    "agentType": "...",
    "agentVersion": "...",
    "agentNotes": "..."
  },
  "event": {
    "eventDateTime": "...",
    "eventType": "...",
    "eventDetail": "...",
    "fileRef": {
      "relativePath": "..."
    },
    "outcome": "...",
    "outcomeDetail": "..."
  }
}
```

Events can be registered at both package level and file level. As a general rule, events should be linked to the package level, the Intellectual Entity (IE), where possible. This is to avoid large numbers of events that essentially convey the same information. It is possible to associate events with individual files when there is a need to document file-level actions. The most important consideration is to be deliberate about what is documented, why it is documented, and at which level.

For norwegian submitters it is recommended that events are written in Norwegian whenever possible. In general the events should be formulated with future management and use in mind, so that the information remains as clear and verifiable as possible over time.

For technical documentation of submissions in API and event foramatting see: [Swagger DPS Submission Service API](https://digitalpreservation.no/swagger/)

# Use of event elements


**The following elements are permitted:**

**Agent:**\*
- **agentName**\*
- **agentType**\*
- **agentVersion**
- **agentNotes**

**Event:**\*
- **eventDateTime**\*
- **eventType**\*
- **eventDetail**
- **outcome**\*
- **outcomeDetail**

Elements marked with \* are required.

## How to use Event Elements:

## Agent:
The Agent describes the actor that performed the action. This may be software, an organization, or a person. The information should be sufficiently precise to identify which actor and configuration was used.


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
The version number of the agent if it is software. AgentVersion is used to ensure traceability and reproducibility, as different versions of the same tool may produce different results.

**Examples:**
- "1.15.0"
- "3.2"
- "1.11.0; DROID_SignatureFile_V116.xml; container-signature-20231127.xml"



### AgentNotes
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
> AgentNotes should be used as consistently as possible for the same agent. Minor variations in wording should be avoided, as this may result in the same agent being registered multiple times.



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
The overall result of the event. This element indicates whether the event was completed as expected, failed, or was completed with deviations. The value should be used consistently for equivalent events.

**Allowed values:**
- "success"
- "failure"
- "warning"


### OutcomeDetail
A concrete and precise description of the result of the event.
This field should be used when the result contains information relevant for further use, control, or documentation.
This element documents what was actually achieved or which deviations were identified. The description should be concise and clear.

**Examples:**
- "Identified as fmt/353 (TIFF 6.0)."
- "Validated against profile E-ARK-SIP-v2-2-0, NB-SIP-STRUCTURE-1.0 and NB-SIP-MOVINGIMAGES-PROFILE-1.0."


# Event-types

The National Library bases its work on the [Library of Congress](https://www.loc.gov/) list of [EventTypes](https://id.loc.gov/vocabulary/preservation/eventType.html). This list has been narrowed down, and the use of the different types has been specified to suit our needs and preservation environments. Event types other than those specified in the list below are not approved in the API.


## EventTypes


### Capture

| Name 	        | **capture** 	                                                                                                                                                                                  |
|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description 	 | The process whereby an agent (organization, team, role, system, service, or automated process) actively acquires an object through mechanisms other than transfer from the creator or donor. 	 |
| Scope	        | IE, File 	                                                                                                                                                                                     |


**Guidelines for use:**
- Used for capture of websites during crawling functions of a repository.

**Examples:**
```json
{
  "agent": {
    "agentName": "Heritrix Web Crawler",
    "agentType": "software",
    "agentVersion": "3.5.0",
    "agentNotes": "Used for web archiving to capture websites; HTML, images, scripts, and linked resources."
  },
  "event": {
    "eventDateTime": "2026-02-03T07:14:01.716+01:00",
    "eventType": "capture",
    "eventDetail": "Captured the website https://example.no; including all pages, images, PDFs, and linked resources, according to the scheduled web archiving crawl.",
    "outcome": "success",
    "outcomeDetail": "Total pages captured: 234; total data size: 1.2 GB; all URLs successfully archived in WARC format."
  }
}
```


### Creation 


| Name         | **creation**                          |
|:-------------|:--------------------------------------|
| Description  | The process of creating a new object. |
| Scope        | File                                  |


**Guidelines for use:**
- Used to document the creation of a digital object.
-	Used to document the origin of the file or Intellectual Entity, describes the method and process of creating the file/IE. See also eventType "imaging".


**Examples:**
```json
{
  "agent": {
    "agentName": "Pyramix",
    "agentType": "software",
    "agentVersion": "15.0.8",
    "agentNotes": "Software for recording, editing, mixing, and mastering audio."
  },
  "event": {
    "eventDateTime": "2026-02-03T07:14:01.716+01:00",
    "eventType": "creation",
    "eventDetail": "Digital representation created through digitisation.",
    "outcome": "success"
  }
}
```


### Filename change 


| Name        | **filename change**              |
|:------------|:---------------------------------|
| Description | The process of modifying a filename. |
| Scope       | File                             |


**Guidelines for use:**
-	Relevant when changing name of a born digital file, or e.g when renaming a file to comply with the constraints of the storage system.
-	Either a removal of prohibited character or a partial or entire replacement of the original filename. This can be used to note changes such as removing characters, or where a system removes the filename entirely and replaces it with a system generated name.


**Examples:**
```json
{
  "agent": {
    "agentName": "Apache NiFi",
    "agentType": "software",
    "agentVersion": "2.4.0",
    "agentNotes": "Dataflow automation tool."
  },
  "event": {
    "eventDateTime": "2026-02-03T10:47:29.332+01:00",
    "eventType": "filename change",
    "eventDetail": "The filename was changed to conform to current file naming convention.",
    "fileRef": {
      "relativePath": "representations/rep-text_20230219/data/document_001.pdf"
    },
    "outcome": "success",
    "outcomeDetail": "Filename changed from NN_TR_2011_01_31_18_40.mp4 to NRK_TR_2011_01_31_18_40.mp4."
  }
}
```


 ### Fixity check 


 | Name 	        | **fixity check** 	                                                               |
|:--------------|:---------------------------------------------------------------------------------|
| Description 	 | The process of verifying that an object has not been changed in a given period.	 |
| Scope 	       | IE, File 	                                                                       |


**Guidelines for use:**
-	The event should be linked to the IE where possible. Linked to the File only when it is necessary to document discrepancies.
-	This will most likely utilize the results of the "message digest calculation" event.
- This is particularly important when checksums are received from external sources. 


**Examples:**
```json
{
  "agent": {
    "agentName": "md5sum (GNU coreutils)",
    "agentType": "software",
    "agentVersion": "8.32",
    "agentNotes": "Tool used to calculate and verify checksums to control data integrity over time."
  },
  "event": {
    "eventDateTime": "2026-02-03T12:05:48.210+01:00",
    "eventType": "fixity check",
    "eventDetail": "MD5 checksums were verified against previously registered values for all files in the package.",
    "outcome": "success"
  }
}
```


 ### Imaging 


 | Name 	        | **imaging** 	                                                                |
|:--------------|:-----------------------------------------------------------------------------|
| Description 	 | The process of extracting a disk image from a physical information carrier.	 |
| Scope 	       | IE 	                                                                         |


**Guidelines for use:**
-	Used to document the process of creating an exact digital copy (disk image) of a storage medium, including all files, metadata, file system structure, and sometimes also free space and deleted data.
-	When applicable, this event should be used instead of, not in addition to, the “creation” event. 

**Examples:**

```json
{
  "agent": {
    "agentName": "dd",
    "agentType": "software",
    "agentVersion": "1.0",
    "agentNotes": "Tool for creating bit-for-bit copies of storage media."
  },
  "event": {
    "eventDateTime": "2026-02-03T09:00:00+01:00",
    "eventType": "imaging",
    "eventDetail": "Created disk image from physical medium.",
    "outcome": "success"
  }
}
```

### Message digest calculation 


 | Name 	        | **message digest calculation** 	                            |
|:--------------|:------------------------------------------------------------|
| Description 	 | The process by which a message digest ("hash") is created.	 |
| Scope 	       | IE, File	                                                   |


**Guidelines for use:**
-	The event should be linked to the IE where possible. Linked to the File only when it is necessary to document discrepancies.
-	Message digest is also commonly referred to as a "checksum". The event "fixity check" checks the message digest.
- Used when generating new checksums. Where checksums are generated locally, there is no need to use the "fixity check" event in addition to the ‘message digest calculation’ event. See also EventType "fixity check".


**Examples:**
```json
{
  "agent": {
    "agentName": "md5sum (GNU coreutils)",
    "agentType": "software",
    "agentVersion": "8.32",
    "agentNotes": "Tool used to calculate checksums for verification of data integrity."
  },
  "event": {
    "eventDateTime": "2026-02-03T13:36:42.455+01:00",
    "eventType": "message digest calculation",
    "eventDetail": "Calculated MD5 checksum for all the files in the package.",
    "outcome": "success"
  }
}
```


### Metadata extraction 


| Name        | **metadata extraction**                                                                             |
|:------------|:----------------------------------------------------------------------------------------------------|
| Description | Extraction of metadata from an object. This includes technical, administrative and descriptive metadata. |
| Scope       | File                                                                                                |


**Guidelines for use:**
 - Used when metadata is extracted from a file, resulting in one or more metadata files.
- The derived file(s) must reference the source file. 


**Examples:**
```json
{
  "agent": {
    "agentName": "ExifTool",
    "agentType": "software",
    "agentVersion": "12.60",
    "agentNotes": "Extracts technical metadata from files."
  },
  "event": {
    "eventDateTime": "2026-02-19T11:45:32.123+01:00",
    "eventType": "metadata extraction",
    "eventDetail": "Extracted technical metadata from image file.",
    "fileRef": {
      "relativePath": "representations/rep-images_20230908/data/DSC_0456.JPG"
    },
    "outcome": "success",
    "outcomeDetail": "Image: format JPEG, resolution 6000x4000 pixels, 24-bit color; Camera: Nikon D850; Lens: 24-70mm f/2.8; Exposure: 1/125 sec at f/8; ISO: 100; File size: 18.2 MB."
  }
}
```
```json
{
  "agent": {
    "agentName": "Audioinspector",
    "agentType": "software",
    "agentVersion": "5.5",
    "agentNotes": "A software tool for automated analysis, quality assessment, and metadata management of audio files."
  },
  "event": {
    "eventDateTime": "2026-02-11T12:01:08Z",
    "eventType": "metadata extraction",
    "eventDetail": "Wav-files were analyzed for quality control and documentation.",
    "fileRef": {
      "relativePath": "representations/primary_20250325/data/something.wav"
    },
    "outcome": "success",
    "outcomeDetail": "An XML metadata file was created, containing detailed analysis results."
  }
}
```


### Migration


| Name        | **migration**                               |
|:------------|:--------------------------------------------|
| Description | Conversion to a new file format.            |
| Scope       | IE, File                                    |


**Guidelines for use:**
- The event should be associated with the Intellectual Entity (IE) whenever possible, for example, if the files have been converted in the same way to the same format. 
-	Migration events should always create a new package or file. 
- The migrated file(s) must reference the source file. 


**Examples:**
```json
{
  "agent": {
    "agentName": "FFmpeg",
    "agentType": "software",
    "agentVersion": "6.0",
    "agentNotes": "Media conversion and encoding of AV files."
  },
  "event": {
    "eventDateTime": "2026-02-03T15:09:55.774+01:00",
    "eventType": "migration",
    "eventDetail": "Converted MOV files to MXF/Op1a format with JPEG2000 video codec and PCM audio codec. Parameters used: command=ffmpeg -i input.mov -c:v jpeg2000 -c:a pcm_s16le output.mxf; container=MXF/Op1a; videoCodec=JPEG2000; audioCodec=PCM; integrityChecked=yes",
    "outcome": "success"
  }
}
```


### Transfer 


| Name        | **transfer**                                                                    |
|:------------|:--------------------------------------------------------------------------------|
| Description | The process of transferring metadata and/or digital object(s) between systems.  |
| Scope       | IE                                                                              |


**Guidelines for use:**
-	Used for transferring objects into or out of the preservation area or temporary working areas.


**Examples:**
```json
{
  "agent": {
    "agentName": "Apache NiFi",
    "agentType": "software",
    "agentVersion": "2.2.0",
    "agentNotes": "Dataflow automation tool that enables the design and management of complex data pipelines."
  },
  "event": {
    "eventDateTime": "2026-02-18T14:02:33+01:00",
    "eventType": "transfer",
    "eventDetail": "Transferred package from Oracle HSM(SAM-FS) to local workspace for further processing; Upload was performed with source checksums verified with md5sum (GNU coreutils); Generated E-ARK SIP with commons-ip2 2.12.0.",
    "outcome": "success"
  }
}
```


### Validation 


| Name        | **validation**                  |
|:------------|:--------------------------------|
| Description | Validation against a standard.  |
| Scope       | IE, File                        |


**Guidelines for use:**
-	The object being validated may be a file or an Intellectual Entity. The event should be linked to the IE whenever possible, for example when the files are validated in the same way using the same tool, or when the structure is validated for the entire informationpackage.
- It may be appropriate to create a single event covering the entire validation process, and instead describe which tools are used in the different steps, rather than creating multiple events for multiple validations.


**Examples:**
```json
{
  "agent": {
    "agentName": "JHOVE",
    "agentType": "software",
    "agentVersion": "1.32.1",
    "agentNotes": "Tool used for identification, validation and characterisation of digital objects."
  },
  "event": {
    "eventDateTime": "2026-02-03T17:30:39.662+01:00",
    "eventType": "validation",
    "eventDetail": "Validated that files comply with the specifications of the applicable file format.",
    "outcome": "success"
  }
}
```
```json
{
  "agent": {
    "agentName": "Apache NiFi",
    "agentType": "software",
    "agentVersion": "2.4.0",
    "agentNotes": "Dataflow automation tool that enables the design and management of complex data pipelines."
  },
  "event": {
    "eventDateTime": "2026-02-03T17:30:39.662+01:00",
    "eventType": "validation",
    "eventDetail": "Validated E-ARK SIP using DPS Validation workflow v.a00f683: nifi-nb-eark-nar,EarkSIPValidator 1.0.7; org.roda-community,commons-ip2 2.12.0.",
    "outcome": "success",
    "outcomeDetail": "Validated against profiles E-ARK-SIP-v2-2-0, NB-SIP-STRUCTURE-1.0 and NB-SIP-MOVINGIMAGES-PROFILE-1.0."
  }
}
```


### Virus check 


 | Name	         | **virus check** 	                                        |
|:--------------|:---------------------------------------------------------|
| Description 	 | The process of scanning a file for malicious programs. 	 |
| Scope 	       | IE, File	                                                |


**Guidelines for use:**
-	The event should be linked to the IE where possible. Linked to the File only when it is necessary to document discrepancies.
 

**Examples:**
```json
{
  "agent": {
    "agentName": "ClamAV",
    "agentType": "software",
    "agentVersion": "1.8.7",
    "agentNotes": "Antivirus program used to detect malicious software."
  },
  "event": {
    "eventDateTime": "2026-02-03T18:27:53.842+01:00",
    "eventType": "virus check",
    "eventDetail": "All files in the package were scanned for viruses and other malicious software prior to further processing.",
    "outcome": "success"
  }
}
```
```json
{
  "agent": {
    "agentName": "ClamAV",
    "agentType": "software",
    "agentVersion": "1.8.7",
    "agentNotes": "Opensource antivirus program designed to detect malicious software. Virus definitions were updated immediately before execution."
  },
  "event": {
    "eventDateTime": "2026-02-03T07:14:01.716+01:00",
    "eventType": "virus check",
    "eventDetail": "All files in the package were scanned using ClamAV prior to transfer. Recursive scan covered 1,245 files.",
    "outcome": "success",
    "outcomeDetail": "Presence of the signature Win.Trojan.MacroVirus-12345 in file_2026.xml was detected."
  }
}
```