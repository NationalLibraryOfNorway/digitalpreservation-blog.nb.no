---
title: Entity management architecture
summary: This post discusses high-level metadata and data handling at the National Library of Norway
date: 2024-10-04
tags: [Systems architecture, PREMIS, Intellectual entities, representations]
authors: 
  - name: Torbjørn Bakken Pedersen
    image: https://avatars.githubusercontent.com/u/113333557?v=4
images: 
  - premis.png
weight: 2
aliases: ["/premis-architecture"]
---

In our ongoing work with the [eArchiving standards and specification](https://dilcis.eu "Website with standards and specifications for E-ARK"), we have to define intellectual package scope and representation rulesets.
Some of these terms come from PREMIS, which again is a framework mainly used in the digital preservation environment.

{{% details title="PREMIS terminology" closed="true" %}}
### Intellectual entities (IE)
> An **Intellectual Entity** is a distinct intellectual or artistic creation that is considered relevant to a designated community in the context of digital preservation: for example, a particular book, map, photograph, database, or hardware or software.

IEs tend to describe *intellectual content*.
In our suggested implementation of the SIP there is a 1:1 relationship between SIP and IE.
At the National Library of Norway the IE is the entity that is identified by the UID linking the our three different system environments together.
Typically, this is the **smallest** described size in any of our metadata management systems.
This is expanded upon in the following text about [intellectual entities and unique IDs FIKS LENKE](/intellectual-scope).

The metadata at the core describes the IE that the SIP represents.
The representations are different data renditions of the IE, and thus do not have their own discrete descriptive metadata.
SIPs therefore have metadata about, and representations of, intellectual content.
<!-- In our metadata management systems, we tend to operate with a lot of different IEs, usually organized in some sort of hierarchy.
In use-case examples of PREMIS and E-ARK, it is usually the highest level entity from these hierarchies, that is referred to as the IE and used to define *intellectual scope of packages*, ie. a *work* or *expression*. -->

### Representations
In the E-ARK SIP specification a SIP is a package holding *metadata* and *representations*.
The representations are again composed of *data* and *metadata* of their own.
The representation concept is defined in PREMIS:

> A **Representation** is the set of all file objects needed to render an Intellectual Entity.
> For example, a journal article may be complete in one PDF file; this single file constitutes the Representation.
> Another journal article may consist of one SGML file and two image files; these three files constitute the Representation.
> A third article may be represented by one TIFF image for each of 12 pages plus an XML file of structural metadata showing the order of the pages; these 13 files constitute the Representation.

A package can consist of multiple representations.
The metadata sitting at the SIP core, is metadata that that describes the whole package and all the representations equally.

### Files
> A **File** is a named and ordered sequence of bytes that is known to an operating system. 
> A File can be zero or more bytes and has a File format, access permissions, and File system characteristics such as size and last modification date.

{{% /details %}}

## Entity management domains
- **Metadata management systems**
	- Manage intellectual entities
	- Define representations (through the representation's relationship with the intellectual entity)
- **Digital Preservation Services (DPS)**
	- Manage representations and files
- **Public access services**
	- Manage and disseminate a harvested subset of intellectual entities, *access* representations and files.

### Metadata management systems
The metadata management systems manage **intellectual entities**.
The representation level (as we interpret it), is typically *not* described in our metadata management systems.
If a user needs to find an intellectual entity or their related digital objects, they should use the metadata management systems.
The metadata management systems handle the UIDs that link an intellectual entity to a SIP/AIP in the DPS.

### Digital Preservation Services (DPS)
The DPS currently manage **files**[^2].
These files are *organized* by intellectual entities and representations.

Files are ingested to the DPS through the delivery of SIPs, which again mirror intellectual entities found in the Metadata management systems.
For the majority of SIPs handled in the National Library, there is a single representation per package.
As mentioned in the [systems architecture description](/systems-architecture), access copies automatically derived from the preserved master file are usually not handled by the DPS.

[^2]: The bitstream level is not yet described in the DPS, but it could be in the future.

We do not aim to replicate the descriptive metadata structures or functionality of our metadata management systems in the DPS. 
Users should already have identified the intellectual entities they are seeking before interfacing with the DPS.
However, If you are seeking files based solely on their technical properties, you could use the DPS directly.

### Public access services (NB.no)
The public access services manage and provide access to *access representations* and *files*, in addition to harvested intellectual entity descriptive metadata.
The data and metadata here is a subset of what is found in the metadata management systems and the DPS.

The public access services transforms harvested metadata in a flattened structure of intellectual entities with a single representation each.
The intellectual entities found online, does not necessarily mirror a single intellectual entity found in the metadata management systems.

## Architecture
We can draw up another idealized architecture diagram, using PREMIS entities, to illustrate the responsibilities of the different system domains:

{{< figure src="premis.svg" alt="Diagram showing various systems' responsibility for PREMIS entities" caption="PREMIS entities across our systems" >}}

The representation entity is somewhat complicated to understand here. 
There is a a 1:1 relationship between the IE used to define the package scope and its primary representation in the metadata management systems. 
This means the primary representation per package often *is* described in technical terms in these systems, even though they do not operate with a representation level as a discrete entity.
Any *additional* representations, however, are *not* described in the metadata management systems. 
They are only described in the DPS.
 
This is confusing, but it stems from the choice of which intellectual entity used to define SIP size.
It is crucial that our three system environments stay in sync, and operate with similar concepts and sizes.
We do not want to end up in a situation where we have parallel, and possibly opposing, "truths" in different systems.
