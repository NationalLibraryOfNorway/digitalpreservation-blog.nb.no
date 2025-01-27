---
title: "Pilot Project for Long-term Digital Preservation of Museum Collections"
draft: true
date: 2025-01-28T12:00:00+01:00
description: "The National Library of Norway, in collaboration with KulturIT and commissioned by the Ministry of Culture, has initiated a pilot project to ensure long-term preservation of the LAM sector's digital cultural heritage."
tags: [Digital Preservation, Museums, Cultural Heritage, Pilot Project, National Library, E-ARK, REST API, S3 Storage, Digital Preservation Services, OAIS, KulturIT, Ministry of Culture, Security, Automation]
authors: 
  - name: Digital Preservation Team
    image: /apple-touch-icon.png
images: 
  - 
---
The National Library of Norway, in collaboration with [KulturIT](https://kulturit.org/en) and commissioned by the Ministry of Culture, has initiated a pilot project focused on ensuring the long-term preservation of museums' digital cultural heritage.
This pilot represents a strategic initiative in preserving Norway's digital cultural heritage for future generations.

The primary objective is to evaluate whether the National Library's digital preservation solution can be integrated with KulturIT's collection management systems currently utilized by museums.
The pilot emphasizes security protocols, user experience optimization, and process automation, with subsequent evaluation based on cost-benefit analysis.

## Key Objectives and Technical Components

The pilot project encompasses several critical technical and operational elements:

- **Technical Integration:** Implementation of machine-to-machine communication between KulturIT's systems and the National Library's preservation infrastructure, utilizing REST API technology. This integration facilitates efficient ingestion and retrieval of archival files.
- **Intermediate Storage:** Development of an S3-protocol-based intermediate storage platform, ensuring secure and efficient file transfer operations between systems.
- **Standardized Package Formats:** Implementation of E-ARK standards to maintain interoperability and ensure consistency in long-term data preservation.
- **Authentication and Authorization:** Development of robust security mechanisms to ensure that only authorized users and systems can access preserved files and associated functionality.
- **Museum User Interface:** Implementation of an intuitive interface enabling museums to select preservation-worthy data and efficiently retrieve preserved data.

The pilot will be conducted with a minimum of two participating museums, initially focusing on the long-term preservation of digital images.
Beyond technical infrastructure testing, the solution will validate that all archival packages received from museums meet specified preservation requirements.

## Architectural Overview

The following architectural diagram illustrates the proposed solution framework:

DIAGRAM

- **Clients:** Entities responsible for submitting or retrieving materials preserved by the National Library.
- **Intermediate Storage:** Platform services implementing shared intermediate storage solutions based on S3 protocol.
- **Archival Storage:** Bit-repository services where preservation data is archived following the 3+2+1 principle. That is three copies, two technologies (disk, tape, tape) and one geographically distributed copy.
- **DPS - Digital Preservation Services:** The National Library's digital preservation solution, based on the OAIS standard.
This encompasses intermediate storage solutions, bit-repository management, API interfaces, and verification mechanisms for materials received and distributed within the National Library's preservation environment.

## Pilot Scope Limitations

The pilot explicitly excludes functionality for access copies or metadata updates.
However, the potential for future expansion to include these capabilities will be evaluated during the assessment phase.

## Project Management and Reporting Structure

The pilot is managed by the National Library of Norway in partnership with KulturIT and the Directorate of Culture.
The project team will maintain regular reporting cycles to the Ministry of Culture.
A comprehensive final report, including findings, cost estimates, and recommendations for future development, will be submitted by December 1, 2025.

The National Library of Norway anticipates productive collaboration with KulturIT in developing solutions that enhance museums' capabilities for preserving and accessing digital cultural heritage materials.
This pilot represents a significant step toward ensuring the long-term preservation of Norway's digital cultural heritage.
