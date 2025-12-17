---
title: "Mission accomplished!"
date: 2025-12-17
description: "Team digital preservation, the Norwegian Directorate for Cultural Heritage and KulturIT has completed the pilot project for the long-term preservation of museums’ digital materials."
tags: ["Digital bevaring, Nasjonalbiblioteket, Digital Preservation, National library of Norway, kulturarv"]
draft: false
authors: 
  - name: Trond Teigen
    image: /apple-touch-icon.png 
---


![Draft for the preservation of museums` digital cultural heritage](/pilot_eng.png)

The National Library of Norway, the Norwegian Directorate for Cultural Heritage, and KulturIT were commissioned by the Norwegian Ministry of Culture and Equality to carry out a pilot project for the long-term preservation of digital museum objects using the National Library’s digital preservation solution (DPS). The assignment was given in December 2024.

Over the past year, the National Library and KulturIT have worked closely together to develop and test a solution for the ingest and delivery of digital museum objects, initially focusing on images. For the Digital Preservation team at the National Library, this work required the establishment of several new functions within the DPS.

An API interface has been developed to enable communication between various data systems and the DPS. The API handles authentication and authorization, and all data exchange is governed by agreements between the National Library and the institutions that chooses to use the service. More information about the API is available [here](https://digitalpreservation.no/docs/dps/api/).

For data ingest and delivery, a data exchange platform based on the Amazon S3 protocol was tested. This solution allows users to transfer data without needing to understand how the data is stored within the platform.

Requirements have been established for data delivered to the National Library to comply with the [E-ARK](https://dilcis.eu/specifications/sip) standard for the structure and content of information packages. More information about these requirements is available [here](https://digitalpreservation.no/docs/dps/sip/1.0/).

In addition, metadata requirements have been defined for information packages submitted for preservation. These metadata are considered essential for the management and preservation of the material within the preservation environment and are submitted via the API. More information about the metadata requirements is available [here](https://digitalpreservation.no/docs/dps/api/submission/metadata/).

[KulturIT](https://kulturit.org/) has, in parallel, developed functionality for selecting museum objects for preservation, as well as solutions for for ingesting and retrieving preserved museum objects from the National Library’s digital preservation system (DPS) based on our requirements.

The solution has been tested by three of KulturIT’s owner museums, and the pilot project is considered successful.

A final report has been submitted to the Ministry of Culture and Equality. The report describes how the assignment was carried out and recommends establishing a permanent service for the long-term digital preservation of images for museums. This service should build on the results of the pilot and include an initial phase involving five museums.

In the longer term, the service may be expanded to include additional museums and extended to cover other media types, such as text, audio, and moving images.

The National Library of Norway, the Norwegian Directorate for Cultural Heritage, and KulturIT have collaborated closely throughout the pilot and support the report’s recommendations for further work.

 