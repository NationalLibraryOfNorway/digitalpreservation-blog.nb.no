---
title: System domain architecture
summary: This post discusses high-level metadata and data handling at the National Library of Norway
date: 2024-09-30
tags: [System architecture]
authors: 
  - name: Torbjørn Bakken Pedersen
    image: https://avatars.githubusercontent.com/u/113333557?v=4
images: 
  - arkitektur.png
weight: 1
aliases: ["/system-architecture"]
---

The National library use the [Open Archival Information System functional model](https://en.wikipedia.org/wiki/Open_Archival_Information_System#The_functional_model "Wikipedia page explaining the OAIS functional model") (OAIS) as a reference point in digital preservation.
However, as our system architecture is complex and has evolved over several years, you can't simply overlay the OAIS model over our organization and make sense of what is happening.

<!-- {{% details title="OAIS terminology" closed="true" %}}

{{% /details %}} -->

The digital preservation team develops and manages the Digital Preservation Services (DPS) software, but this is only one aspect of data and metadata management in the National Library.
As we continue to develop the DPS and standardizing information packages, awareness of the different system domains' responsibilities, and how these interact, is essential.

## System domains
The responsibility for any digital object[^1], in the National Library is spread between a triad of different system domains, each managing different aspects of the object:


- **Metadata management systems**
	- Manages descriptive metadata
	- Manages the unique identifier (UID) for digital objects
- **Digital Preservation Services (DPS)** 
	- Manages preservation data
	- Has a copy of descriptive metadata (from metadata management systems)
- **Public access services**
	- Manages access data (derived from preservation data).
	- Manages access descriptive metadata (derived from metadata management systems)

The glue that holds everything together is a UID (typically a URN) used across systems, but managed in the metadata management systems.
This needs to be unique across systems and should not be reused.

### Metadata management systems
Our metadata management systems are masters and authoritative source for descriptive metadata in the National Library. 
By metadata management systems, we refer to catalogs, registries, asset management systems, collection management systems and so on.
Some examples of such systems currently in use are Alma, Mavis and Hanske.
Put very simply, these are systems in a wider sense that manage descriptive metadata for various digital and non-digital objects held by the National Library.

The metadata management systems are the systems used within the organization to find collection objects [^2].
These systems hold the key UID that allows for identification of access and preservation data.


### Digital Preservation Services (DPS)
Our Digital Preservation Services manage all data in our bit-repository and controls data integrity and access for long-term storage. 
It is in this environment we operate with the OAIS concepts[^4] of SIP, AIP, DIP, etc. 
Along with the preserved data, we store a *copy* of select descriptive data, to make the digital object identifiable and usable in the long term.

SIPs received for preservation in the DPS, represents some described entity in the metadata management systems.
The DPS is the master and authorative source for technical *file* metadata in the National Library.

The DPS can be used to identify and find *files* (through technical metadata), but this is still a rare use-case in our organization.

### Public access services
The public access services manage a *harvested* subset of descriptive metadata from our metadata management systems and access *files*.
The main public access services are: [Nettbiblioteket](https://www.nb.no/search "link to nettbiblioteket on nb.no"), which allows you to *search* and *access* a selection of digital objects from our digital collections; and [Oria](http://nb.oria.no/ "link to the Oria search service"), which lets you *search* our printed collections.

The access files are proxy copies derived from preserved high-quality files in the DPS. 
These are typically smaller and lossy derivates of the much larger preservation files in the DPS.

The public access services are our public facing discovery and access systems.
They disseminate a subset of harvested metadata from the metadata management systems and related access data online.

## Architecture
This is an idealized and simplified version of our architecture, but still helpful to understand the kind of system interactions we deal with.
While we use the OAIS framework to discuss our architecture, the various OAIS components and flows becomes quite abstract in this context[^3]. 


{{< figure src="arkitektur.svg" alt="architecture diagram" caption="Data and metadata flow between systems" >}}

The SIP in this drawing contains data for preservation in addition to a copy of metadata from the metadata management systems in a standardized format (e.g. MODS).
Our DPS is currently not exposed to the public. 
Any public access to preserved data goes through other internal services built on top of the DPS. 

The DPS does not preserve access copies that can be automatically derived from preservation files. 
Such copies are managed in the public access services.

[^1]: A digital object or asset can encompass both *simple digital objects* (discrete individual files), and *complex digital objects* (groups of files). An example of a simple digital objects can be singular images in TIFF-format, while an example of a complex digital object can be a DCP (which is a directory containing image and audio streams in MXF containers and xml-files) (Higgins, Sarah. “The DCC Curation Lifecycle Model.” *International Journal of Digital Curation*, vol. 3, no. 1, Dec. 2008, pp. 134–40. DOI.org (Crossref), [https://doi.org/10.2218/ijdc.v3i1.48](https://doi.org/10.2218/ijdc.v3i1.48)).
[^2]: Some of these systems are also exposed externally.
[^3]: You could apply the DIP concept to the public access services' dissemination of access copies, but traditionally, we have only used the OAIS terminology in the digital preservation domain.
[^4]: <mark>LENKE TIL OAIS-DOKUMENT</mark>

