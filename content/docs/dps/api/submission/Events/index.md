---
title: Events/preservation metadata
weight: 2
draft: True
---

In digital preservation, an “event” documents an action or occurrence that has affected a digital object, such as creation, migration, validation, or transfer. Events are considered important preservation metadata, as they provide traceability and evidence of what has been done to the object throughout its entire lifecycle.

The National Library bases its work on the [Library of Congress](https://www.loc.gov/) list of [EventTypes](https://id.loc.gov/vocabulary/preservation/eventType.html). This list has been narrowed down, and the use of the different types has been specified to suit our needs and preservation environments. Event types other than those specified in the list below are not approved in the API.

Submitting events is not mandatory, but we recommend doing so when such information is available. Events added through the API will be preserved in a dedicated event database. If you want do submit other types of preservation metadata, it is also possible to submit preservation metadata as part of the information package (SIP). See more information under [metadata primer](docs/dps/sip/1.0/metadata/) and [requirements for SIP structure](docs/dps/sip/1.0/structure-requirements/). Information relating directly to provenance may be included under [metadata requirements](docs/dps/api/submission/metadata/).

Events can be associated with either the entire information package or with individual files. In general, events should be associated with the package level, the Intellectual Entity (IE), where possible. This is to avoid large numbers of events that essentially convey the same information. It is possible to associate events with individual files when there is a need to document file-level actions. The most important consideration is to be deliberate about what is documented, why it is documented, and at which level.

The technical documentation of submissions in API are to be found here: [Swagger DPS Submission Service API](https://digitalpreservation.no/swagger/)




## EventTypes


### Capture

| Name 	| **capture** 	|
|:---	|:---	|
| Description 	| The process whereby an agent (organization, team, role, system, service, or automated process) actively acquires an object through mechanisms other than transfer from the creator or donor. 	|
| Scope	| IE, File 	|


**Guidelines for use:**
- Used for capture of websites during crawling functions of a repository.

**Examples:**

 

### Compression

 | Name	| **compression** 	|
|:---	|:---	|
| Description 	| The process of encoding data to save storage space or transmission time.  	|
| Scope 	| IE, File 	|

**Guidelines for use:**
-	The event should be linked to the IE when possible. For example if the files are compressed in the same way.
-	Used to document compression as part of storage optimization.
-	This should not be used as part of a format migration to a compressed format. See also eventType "migration".
-	Within a PREMIS context, information about the lossiness of the compression should be in the eventDetailInformation or eventOutcomeInformation.



**Examples:**


### Creation 


 | Name 	| **creation** 	|
|:---	|:---	|
| Description	| The process of creating a new object. 	|
| Scope 	| File 	|


**Guidelines for use:**
- Used to document the digital object within an information package. 
-	Used to document the origin of the file or Intellectual Entity, describes the method and process of creating the file/IE. See also eventType "imaging".


**Examples:**



### Filename change 


 | Name	| **filename change** 	|
|:---	|:---	|
| Description	| The process of modifying a filename. 	|
| Scope 	| File 	|


**Guidelines for use:**
-	Relevant when changing name of a born digital file, or e.g when renaming a file to comply with the constraints of the storage system.
-	Either a removal of prohibited character or a partial or entire replacement of the original filename. This can be used to note changes such as removing characters, or where a system removes the filename entirely and replaces it with a system generated name.




**Examples:**
 


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




### Metadata extraction 


 | Name	| **metadata extraction** 	|
|:---	|:---	|
| Description 	| The process of extracting metadata from an object. This includes technical, administrative and descriptive metadata.	|
| Scope	| File	|


**Guidelines for use:**
 - Used when metadata is extracted from a file, resulting in one or more metadata files.
- The derived file(s) must reference the source file. 


**Examples:**




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




### Transfer 


 | Name	| **transfer** 	|
|:---	|:---	|
| Description 	| The process of transferring metadata and/or digital object(s) between systems. 	|
| Skope	| IE	|


**Guidelines for use:**
-	Used for transferring objects into or out of the preservation area or temporary working areas. This typically includes moving objects between storage locations, from storage to a working area for processing, or from a working area to storage.



**Examples:**




### Validation 


 | Name	| **validation** 	|
|:---	|:---	|
| Description 	| The process of comparing an object with a standard and noting compliance or exceptions. 	|
| Scope	| IE, File	|


**Guidelines for use:**
-	The object being validated may be a file or an Intellectual Entity. The event should be linked to the IE whenever possible, for example when the files are validated in the same way using the same tool, or when the structure is validated for the entire informationpackage.
- It may be appropriate to create a single event covering the entire validation process, and instead describe which tools are used in the different steps, rather than creating multiple events for multiple validations.

 


**Examples:**




### Virus check 


 | Name	| **virus check** 	|
|:---	|:---	|
| Description 	| The process of scanning a file for malicious programs. 	|
| Scope 	| IE, File	|


**Guidelines for use:**
-	The event should be linked to the IE where possible. Linked to the File only when it is necessary to document discrepancies.

 

**Examples:**