---
title: Digital Preservation Services (DPS)
weight: 4
aliases:
  - /docs/services/dps/
  - /docs/services/
---

DPS (Digital Preservation Services) refers to the National Library of Norway’s services for preserving digital cultural heritage material. Digital cultural heritage material includes both digitized and “born-digital” material. It covers material subject to the Legal Deposit Act, digital content considered part of the national cultural heritage, and material otherwise considered worthy of digital preservation. DPS is based on the OAIS model. 

{{% details title="OAIS terminology" closed="true" %}}

OAIS (Open Archival Information System) is a reference model for archiving digital information. The National Library uses OAIS as a reference point in digital preservation, although the complexity and evolution of our architecture means the OAIS model cannot simply be overlaid onto our organization.

{{< figure src="OAIS_Functional_Model_(en).svg" alt="OAIS functional model" caption="" attr="Mathieualexhache (original work); Mess (SVG conversion & English translation), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0), via Wikimedia Commons" >}}

Key OAIS concepts are the different information packages:

- **SIP** (Submission Information Package): delivered for preservation. Contains content data, documentation, and metadata needed for long-term preservation and access.
- **AIP** (Archival Information Package): as stored in the bit repository. May be identical to the SIP or contain additional preservation information.
- **DIP** (Dissemination Information Package): disseminated from preservation. May consist of all or part of an AIP.

Unless otherwise specified, references to information packages in these documents refer to SIPs.

{{% /details %}}

## Who can use the DPS

DPS is publicly available, but access requires an agreement with the National Library of Norway. For details, see [Data management](/docs/dps/data/).

## What the DPS does

DPS uses a public API for both ingest and dissemination of information. The system receives Submission Information Packages (SIPs), validates them, and securely stores data and metadata. Dissemination is provided through the same API as Dissemination Information Packages (DIPs). All access and use are governed by role-based access control linked to preservation agreements. 

DPS consists of several services: 

- **API service**: 
The interface is used for both submission and dissemination, including file transfers. All communication with DPS takes place through the API service. 
- **Ingest**: 
A chain of services (transfer, validation, characterization, packaging, archiving, and notification) that processes packages before they are preserved in the bit repository. 
- **Dissemination**: 
A chain of services that processes packages for retrieval before they are delivered through the API. 

The **metadata service** and the **bit repository** form the core of DPS. This is where digital content is preserved and secured. 

- **Metadata service**: 
Databases and object storage that maintain an overview of preserved content and associated metadata. Most services in DPS store metadata in, or retrieve metadata from, the metadata service.  

- **Bit repository**: 
Various technical solutions that ensure secure and long-term storage of digital content. 

- **API service**: 
All communication with DPS takes place through the API service. 

{{< figure src="dpskonsept.drawio.svg" alt="DPS conceptual architecture" caption="Conceptual overview of the DPS. Solid lines represent submission and ingest, dashed lines represent dissemination. Data flows are shown in black, metadata in red." >}}

## The role of DPS in the National Library of Norway

DPS is one of three system domains that share responsibility for digital objects at the National Library of Norway. These domains manage different aspects of the objects. The domains operate independently but influence each other.

## The three system domains:

### Metadata management systems
Library systems, catalogues, registers, and collection management systems (such as Alma, Mavis, and Hanske). These are the primary sources of descriptive metadata and issue unique identifiers (UIDs, typically URNs) for digital objects. These systems manage a wide range of resources. 

This is where intellectual entities[^1] are defined: the decision regarding what constitutes a preservation-worthy information package starts here, not in DPS. One URN typically corresponds to one package. For details about package scope, see [Package, representation, and data scope](/docs/dps/sip/scope/). 

### Digital Preservation Services (DPS)

**The preservation system**: DPS manages preservation data using a PREMIS-based data model[^2] (intellectual entities, representations, files, events, and agents). DPS provides long-term storage with asynchronous access. DPS is the primary source for technical metadata at file level within the National Library of Norway. DPS is not the primary source for descriptive metadata: the system maintains the metadata it requires to operate independently, without recreating the full catalogue structures of the metadata systems.   

**DPS functions as an independent service**: identifiers and metadata are provided through the API, and DPS manages preservation. For details on how data and metadata are managed in DPS, see [Data management](/docs/dps/data/) and [Metadata management](/docs/dps/metadata/).

### Public access services

The National Library of Norway’s online services. These services manage a subset of descriptive metadata and provide immediate access to access copies derived from preservation files. 

The public access services adapt harvested metadata into a flatter structure, with a single representation per intellectual entity. The intellectual entities available online therefore do not necessarily correspond directly to the entities in the metadata systems. 

A UID, managed by the metadata systems, connects the three domains. It must be unique across the systems and should not be reused.   

## Data and metadata flow

The diagram below provides a simplified representation of how data and metadata move between the system domains at the National Library of Norway: 

{{< figure src="context.svg" alt="architecture diagram" caption="Data and metadata flow between the system domains at the NLN" >}}

The SIP contains preservation data and a copy of descriptive metadata from the metadata systems. DPS does not preserve access copies that can be automatically derived from preservation files; such copies are managed by the public access services. 

## Understanding the DPS

These pages explain concepts, responsibilities, and how the DPS works:

{{< cards >}}
  {{< card link="data" title="Data management" subtitle="How data is preserved, stored, and accessed in the DPS" icon="database" >}}
  {{< card link="metadata" title="Metadata management" subtitle="How metadata enters, is stored, and utilized in the DPS" icon="tag" >}}
  {{< card link="access-control" title="Access control" subtitle="How roles, submission agreements, and permissions govern access" icon="shield-check" >}}
{{< /cards >}}

## Using the DPS

These pages are specifications and API references for producers and consumers:

{{< cards >}}
  {{< card link="api" title="Submission Service API" subtitle="Endpoints for submission, dissemination, and webhooks" icon="code" >}} 
  {{< card link="sip" title="SIP specifications" subtitle="E-ARK package structure, METS.xml requirements, and examples" icon="archive" >}}
{{< /cards >}}

[^1]: [Intellectial entities and content](https://digitalpreservation.no/docs/dps/sip/scope/#intellectial-entities-and-content)
[^2]: *PREMIS Data Dictionary (full document)*, Version 3.0, Nov. 2015, [https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf](https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf)