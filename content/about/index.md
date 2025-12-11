---
title: Team Digital Preservation
tags: [Team presentation, team organization, product teams]
---

In June 2022, a dedicated team was established at [The National Library of Norway](https://nb.no/ "National Library of Norway homepage") to manage the preservation of its digital collection. The team is responsible for handling all types of digital material, whether digitized from analog sources or born-digital. This includes media formats such as websites, text documents, images, audio, and moving images.

Areas of responsibility include managing long-term digital preservation solutions and working across the entire process: ingest, quality control, storage, preservation, and access. Data included for long term preservation typically consists of large, high-quality files, as opposed to compressed access copies.

The Digital Preservation Team collaborates closely with several other specialized media teams within the institution. In addition to receiving digital material covered by the [Legal Deposit Act](https://lovdata.no/dokument/NL/lov/1989-06-09-32), the National Library of Norway also produces large vulumes of data through digitization efforts. This includes both material from its own collections and from institutions across the archive, library, and museum (ALM) sector.

The team is a members of the [Digital Preservation Coalition](https://www.dpconline.org/ "Digital Preservation Coalition homepage").

## Organisation
The [Digital Preservation](https://www.nb.no/en/digital-preservation "Short page about Digital Preservation at NLN") team consist of 8 members:

{{< cards cols="6" minWidth="120px" >}}
  {{< card link="/" title="Trond Teigen" image="images/team/trond-Small.jpeg" link="https://www.linkedin.com/in/trond-teigen-191954ab" subtitle="Team lead" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Torbjørn Bakken Pedersen" image="images/team/torbjorn-Small.jpeg" link="https://www.linkedin.com/in/torbjørn-pedersen-57617b227b" subtitle="Product lead" >}}
  {{< card link="/" title="Thomas Edvardsen" image="images/team/thomas-Small.jpeg" link="https://www.linkedin.com/in/thomasedvardsen" subtitle="Tech lead" >}}
  {{< card link="/" title="Vigdis Marie Sørensen" image="images/team/vigdis-Small.jpeg" link="https://www.linkedin.com/in/vigdis-sørensen-8a3618a6" subtitle="Senior platform developer" >}}
  {{< card link="/" title="Siarhei Kulakou" image="images/team/siarhei-Small.jpeg" link="https://www.linkedin.com/in/siarhei-kulakou-0702ba245" subtitle="Application developer" >}}
  {{< card link="/" title="Johannes Karlsen" image="images/team/johannes2.0-Small.jpeg" link="https://www.linkedin.com/in/johannes-karlsen-476197267" subtitle="Application developer" >}}
  {{< card link="/" title="Lise-Lotte Melkild" image="images/team/LiseLotte-Small.jpeg" link="" subtitle="Metadata specialist" >}}
  {{< card link="/" title="Sandra Kråkstad" image="images/team/sandra-Small.jpeg" link="" subtitle="Metadata specialist" >}}
{{< /cards >}}

This team reports to a committee of leaders responsible for this area in the National Library. The members are:
- IT Director (Product owner)
- Director of Digitalizing Cultural Heritage
- Head of Metadata Standards Development Section
- Head of IT Platform Section

## The National Library’s digital collection in numbers
- Over 2 billion files
- More than 100 different file formats
- 18 Petabytes of data (that’s 18,000 Terabytes!) stored in 3 copies
- The largest single file is 2.5 Terabytes
- Daily ingest of new material averages over 6 Terabytes

## Data volume by type
- Video and television: 22%
- Film: 21%
- Newspapers: 19%
- Web Archive: 16%
- Radio and audio: 12%
- Books: 8%
- Photos: 2%

## Technology choices used when working with digital preservation
- [Apache Kafka](https://kafka.apache.org "Apache Kafka's homepage") for sending messages between systems
- [Apache NiFi](https://nifi.apache.org "Apache NiFi's homepage") for running the data flows that validate, move, and package data
- [MariaDB](https://mariadb.org "MariaDB's homepage") as the database engine
- [DROID](https://digital-preservation.github.io/droid "DROIDs hjemmeside") and [Siegfried](https://github.com/richardlehane/siegfried) for file format identification
- [Grafana](https://grafana.com "Grafana's homepage") for statistics and reporting
- [IBM High Performance Storage System (HPSS)](https://www.hpss-collaboration.org "HPSS's homepage") as bit repository
- [CentOS](https://www.centos.org "CentOS's homepage") Linux as server platform
- [CommonsIP](https://github.com/keeps/commons-ip) for packaging and validation of information packages following the [E-ARK standard](https://dilcis.eu/)
