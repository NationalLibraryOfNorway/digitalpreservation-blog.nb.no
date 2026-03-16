---
title: Event-types
weight: 2
draft: true
---



The National Library bases its work on the [Library of Congress](https://www.loc.gov/) list of [EventTypes](https://id.loc.gov/vocabulary/preservation/eventType.html). This list has been narrowed down, and the use of the different types has been specified to suit our needs and preservation environments. Event types other than those specified in the list below are not approved in the API.


## EventTypes


### Capture

| Name 	| **capture** 	|
|:---	|:---	|
| Description 	| The process whereby an agent (organization, team, role, system, service, or automated process) actively acquires an object through mechanisms other than transfer from the creator or donor. 	|
| Scope	| IE, File 	|


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


 | Name 	| **creation** 	|
|:---	|:---	|
| Description	| The process of creating a new object. 	|
| Scope 	| File 	|


**Guidelines for use:**
- Used to document the digital object within an information package. 
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
            "eventDetail": "A digital representation of the physical material was created by means of a digitization process.",
            "outcome": "success",
            "outcomeDetail": "The resulting wav-files was rendered to disk on the sound studio workstation."
        }
    }
```


### Filename change 


 | Name	| **filename change** 	|
|:---	|:---	|
| Description	| The process of modifying a filename. 	|
| Scope 	| File 	|


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
            "agentNotes": "Dataflow automation tool that enables the design and management of complex data pipelines."
        },
        "event": {
            "eventDateTime": "2026-02-03T10:47:29.332+01:00",
            "eventType": "filename change",
            "eventDetail": "The filename was changed to conform to current file naming convention.",
            "fileRef": {
                "fileId": "a1b2c3d4e5f67890123456789abcdef0",
                "relativePath": "representations/rep-text_20230219/data/document_001.pdf"
            },
            "outcome": "success",
            "outcomeDetail": "Filename changed from NN_TR_2011_01_31_18_40.mp4 to NRK_TR_2011_01_31_18_40.mp4."
        }
    }
```


 ### Fixity check 


 | Name 	| **fixity check** 	|
|:---	|:---	|
| Description 	| The process of verifying that an object has not been changed in a given period.	|
| Scope 	| IE, File 	|


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
            "agentNotes": "Calculates MD5 checksums and verifies against stored checksum manifest."
        },
        "event": {
            "eventDateTime": "2026-02-03T12:05:48.210+01:00",
            "eventType": "fixity check",
            "eventDetail": "Calculated MD5 checksums for all files in the package and verified against the stored checksums in the manifest file.",
            "outcome": "success"
        }
    }
```


 ### Imaging 


 | Name 	| **imaging** 	|
|:---	|:---	|
| Description 	| The process of extracting a disk image from a physical information carrier.	|
| Scope 	| IE 	|


**Guidelines for use:**
-	Used to document the process of creating an exact digital copy (disk image) of a storage medium, including all files, metadata, file system structure, and sometimes also free space and deleted data.
-	When applicable, this event should be used instead of, not in addition to, the “creation” event. 

**Examples:**



### Message digest calculation 


 | Name 	| **message digest calculation** 	|
|:---	|:---	|
| Description 	| The process by which a message digest ("hash") is created.	|
| Scope 	| IE, File	|


**Guidelines for use:**
-	The event should be linked to the IE where possible. Linked to the File only when it is necessary to document discrepancies.
-	Message digest is also commonly referred to as a "checksum". The event "fixity check" checks the message digest.
- Used when generating new checksums. Where checksums are generated locally, there is no need to use the "fixity check" event in addition to the ‘message digest calculation’ event. See also EventType "fixity check".


**Examples:**
```json
    {
        "agent":{
            "agentName": "md5sum (GNU coreutils)",
            "agentType": "software",
            "agentVersion": "8.32",
            "agentNotes": "Calculates MD5 checksums and verifies against stored checksum manifest."
        },
        "event":{
            "eventDateTime": "2026-02-03T13:36:42.455+01:00",
            "eventType": "message digest calculation",
            "eventDetail": "Calculated MD5 checksum for all the files in the package.",
            "outcome": "success"
        }
    }
