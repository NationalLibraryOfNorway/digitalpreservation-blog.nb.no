---
title: "Team Digital Preservation"
summary:
date: 2023-10-26
weight: 
tags: ["team"]
author: ["Thomas Edvardsen"]
cover:
  image: /cover.webp
  hiddenInList: false
showtoc: true
aliases: /team-digital-preservation-70f5805ba536
---

In June 2022 the IT Department established a team dedicated to preserving the [National Library’s](https://nb.no/) digital collection. This team handles all kinds of digital content, whether it’s digitized from physical sources or born digital. This includes media types like web pages, text documents, images, audio, and moving images.

The team’s responsibilities involve ingesting, checking, storing, preserving, and providing access to high-quality digital files. We work closely with several other specialized media teams in the library. In addition we are members of the Digital [Preservation Coalition (DPC)](https://www.dpconline.org/)

## Organisation
The [Digital Preservation](https://www.nb.no/en/digital-preservation "Short page about Digital Preservation at NLN") team consist of 7 members:

- Junior Application Developer: [Johannes Karlsen](https://www.linkedin.com/in/johannes-karlsen-476197267)
- Application Developer: [Siarhei Kulakou](https://www.linkedin.com/in/siarhei-kulakou-0702ba245)
- Product Lead: [Torbjørn Pedersen](https://www.linkedin.com/in/torbjørn-pedersen-57617b227b) 
- Tech Lead: [Thomas Edvardsen](https://www.linkedin.com/in/thomasedvardsen) 
- Application Developer: [Daniel Aaron Salwerowicz](https://www.linkedin.com/in/salwerowicz)  
- Senior Platform Developer: [Vigdis Marie Sørensen](https://www.linkedin.com/in/vigdis-sørensen-8a3618a6)  
- Team Lead: [Trond Teigen](https://www.linkedin.com/in/trond-teigen-191954ab)  

{{< figure src="teamphoto.jpeg" attr="From the back, left to right: Johannes Karlsen, Siarhei Kulakou, Torbjørn Pedersen, Thomas Edvardsen, Daniel Aaorn Salwerowicz, Vigdis Marie Sørensen, Trond Teigen" align=center >}}
 
This team reports to a committee of leaders responsible for this area in the National Library. The members are:
- IT Director (Product owner)
- Director of Digitalizing Cultural Heritage
- Head of Metadata Standards Development Section
- Head of IT Platform Section

## The National Library’s digital collection in numbers
- Over 2 billion files
- More than 90 different file formats
- 15 Petabytes of data (that’s 15,000 Terabytes!) stored in 3 copies
- The largest single file is 2.5 Terabytes
- Daily ingest of new material averages over 4 Terabytes

## Data volume by type
- Video and television: 22%
- Film: 21%
- Newspapers: 19%
- Web Archive: 16%
- Radio and audio: 12%
- Books: 8%
- Photos: 2%

## Technology choices used when working with digital preservation
- [Apache Kafka](https://kafka.apache.org) for messaging
- [Apache NiFi](https://nifi.apache.org) for running the data flows that validate, move, and package data
- [MariaDB](https://mariadb.org) as the database engine
- [DROID](https://digital-preservation.github.io/droid) for identifying fileformats
- [Grafana](https://grafana.com) for statistics and reporting
- [IBM High Performance Storage System (HPSS)](https://www.hpss-collaboration.org) as bit repository
- [GlusterFS](https://www.gluster.org) for shared temporary storage
- [CentOS](https://www.centos.org) Linux as server platform
