---
title: Digital Preservation Services (DPS)
breadcrumbs: false
sidebar:
  landingTitle: Start here
aliases:
  - /docs/services/dps/
  - /docs/services/
  - /docs/dps/
---

DPS (Digital Preservation Services) refers to the National Library of Norway’s services for preserving digital cultural heritage material. Digital cultural heritage material includes both digitized and “born-digital” material. It covers material subject to the Legal Deposit Act, digital content considered part of the national cultural heritage, and material otherwise considered worthy of digital preservation. DPS is based on the OAIS model.

## Who can use the DPS

DPS is publicly available, but access requires a preservation agreement with the National Library of Norway. How agreements and roles govern access is described in [Access control](/docs/understanding/access-and-agreements/).

## What the DPS does

DPS uses a public API for both ingest and dissemination of information. The system receives Submission Information Packages (SIPs), validates them, and securely stores data and metadata. Dissemination is provided through the same API as Dissemination Information Packages (DIPs). All access and use are governed by role-based access control linked to preservation agreements.

[How the DPS works](/docs/understanding/how-dps-works/) describes the services the DPS consists of.

## Understanding the DPS

These pages explain concepts, responsibilities, and how the DPS works:

{{< cards >}}
  {{< card link="understanding/how-dps-works" title="How the DPS works" subtitle="OAIS, the services in the DPS, and how they fit together" icon="cube" >}}
  {{< card link="understanding/information-packages" title="Information packages" subtitle="What a package contains, kinds of metadata, and package scope" icon="archive" >}}
  {{< card link="understanding/data-management" title="Data management" subtitle="How data is preserved, stored, and accessed in the DPS" icon="database" >}}
  {{< card link="understanding/metadata-management" title="Metadata management" subtitle="How metadata enters, is stored, and utilized in the DPS" icon="tag" >}}
  {{< card link="understanding/access-and-agreements" title="Access control" subtitle="How roles, agreements, and permissions govern access" icon="shield-check" >}}
  {{< card link="understanding/preservation-at-nln" title="DPS at the National Library" subtitle="The National Library's own system domains and how the DPS fits among them" icon="map" >}}
{{< /cards >}}

## Using the DPS

Step-by-step guides for producers and consumers:

{{< cards >}}
  {{< card link="how-to/prepare-content" title="Prepare content for submission" subtitle="Package content as a SIP that meets the requirements" icon="archive" >}}
  {{< card link="how-to/submit-content" title="Submit content for preservation" subtitle="Register a submission, upload files, and finalize it" icon="upload" >}}
  {{< card link="how-to/add-preservation-events" title="Add preservation events" subtitle="Choose and add preservation events to a submission" icon="collection" >}}
  {{< card link="how-to/retrieve-content" title="Request preserved content" subtitle="Order delivery of preserved content and download it" icon="download" >}}
  {{< card link="how-to/receive-notifications" title="Receive notifications" subtitle="Get status updates in your systems through webhooks" icon="bell" >}}
{{< /cards >}}

## Reference

Specifications and API reference:

{{< cards >}}
  {{< card link="reference/api" title="Application Programming Interface" subtitle="Authentication, roles, and error handling" icon="code" >}}
  {{< card link="reference/sip" title="SIP specifications" subtitle="E-ARK package structure, METS.xml requirements, and examples" icon="archive" >}}
  {{< card link="reference/descriptive-metadata" title="Metadata Requirements" subtitle="Dublin Core elements submitted with each package" icon="tag" >}}
  {{< card link="reference/preservation-events" title="Preservation events" subtitle="Event elements, agents, and event types" icon="collection" >}}
{{< /cards >}}
