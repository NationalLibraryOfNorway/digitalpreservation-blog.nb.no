---
title: Intellectual scope of SIPs
summary: This post discusses some key concepts related to information package scope and the eArchviving standards and specifications
date: 2024-10-04
tags: [Information packages, IP, E-ARK, eArchiving, asset management, cataloging]
authors: 
  - name: Torbjørn Bakken Pedersen
    image: https://avatars.githubusercontent.com/u/113333557?v=4
images: 
  - ie-sip.png
weight: 3
aliases: ["/intellectual-sip-scope"]
---

In the previous text, the complicated nature of the representation was highlighted.
To understand the complexity in our organizational architecture better we first need to examine how our metadata management systems are modeled.

## Intellectual entities in the metadata management systems
Intellectual entities (IE) is a concept we find in the various metadata systems outside the digital preservation environment. 
In these systems, we tend to operate with a lot of different IEs, usually organized in some sort of hierarchy.

In use-case examples of PREMIS and E-ARK, it is usually the highest level entity from these hierarchies, that is referred to as the IE and used to define *intellectual scope of packages/SIPs*, i.e. a *work* or *expression*.
However, we have to define scope differently, using an entity that sits at a lower level of description: 

- SIP scope is defined by the metadata management system IE that holds the UID linking the IE to the SIP. 

This is a necessity for keeping all components of our [system architecture](/system-architecture) in sync.
The UID sits at specifically defined IEs in our metadata management systems.

## Hierarchies and flatness
A change in architecture could open for using a different key UID placed at a different location of these metadata hierarchies.
However, we believe it is impractical to do so as it introduces multiple issues related that prohibits scale across our systems.

Intellectual scope defined by abstract high-level entities introduce different challenges with:
- Vast package sizes (dozens of terabytes)
- Huge number of representations within SIPs
- Content description metadata changes leading to restructuring of stored data
- Preservation of unidentified digital objects having no relationships to IEs holding the key UID
- Increased complexity in keeping our three system domains in sync

Some of this complexity stems from complex metadata structures found in our metadata management systems.
We do not want to mirror and manage entire hierarchical catalogs in the preservation environment. This is after all what the metadata managements systems excels at!

We prefer keeping the structure of information packages in a flat structure, with a 1:1 relationship between information packages and a tangible IE in the metadata management systems.
This is to avoid operating with unique metadata entities or "sizes" in the preservation environment, as well as to ease the metadata ingest processes.

## Intellectual package scope
The ruleset we end up with is thus:

- A **data object** is described as an **IE** in the metadata management systems.
- The **data object** is packaged as the **primary representation** in a **SIP**
- The **SIP** and the **IE** share a **URN**, managed in the metadata management system.
- Any new digital object is described as a new **IE**, which receives a **new URN**, and thus has to be represented as a primary representation in a **new SIP**

Due to how URNs link everything together, the ruleset deciding whether you should create a new SIP or a new representation, lies in the metadata management domain.
- A single URN = a single SIP
- Multiple URNs = multiple SIPs

If you only have a single URN but still want to preserve a second derivate digital object in the DPS, you will create a second representation in the same SIP as the primary digital object.

{{< figure src="ie-sip.svg" alt="Diagram showing relationship between IE in metadata management system and SIP in DPS" caption="IE to SIP/IE relationship" >}}

## Metadata management system IEs
In our systems the essential UID that holds all our systems together sits or refers to the *lowest* level of description in our asset management systems.

Our more complex metadata management systems (e.g. Axiell Collections), are advanced asset management systems and describe the actual data object in technical detail using a *carrier* IE. The URN identifies the carrier IE, and in extension the SIP.

Our MARC-based metadata management systems (e.g. Alma), use the URN to *link* to the SIP and it's primary representation, while not actually describing the data object in the metadata management system. 
The URN identifies the SIP, but not the record holding the URN.

Using the smallest size of description has multiple positive side effects:
- Package size is kept small
- Representation ruleset is kept simple
- Package scope definition sits in producer environment
- Ingest requirements are lowered (we only need to describe the technical asset, not its intellectual contents)
- Package restructuring due to descriptive metadata changes are kept to a minimum


