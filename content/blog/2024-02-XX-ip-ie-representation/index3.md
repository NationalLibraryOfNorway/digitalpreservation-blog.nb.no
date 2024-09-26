---
title: Intellectual package scope, intellectual entities and representations
summary: This post discusses some key concepts related to information package scope and the eArchviving standards and specifications.
draft: true
category: blog
date: 2024-09-23
tags: [Information packages, IP, E-ARK, eArchiving, asset management, cataloging]
author: [Torbjørn Pedersen]
cover:
  image: earkip.webp
  hiddenInList: false
  relative: true
showtoc: true
---

Standardizing preservation package structures is crucial for managing high-volume digital preservation. 
This text proposes a practical interpretation of eArchiving standards, focusing on intellectual entities and package scope for Submission and Archival Information Packages (SIP/AIP). 
We present an approach that balances standardization needs with the realities of diverse digital objects and metadata management, examining how intellectual entities, representations, and "carriers" can define a flexible yet consistent SIP/AIP scope framework.

## Background
In our strategy we have defined standardization of how we work as a [strategic area of focus](/docs/strategy/nln-digipres-strategy-en/#strategic-areas-of-focus).
This aim includes all aspects of our digital preservation work, and stems from the constant high volumes of data flowing through and being managed by our systems.
To deal with these volumes, we are reliant on automation, which in turn requires standardization to be effective.

One of the core things to standardize is the formatting of our *preservation packages*.
In short though, we need to have a clear understanding of the different *kinds* of digital objects we are operating with and the kind of *sets* of objects we want to put in each information package.

## eArchiving standards and specifications

To standardize our package structures we are working towards implementing the [eArchiving standards and specification](https://dilcis.eu "Website with standards and specifications for E-ARK") developed in the [E-ARK project](https://www.eark-project.com "Link to the E-ARK project website, historic and not updated").
This is also stated in our newly revised [digital preservation principles](/docs/principles/nln-digipres-principles-en/#use-a-standardized-format-to-package-files-for-preservation "Section discussing format for packaging files for preservation").
In the end we hope to have a standardized package structure specification for all *cultural heritage objects* that the National Library deals with.
In the long-term, if feasible, we will try to define one or multiple eArchiving Content Information Type Specifications (CITS) or Content Profiles (like [Meemoo](https://developer.meemoo.be/docs/diginstroom/sip/2.0/profiles/ "Meemoo's SIP content profiles") has done) for our relevant content types.

The eArchiving specifications and standards operate with different information packages.
This document attempts to define a practical interpretation of key concepts in relation to logical Submission Information Packages (SIPs).
The suggested SIP scope allows for AIP and DIP creation in a manageable manner.

The key concepts discussed is the intellectual entity used to define logical package scope, as well as the representation level below it.

## SIP mirrors intellectual Entity

In the E-ARK SIP specification a SIP is a package holding *metadata* and *representations*.
The representations are again composed of *data* and *metadata* of their own.
The representation concept is defined in PREMIS:

> A **Representation** is the set of all file objects needed to render an Intellectual Entity.
> For example, a journal article may be complete in one PDF file; this single file constitutes the Representation.
> Another journal article may consist of one SGML file and two image files; these three files constitute the Representation.
> A third article may be represented by one TIFF image for each of 12 pages plus an XML file of structural metadata showing the order of the pages; these 13 files constitute the Representation.

A package can consist of multiple representations.
The metadata sitting at the SIP core, is metadata that that describes the whole package and all the representations equally.

The representation definition also introduces the concept of the *Intellectual Entity* (subsequently referred to as IE).
It is also defined in PREMIS:

> An **Intellectual Entity** is a distinct intellectual or artistic creation that is considered relevant to a designated community in the context of digital preservation: for example, a particular book, map, photograph, database, or hardware or software.

IEs tend to describe *intellectual content*.
In our suggested implementation of the SIP there is a 1:1 relationship between SIP and IE.
The metadata at the core describes the IE that the SIP represents.
The representations are different data renditions of the IE.
SIPs thus have metadata about and representations of intellectual content.
Representations do not have discrete descriptive metadata.

### Simplified view of E-ARK SIP structure

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

## Intellectual entities, catalogs and asset management systems

Intellectual entities is also a concept we find in the various metadata systems outside the digital preservation environment. It is our asset management systems that is the authoritative "truth" for descriptive metadata, while the preservation environment holds a copy of it.
I'm going to refer to these metadata systems as *asset management systems* for the purposes of this text[^1].

[^1]: I could have called these systems "metadata systems", "collection management systems", "catalogs" etc.
      The point is that they are systems (in a wider sense) outside of the digital preservation environment, that manages the primary descriptive metadata for data objects within the digital preservation environment. 

In our asset management systems, we tend to operate with a lot of different IEs, usually organized in some sort of hierarchy.

In use-case examples of PREMIS and E-ARK, it is usually the highest level entity from these hierarchies, that is referred to as the IE and used to define *intellectual scope of packages*, ie. a *work* or *expression*.
However, we find this impractical for a variety of reasons.

As an example, one of our more extensive intellectual hierarchies is found in our audiovisual catalog.
It is a 4-level hierarchy based on the IFLA LRM and EN15907 conceptual models.
It consist of these entities:

```text
┌───────────────┐
│WORK-EXPRESSION│
└───────┬───────┘
        │0..n
        │
        │
        │0..n
┌───────┴───────┐
│ MANIFESTATION │
└───────┬───────┘
        │1
        │
        │
        │0..n
┌───────┴───────┐
│     ITEM      │
└───────┬───────┘
        │0..1
        │
        │
        │1..n
┌───────┴───────┐
│    CARRIER    │
└───────────────┘
```

This is a data model made for describing intellectual *content*.
The 3 top level entities all describe abstract concepts in some manner.
The carrier is the only entity describing a tangible object in this hierarchy.

The more abstract a concept an IE describes, the more open it is to subjective interpretation.
These entities are thus often subject to changes in their asset management systems.
Content is reinterpreted, new information appears, work definitions change, new work-expressions and manifestations are identified, and even items (which describes logical units of carriers) can be split or have its carriers rearranged.
We also have a lot of *orphaned* carriers without identified content, which are not (yet) attached to higher-level entities of description.
Furthermore, cataloging rules and data models can be modified or replaced.

Such intellectual hierarchies are not set in stone, but rather in constant flux.
Despite all of this, our carriers will very rarely be split or merged, due to their inherent tangible nature.

We *could* model multiple complex hierarchies of IEs in PREMIS, but this would introduce a difficult complication of ever-changing package structures in our digital preservation environment.
It would also potentially create very large packages including a multitude of representations and files.
It will increase the complexity of managing the relationships between SIPs and AIPs over time.
We prefer if the data in our packages and representations do not have to move between packages and representations, due to external metadata changes.

We also do not want to mirror and manage entire hierarchical catalogs in the preservation environment - that is what the asset managements systems are for!
Instead, we would prefer to keep the information packages in a flat structure, with a 1:1 relationship between information packages and some IE in the external Asset Management systems.
This is to avoid operating with unique metadata entities or "sizes" in the preservation environment, as well as to ease the metadata ingest processes.

### Carrier
To create a flat structure in the digital preservation environment, we intend to define SIP scope using the IE representing the *smallest* described size in any of our asset management systems.
I'm going to refer to this size as the *carrier* in this text, even though it is not necessarily called a carrier in all our asset management systems.

The reason for wanting to use the carrier, is because it represents an actual tangible object, and, as such, it is a *persistent* IE in our asset management systems.

In an analog context the carrier refers to a single book, a single paper photo, or a single film reel.
In a digital context the carrier concept refers to digital objects.
It can refer to both *simple digital objects* (discrete individual files), and *complex digital objects*[^3] (groups of files).
For a digital book it tends to refer to the whole "book" (a PDF, or a sequence of images per page, etc.), for digital photos it tends to refer to a single TIFF, and for a film scan it refers to a single DPX sequence or a DCP.

[^3]: Higgins, Sarah. “The DCC Curation Lifecycle Model.” *International Journal of Digital Curation*, vol. 3, no. 1, Dec. 2008, pp. 134–40. DOI.org (Crossref), [https://doi.org/10.2218/ijdc.v3i1.48](https://doi.org/10.2218/ijdc.v3i1.48).

We can try to simplify it even further, some package owners[^4] will not operate with a complex Asset Management System, and will thus not operate with a size recognizable as a carrier entity.
However, every preservation package needs a unique identifier to function as key between the environments outside digital preservation and the package.
We could adopt the carrier concept in an abstract sense here, to mean the size referred to using such an identifier key.
In our asset management systems that identifier is typically the unique carrier ID (usually a URN).

[^4]: The environment delivering SIPs and owning their content. At the present, the only environments deliving SIPs to the DPS and own material in the DPS are internal user environments from the National Library. 

Again, the scope of carriers can vary, its size is defined by what is a practical level of description in a given asset management system.
If it makes sense to describe multiple individual objects as one carrier, you can do that (with all pros/cons that follow).
*The carrier scope definition is the responsibility of the package owner.* 
In the digital preservation environment a SIP will be accepted regardless of its complexity or lack thereof.

## Representation and carrier
Operating with the carrier as our IE, the *representation* is then what is needed to render the *whole* of the carrier.

It is important to keep in mind *what kind* or *which* carrier we want to use as IE to define package scope.
We are talking about a digital carrier that describe the digital object (simple or complex) that is contained in the preservation package.

In the case of analog materials having been digitized, we are referring to the digital carrier that describes the digital *derivate*, **not** the carrier representing the analog *original* it has been derived from.

If we for example digitize a film reel, producing both an image sequence and a sound stream, whether it should be structured as one SIP with one representation (containing both sound and image), or whether we describe it as two SIPs with one representation each, depends on how the carrier(s) is described by the package owner in the asset management system.

In a use-case where the sound and image is described using a single carrier, the option of creating one package with two representations (one for sound and one for images), is no longer relevant.
Neither of those representations represent the whole of the carrier/IE.
The higher-level entities used as IEs, and the more abstract concepts these describe, the more complex your SIPs become.

Another reason for going down this route is that we need a flexible model.
Some packages stem from package owner environments that are completely flat.
Package owners do not necessarily operate with data in intellectual hierarchies.
In addition, we regularly digitize materials before their contents are identified and determined. 
This means we have information at the carrier level, but lack relations to the higher descriptive levels.

By using the carrier to define package scope, we have a model that fits many different descriptions systems.
We can deal with complex and simple descriptive hierarchies in the same way, and thus keep the bar for submitting data for preservation low.

### Carriers and descriptive metadata
What then happens with the descriptive metadata from the higher level IEs of the asset management system? 
The descriptive metadata provided with the carrier should contain the available metadata of the higher descriptive levels, or links/relationships to it. 
We want the data from it's parent records, but not necessarily its siblings.

## SIPs, representations and versioning/updates
In practical terms, this means the logic surrounding whether the content of a received SIP should be dealt with as a new package, new files being added to an existing package, or existing files in an existing package being updated, lies with the package owner, through metadata practices in an asset management system. 

For example: 
- If a new digital object is dealt with as a new carrier (with a new ID) in an asset management system, it needs to be a new package (e.g. a TIFF resulting from a new digitization of a photography).
- If a new digital object is described using an existing carrier entity (with an existing ID) in the asset management systems, then the new files would either need to be:
    - added to an existing package as a new representation (e.g. A jp2 representation is added to a package with a TIFF representation). 
    - existing files in an existing representation would need to be updated/versioned (e.g. a modified TIFF is replacing an existing TIFF).

The usual practice in our asset management systems is to create new carriers when new digitizations are made, but there are rare instances where we would do mere updates.
Versioning of core *metadata* will be a common occurrence, while versioning of already existing representations and their data will happen more rarely. 
All additions and file changes will (most likely) be handled using OCFL and additionally be documented using PREMIS events. 


### Multiple representations
If we perform format migrations for preservation purposes, this will result in new representations with new data appearing within existing packages.
However, if we chose to describe the migrated copy as it's own carrier in the asset management systems (with their own unique ID), these would instead be handled as new packages.

Another typical usecase for multiple representations seem to be access copies, but they would be relatively rare in our environment.
Access copies (proxies) that can easily/automatically be derived from a preserved master file are not kept in our preservation environment, but rather managed on our streaming servers.
Access copies that cannot be readily derived from our master copies are, however, kept in the preservation environment.
An example would be access copies that are the result of labour intensive manual processing (e.g. additional colour correction), but which are not given their own URN in the asset management systems.
At the moment this is the case for digitized photo negatives.

