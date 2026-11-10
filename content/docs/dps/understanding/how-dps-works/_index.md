---
title: How the DPS works
weight: 1
---

The DPS receives information packages through a public API, validates them, and securely stores data and metadata. Preserved content is delivered through the same API. This page describes the reference model the DPS builds on and the services it consists of.

## OAIS as a reference point

OAIS (Open Archival Information System) is a reference model for archiving digital information. The National Library uses OAIS as a reference point in digital preservation, although the complexity and evolution of our architecture means the OAIS model cannot simply be overlaid onto our organization.

{{< figure src="OAIS_Functional_Model_(en).svg" alt="OAIS functional model" caption="" attr="Mathieualexhache (original work); Mess (SVG conversion & English translation), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0), via Wikimedia Commons" >}}

Key OAIS concepts are the different information packages:

- **SIP** (Submission Information Package): delivered for preservation. Contains content data, documentation, and metadata needed for long-term preservation and access.
- **AIP** (Archival Information Package): as stored in the bit repository. May be identical to the SIP or contain additional preservation information.
- **DIP** (Dissemination Information Package): disseminated from preservation. May consist of all or part of an AIP.

Unless otherwise specified, references to information packages in these documents refer to SIPs.

## The services in the DPS

DPS consists of several services:

- **API service**: The interface used for both submission and dissemination, including file transfers. All communication with DPS takes place through the API service.
- **Ingest**: A chain of services (transfer, validation, characterization, packaging, archiving, and notification) that processes packages before they are preserved in the bit repository.
- **Dissemination**: A chain of services that processes packages for retrieval before they are delivered through the API.

The **metadata service** and the **bit repository** form the core of DPS. This is where digital content is preserved and secured.

- **Metadata service**: Databases and object storage that maintain an overview of preserved content and associated metadata. Most services in DPS store metadata in, or retrieve metadata from, the metadata service.
- **Bit repository**: Various technical solutions that ensure secure and long-term storage of digital content.

{{< figure src="dpskonsept.drawio.svg" alt="DPS conceptual architecture" caption="Conceptual overview of the DPS. Solid lines represent submission and ingest, dashed lines represent dissemination. Data flows are shown in black, metadata in red." >}}

All access and use are governed by role-based access control linked to preservation agreements. See [Access control](/docs/dps/understanding/access-and-agreements/).

## Read more

- [Data management](/docs/dps/understanding/data-management/) and [Metadata management](/docs/dps/understanding/metadata-management/): what happens to data and metadata in the DPS.
- [DPS at the National Library](/docs/dps/understanding/preservation-at-nln/): how the DPS fits into the National Library's own system landscape.
