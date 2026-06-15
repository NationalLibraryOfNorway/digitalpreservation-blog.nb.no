---
title: Digital Preservation Services (DPS)
weight: 2
---

DPS, or Digital Preservation Services, refers to the National Library of Norway's services for preserving digital cultural heritage materials. This includes both digitized content and materials that are "born digital." The scope covers materials subject to legal deposit, digital content considered part of the national cultural heritage, and other materials considered worthy of digital preservation.

## Who uses the DPS

Throughout these pages, we refer to *clients*: the organizations and systems that interact with the DPS. A client can act as a **producer** (submitting data) or a **consumer** (retrieving data), following the established OAIS terminology. A single client may be both a producer and a consumer.

## What DPS does

DPS ingests Submission Information Packages (SIPs), validates their structure and content, stores data and metadata with bit-level integrity, and provides dissemination through a public API. Everything is governed by role-based access control tied to submission agreements.

Under the hood, the DPS consists of several services:

- **API service**: the public-facing interface that clients use for both submission and dissemination, including file transfers.
- **Ingest pipeline**: a chain of services (transfer, validation, characterization, packaging, archive, notification) that process packages before they enter the bit repository.
- **Metadata service**: the databases and object storage that track everything. Most services in the pipeline feed or read metadata from it. See [Metadata management](/docs/services/dps/metadata/) for details.
- **Bit repository**: tape robots and disk libraries for long-term storage.

The ingest pipeline, metadata service, and bit repository are internal to the DPS. You only interface with us through the API service.

For details on specific aspects of the DPS, see:
- [Data management](/docs/services/dps/data/): how data is preserved, stored, and accessed
- [Metadata management](/docs/services/dps/metadata/): how metadata enters, is stored, and is utilized
- [Access control](/docs/services/dps/access-control/): how roles and submission agreements govern access
