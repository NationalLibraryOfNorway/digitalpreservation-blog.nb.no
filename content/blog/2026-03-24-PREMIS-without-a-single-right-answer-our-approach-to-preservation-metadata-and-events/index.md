---
title: "PREMIS without a single right answer – our approach to preservation metadata and events"
date: 2026-03-24
description: "The Digital Preservation team has been working on how to document preservation metadata in our preservation environment. Here you can read about our progress so far."
tags: ["Digital bevaring, Nasjonalbiblioteket, Digital Preservation, National library of Norway, metadata, bevaringsmetadata, preservation metadata, PREMIS"]
draft: false
authors: 
  - name: Lise-Lotte Melkild
    image: /apple-touch-icon.png 
---


![AI-generated illustration preservation metadata](/chatGPTimage.png)


🗂️ Preservation metadata describes the origin of digital material, where it comes from and how it was created. It documents the actions and events (in this blogpost referred to as "events") that have affected a digital object, such as creation, migration, validation, and transfer. This type of metadata is particularly important for digital materials, as it ensures traceability and provides a record of what has been done to the object throughout its lifecycle.

🕰️ Historically, there has been limited focus on systematic work with preservation metadata for digital content at the National Library. Following the establishment of the Digital Preservation Team, dedicated attention has been given to how both data and metadata will be better managed over time. The PREMIS standard[^1], which is designed to support the structured description of preservation metadata, has been discussed on several occasions. When the decision was made to adopt the [E-ARK standard](https://dilcis.eu/) for our preservation packages, the choice became clear, as E-ARK also recommends and refers to the use of PREMIS for this type of metadata.

In recent years, we have documented certain preservation events in a separate database. As part of the ongoing work to upgrade our DPS solution[^2], we also decided to explore the possibility of implementing PREMIS events.

🧐 As we had little prior knowledge of PREMIS, we had to begin by familiarizing ourselves with what the standard is, what it is intended for, and how it can be applied. We quickly discovered that there is limited guidance on how it should be implemented in practice, and that the standard functions more as a flexible framework that can be interpreted and realized in many different ways.

📊 Next our approach was to begin with a systematic review of the [PREMIS Data Dictionary](https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf). We examined all entities and their semantic units to map what we already document, what would be relevant to document in the short term (to get started), what we would like to implement over time, and what we consider less relevant for our collection. Throughout, we have had to balance the need for sufficient documentation against the risk of ending up with unnecessary amounts of metadata being stored and managed. It is also important to keep in mind the scale of our holdings, larger than most, about 19 petabytes (19.000 terabytes) with unique data by the end of 2025. Even by documenting only a limited set of events in the first DPS solution, we have already accumulated more than 53 million events at the package level and over 76 million events at the file level.

🔄 We then identified which events were relevant for the team to document internally within the DPS workflow, during ingest, within the preservation process, and at the point of dissemination. As an extension of this work, we saw that it could be possible for depositors to add PREMIS events via our API at the same time as they submit new information packages (SIPs). In this way, we can also enable depositors to include relevant preservation metadata that has been documented before the digital material is received in the DPS. Events submitted via the API are preserved in the same way as those created within the DPS.

📋 To determine which events we consider relevant to document, we based our work on the Library of Congress list of [eventTypes](https://id.loc.gov/vocabulary/preservation/eventType.html) and refined it to better fit our material and preservation environment. At present, we allow 11 event types to be submitted via our API, while some additional types are used internally within the DPS. The set of event types currently accepted through the API has initially been developed for the National Library’s internal production workflows, but will be adapted for external depositors as needed.

💾 So far, we have adopted a simple modeling approach for PREMIS events, documenting three core components: object, event, and agent. For the object, we record two levels: the intellectual entity (essentially the information package) and the file level. We have decided to continue using our own event database, rather than writing events to files within the information package. This approach makes it easier to collect information and add new events without having to update the information package itself. Events are stored in the database in JSON format, not in PREMIS.xml. We have planned for the possibility of writing events from the database into information packages (for example, DIPs at dissemination) in PREMIS.xml format. This also applies to events submitted by depositors via the API. For clarity, our databases are maintained according to the same preservation standards as our bit-level storage.

In addition to recommending the submission of preservation metadata as events via the API, it is also possible to include this type of metadata as part of the information package (SIP). More information can be found here: [SIP 1.0 (E-ARK)](/docs/dps/sip/1.0/).

🚀 We view the work we have done so far as a starting point. We have chosen to document what we consider important for now, to get up and running, with a deliberate approach that allows us to adjust course along the way. For us, it is more important to establish a practice that can be further developed than to aim for a perfect solution from the start, where we risk spending time on endless discussions - and few practical solutions.

Documentation on the use of event elements and event types is published here: [Events/preservation metadata](/docs/dps/api/submission/events/).

More technical information is available here: [Swagger DPS Submission Service API](https://digitalpreservation.no/swagger/).

Please feel free to reach out if you have any comments or questions 😊



[^1]: Preservation Metadata Implementation Strategies (PREMIS) is a metadata standard for recording information required for preservation of digital objects. The standard's documentation and metadata schema are hosted by the Library of Congress.
[^2]: Digital Preservation Services (DPS) is an umbrella term for services and software used to manage digital preservation at the National Library. The system ingests data for preservation, ensures data integrity, and manages access to preserved data.