---
title: Data management
weight: 2
aliases:
  - /docs/services/dps/data/
---

## What is data?

The Digital Preservation Service (DPS) is a set of services designed to preserve digital information. Within the DPS context, we distinguish between *data* and *metadata*. **Data** refers to the digital content being preserved, such as documents, images, audio and video recordings, or database exports. **Metadata** describes the data by providing information about its content, structure, context, and management. DPS does not accept metadata without the associated data.  

Before data can be transferred to DPS, it must be packaged as a Submission Information Package (SIP)[^1] in accordance with the [SIP specifications](/docs/dps/sip/). Within a SIP, the digital content is stored in a dedicated data directory. The METS.xml files, metadata directories, schemas, and supporting documentation located outside the data directory define the package structure, making its contents machine-readable and verifiable. The [E-ARK specifications](https://dilcis.eu/specifications) define where each file type belongs within the preservation package. This standardized structure makes it easier to locate, interpret, and reuse the preserved content in the future. 

## Choosing what to preserve

Neither DPS nor the Digital Preservation team determines whether digital objects are suitable for long-term preservation. The Producer is responsible for selecting what should be preserved. This selection takes place at two levels:  

- **Agreement level**: The National Library and the Producer establish a preservation agreement for the use of DPS. A single preservation agreement may include one or more access agreements, which define who is authorized to transfer content to DPS and who is permitted to access the preserved content.
- **Object level**: The Producer decides which digital objects are submitted to DPS for preservation.

At the agreement level, the preservation agreement defines the types of content that may be transferred and the terms under which they are preserved. DPS does not automatically verify that each individual object complies with the preservation agreement. Instead, the system assumes that all submissions are made in accordance with the agreed terms. 

Once content has been submitted under a preservation agreement, DPS is responsible for ensuring that it is preserved unchanged, remains authentic, and continues to be accessible over time, regardless of which files the Producer has chosen to submit. 

When selecting digital objects and file formats for preservation, Producers are encouraged to follow the [Principles for Digital Preservation](/docs/principles/).

## How data enters the DPS

Data is transferred to DPS by submitting Submission Information Packages (SIPs) through the Submission Service. Before a submission can be made, the submitter authenticates with the API. The API verifies that the submitter has the necessary permissions under the applicable preservation agreement (see [role-based access control](/docs/dps/access-control/)). 

The submission workflow consists of the following steps: 

Create a submission → Register the files that make up the SIP → Upload the file contents → Upload the file contents.  

A submission is accepted for preservation only if it complies with the [SIP structure requirements](/docs/dps/sip/structure-requirements/), the [METS.xml requirements](/docs/dps/sip/mets/), and the [API requirements](/docs/dps/api/submission/). Submissions that do not meet these requirements are rejected. 

## How data is preserved in the DPS

Once data has been ingested into DPS, the guiding principle is simple: what you submit is what you get back, unchanged. Preservation is carried out at two levels, passive preservation and active preservation.

### Passive preservation

Passive preservation ensures that data remains unchanged over time. It does not require any understanding of the content itself, only that the files remain identical to the originals.

- **Bit-level preservation**: Original files are preserved exactly as received. Data is stored without conversion, compression, or any other modification that would alter its bitstream. DPS requires every file to be accompanied by a checksum in the SIP. These checksums are stored, verified during ingest, and checked again when the data is retrieved. If a mismatch is detected, it is documented, and the remaining copies are used to restore an intact version.
- **Redundant storage**: Data is protected according to the 3-2-1 backup principle: three copies, stored on two different storage technologies, with one copy kept at a separate geographic location. If one copy is lost or becomes corrupted, the remaining copies ensure that the data survives. Multiple copies also make integrity verification meaningful. If an inconsistency is detected in one copy, the remaining copies provide a trusted reference for identifying and restoring the correct version.

All data is stored in the bit repository. The physical location of each file is recorded and linked to the digital object to which it belongs. DPS may internally repackage files to optimize storage efficiency, but this process is transparent to users. When data is retrieved, it is delivered in its original form.

### Active preservation

Active preservation involves more than the secure storage of digital objects. Its purpose is to establish and maintain knowledge about the preserved content so that it can be managed and preserved over time. 

As part of the ingest process, DPS performs file format identification and extracts technical metadata for every file. This provides an inventory of the files stored in DPS, their file formats, and their technical characteristics. The process may also identify anomalies or potential issues. If DPS detects conditions that may indicate a problem with a file after the SIP structure has been successfully validated, the issue is documented and the Producer is notified. The file is then preserved as part of DPS. If the same issue is identified at a later date, the documentation will show that it was already present at the time of ingest and that the file's integrity has remained unchanged since then. 

The information collected during ingest forms the basis for preservation planning. Knowing which file formats are stored in DPS, and how extensively they are used, makes it possible to monitor formats that may become technologically obsolete and to determine when preservation actions may be required. Periodic integrity checks verify that files have not changed over time. All preservation activities are documented, providing a complete record of the actions performed on each file and when they occurred. 

For more information about how metadata is managed, see [Metadata management](/docs/dps/metadata/).

## How data is accessed

Content stored in DPS is not available for immediate retrieval. The system is based on an asynchronous architecture, and the underlying storage solution is designed to prioritize long-term preservation, durability, and cost-efficient operation rather than low-latency access. 

Access to preserved content and data retrieval is governed by separate access agreements. Retrieval requests are submitted through the API, which verifies that the requester has the necessary permissions (see [role-based access control](/docs/dps/access-control/)).

## How data changes over time

Data preserved in DPS is immutable. Once a Submission Information Package (SIP) has been ingested and preserved, its original files cannot be modified. If content needs to be updated or replaced, it must be submitted as a new SIP. The original version is preserved alongside the new one, ensuring that both versions remain available. 

Preservation activities, such as format migration and integrity checks, are documented as part of the preservation process. These activities may produce new derivative files, but they do not alter the preserved original files. 

DPS is continuously evolving. Support for adding new data to existing information packages is currently being evaluated. This functionality is not yet available. 

[^1]: Submission Information Package: The information package as submitted for preservation. It contains the data, documentation, and metadata required for long-term preservation and access.