```


### Metadata extraction 


 | Name	| **metadata extraction** 	|
|:---	|:---	|
| Description 	| The process of extracting metadata from an object. This includes technical, administrative and descriptive metadata.	|
| Scope	| File	|


**Guidelines for use:**
 - Used when metadata is extracted from a file, resulting in one or more metadata files.
- The derived file(s) must reference the source file. 


**Examples:**
```json
    {
        "agent":{
            "agentName": "ExifTool",
            "agentType": "software",
            "agentVersion": "12.60",
            "agentNotes": "Used for extracting metadata from image and video files."
        },
        "event":{
            "eventDateTime": "2026-02-19T11:45:32.123+01:00",
            "eventType": "metadata extraction",
            "eventDetail": "Extracted technical and descriptive metadata from image file: DSC_0456.JPG.",
            "fileRef": {
                "fileId": "b1c2d3e4f567890123456789abcdef01",
                "relativePath": "representations/rep-images_20230908/data/DSC_0456.JPG"
            },
            "outcome": "success",
            "outcomeDetail": "Image: format JPEG, resolution 6000x4000 pixels, 24-bit color; Camera: Nikon D850; Lens: 24-70mm f/2.8; Exposure: 1/125 sec at f/8; ISO: 100; File size: 18.2 MB."
        }
    }
```
```json
    {
        "agent":{
            "agentName": "Audioinspector",
            "agentType": "software",
            "agentVersion": "5.5",
            "agentNotes": "A software tool for automated analysis, quality assessment, and metadata management of audio files."
        },
        "event":{
            "eventDateTime": "2026-02-11T12:01:08Z",
            "eventType": "metadata extraction",
            "eventDetail": "Wav-files were analyzed for quality control and documentation.",
            "fileRef":{
                "relativePath": "representations/primary_20250325/data/something.wav"
            },
            "outcome": "success",
            "outcomeDetail": "An XML metadata file was created, containing detailed analysis results."
        }
    }
```


### Migration


 | Name 	| **migration** 	|
|:---	|:---	|
| Description 	| The act of transforming an object from one file format(s) into another file format(s).	|
| Scope 	| IE, File	|


**Guidelines for use:**
- The event should be associated with the Intellectual Entity (IE) whenever possible, for example, if the files have been converted in the same way to the same format. 
-	Used when changing fileformat, not to document compression as part of storage optimization. See also eventType “compression”.
-	Migration events should always create a new package or file. 
- The migrated file(s) must reference the source file. 


**Examples:**
```json
    {
        "agent":{
            "agentName": "FFmpeg",
            "agentType": "software",
            "agentVersion": "6.0",
            "agentNotes": "Used for media conversion and encoding."
        },
        "event":{
            "eventDateTime": "2026-02-03T15:09:55.774+01:00",
            "eventType": "migration",
            "eventDetail": "Converted MOV files to MXF/Op1a format with JPEG2000 video codec and PCM audio codec.",
            "outcome": "success",
            "outcomeDetail": "command=ffmpeg -i input.mov -c:v jpeg2000 -c:a pcm_s16le output.mxf; container=MXF/Op1a; videoCodec=JPEG2000; audioCodec=PCM; integrityChecked=yes"
        }
    }
