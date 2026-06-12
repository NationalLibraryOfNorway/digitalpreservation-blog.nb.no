---
title: Metadata management
weight: 2
---

## What is metadata?

Metadata is structured information about digital objects. Without metadata, a digital file is just an opaque sequence of bits: you cannot find it, you cannot understand what it represents, and you cannot prove it is what it claims to be.

For digital preservation, metadata serves several essential functions:

- It enables the four fundamental user tasks: **find** content matching your criteria, **identify** the right object among similar results, **select** the appropriate representation, and **obtain** the actual content through dissemination
- It documents **who created** the content, **when**, and under what **rights**
- It records the **lifecycle** of the object: what happened to it and when, documenting the origin, creation context, and provenance so that future users can trust what it represents
- It captures **technical properties** needed to keep files usable as formats evolve
- It provides **context**: how the content relates to other objects in the collection

Some metadata you provide directly. Some is generated automatically by the preservation system. Together, these layers form a complete picture of every digital object in our care.

Metadata is not created all at once. It accumulates over the lifetime of a digital object: some layers are provided at submission, others are produced during ingest, and others build up over decades of preservation processing. Some layers are designed for enrichment over time, while others are deliberate snapshots frozen at the point of submission. Each layer serves a different purpose and is created at a different stage.

Metadata is central enough to digital preservation that it is stated as a principle in the National Library's [Principles for Digital Preservation](/docs/principles/).

## Why metadata matters in DPS

Many client partners already maintain rich cataloguing and metadata systems. A natural question is: if the content is already well described in our own systems, why do we need to provide metadata again through the DPS?

The answer lies in how access to preserved content works. Access to the DPS is governed by [submission agreements and consumer roles](/docs/services/dps/access-control/). A client who submits content (producer) may not be the same client who retrieves it (consumer). For example:

- A regional archive deposits digitised photographs
- A university library is granted consumer access to those photographs for research
- The researcher can search the DPS for the photographs, but has no access to the regional archive's internal catalogue

More broadly, a single consumer can have access to content spread across many different submission agreements, delivered by many different submitters. The same digital content may even be described in several different catalogue systems across different organisations. The Dublin Core metadata model provides a unified way to search across all of this content within the DPS, regardless of which catalogue system it came from, how it was catalogued, or whether it was catalogued at all in another system. A photograph might be described one way in a museum's collection system, while a film is described differently in a broadcaster's media archive. Through Dublin Core, both are at minimum described using the same set of attributes: type, title, creator, date, making cross-collection search possible for any authorized consumer.

In this scenario, the DPS is the only discovery layer available to the consumer. The Dublin Core metadata submitted through the API is what makes the content findable. Together, they form a shared, self-contained discovery layer that works for every authorized consumer, regardless of whether they have access to the source catalogue.

The richer metadata you pack into SIP files is still preserved and available through dissemination, but a consumer must first be able to find the right package to request. That is what the searchable layers provide.

If you already maintain this metadata in your own cataloguing systems, providing it through the Submission API is typically straightforward. The Dublin Core fields are well-defined, and in many cases mapping from your existing metadata formats is a one-time configuration effort.

Ultimately, the metadata you provide in the DPS enables a higher degree of self-service. Authorized consumers can find and retrieve the content they are after without having to go through intermediaries, whether that is the original submitter, a catalogue team, or a preservation custodian. The searchable and retrievable layers together make the DPS a self-contained platform for discovery and access.

## How metadata enters the DPS

Each type of metadata serves a specific purpose in the preservation lifecycle, from making content findable to building the audit trail to preserving the full context of a submission. The following subsections walk through how each type enters the DPS and where it ends up in the metadata service.

Metadata can enter the DPS through three channels:

### Through the Submission API

Metadata enters through the Submission API at several points in the submission workflow.

The typical sequence is: create a submission → register the files that make up the SIP → optionally submit PREMIS events → finalize to trigger ingest.

A successful submission is what leads to an Intellectual Entity (AIP) being created in the preservation metadata database. A rejected submission is purged from the database.

- **Administrative metadata** is provided when you create a submission. A contract ID identifies which submission agreement governs the submission (see [role-based access control](/docs/services/dps/access-control/)), and an object ID uniquely identifies this object within your contract. Both are stored in the preservation metadata database, enriching the Intellectual Entity document.
- **Dublin Core metadata** is also provided at submission creation. It is stored in the descriptive metadata database, linked to the Intellectual Entity, and makes your content discoverable. Dublin Core also lets you link a package to an external record, so that anyone who retrieves it knows which systems to consult for richer information about the content. Required fields include a type from a controlled vocabulary (such as `Bok`, `Film`, `Bilde`), a title, and at least one identifier. Optional fields let you record creators, contributors, publishers, dates, language, spatial coverage, subjects, descriptions, and relations, many with support for authority records. See the [Metadata Requirements](/docs/dps/api/submission/metadata/) for the full specification.
- **PREMIS events** are optionally submitted before the submission is finalized for ingest. Each event records a preservation action that occurred outside the DPS, such as transfer, creation, digitisation, validation, or virus checking, and can optionally reference a specific file within the submission. They are stored in the preservation metadata database as event documents, linked to the IE and optionally a file. See the [Events documentation](/docs/dps/api/submission/events/) for details.

### Through SIP metadata files

Metadata can also be embedded directly in the SIP structure, where it travels alongside the content files. See the [SIP structure requirements](/docs/dps/sip/1.0/structure-requirements/) for the full package layout.

