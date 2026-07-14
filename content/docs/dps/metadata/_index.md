---
title: Metadata management
weight: 3
aliases:
  - /docs/services/dps/metadata/
---

## What is metadata?

Metadata is structured information that describes digital objects. It enables digital files to be identified, discovered, understood, and managed over time. Without metadata, a digital file lacks the context needed to interpret, understand, and document its content. For more information about how DPS manages digital content, see [Data management](/docs/dps/data/).

In digital preservation, metadata serves several essential purposes: 

- It supports four fundamental user tasks: **discovering** content that matches specific criteria, **identifying** the correct object, **selecting** the appropriate representation, and **retrieving** the digital object. 
- It records **who created** the content, **when** it was created, and the **rights** associated with it. 
- It documents the object's **lifecycle** by recording preservation events, provenance, and the context in which the object was created. Enabling future users to understand and trust what the object represents. 
- It describes the **technical characteristics** required to ensure that files remain usable as technologies and file formats evolve. 
- It provides **context** by describing relationships between the object and other digital objects, both within and outside the collection. 

Metadata is enriched throughout the lifetime of a digital object. Some metadata is supplied by the Producer at the time of submission, some is generated automatically as part of the DPS ingest process, and additional metadata is accumulated over decades of preservation activities. 

Some metadata can be updated or supplemented over time, while other metadata captures the state of the object at the time it was submitted and remains unchanged. Different types of metadata serve different purposes and are created at different stages of the preservation process. Together, they provide a comprehensive description of each digital object. 

Metadata is a fundamental component of digital preservation and is established as one of the National Library's [Principles for Digital Preservation](/docs/principles/).

## Why metadata matters in DPS

Many DPS users already maintain comprehensive catalogues and metadata systems to describe their digital collections. Even so, metadata is also submitted to DPS because it serves a different purpose from the metadata maintained in the original source systems. 

Access to content in DPS is governed by preservation agreements and consumer roles. As a result, the organization that submits content (the Producer) is not necessarily the same organization that later retrieves it (the Consumer). A Consumer may have access to content from multiple Producers and preservation agreements, where the material is described in different catalogue systems and according to different metadata standards or cataloguing practices. 

Dublin Core metadata provides a common metadata layer within DPS. It enables authorized Consumers to search across all content they are permitted to access, regardless of which catalogue system the material originated from or whether the original catalogue is still available. For example, a photograph from a museum and a film from a broadcasting archive can be discovered using the same core metadata, even if they were originally described according to different cataloguing practices. 

Metadata also serves an important purpose beyond search and discovery. It enables digital objects to be understood even if the original catalogues or source systems no longer exist. This follows the principles of the OAIS Reference Model, which recommends that preservation objects should be as self-contained as possible. The information required to understand and interpret the preserved content therefore accompanies the object into the preservation system, rather than remaining dependent on external systems. 

More detailed metadata is included in the SIP and preserved as part of the preservation package. It can be made available when the content is retrieved. The searchable Dublin Core metadata is used to identify and locate the correct preservation package. 

For organizations that already manage metadata in their own catalogue systems, submitting metadata to DPS is typically a straightforward process. The Dublin Core elements are well defined, and mapping from existing metadata schemas is, in most cases, a one-time task. 

## How metadata enters the DPS

Metadata supports different functions throughout the preservation process. It makes preserved content searchable, documents the history of digital objects, and records their provenance and context. Metadata enters DPS from three sources: 

### Through the API

Metadata is submitted through the API at several stages of the submission process. 

A successful submission results in the creation of an Archival Information Package (AIP)[^1], represented as an Intellectual Entity in the preservation metadata database. If a submission is rejected, the associated metadata is removed from the database.

- **Administrative metadata** is registered when a submission is created. An Agreement-ID identifies the preservation agreement under which the SIP is submitted, while an Object-ID uniquely identifies the object within that agreement. Both identifiers are stored as part of the preservation metadata.
- **Descriptive metadata** is submitted as Dublin Core metadata together with the SIP. It is stored in the descriptive metadata database and linked to the corresponding preservation package. This metadata enables cross-collection searching and supports links to external catalogue systems through persistent identifiers. These links allow Consumers to identify external systems that contain more detailed descriptions of the preserved content. The long-term goal is to allow descriptive metadata to be updated after ingest. This will make it possible to correct, supplement, and enrich metadata over time without modifying either the AIP or the preserved content. Required Dublin Core elements include *Type* (using a controlled vocabulary such as `Book`, `Film`, or `Image`), *Title*, and at least one *Identifier*. Optional elements include *creators, contributors, publishers, dates, languages, geographic coverage, subjects, descriptions*, and *relationships*. Several of these elements may be linked to authority records. See [Metadata Requirements](/docs/dps/api/submission/metadata/) for the complete specification.
- **PREMIS events** may also be submitted as an optional part of the submission. These events document preservation-related activities that took place outside DPS, such as file creation, digitization, validation, virus scanning, or transfer. An event may relate either to the entire SIP or to an individual file. Once recorded, PREMIS events cannot be modified or deleted. Additional events are created automatically by DPS as the object undergoes further preservation activities. See [Preservation Metadata](/docs/dps/api/submission/events/) for details.