```


### Transfer 


 | Name	| **transfer** 	|
|:---	|:---	|
| Description 	| The process of transferring metadata and/or digital object(s) between systems. 	|
| Skope	| IE	|


**Guidelines for use:**
-	Used for transferring objects into or out of the preservation area or temporary working areas. This typically includes moving objects between storage locations, from storage to a working area for processing, or from a working area to storage.


**Examples:**
```json
    {
        "agent":{
            "agentName": "Apache NiFi",
            "agentType": "software",
            "agentVersion": "2.2.0",
            "agentNotes": "Dataflow automation tool that enables the design and management of complex data pipelines."
        },
        "event":{
            "eventDateTime": "2026-02-18T14:02:33Z",
            "eventType": "transfer",
            "eventDetail": "Transferred package from Oracle HSM(SAM-FS) to local workspace for further processing; Upload was performed with source checksums verified; Generated E-ARK SIP.",
            "outcome": "success",
            "outcomeDetail": "Verified checksums with md5sum (GNU coreutils); Generated E-ARK SIP with commons-ip2 2.12.0."
        }
    }
```


### Validation 


 | Name	| **validation** 	|
|:---	|:---	|
| Description 	| The process of comparing an object with a standard and noting compliance or exceptions. 	|
| Scope	| IE, File	|


**Guidelines for use:**
-	The object being validated may be a file or an Intellectual Entity. The event should be linked to the IE whenever possible, for example when the files are validated in the same way using the same tool, or when the structure is validated for the entire informationpackage.
- It may be appropriate to create a single event covering the entire validation process, and instead describe which tools are used in the different steps, rather than creating multiple events for multiple validations.


**Examples:**
```json
    {
        "agent":{
            "agentName": "JHOVE",
            "agentType": "software",
            "agentVersion": "1.32.1",
            "agentNotes": "An extensible software framework for performing format identification, validation, and characterization of digital objects."
        },
        "event":{
            "eventDateTime": "2026-02-03T17:30:39.662+01:00",
            "eventType": "validation", 
            "eventDetail": "Validated that the audio-files comply with the specifications of the WAVE format",
            "outcome": "success"
        }
    }
```
```json
    {
        "agent":{
            "agentName": "Apache NiFi",
            "agentType": "software",
            "agentVersion": "2.4.0",
            "agentNotes": "Dataflow automation tool that enables the design and management of complex data pipelines."
        },
        "event":{
            "eventDateTime": "2026-02-03T17:30:39.662+01:00",
            "eventType": "validation", 
            "eventDetail": "Validated E-ARK SIP using DPS Validation workflow v.a00f683: nifi-nb-eark-nar,EarkSIPValidator 1.0.7; org.roda-community,commons-ip2 2.12.0.",
            "outcome": "success",
            "outcomeDetail": "Validated against profiles E-ARK-SIP-v2-2-0, NB-SIP-STRUCTURE-1.0 and NB-SIP-MOVINGIMAGES-PROFILE-1.0."
        }
    }
```


### Virus check 


 | Name	| **virus check** 	|
|:---	|:---	|
| Description 	| The process of scanning a file for malicious programs. 	|
| Scope 	| IE, File	|


**Guidelines for use:**
-	The event should be linked to the IE where possible. Linked to the File only when it is necessary to document discrepancies.
 

**Examples:**
```json
    {
        "agent":{
            "agentName": "ClamAV",
            "agentType": "software",
            "agentVersion": "1.8.7",
            "agentNotes": "Antivirus program designed to detect malicious software."
        },
        "event":{
            "eventDateTime": "2026-02-03T18:27:53.842+01:00",
            "eventType": "virus check",
            "eventDetail": "All files in the package were scanned prior to transfer.",
            "outcome": "success",
            "outcomeDetail": "No infected files were detected."
        }
    }
```
```json
    {
        "agent":{
            "agentName": "ClamAV",
            "agentType": "software",
            "agentVersion":"1.8.7",
            "agentNotes": "Opensource antivirus program designed to detect malicious software. Virus definitions were updated immediately before execution."
        },
        "event":{
            "eventDateTime": "2026-02-03T07:14:01.716+01:00",
            "eventType": "virus check",
            "eventDetail": "All files in the package were scanned using ClamAV prior to transfer. Recursive scan covered 1,245 files.",
            "outcome": "success",
            "outcomeDetail": "Presence of the signature Win.Trojan.MacroVirus-12345 in file_2026.xml was detected."
        }
    }
```