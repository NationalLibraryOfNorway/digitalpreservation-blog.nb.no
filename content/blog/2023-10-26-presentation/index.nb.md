---
title: Team digital bevaring
description: Presentasjon av team digital bevaring ved Nasjonalbiblioteket
date: 2023-10-26
tags: [Team presentation, team organization, product teams]
authors: 
  - name: Digital Preservation Team
    image: /apple-touch-icon.png
images: 
  - cover.nb.png
aliases: ["/nb/about"]
breadcrumbs: false
---

I juni 2022 ble det etablert et eget team med ansvar for bevaring av [Nasjonalbibliotekets](https://nb.no/ "National Library of Norway homepage") digitale samling.
Teamet håndterer alle typer digitalt materiale, uavhengig om materialet er digitalisert fra analoge kilder eller om det er født digitalt. Dette inkluderer medietyper som websider, tekstdokumenter, bilder, lyd og levende bilder.

Teamet har ansvar for å forvalte løsninger for langtidsbevaring av digitalt materiale, og jobber med inntak, kontroll, lagring, bevaring- og tilgjengeliggjøring av data. Data som langtidsbevares er typisk store filer av høy kvalitet (i motsetning til komprimerte tilgangsfiler).  

Team Digital bevaring samarbeider tett med flere andre spesialiserte medieteam i institusjonen. I tillegg til mottak av digitalt materiale som omfattes av [Pliktavleveringsloven](https://lovdata.no/dokument/NL/lov/1989-06-09-32), produserer Nasjonalbibliotek store mengder data gjennom digitalisering. Det digitaliseres både materiale fra egen samling og på vegne av ulike institusjoner i ABM-sektoren.

Teamet er medlem av [Digital Preservation Coalition (DPC)](https://www.dpconline.org/ "Digital Preservation Coalitions hjemmesider").

## Organisasjon
Team digital bevaring består i dag av 8 medlemmer:

{{< cards cols="6" minWidth="120px" >}}
  {{< card link="/" title="Trond Teigen" image="images/team/trond.jpeg" link="https://www.linkedin.com/in/trond-teigen-191954ab" subtitle="Teamleder" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Torbjørn Bakken Pedersen" image="images/team/torbjorn.jpeg" link="https://www.linkedin.com/in/torbjørn-pedersen-57617b227b" subtitle="Produktleder" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Thomas Edvardsen" image="images/team/thomas.jpeg" link="https://www.linkedin.com/in/thomasedvardsen" subtitle="Techleder" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Vigdis Marie Sørensen" image="images/team/vigdis.jpeg" link="https://www.linkedin.com/in/vigdis-sørensen-8a3618a6" subtitle="Senior platformutvikler" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Siarhei Kulakou" image="images/team/siarhei.jpeg" link="https://www.linkedin.com/in/siarhei-kulakou-0702ba245" subtitle="Applikasjonsutvikler" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Johannes Karlsen" image="images/team/johannes.jpeg" link="https://www.linkedin.com/in/johannes-karlsen-476197267" subtitle="Applikasjonsutvikler" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Lise-Lotte Melkild" image="images/team/LiseLotte.jpg" link="" subtitle="Metadataspesialist" method="Resize" options="250x q85 webp" >}}
  {{< card link="/" title="Sandra Kråkstad" image="images/team/sandra.jpg" link="" subtitle="Metadataspesialist" method="Resize" options="250x q85 webp" >}}
{{< /cards >}}

Teamet svarer til en eiergruppe bestående av:
- Direktør for IT (produkteier)
- Direktør for Kulturarvdigitalisering
- Seksjonsleder for Tilvekst og kunnskapsorganisering utvikling
- Seksjonsleder for IT-plattform

## Nasjonalbibliotekets digitale samling i tall
- Over 2 milliarder filer
- Mer enn 100 forskjellige filformater
- 18 Petabyte med data (det er 18 000 Terabyte!) lagret i 3 kopier
- Den største enkeltfilen er på 2,5 Terabyte
- Gjennomsnittlig daglig tilvekst på over 6 Terabyte med nye data

## Datavolum etter type
- Video og TV: 22%
- Film: 21%
- Aviser 19%
- Webarkiv: 16%
- Radio og lyd 12%
- Bøker 8%
- Bilder 2%

## Teknologi som brukes i arbeidet med digital bevaring
- [Apache Kafka](https://kafka.apache.org "Apache Kafkas hjemmeside") for kommunikasjon mellom systemer
- [Apache NiFi](https://nifi.apache.org "Apache NiFi's hjemmeside") for å kjøre prosesser som validerer, flytter og pakker data
- [MariaDB](https://mariadb.org "MariaDBs hjemmeside") som databasemotor
- [DROID](https://digital-preservation.github.io/droid "DROIDs hjemmeside") og [Siegfried](https://github.com/richardlehane/siegfried) for identifisering av filformater
- [Grafana](https://grafana.com "Grafanas hjemmeside") for statistikk og rapportering
- [IBM High Performance Storage System (HPSS)](https://www.hpss-collaboration.org "HPSSs hjemmeside") som bit-repository
- [CentOS](https://www.centos.org "CentOS' hjemmeside") Linux som serverplattform
- [CommonsIP](https://github.com/keeps/commons-ip) for pakking og validering av arkivpakker på [E-ARK standard](https://dilcis.eu/)