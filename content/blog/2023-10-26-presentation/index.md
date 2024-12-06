---
title: Team Digital Preservation
description: "Presentation of the Digital Preservation team at the National Library of Norway"
date: 2023-10-26
tags: [Team presentation, team organization, product teams]
authors: 
  - name: Digital Preservation Team
    image: /apple-touch-icon.png
images: 
  - cover.webp
aliases: ["/team-digital-preservation-70f5805ba536", "/about"]
breadcrumbs: false
---

In June 2022 the IT Department established a team dedicated to preserving the [National Library’s](https://nb.no/ "National Library of Norway homepage") digital collection.
This team handles all kinds of digital content, whether it’s digitized from physical sources or born digital.
This includes media types like web pages, text documents, images, audio, and moving images.

The team’s responsibilities involve ingesting, checking, storing, preserving, and providing access to high-quality digital files.
We work closely with several other specialized media teams in the library.
In addition we are members of the [Digital Preservation Coalition](https://www.dpconline.org/ "Digital Preservation Coalition homepage").

## Organisation
The [Digital Preservation](https://www.nb.no/en/digital-preservation "Short page about Digital Preservation at NLN") team consist of 8 members:

{{< cards cols="6" minWidth="120px" >}}
  {{< card link="/" title="Trond Teigen" image="images/team/trond.jpeg" link="https://www.linkedin.com/in/trond-teigen-191954ab" subtitle="Team lead" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Torbjørn Bakken Pedersen" image="images/team/torbjorn.jpeg" link="https://www.linkedin.com/in/torbjørn-pedersen-57617b227b" subtitle="Product lead" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Thomas Edvardsen" image="images/team/thomas.jpeg" link="https://www.linkedin.com/in/thomasedvardsen" subtitle="Tech lead" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Vigdis Marie Sørensen" image="images/team/vigdis.jpeg" link="https://www.linkedin.com/in/vigdis-sørensen-8a3618a6" subtitle="Senior platform developer" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Siarhei Kulakou" image="images/team/siarhei.jpeg" link="https://www.linkedin.com/in/siarhei-kulakou-0702ba245" subtitle="Application developer" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Johannes Karlsen" image="images/team/johannes.jpeg" link="https://www.linkedin.com/in/johannes-karlsen-476197267" subtitle="Application developer" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Lise-Lotte Melkild" image="images/team/Blank_woman_placeholder.png" link="" subtitle="Metadata specialist" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Sandra Kråkstad" image="images/team/sandra.jpg" link="" subtitle="Metadata specialist" method="Resize" options="250x q85 webp" >}}
{{< /cards >}}

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
- [Apache Kafka](https://kafka.apache.org "Apache Kafka's homepage") for sending messages between systems
- [Apache NiFi](https://nifi.apache.org "Apache NiFi's homepage") for running the data flows that validate, move, and package data
- [MariaDB](https://mariadb.org "MariaDB's homepage") as the database engine
- [DROID](https://digital-preservation.github.io/droid "DROID's homepage") for identifying fileformats
- [Grafana](https://grafana.com "Grafana's homepage") for statistics and reporting
- [IBM High Performance Storage System (HPSS)](https://www.hpss-collaboration.org "HPSS's homepage") as bit repository
- [GlusterFS](https://www.gluster.org "GlusterFS's homepage") for shared temporary storage
- [CentOS](https://www.centos.org "CentOS's homepage") Linux as server platform
