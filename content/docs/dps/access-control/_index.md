---
title: Model for Role-Based Access
tags: [Digital Preservation, OAIS Model, Role-Based Access Control, Preservation Agreements, Information Packages, Authorization Systems, Access Management, Digital Archives]
---

The model governing access to submit data to or retrieve data from DPS has five main components: *clients*, *roles*, *preservation agreements*, *information packages*, and *DPS IDs*.

## Clients
All users who need to communicate with the DPS will be assigned a client by the digital preservation team at the National Library.

All clients are assigned one or more roles.

### Roles
The roles come in two variants: *producer* and *consumer*.

A producer role gives the client rights to *submit* data to the DPS in the form of information packages, while a consumer role provides access to retrieve information packages from DPS.

All individual roles are in turn linked to specific submission agreements.

### Submission agreement
Submission agreements define how a given information package should be managed.
The term originates from OAIS and are also summarized in the E-ARK-SIP specifications[^1] as follows:

> Interactions between Producers and the OAIS are often guided by a Submission Agreement, which establishes specific details about how these interactions should take place, e.g. the type of information expected to be exchanged, the metadata the Producer is expected to deliver, the logistics of the actual transfer, statements regarding access restrictions on the submitted material, etc.

In the context of role-based access, it is not the details of these submission agreements that are important, but rather that the submission agreements are established in our systems.

Submission agreements are created in collaboration between producers and the digital preservation team.
Producer/consumer roles related to the submission agreements are created in our authorization system.
A preservation agreement must exist *before* the submission of information packages to DPS can occur.

Submission agreements are linked to one or more information packages.

{{< figure src="tilgangskontroll.svg" alt="A diagram showing the relationships between components relevant for access control" caption="Components governing role-based access" >}}

### Information Packages
When data or metadata is to be submitted to or retrieved from DPS, this is done in the form of information packages[^2].
Individual information packages are linked to one (and only one) submission agreement.

## In practical use
A client submitting an information package to the DPS must specify which submission agreement should apply to the package.
One can only submit information packages linked to submission agreements one is authorized to *produce*.
If one has the correct roles, the DPS will initiate the ingest process.

After successful ingest, the DPS takes over management responsibility for the data in the information package.
The information package is assigned a unique DPS-ID, which is given to the submitter as a receipt.

A client wishing to retrieve this information package must specify which package to retrieve using the package's DPS-ID.
If the client has a consumer role linked to the preservation agreement governing the relevant information package, the DPS will initiate the dissemination process.

A client wishing to search for contents managed by the DPS, will be able to search all information packages connected to the preservation agreements for which they have a consumer role.

[^1]: [E-ARK SIP: 4.1. Submission Agreements](https://earksip.dilcis.eu/#submissionagreements)