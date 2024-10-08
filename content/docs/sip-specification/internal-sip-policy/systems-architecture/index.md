---
title: System domain architecture
summary: This post discusses high-level metadata and data handling at the National Library of Norway
date: 2024-09-30
tags: [Systems architecture]
authors: 
  - name: Torbjørn Bakken Pedersen
    image: https://avatars.githubusercontent.com/u/113333557?v=4
images: 
  - arkitektur.pn
weight: 1
aliases: ["/systems-architecture"]
---

The digital preservation team uses the [Open Archival Information system functional model](https://en.wikipedia.org/wiki/Open_Archival_Information_System#The_functional_model "Wikipedia page explaining the OAIS functional model") (OAIS) as a reference point.
However, as our systems architecture is complex and has evolved over several years, you can't simply overlay the OAIS model over our organization and make sense of what is happening.

The digital preservation team develops and manages the Digital Preservation Services (DPS) software, but this is only one aspect of data and metadata management in the National Library.
As we continue to develop the DPS and standardizing information packages, awareness of the different system domains' responsibilities, and how these interact, is essential.

## System domains
The responsibilities for any digital object[^1], in the National Library is spread between a triad of different system domains each holding a part of the "truth":

[^1]: A digital object or asset can encompass both *simple digital objects* (discrete individual files), and *complex digital objects* (groups of files). (Higgins, Sarah. “The DCC Curation Lifecycle Model.” *International Journal of Digital Curation*, vol. 3, no. 1, Dec. 2008, pp. 134–40. DOI.org (Crossref), [https://doi.org/10.2218/ijdc.v3i1.48](https://doi.org/10.2218/ijdc.v3i1.48)).

- **Metadata management systems**
	- Manages descriptive metadata
	- Holds the unique identifier (UID) for digital objects
- **Digital Preservation Services (DPS)** 
	- Manages preservation data
	- Has a copy of descriptive metadata (from metadata management systems)
- **Public access services**
	- Manages access data (derived from preservation data).
	- Manages access descriptive metadata (derived from metadata management systems)

The glue that holds everything together is a UID (typically a URN) shared by all systems, but managed in the metadata management systems.
This needs to be unique across systems and should not be reused.

### Metadata management systems
Our metadata management systems are the authoritative "truth" for descriptive metadata. 
By metadata management systems, we refer to catalogs, registries, asset management systems, collection management systems and so on.
Put very simply, these are systems in a wider sense that manage descriptive metadata for various digital and non-digital objects held by the National Library.

The metadata management systems are the systems used within the organization to find collection objects [^2].
These systems hold the key UID that allows for identification of access and preservation data.

[^2]: Some of these systems are also exposed externally.

### Digital Preservation Services (DPS)
Our Digital Preservation Services manages all data in our bit-repository and controls data integrity and access for long-term storage. 
It is in this environment we operate with the OAIS concepts of SIP and AIP. 
Along with the preserved data we store a *copy* of select descriptive data, to make the digital object identifiable and usable in the long-term.

SIPs received for preservation in the DPS, represents some described entity in the metadata management systems.
The DPS holds the "truth" for technical *file* metadata.

The DPS can be used to identify and find *files* (through technical metadata), but this is still a rare use-case in our organization.

### Public access services
The public access services manages a *harvested* subset of descriptive metadata from our metadata management systems and access *files*.
They disseminate this on our public facing webpages [NB.no](https://www.nb.no/search "National library online portal").
The access files are proxy copies derived from preserved high quality files in the DPS. 
These are typically smaller and lossy derivates of the much larger preservation files in the DPS.

The public access services are our public facing discovery and access systems.
They disseminate a subset of harvested metadata from the metadata management systems and related access data online.

## Architecture
This is an idealized and simplified version of our architecture, but still helpful to understand the kind of systems interactions we deal with.
While we use the OAIS framework to discuss our architecture, the various OAIS components and flows becomes quite abstract in this context[^3]. 

[^3]: You could apply the DIP concept to the public access services' dissemination of access copies, but traditionally we have only used the OAIS terminology in the digital preservation domain.

{{< figure src="arkitektur.svg" alt="architecture diagram" caption="Data and metadata flow between systems" >}}

The SIP in this drawing contains data for preservation in addition to a copy of metadata from the metadata management systems in a standardized format (e.g. MODS).
Our DPS is currently not exposed to the public. 
Any public access to preserved data goes through other internal services built on top of the DPS. 
The DPS does not preserve access copies that can be automatically derived from presservation files. 
Such copies are managed in the public access services.