- **METS.xml files** are required at both the package root and within each representation folder. Unlike the other metadata files in the SIP, METS.xml is parsed by the DPS ingest workflow. The DPS extracts metadata from the METS header to enrich the Intellectual Entity document, and extracts files and checksums from the file section to create the Representation and File documents in the preservation metadata database. See the [METS.xml requirements](/docs/dps/sip/1.0/mets/) for the full specification.
- **Rich metadata files**, such as MARC, MODS, Dublin Core XML, or domain-specific metadata, can also be embedded directly in your SIPs alongside the content files, at both the package and representation level. The DPS ingest workflow treats these files like any other data file: they are modelled as File documents in the preservation metadata database and go through format identification and metadata extraction. However, their contents **are not parsed or indexed by the DPS**. See the [Metadata primer](/docs/dps/sip/1.0/metadata/) for placement guidance.

### Generated by the DPS

When an information package is received, the DPS constructs the PREMIS object model in the preservation metadata database. Intellectual Entity, Representation, and File documents are populated from the data you provide (METS.xml, administrative metadata, Dublin Core) combined with what the DPS extracts during processing. This internal model ties everything together. It is not something you interact with directly. The closest you get to touching it is by providing PREMIS events in the correct format through the API.

Several additional kinds of metadata are also generated automatically during ingest:

- **PREMIS events**: the DPS records an event for every operation it performs during ingest: transfer, validation, ingestion, format identification, and metadata extraction. In the same manner, preservation activities and dissemination of files are documented through events also after ingest. Each event is stored in the preservation metadata database as an event document, linked to the IE and optionally a file, with a timestamp, outcome, and agent.
- **Format identification results** are stored in the preservation metadata database, enriching the File documents with their identified format.
- **Extracted technical metadata** is produced for every file using MediaInfo and ExifTool. These extraction outputs are stored as files in the S3 object storage, referenced by the File documents. They capture detailed technical properties: checksums, resolution, bitrate, color space, and more. They are put in object storage for easier retrieval and possible use by analytical processing tools.

## How metadata is stored

Metadata in the DPS is handled by the metadata service, which consists of several components. Like all data in the DPS, metadata is protected by the same 3-2-1 storage policy (see [Principles for Digital Preservation](/docs/principles/)).

{{< figure src="metadata-service.svg" alt="Diagram showing the metadata service databases and their relationships. The preservation metadata database (PREMIS) contains intellectual entities, representations, files, events, agents, and a planned rights entity. The descriptive metadata database holds Dublin Core documents. The location database tracks repository files. Technical metadata is stored in S3 object storage." >}}

### Preservation metadata database

A MongoDB database based on the PREMIS data model. It holds these document types:

- **Intellectual Entities (IEs)**: each information package (AIP) is described as one IE document, representing the root level of the package. Every IE carries a submission agreement identifier. A dedicated rights entity is planned for the future to hold this data.
- **Representations**: each IE contains at least one representation.
- **Files**: the files within each representation. Format identification results from ingest are stored here, enhancing each file document with its identified format.
- **Events**: PREMIS events, both client-submitted and DPS-generated. Every event is related to an IE, and can optionally also be attached to a specific file.
- **Agents**: the people, organisations, or software that performed each event.

For formal PREMIS definitions of these entity types, see [Entity management at the NLN](/docs/services/nln/premis-architecture/).

### Descriptive metadata database

A MongoDB database. Each IE is linked to exactly one Dublin Core document. This is the metadata you submit through the Submission API, stored separately from the preservation metadata but connected to the same IEs.

### Location database

A MongoDB database. The DPS repackages and reorganises the files submitted in SIPs for better utilisation of the bit repository. This database tracks where files are physically stored. Each repository file document is linked to both an IE document and the file documents it contains.

### Object storage for extracted metadata

The outputs of metadata extraction tools (MediaInfo and ExifTool) are stored as files in an S3 object storage bucket. File documents in the databases refer to the paths in this bucket.

## How metadata is accessed

Metadata access currently happens through the public API. The following data is available:

### Dublin Core metadata

Retrievable per submission through the API. When you request a specific submission, you can include the descriptive metadata that was submitted with it.

### PREMIS events

Retrievable per submission through the API. Both client-submitted and DPS-generated events can be retrieved for a given submission.

### File metadata

Retrievable per file through the API, including file paths and checksums.

### Submission listing

You can list submissions within a given contract through the API, paginated.

### Dissemination

You can create a dissemination request and poll its status through the API. The actual download of disseminated content happens outside the API. SIP metadata files are preserved in the same manner as the data, and can be retrieved this way.

---

Metadata stored but not currently accessible through the API:

- **Extracted technical metadata** is stored in S3 object storage but is not yet accessible to clients through the API.

We are working towards a richer access model where searches can be performed across intellectual entities in the preservation database, and events and other metadata can be retrieved in the context of IEs. The current section describes what is available today. The access layer is under active development.

## How metadata changes over time

Metadata in the DPS follows three different update models. Some of these are implemented, while others are planned:

- **Versioned** (planned): Dublin Core metadata will be updateable through the API, with each change recorded as an auditable event. This is not yet available.
- **Append-only**: PREMIS events can only be added, never modified. New events are appended to the existing record. A custodian can trigger re-extraction of technical metadata for individual files, producing a new extraction output while keeping the old.
- **Immutable**: SIP metadata files are frozen at submission and cannot be changed.
