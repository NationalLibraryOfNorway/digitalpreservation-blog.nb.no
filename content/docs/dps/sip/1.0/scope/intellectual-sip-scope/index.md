---
title: Intellectual scope of SIPs
summary: This post discusses some key concepts related to information package scope and the eArchviving standards and specifications
date: 2024-10-04
tags: [Information packages, IP, E-ARK, eArchiving, asset management, cataloging]
authors: 
  - name: Torbjørn Bakken Pederse
images: 
  - ie-sip.png
weight: 3
aliases: ["/intellectual-sip-scope"]
---

The DPS is a system designed to receive, safely preserve and disseminate preserved digital objects.
By "digital objects" we refer to discrete digital items, representing intellectual content. 
Digital objects can be either simple objects consisting of discrete files, or composite objects consisting of groups of files intended to be utilized together. 
An example of a simple digital objects can be singular images in TIFF-format, while an example of a complex digital object can be a DCP (which is a directory containing image and audio streams in MXF containers along with xml-files).

The intellectual scope of an information package is what defines when data to be ingested should be handled as a new package, a new representation in an existing package or is a an update of an existing package.

In our use case the package scope is defined by what "intellectual entity" the package contains one or more renditions of.
Intellectual entities (IE) is a concept we find in the various metadata systems outside the digital preservation environment. 
In these systems, we tend to operate with a lot of different IEs, usually organized in some sort of hierarchy.

{{% details title="PREMIS terminology" closed="true" %}}
### Intellectual entities (IE)
The following definitions stem from the PREMIS data dictionary:
> An **Intellectual Entity** is a distinct intellectual or artistic creation that is considered relevant to a designated community in the context of digital preservation: for example, a particular book, map, photograph, database, or hardware or software.

IEs tend to describe *intellectual content*.
In our suggested implementation of the SIP there is a 1:1 relationship between SIP and IE.
At the National Library of Norway, the IE is the entity that is identified by the UID linking our three different system environments together.
Typically, this is the **smallest** described size in any of our metadata management systems.

The metadata at the root of the SIP, describes the IE that the SIP holds representations of.
The representations are different data renditions of the IE, and thus do not have their own discrete descriptive metadata.
SIPs therefore have metadata about, and representations of, intellectual content.

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

<!-- ### Files
Data and metadata come in the form of files:
> A **File** is a named and ordered sequence of bytes that is known to an operating system. 
> A File can be zero or more bytes and has a File format, access permissions, and File system characteristics such as size and last modification date. -->

In use-case examples of PREMIS and E-ARK, it is usually the highest level entity from these hierarchies, that is referred to as the IE and used to define *intellectual scope of packages/SIPs*, i.e. a *work* or *expression*.
However, we find it more practical to define package scope using more tangible intellectual entities.

{{% /details %}}

{{< callout >}}
We **strongly** recommend that the scope of an individual package is limited to a single digital object.
{{< /callout >}}

The digital object to be preserved is what is placed in the `data` folder under a representation in our E-Ark packages.

Metadata is essential in preservation, but it is important to state explicitly that the DPS is **not** aiming to be a catalogue or a complex metadata management system.

- Vi støtter ikke versjonering
- vi støtter ikke oppdatering osv

## Internal examples

Within the National Library, most digital objects are represented as intellectual entities in metadata management systems or catalogues. 
A digital object can be a particular a particular scan of a film reel, a particular digitization of an audio record or a particular digitization of a book. 
A new digitization of a physical source object that has been previously digitized, is typically handled as a new and discrete digital object and intellectual entity.

- A **digital object** is described as an **IE** in the metadata management systems.
- This **digital object** is packaged as the **primary representation** in a **SIP**
- The **SIP** and the **IE** share a **URN**, managed in the metadata management system.
- Any new digital object is described as a new **IE**, which receives a **new URN**, and thus has to be represented as a primary representation in a **new SIP**

Due to how URNs link everything together, the ruleset deciding whether you should create a new SIP or a new representation, lies in the metadata management domain.
- A single URN = a single SIP
- Multiple URNs = multiple SIPs

If you only have a single URN but still want to preserve a second or third **derivate** digital object in the DPS, you will create a second representation in the same SIP as the primary digital object.

---

## Hierarchies and flatness
A change in architecture could open for using a different key UID placed at a different location of these metadata hierarchies.
However, we believe it is impractical to do so as it introduces multiple issues related that prohibits scale across our systems.

The higher level entities in such metadata hiearchies tend to describe abstract concepts. 
Further down the hierarchy the intellectual entities describe increasingly concrete and tangible concepts.
The lowest level IE in these hierarchies is thus the most specific and tend to describe tangible physical or digital objects.

Intellectual scope defined by abstract high-level entities introduce different challenges with:
- Vast package sizes (tens of terabytes)
- Huge number of representations within SIPs
- Complex representation-to-representation relationhips
- Content description metadata changes leading to restructuring of stored data
- Preservation of unidentified digital objects having no relationships to IEs holding the key UID
- Increased complexity in keeping our three system domains in sync

Some of this complexity stems from complex metadata structures found in our metadata management systems.
We do not want to mirror and manage entire hierarchical catalogs in the preservation environment. This is after all what the metadata managements systems excels at!

We prefer keeping the structure of information packages in a flat structure, with a 1:1 relationship between information packages and an IE in the metadata management systems describing something tangible.
This is to avoid operating with unique metadata entities or "sizes" in the preservation environment, as well as to ease the metadata ingest processes.

