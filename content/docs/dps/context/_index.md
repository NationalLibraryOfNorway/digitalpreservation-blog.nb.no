---
title: The role of DPS in the NLN
weight: 1
aliases:
  - /system-architecture
  - /premis-architecture
  - /docs/dps/architecture/
---

The Digital Preservation Services (DPS) is the National Library's system for long-term digital preservation.
The DPS does not operate in isolation: it is one of three system domains that share responsibility for digital objects at the National Library. These domains operate independently, but each domain's responsibilities influence the others.
This page describes the context the DPS was built in and how that context shapes the system.

The three system domains described here reflect the National Library's internal operational landscape.

External clients interact with the DPS directly through the API, bringing their own identifiers, metadata, and scope definitions.

{{< figure src="onioncontext.svg" alt="DPS within the NLN organizational context" caption="DPS within the NLN organizational context" >}}

## The three system domains

Within the National Library's own collections, responsibility for any digital object[^1] is spread between three system domains, each managing different aspects of the object:

### Metadata management systems

Catalogs, registries, and collection management systems (such as Alma, Mavis, and Hanske). They are the authoritative source for descriptive metadata and issue unique identifiers (UIDs, typically URNs) for digital objects. These systems manage a wide range of entities; only a subset describe digital objects relevant to digital preservation.

This is where intellectual entities are defined: the choice of what constitutes a preservable information package originates here, not in DPS. A single URN typically maps to a single package. For details on scoping, see [Package, representation and data scope](/docs/dps/sip/scope/).

### Digital Preservation Services (DPS)

The preservation system. Manages preservation data using a PREMIS-based data model (Intellectual Entities, Representations, Files, Events, Agents). The DPS provides "cold" long-term storage with asynchronous access, designed for preservation rather than immediate retrieval. The DPS is the authoritative source for technical file metadata in the National Library. It is not the authoritative source for descriptive metadata: it keeps the metadata it needs to operate independently, without replicating the full cataloguing structures of the metadata management systems.

For external producers and consumers, the DPS operates as a self-contained service: you provide your own identifiers and metadata through the API, and the DPS manages preservation independently. For details on how data and metadata are handled within DPS, see [Data management](/docs/dps/data/) and [Metadata management](/docs/dps/metadata/).

### Public access services

Nettbiblioteket and Oria. Manage a harvested subset of descriptive metadata and provide access copies derived from preservation files. These services offer "hot" storage with immediate access, unlike the preservation storage of the DPS.

The public access services transform the harvested metadata into a flattened structure, operating with a single representation per intellectual entity. As a result, the intellectual entities found online do not necessarily mirror the entities in the metadata management systems.

A UID, managed by the metadata management systems, ties the three domains together. It must be unique across systems and should not be reused.

## Data and metadata flow

The diagram below is an idealized and simplified view of how data and metadata move between the domains:

{{< figure src="context.svg" alt="architecture diagram" caption="Data and metadata flow between systems in NLN" >}}

The SIP carries preservation data and a copy of descriptive metadata from the metadata management systems. The DPS does not preserve access copies that can be automatically derived from preservation files; such copies are managed by the public access services.

## PREMIS entities and overlapping responsibilities

The DPS uses PREMIS as its preservation metadata model. Neither the metadata management systems nor the public access services use PREMIS natively, but PREMIS concepts help explain where responsibilities begin and end across the three domains within the NLN. This mapping explains why the DPS was designed the way it is, not how external users should model their own data[^2].

{{% details title="PREMIS terminology" closed="true" %}}

### Intellectual entities (IE)

> An **Intellectual Entity** is a distinct intellectual or artistic creation that is considered relevant to a designated community in the context of digital preservation: for example, a particular book, map, photograph, database, or hardware or software.

In our implementation, there is a 1:1 relationship between SIP and IE. The IE is the entity identified by the UID that links the three system domains together. Typically this is the **smallest** described size in any of our metadata management systems. For details on how this shapes package scope, see [Package, representation and data scope](/docs/dps/sip/scope/).

Metadata at the package root describes the IE that the SIP holds representations of. The representations are different data renditions of the IE and do not have their own discrete descriptive metadata.

### Representations

> A **Representation** is the set of all file objects needed to render an Intellectual Entity.

A package can contain multiple representations. For the majority of SIPs at the National Library, there is a single representation per package. The metadata at the SIP core describes the whole package and all representations equally.

### Files

> A **File** is a named and ordered sequence of bytes that is known to an operating system. A File can be zero or more bytes and has a File format, access permissions, and File system characteristics such as size and last modification date.

{{% /details %}}

Within the NLN, PREMIS entities are distributed across the three system domains. For external users, the DPS manages its own data model (Intellectual Entities, Representations, and Files) and scope is defined by the client. The roles of the other two domains are filled by your own systems.

- **Metadata management systems**: within the NLN, this is where intellectual entities are defined and identified. The representation level is typically *not* described in these systems. They define representations implicitly through the representation's 1:1 relationship with the IE.
- **Digital Preservation Services (DPS)**: manages the full PREMIS data model: Intellectual Entities, Representations, and Files. The DPS does not replicate the full descriptive metadata structures of the metadata management systems. It offers searches based on the metadata provided to and generated by the DPS. For details, see [Metadata management](/docs/dps/metadata/).
- **Public access services**: manage and disseminate a harvested subset of intellectual entities, access representations, and files.

[^1]: A digital object or asset can encompass both *simple digital objects* (discrete individual files) and *complex digital objects* (groups of files). An example of a simple digital object can be a singular image in TIFF format, while a complex digital object can be a DCP (a directory containing image and audio streams in MXF containers and XML files).
[^2]: *PREMIS Data Dictionary (full document)*, Version 3.0, Nov. 2015, [https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf](https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf)
