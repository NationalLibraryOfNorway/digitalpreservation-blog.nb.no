---
title: Intellectual entities and representations
summary: This post discusses some key concepts related to information package scope and the eArchviving standards and specifications.
draft: true
date: 2024-09-23
tags: [Information packages, IP, E-ARK, eArchiving, asset management, cataloging]
authors: 
  - name: Torbjørn Bakken Pedersen
    image: https://avatars.githubusercontent.com/u/113333557?v=4
images: 
  - earkip.webp
weight: 2
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

In our asset management systems, we tend to operate with a lot of different IEs, usually organized in some sort of hierarchy.
In use-case examples of PREMIS and E-ARK, it is usually the highest level entity from these hierarchies, that is referred to as the IE and used to define *intellectual scope of packages*, ie. a *work* or *expression*.

As the essential PID that holds all our systems together sits at the *lowest* level of description in our asset management systems, it seems natural to let this entity define package size.
This has multiple positive side effects:
- Package size is kept small
- Representation ruleset is kept simple
- Package scope definition sits in producer environment
- Ingest requirements are lowered (we only need to describe the technical asset, not its intellectual contents)
- Package restructuring due to descriptive metadata changes are kept to a minimum