### As metadata files contained in SIPs

Metadata can also be submitted as files included in the Submission Information Package (SIP). Some files containing metadata is mandatory in the SIP. See the [SIP structure requirements](/docs/dps/sip/structure-requirements/) for details.

- **METS.xml files** files are mandatory both in the root of the package and within each representation. During ingest, DPS analyses the METS.xml files and extracts information about the package structure, content, and files, which is used to enrich the preservation metadata. See the [METS.xml requirements](/docs/dps/sip/mets/) for the complete specification.
- **Additional metadata files**, such as MARC, MODS, Dublin Core XML, or domain-specific metadata formats, may also be included in the SIP. At least one file containing descriptive metadata must be submitted. DPS preserves these files, identifies their file formats, and extracts technical metadata, but it does not interpret or index their contents. See [Introduction to metadata](/docs/dps/sip/metadata/) for guidance on where metadata files should be placed within the SIP.

### Generated by the DPS

During ingest, DPS builds an internal PREMIS representation of each preservation object. Information about the Intellectual Entity, representations, and files is derived from the submitted metadata (METS.xml, administrative metadata, and Dublin Core metadata), together with metadata generated by DPS itself. This information is combined and maintained in the preservation metadata database. 

DPS generates several types of metadata during ingest and preservation: 

- **PREMIS events**: are created for every operation performed by DPS, including transfer, validation, verification, file format identification, and technical metadata extraction. Preservation activities carried out after ingest, as well as file retrieval requests, are documented in the same way. Each event is stored together with its timestamp, outcome, and responsible agent.
- **File format identification** results are stored in the preservation metadata database and recorded for each file.
- **Technical metadata** is extracted for every file using analysis tools such as MediaInfo and ExifTool. The extracted metadata is stored as separate files in object storage (S3) and linked to the corresponding files. It records technical characteristics such as image resolution, bitrate, colour space, and other format-specific properties. Storing technical metadata in object storage enables efficient retrieval and supports future analysis and preservation activities.

## How metadata is stored

In DPS, different types of metadata are managed through a dedicated metadata service consisting of several components. Metadata is protected and stored according to the same principles as the preserved content and follows the 3-2-1 principle for secure and long-term storage. See [Principles for Digital Preservation](/docs/principles/).

{{< figure src="metadata-service.svg" alt="Diagram showing the metadata service databases and their relationships. The preservation metadata database (PREMIS) contains intellectual entities, representations, files, events, agents, and a planned rights entity. The descriptive metadata database holds Dublin Core documents. The location database tracks repository files. Technical metadata is stored in S3 object storage." >}}

### Preservation metadata database

The preservation metadata database (MongoDB) is based on the [PREMIS data model](https://www.loc.gov/standards/premis/v3/). It contains metadata that documents the preserved content and the preservation process. 

The database stores information about, among other things: 

- **Information packages (*Intellectual Entities*)**: Each information package is registered as a separate entity containing information such as the preservation agreement to which it belongs. 
- **Representations**: An Information Package (*Intellectual Entity*) may contain one or more representations, for example different versions or forms of presentation of the same content. 
- **Files**: All files that are part of the Information Package (*Intellectual Entity*). For each file, the database stores information such as the result of the file format identification performed during ingest. 
- **Events**: Events documenting actions performed on the Information Package (*Intellectual Entity*) or its files, such as submission, validation, or other processing activities. Events may be submitted by the Producer or generated automatically by DPS. 
- **Agents**: Individuals, organizations, or systems responsible for carrying out events. 

### Descriptive metadata database

A separate database (MongoDB) stores the descriptive metadata submitted through the API. Each Information Package (*Intellectual Entity*) is associated with a set of descriptive metadata based on Dublin Core. The descriptive metadata is stored separately from the preservation metadata but remains linked to the same Information Package. 

### Location database

A database (MongoDB) that maintains information about the physical storage location of files within the preservation storage system. During ingest, DPS may reorganize files to optimize them for the underlying storage solution. The location database ensures that each file remains associated with the correct Information Package and can be located and retrieved when needed. 

### Object storage for extracted metadata

Metadata automatically extracted from files by DPS using analysis tools (MediaInfo and ExifTool) is stored separately in object storage (S3). The extracted metadata is linked to the corresponding files through the metadata service. 

## How metadata can be used

Access to metadata is currently provided through the public API. The following types of metadata are available: 

### Dublin Core metadata

The API provides access to the descriptive Dublin Core metadata associated with each submitted Information Package. This metadata can be returned together with the Information Package when content is retrieved. 

### PREMIS events

PREMIS events can be retrieved through the API for each submitted Information Package. This includes both events submitted by the Producer and events generated by DPS. 

### File metadata

File metadata can be retrieved through the API for each individual file. This includes information such as file paths and checksums.

### Overview of Preserved Information Packages

The API can be used to retrieve an overview of the Information Packages submitted under a specific preservation agreement. 

### Dissemination

Preserved Information Packages can be requested through the API, and the status of the retrieval job can be monitored. The actual download of the content takes place outside the API. Metadata files included as part of the preservation package are included when content is retrieved. 


[^1]: Archival Information Package: The information package as stored in the bit repository. It may be identical to the SIP or may include additional preservation information.