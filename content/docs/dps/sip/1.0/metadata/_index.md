---
title: Metadata primer
weight: 2
---

This page describes the kinds of metadata that exists within an information package, where they should be placed in the information package, and how it is referenced in METS.
A package contains metadata on the root level of the package, as well as on each representation on the representation level of the package.

## Package metadata

### Descriptive metadata

Descriptive metadata describes the intellectual object the package represents (typically an exemplar of a work).
Descriptive metadata can be used to identify and retrieve the intellectual content of the package.
It does not describe specific files.

| File location in SIP         | Example files                  |  METS-element | 
| ------------------------ | ------------------------------ | --------------- | 
| `/metadata/descriptive/` | <ul><li> MODS.xml<br><li> mavisTitle.xml</ul> |  `dmdSec` | 

### Preservation/Digital provenance metadata

Short definition from E-ARK CSIP:
> Digital provenance metadata [...] records digital preservation information, e.g. audit information covering a digital library object’s life-cycle[^1].

On the **package** level preservation and digital provenance metadata describes the origin of the **package**, where it come from and how it has come into being.
Preservation metadata typically describes digital processes, actions and events, and the outcomes of these. 

| File location in SIP        | Example files                  | METS-element | 
| ------------------------ | ------------------------------ | -------------- | 
| `/representations/*/metadata/preservation/` | <ul><li> ScanityTransfer.xml<br><li> MAVIS_film_carrier.xml (ved digitalisering)<br><li> MAVIS_sound_carrier_*.xml (ved digitalisering)<br><li> PREMIS events</ul> | `digiprovMD` |

## Representation metadata (per representation)

### Source metadata

Short definition from E-ARK CSIP:
> Source metadata [...] records descriptive, technical or rights metadata for an analog source for a digital library object.[^1]
 
Source metadata describes the object a representation is derived from.
This is typically metadata about a physical information carrier (e.g. a book, a photography, a film reel) that has been digitized, and its state and condition at the time of digitization. Similarly it can be metadata about a digital object that has been used to derive a different digital object. 

| File location in SIP        | Example files                  | METS-element | 
| ------------------------ | ------------------------------ | -------------- | 
| `/representations/*/metadata/source/` | <ul><li> mavisAnalogCarrier.xml<br><li> mavisAnalogComponent.xml<br><li> mavisDigitalCarrier.xml<br><li> mavisDigitalComponent.xml<br><li> mavisSoundTrackCarrier.xml<br><li> mavisSoundTrackComponent.xml</ul> | `sourceMD` |


### Technical metadata

Short definition from E-ARK CSIP:
> [Technical metadata describes] technical details of the data themselves[^2].

Technical metadata documents measurable, system generated technical properties of the digital files in a representation.
Technical metadata describes what the digital files actually are, based on file analysis. 
Technical metadata **is not** descriptions of the intellectual content of those files, or what has been done to the file/process history.

| File location in SIP        | Example files                  | METS-element | 
| ------------------------ | ------------------------------ | -------------- | 
| `/representations/*/metadata/technical/` | <ul><li> FITS<br><li> MediaInfo<br><li> ExifTool<br><li> JHOVE</ul> | `techMD` |

### Preservation/Digital provenance metadata

Short definition from E-ARK CSIP:
> Digital provenance metadata [...] records digital preservation information, e.g. audit information covering a digital library object’s life-cycle[^1].

On the representation level preservation and digital provenance metadata describes the origin of the **files** in a representation, where they come from and how they have come into being.
Preservation metadata typically describes digitization processes, actions and events, and the outcomes of these. 

| File location in SIP        | Example files                  | METS-element | 
| ------------------------ | ------------------------------ | -------------- | 
| `/representations/*/metadata/preservation/` | <ul><li> ScanityTransfer.xml<br><li> MAVIS_film_carrier.xml (ved digitalisering)<br><li> MAVIS_sound_carrier_*.xml (ved digitalisering)<br><li> PREMIS events</ul> | `digiprovMD` |

[^1]: [Common Specification for Information Packages
v2.2.0 : Use of the METS administrative metadata section (element amdSec)](https://earkcsip.dilcis.eu/#useofthemetsadministrativemetadatasectionelementamdsec)
[^2]: [Common Specification for Information Packages
v2.2.0 : Principle 4.1](https://earkcsip.dilcis.eu/#principle4.1:)
