---
title: Package scope and representations
weight: 1
---

The DPS is a system designed to receive, safely preserve and disseminate preserved **digital objects**. 
In our terminology a digital object is used synonymously with a digital **representation** of some **intellectual entity**. 

The DPS handles and manages submission, archiving and dissemination of such representations through the exchange of information packages. 
Each information package can contain one or more representations.
To be able to create and submit an information package to the DPS you first need to decide what data to put in a single package.
Each package has an **intellectual scope**, which again defines the **data scope** of each package.

## Representations
The representation concept is defined in PREMIS:

> A **Representation** is the set of all file objects needed to render an Intellectual Entity.
> For example, a journal article may be complete in one PDF file; this single file constitutes the Representation.
> Another journal article may consist of one SGML file and two image files; these three files constitute the Representation.
> A third article may be represented by one TIFF image for each of 12 pages plus an XML file of structural metadata showing the order of the pages; these 13 files constitute the Representation. 

Representations can thus be either **simple objects** consisting of single discrete files, or **composite objects** consisting of groups of files intended to be utilized together. 
An example of a simple digital object can be a singular image in TIFF-format, while an example of a composite digital object can be the aforementioned example of the article represented by 12 TIFF images and an XML or a DCP (which is a directory containing image and audio streams in MXF containers along with xml-files).

## Intellectial entities and content
The following definitions stem from the PREMIS data dictionary:
> An **Intellectual Entity** is a distinct intellectual or artistic creation that is considered relevant to a designated community in the context of digital preservation: for example, a particular book, map, photograph, database, or hardware or software.

Intellectual entities tend to describe **intellectual content**.
To keep complexity down, we recommend letting simple, tangible intellectual entites define package scope (like **items** or **exemplars**), rather than high-level abstract intellectual entities (like **works**).

> [!WARNING]
> We **strongly recommend** limiting the intellectual scope of a package to a particular digital exemplar. 

This means the intellectual entity defining the package scope, and its primary representation is very closely intertwined.
The descriptive metadata on the package root describes the intellectual content of that particular copy.
Most packages will consist of a single representation.

Some examples of package scope for born-digital materials:
- A particular digital image
- A particular digital exemplar of a book
- A particular audio master file of an audio track
- A particular video master file of a feature film

Some examples of package scope for digitized materials:
- A particular scan of a photographic image
- A particular digitization of a book
- A particular digitization of a video tape
- A particular scan of a film reel

In other words a package will contain a particular digital exemplar of a book, not all digitized versions and digital editions of that particular literary work.
Those other exemplars are other discrete intellectual entities and packages.
Similarly a new digitization of a physical source object that has been previously digitized, is handled as a new, discrete intellectual entity and package.

## New package or new representation?

With the intellectual entity and its primary representation so closely defined, the question becomes when to create a new package and when do you create a new representation.

In very simple terms a new representation in our ruleset, is a **technical format variation** of the primary representation. 
If the intellectual scope of a package is an exemplar, the different representations within a package are different variants of **this specific** exemplar.

In the National Library, a new package is typically created when a new digital exemplar is created as an entity in the metadata management systems and given a URN.
The URN identifies the **intellectual entity** that defines the package, and its primary representation.
Secondary representations are format variations derived from the primary representation, that are not deemed different enough to be described in the metadata systems on their own.
All representations within the package are identified by the same URN.

Internally the ruleset is:

- A single URN = a single package
- Multiple URNs = multiple packages

If you only have a single URN but still want to preserve a second or third derivate representation in the DPS, you will create a second representation in the same package as the primary digital representation.

<!-- {{< callout >}}
En ide å si noe om DPS-føringer?

- IDs are given at the package level
- Access control is set at the package level
- Versioning is not permitted (additions?)
- Packages are typically disseminated as a whole
{{< /callout >}} -->

## Examples of representations
Most of the packages that are created in our organization only contain one single representation. Secondary representations are also produced, e.g access representation for our website, but there are only a few use-cases where these are also preserved in the DPS.  

We operate with two types of representations:

### Primary
The initial primary representation is the representation containing the digital object described as an intellectual entity in the relevant metadata management system.

### Derivatives of the primary representation
Creating multiple representations in one package is only relevant if it is especially important to preserve both the primary representation and something derived from it, together in one information package. 
This might be an access copy, a processed, normalized, format migrated or repaired version of the primary representation. Unless of course, these are represented as separate intellectual entities in the metadata system. 

If we for example normalize or convert the primary digital object to another format for preservation, we can preserve both the primary digital object and a presumed more durable representation in the same information package. 

The purpose of a derivative, how it is produced, and how it is related to the primary representation should be documented as preservation metadata in the package. 

> [!IMPORTANT]
> We strongly recommend against preserving derivatives that easily and mechanically can be recreated from the primary representation. 

Access representations may, for example, only be relevant to include in DPS if they are the result of significant work and/or cannot be derived automatically from the primary representation.

### Examples:
#### Example showing a typical package containing a single representation
{{< figure src="1repsip.svg" alt="Film digitization SIP with 1 representation" >}}

#### Example containing two representations
In-house digitization of photo negatives currently produces a large TIFF file for preservation and an inverted and heavily post-processed access JP2-file. 
Only the TIFF is described using a carrier in the metadata management system, but both digital objects are preserved in the DPS.
The JP2 is the result of extensive manual labor and cannot be automatically or easily reproduced from the primary TIFF.

The TIFF file is contained in the primary representation in the SIP, while the JP2 is contained in an access derivate representation.

{{< figure src="tiffjp2.svg" alt="Photo negative digitization SIP with 2 representations" >}}

#### Example containing three representations
An example showing a video master, with an access representation and a representation holding a digital object resulting from a hypothetical format migration/normalization.

{{< figure src="avsip.svg" alt="Video SIP with 3 representations" >}}
