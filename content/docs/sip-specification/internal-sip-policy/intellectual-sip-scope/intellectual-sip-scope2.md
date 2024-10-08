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
weight: 3
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

## Intellectual entities in metadata management systems

In our asset management systems, we tend to operate with a lot of different IEs, usually organized in some sort of hierarchy.
In use-case examples of PREMIS and E-ARK, it is usually the highest level entity from these hierarchies, that is referred to as the IE and used to define *intellectual scope of packages*, ie. a *work* or *expression*.

As the essential PID that holds all our systems together sits at the *lowest* level of description in our asset management systems, it seems natural to let this entity define package size.
This has multiple positive side effects:
- Package size is kept small
- Representation ruleset is kept simple
- Package scope definition sits in producer environment
- Ingest requirements are lowered (we only need to describe the technical asset, not its intellectual contents)
- Package restructuring due to descriptive metadata changes are kept to a minimum


---

To summarize we need to have a 1:1 relationship between: 
- the metadata management system IE holding the unique identifier linking everything together, and 
- the SIP/IE identified by that same unique Identifier

## Complex example
As an example, one of our more extensive intellectual hierarchies is found in our audiovisual catalog.
It is a 4-level hierarchy based on the [IFLA LRM](https://repository.ifla.org/handle/20.500.14598/40 "link to the IFLA Library Reference model") and [EN15907](https://filmstandards.org/fsc/index.php/EN_15907 "Link to the EN15907 landing page on filmstandards.org") conceptual models.
It consist of these core intellectual entities:

```txt
┌───────────────┐
│WORK-EXPRESSION│
└───────┬───────┘
┌───────┴───────┐
│ MANIFESTATION │
└───────┬───────┘
┌───────┴───────┐
│     ITEM      │
└───────┬───────┘
┌───────┴───────┐
│    CARRIER    │
└───────────────┘
```

This is a data model made for describing intellectual *content*.
The 3 top level entities all describe abstract concepts in some manner.
The carrier is the only entity describing a tangible object in this hierarchy.

### IE to SIP relation
The more abstract a concept an IE describes, the more open it is to subjective interpretation.
These entities are thus often subject to changes in their metadata management systems.
Content is reinterpreted, new information appears, work definitions change, new work-expressions and manifestations are identified, and even items (which describes logical units of carriers) can be split or have its carriers rearranged.
We also have a lot of *orphaned* carriers without identified content, which are not (yet) attached to higher-level entities of description.
Furthermore, cataloging rules and data models can be modified or replaced.

Such intellectual hierarchies are not set in stone, but rather in constant flux.
Despite all of this, our carriers will very rarely be split or merged, due to their inherent tangible nature.

We *could* model multiple complex hierarchies of IEs in PREMIS, but this would introduce a difficult complication of ever-changing package structures in our digital preservation environment.

- It would also potentially create very large packages including a multitude of representations and files.
  - E. g. one of our larger audiovisual work records could end up having 30+ primary representations alone (with complex interrelations), with a data volume of *dozens of terabytes*.
- It will increase the complexity of managing the relationships between metadata management systems and the DPS over time.

We prefer if the data in our packages and representations do not have to move between packages and representations, due to external metadata changes.

We also do not want to mirror and manage entire hierarchical catalogs in the preservation environment (that is what the metadata managements systems excels at!).

Instead, we would prefer to keep the information packages in a flat structure, with a 1:1 relationship between information packages and an IE in the external metadata management systems.
This is to avoid operating with unique metadata entities or "sizes" in the preservation environment, as well as to ease the metadata ingest processes.

To summarize we need to have a 1:1 relationship between: 
- the metadata management system IE holding the unique identifier linking everything together, and 
- the SIP/IE identified by that same unique Identifier

To complicate things the metadata management systems IE holding the unique ID (URN) linking our three system domains together is doing this in two slightly different ways:

### Unique IDs in our non-MARC metadata systems
In our non-MARC based metadata systems the unique identifier linking the different system environments together sits at the IE representing the *smallest* described size in any of our asset management systems.
I'm going to refer to this IE as the *carrier* in this text, even though it is not necessarily called a carrier in all our asset management systems.
Digital carriers describe *digital objects*.

These metadata management systems handle both non-digital and digital carriers, and relate the carrier *resulting* from digitization to the *digitized* carrier.
In many ways, the carrier concept is similar to the representation concept in PREMIS.
The digitization of non-digital carriers is one of the driving forces behind the decision to use the carrier instead of a higher-level IE for defining SIP scope.

In the metadata management systems, you could say that the digitized carrier *represents* its higher level IEs, while it is also *represented* by the carrier resulting from digitization.
For born-digital materials on the other hand, this analogy does not work. 
Here the born-digital material only represents its higher level IE.

- FÅ INN NOE OM AT EN BÆRER OFTE BARE ER EN DEL AV VERKET
- fra meeemoo: https://arc.net/l/quote/zupkchko "Typically, something that has individual descriptive metadata at the source (e.g. an entry in a collection registration or asset management system) and is expected to be distinguishable in search, should be viewed as an IE."
- få inn noe om at alle bærere kan ha en påsynskopi (ikke beskrevet i MMS)

Due to the streamlining of digitization efforts we often digitize carriers without identified content.
This means we digitize *orphaned* carriers, that is, carriers that are not attached to the content description hierarchies' higher-level IEs.
 
Similarly, to streamline preservation ingest workflows we also need to handle orphaned digital carriers.

{{< figure src="ie-to-ie.svg" alt="Diagram showing carrier mirroring SIP" >}}

### IE and primary representation
- A *data object* is described as a carrier in the metadata management systems.
- The *data object* is packaged as the primary representation in a SIP

- The SIP and the digital carrier shares a unique ID, managed in the metadata management system.
- Any new digital carrier receives a new unique ID, and thus has to be represented as a primary representation in a new SIP

### Secondary representations
Secondary representations *are* produced in the organization though, but there are only a few use-cases where these are stored in the DPS.

Any digital carrier can have an access/proxy representation, but these are primarily managed and stored in the public access environment alone.
Access representations are only kept in the DPS if they are the result of significant labour and/or cannot be easily deprived from the preservation representation.

The only other type of secondary representation stored in the DPS are representations produced as a result of file normalization and/or format migration, where we also keep the original representation


However, the carrier is also an IE in itself.

```txt
SKISSE AV SIPer opp mot Carrier
```




WE ONLY ACCEPT THREE TYPES OF REPRESENTATIONS
- PRIMARY PRESERVATION REPRESENTATION
- ACCESS REPRESENTATION (at the moment only labour-intensive ones)
- FORMAT MIGRATIONS/NORMALIZATIONS OF OTHER REPRESENTATIONS



### Unique IDs in the MARC-based metadata systems

