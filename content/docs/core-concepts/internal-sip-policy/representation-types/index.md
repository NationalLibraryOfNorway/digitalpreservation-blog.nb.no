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

Most of our in-house SIPs will only contain a single representation. 
Secondary representations are produced in the organization, but there are only a few use-cases where these are stored in the DPS.

We operate with three types of representations:

## Primary
The initial primary representation is the representation containing the digital object described using an IE in the relevant metadata management system[^1].

[^1]: Not described in our MARC-based systems. See [previous document](/intellectual-sip-scope). 

## Access derivate
Access derivate representations are used for digital objects derived from the digital object in the *primary* representation, to provide easier access. 
They are used as a proxy/stand-in for the primary representation.
They typically contain much smaller, lossy (or lossier) files.

Any representation can in theory have an access representation, but these are primarily managed and stored in the public access environment alone.
Access representations are only kept in the DPS if they are the result of significant labor and/or cannot be easily derived from the primary representation.
The public access environment, on the other hand, only supports a single access representation per UID.

## Preservation derivate
In the case where the primary digital object is normalized or converted to a different format for preservation, you can use the preservation derivate representation type.
This enables us to preserve both the primary digital object and its preservation derivate.
Currently, this is more of a hypothetical use-case, than something that regularly happens in the organization.

Below are a few examples showing typical SIPs with representations:

## Examples:
### Example showing a typical SIP with a single representation
{{< figure src="1repsip.svg" alt="Film digitization SIP with 1 representation" >}}

### Example with two representations
In-house digitization of photo negatives currently produces a large TIFF file for preservation and an inverted and heavily post-processed access JP2-file. 
Only the TIFF is described using a carrier in the metadata management system, but both digital objects are preserved in the DPS.
The JP2 is the result of extensive manual labor and cannot be automatically or easily reproduced from the primary TIFF.

The TIFF file is contained in the primary representation in the SIP, while the JP2 is contained in an access derivate representation.

{{< figure src="tiffjp2.svg" alt="Photo negative digitization SIP with 2 representations" >}}

### Example showing all three representation types
An example showing a video master, with an access representation and a representation holding a digital object resulting from a hypothetical format migration/normalization.

{{< figure src="avsip.svg" alt="Video SIP with 3 representations" >}}