---
title: Intellectual entities, representations and assets
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
This text proposes a practical interpretation of intellectual entities and package scope for Submission and Archival Information Packages (SIP/AIP). 
I present an approach that balances standardization needs with the realities of diverse digital objects and metadata management, examining how intellectual entities, representations, and "carriers" can define a flexible yet consistent SIP/AIP scope framework.

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

## SIP and intellectual Entity
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

## National Library architecture
The responsibilities for any digital object in the National Library is spread between a triad of different system domains each holding a part of the "truth":
- **Asset management systems**
	- Manages descriptive metadata
- **Digital Preservation Services**
	- Manages preservation data
	- Has a **copy** of metadata from asset management systems
- **Public access services**
	- Manages access data
	- Has a **copy** of metadata from asset management systems

Our asset management systems is the authoritative "truth" for descriptive metadata in our organization. 
I'm using the term "asset management systems" in this text, but I could have called these "catalogs" or "metadata systems". 
Put very simply, they are systems in a wider sense that manage the metadata of assets.
We have many such systems.

Our Digitial Preservation Services (DPS) manages all data in our bit-repository and controls data integrity and access for long-term storage. 
It is in this environment the standardization of packages is essential. 
Along with the preserved data, we store a copy of select descriptive data to make the digital asset identifiable and usable in the long-term.

Our public access services manages access copies of preserved data on streaming servers. 
These are typically smaller and lossy proxy files of the much larger preservation files in the DPS. 
The public access services also harvests select metadata from our various asset management systems, to provide public access to metadata and access copies on our webpages [NB.no](https://www.nb.no/search "National library online portal").

The glue that holds everything together is a PID (typically a URN) shared by all systems, but managed in the asset management systems.

![architecture drawing](arkitektur.png)

This is an idealized and simplified version of our architecture, but still helpful to understand the kind of systems interactions we deal with.
While we use the OAIS framework to discuss our architecture, the various components and flows becomes quite abstract in this context[^1].

[^1]: You could apply the DIP concept to the public access services' dissemination of access copies, but traditionally we have only used the OAIS terminology in the digital preservation domain.

The SIP in this drawing contains data for preservation in addition to a copy of metadata from the asset management system in a standardized format (e.g. MODS).
Our DPS is currently not exposed to the public, any public access to preserved data goes through other internal services built on top of the DPS first. Access copies that can easily/automatically be derived from a preserved master file are out of principle not preserved in the DPS.

## Intellectual entities across environments
With this context it becomes clear that how we define package scope has wide-ranging concequences.
Our three environments needs to stay in sync somehow and operate with similar concepts.
We do not want to end up in a situation where we have paralell, and possibly opposing, "truths" in different systems.

In our asset management systems, we tend to operate with a lot of different IEs, usually organized in some sort of hierarchy.
In use-case examples of PREMIS and E-ARK, it is usually the highest level entity from these hierarchies, that is referred to as the IE and used to define *intellectual scope of packages*, ie. a *work* or *expression*.

As the essential PID that holds all our systems together sits at the *lowest* level of description in our asset management systems, it seems natural to let this entity define package size.
This has multiple positive side effects:
- Package size is kept small
- Representation ruleset is kept simple
- Package scope definition sits in producer environment
- Ingest requirements are lowered (we only need to describe the technical asset, not its intellectual contents)
- Package restructuring due to descriptive metadata changes are kept to a minimum




