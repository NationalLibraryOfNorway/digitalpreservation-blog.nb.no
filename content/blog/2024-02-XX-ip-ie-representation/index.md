---
title: "Intellectual package scope, intellectual entities and representations"
summary: "To enable effective automation of data handling the National Library of Norway needs to standardize as many aspects of digital preservation as possible. This post discusses some key concepts related to information package scope and the eArchviving standards and specifications."
draft: true
category: blog
date: 2024-02-27
tags: ["team"]
author: ["Torbjørn Pedersen"]
cover:
  image: earkip.webp
  hiddenInList: false
showtoc: true
---

In our strategy we have defined standardization of how we work as a [strategic area of focus](/docs/strategy/nln-digipres-strategy-en/#strategic-areas-of-focus). This aim includes all aspects of our digital preservation work, and stems from the constant high volumes of data flowing through and being managed by our systems. To deal with these volumes, we are reliant on automation, which in turn requires standardization to be effective.

One of the core things to standardize is the formatting of our OAIS *preservation packages*. In short though, we need to a clear understanding of the different *kinds* of digital objects we are operating with and the kind of *sets* of objects we want to put in each information package. 

## eArchiving standards and specifications
To standardize our package structures we are working towards implementing the [eArchiving standards and specification](https://dilcis.eu) developed in the [E-ARK project](https://www.eark-project.com). This is also stated in our newly revised [digital preservation principles](/docs/principles/#use-a-standardized-format-to-package-files-for-preservation). In the end we hope to have a standardised package structure specification for all *cultural heritage objects* that the National Library deals with. In the long-term, if feasible, we will try to define one or multiple eArchiving Content Information Type Specifications (CITS) for our relevant content types.

The eArhciving specifications and standards operate with different information packages. This document attempts to define a practical interpretation of key concepts in relation to logical Submission Information Packages (SIPs). The suggested SIP scope allows for AIP and DIP creation in a manageable manner.

The key concepts discussed is the intellectual entity used to define logical package scope, as well as the representation level below it.

## SIP mirrors intellectual Entity
In the E-ARK SIP specification a SIP is a package holding _metadata_ and _representations_. The representations are again composed of _data_ and _metadata_ of their own. The representation concept is defined in PREMIS:

> A **Representation** is the set of all file objects needed to render an Intellectual Entity. For example, a journal article may be complete in one PDF file; this single file constitutes the Representation. Another journal article may consist of one SGML file and two image files; these three files constitute the Representation. A third article may be represented by one TIFF image for each of 12 pages plus an XML file of structural metadata showing the order of the pages; these 13 files constitute the Representation.

A package can consist of multiple representations. The metadata sitting at the SIP core is metadata that that describes the whole package and all the representations equally.

The representation definition also introduces the concept of the _Intellectual Entity_ (subsequently referred to as IE). Is is also defined in PREMIS:

> An **Intellectual Entity** is a distinct intellectual or artistic creation that is considered relevant to a designated community in the context of digital preservation: for example, a particular book, map, photograph, database, or hardware or software.

IEs tend to describe _intellectual content_. In our suggested implementation of the SIP there is a 1:1 relationship between SIP and IE. The metadata at the core describes the IE that the SIP represents. The representations are different data renditions of the IE. SIPs thus have metadata about and representations of intellectual content.

**Simplified view of E-ARK SIP structure:**

```
SIP
├── metadata
└── representations
    ├── representationID
    │   ├── data
    │   └── metadata
    ├── representationID
    │   ├── data
    │   └── metadata
    ├── ...
    │   ├── ...
    │   └── ...
    └── representationID
        ├── data
        └── metadata
```

## Intellectual entity and catalogs
Intellectual entities is also a concept we find in the various metadata systems outside the digital preservation environment. I'm going to refer to these metadata systems as _asset management systems_ for the purposes of this text[^1].

[^1]: I could called these systems "metadata systems", "collection management systems", "catalogs" etc. The point is that they are systems (in a wider sense) outside of the digital preservation environment, that manages the primary descriptive metadata for data objects within the digital preservation environment. 

In our asset management systems, we tend to operate with a lot of different IEs, usually organised in some sort of hierarchy. In use-case examples of PREMIS and E-ARK, it is usually the highest level entity from these hierarchies, that is referred to as the IE and used to define _intellectual scope of packages_, ie. a *work* or *expression*. However, we find this impractical for a variety of reasons.

As an example, one of our more extensive intellectual hierarchies is found in our audiovisual catalog. It is a 4-level hierarchy based on the IFLA LRM and EN15907 conceptual models. It consist of these entities:
- Work-expression
- Manifestation
- Item
- Carrier

This is a data model made for describing intellectual _content_. The 3 top level entities all describe abstract concepts in some manner. The carrier is the only entity describing a tangible object in this hierarchy.

The more abstract a concept an IE describes, the more open it is to subjective interpretation. These entities are thus often subject to changes in their asset management systems. Content is reinterpreted, new information appears, work definitions change, new work-expressions and manifestations are identified, and even items (which describes logical units of carriers) can be split or have its carriers rearranged. Furthermore cataloging rules and data models can be modified or replaced.

Such intellectual hierarchies are not set in stone, but rather in constant flux. Despite all of this, our carriers will very rarely be split or merged, due to their inherent tangible nature.

We _could_ model multiple complex hierarchies of IEs in PREMIS, but this would introduce a difficult complication of ever-changing package structures in our digital preservation environment. It will increase the complexity of managing the relationships between SIPs and AIPs over time. We prefer if the data in our packages and representations do not have to move between packages and representations, due to external metadata changes.

We do not want to mirror and manage entire hierarchical catalogs in the preservation environment. Instead, we would prefer to keep the information packages in a flat structure. We also find it beneficial to operate with a 1:1 relationship between information packages and some IE in an external Asset Management system. This is to avoid operating with unique metadata "sizes" in the preservation environment, as well as to ease the metadata ingest processes.

### Carrier

To create a flat structure in the digital preservation environment, we intend to define SIP scope using IE describing the _smallest_ described size in any of our asset management systems. I'm going to refer to this size as the _carrier_ for the purposes of this text, even though it is not necessarily called a carrier in all of our asset management systems.

The reason for wanting to use the carrier, is because it represents an actual tangible object, and, as such, it is a _persistent_ Intellectual entity in our asset management systems.

In an analog context the carrier refers to a single book, a single paper photo, or a single film reel. In a digital context the carrier concept refers to a digital objects. It can refer to both _simple digital objects_ (discrete individual files), as well as _complex digital objects_[^2](groups of files). For a digital book it tends to refers to the whole "book" (a PDF, or a sequence of images per page, etc), for digital photos it tends to refer to a single TIFF, and for a film scan it refers to a single DPX _sequence_. 

[^2]: Higgins, Sarah. “The DCC Curation Lifecycle Model.” *International Journal of Digital Curation*, vol. 3, no. 1, Dec. 2008, pp. 134–40. DOI.org (Crossref), [https://doi.org/10.2218/ijdc.v3i1.48](https://doi.org/10.2218/ijdc.v3i1.48).


We can try to simplify it even further, some package owners[^3] will not operate with a complex Asset Management System, and will thus not operate with a size easily recognisable as a carrier entity. However, every preservation package needs a unique identifier to function as key between the environments outside digital preservation and the package. We could adopt the carrier concept in a quite abstract sense here, to mean the size referred to using such an identifier key. In our asset management systems that identifier is typically the unique carrier ID (usually a URN).

[^3]: The environment delivering SIPs and owning their content

Again, the scope of carriers can vary, its size is defined by what is a practical level of description in a given asset management system. If it makes sense to describe multiple individual objects as one carrier, you can do that (with all pros/cons that follow). _The carrier scope definition is the responsibility of the package owner._ In the digital preservation environment a SIP will be accepted regardless of its complexity or lack thereof.

## Representation and carrier
Operating with the carrier as our IE, the _representation_ is then what is needed to render the _whole_ of the carrier. 

It is important to keep in mind _what kind_ or _which_ carrier we want to use as IE to define package scope. We are talking about a digital carrier that describe the digital object (simple or complex) that is contained in the preservation package. 

In the case of analog materials having been digitised we are referring to the digital carrier that describes the digital _derivate_, **not** the carrier representing the analog _original_ it has been derived from.

If we for example digitise a film reel, producing both an image sequence and a sound stream, whether it should be structured as one SIP with one representation (containing both sound and image), or whether we describe it as two SIPs with one representation each, depends on how the carrier(s) is described by the package owner in the asset management system. 

In a use-case where the sound and image is described using a single carrier, the option of creating one package with two representations (one for sound and one for images), is no longer relevant. Neither of those representations represent the whole of the carrier. The higher-level entities used as IEs, and the more abstract concepts these describe, the more complex your SIPs become.

Another reason for going down this route is that we need a flexible model. Some packages stem from package owner environments that are completely flat. Package owners do not necessarily operate with data in intellectual hierarchies. It is beneficial to keep the package scope definition as general as possible across material types. Generalist solutions allow more unified interfacing for all materials.

## SIPs, representations and versioning/updates
In practical terms, this means the logic surrounding whether content of a received SIP should be dealt with as a new package, new files being added to an existing package, or existing files in an existing package being updated, lies with the package owner. Usually through metadata practices in an asset management system.

For example: if a new digital object is dealt with as a new carrier in an asset management systems, it needs to be a new package. If it is described using an existing carrier entity in the asset management systems, then the new files would either need to be added to an existing package, or existing files needs to be updated/versioned. 

The vast majority of such operations would lead to the creation of new packages, as well as updates to core metadata for existing packages.

Over time format migrations for preservation purposes will result in new representations, with new data appearing within existing packages.

The usual practice in our asset management systems is to create new carriers when new digitisations are made, but there are instances where we would do mere updates. Versioning of core metadata will be a common occurrence, while versioning of already existing representations and their data will happen very rarely. All additions and file changes will be handled using OCFL.

## Representation structure
Within the representation folders data and representation metadata will sit in their own folders. The file structure within those folders will be defined by the various package owners. It should allow for human identification of its content and be understandable with minimal effort in the long term.

