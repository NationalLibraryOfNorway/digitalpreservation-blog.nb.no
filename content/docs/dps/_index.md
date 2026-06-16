---
title: Digital Preservation Services (DPS)
weight: 4
aliases:
  - /docs/services/dps/
  - /docs/services/
---

DPS, or Digital Preservation Services, refers to the National Library of Norway's services for preserving digital cultural heritage materials. This includes both digitized content and materials that are "born digital." The scope covers materials subject to legal deposit, digital content considered part of the national cultural heritage, and other materials considered worthy of digital preservation. The DPS is an OAIS repository.

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

Throughout these pages, we refer to *clients*: the organizations and systems that interact with the DPS. A client can act as a **producer** (submitting data) or a **consumer** (retrieving data), following the established OAIS terminology. A single client may be both a producer and a consumer.

The DPS is publicly available, but access requires an agreement with the National Library of Norway. For details, see [Data management](/docs/dps/data/).

## What DPS does

DPS ingests Submission Information Packages (SIPs), validates their structure and content, stores data and metadata with bit-level integrity, and provides dissemination through a public API. Everything is governed by role-based access control tied to submission agreements.

Under the hood, the DPS consists of several services:

- **API service**: the public-facing interface that clients use for both submission and dissemination, including file transfers.
- **Ingest pipeline**: a chain of services (transfer, validation, characterization, packaging, archive, notification) that process packages before they enter the bit repository.
- **Dissemination pipeline**: a chain of services that process packages for retrieval before they are delivered through the API.

Together, the **metadata service** and the **bit repository** form the DPS core. These hold the contents we preserve and safeguard. The surrounding services can be exchanged. The DPS core itself can also be replaced, but its contents would need to be migrated:

- **Metadata service**: the databases and object storage that track everything. Most services in the DPS send metadata to or read metadata from this service.
- **Bit repository**: tape robots and disk libraries for safe long-term storage.

You only interface with the DPS through the API service.

{{< figure src="dpskonsept.drawio.svg" alt="DPS conceptual architecture" caption="Conceptual overview of the DPS. Solid lines represent submission and ingest, dashed lines represent dissemination. Data flows are shown in black, metadata in red." >}}

## Understanding the DPS

These pages explain concepts, responsibilities, and how the DPS works:

{{< cards >}}
  {{< card link="context" title="The role of DPS in the NLN" subtitle="The system context the DPS was built in and how it shapes the service" icon="view-grid" >}}
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
