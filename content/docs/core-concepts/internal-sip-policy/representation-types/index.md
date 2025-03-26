---
title: Representation types
summary: This post discusses high-level metadata and data handling at the National Library of Norway
date: 2024-09-30
tags: [System architecture, PREMIS, Intellectual entities, representations]
authors: 
  - name: Torbjørn Bakken Pedersen
    image: https://avatars.githubusercontent.com/u/113333557?v=4
images: 
  - avsip.png
weight: 4
aliases: ["/representation-types"]
---

Most of the SIPs that are created in our organization only contain one single representation. Secondary representations are also produced, e.g access representation for our website, but there are only a few use-cases where these are stored in the DPS.  

We operate with two types of representations:

## Primary
The initial primary representation is the representation containing the digital object described using an IE in the relevant metadata management system[^1].

[^1]: Not described in our MARC-based systems. See [previous document](/intellectual-sip-scope). 

## Derivatives of the primary representation
Creating multiple representations in one SIP is only relevant if it is especially important to preserve both the primary representation and something derived from it, together in one information package. This might be an access copy, a processed, normalized, format migrated or repaired version of the primary representation. Typically, these are not represented as a separate IE in the metadata system. 

If we for example normalize or convert the primary digital object to another format for preservation, we can preserve both the primary digital object and a presumed more durable representation in the same information package. 

The purpose of a derivative, how it is produced, and how it is related to the primary representation should be documented as preservation metadata in the package. We advise against preserving derivatives that easily and mechanically can be recreated from the primary representation. Access representations may, for example, only be relevant to include in DPS if they are the result of significant work and/or cannot be derived mechanically from the primary representation.  

## Examples:
### Example showing a typical SIP with a single representation
{{< figure src="1repsip.svg" alt="Film digitization SIP with 1 representation" >}}

### Example with two representations
In-house digitization of photo negatives currently produces a large TIFF file for preservation and an inverted and heavily post-processed access JP2-file. 
Only the TIFF is described using a carrier in the metadata management system, but both digital objects are preserved in the DPS.
The JP2 is the result of extensive manual labor and cannot be automatically or easily reproduced from the primary TIFF.

The TIFF file is contained in the primary representation in the SIP, while the JP2 is contained in an access derivate representation.

{{< figure src="tiffjp2.svg" alt="Photo negative digitization SIP with 2 representations" >}}

### Example showing three representation types
An example showing a video master, with an access representation and a representation holding a digital object resulting from a hypothetical format migration/normalization.

{{< figure src="avsip.svg" alt="Video SIP with 3 representations" >}}