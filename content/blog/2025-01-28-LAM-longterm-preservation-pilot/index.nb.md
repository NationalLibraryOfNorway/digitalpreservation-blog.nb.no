---
title: "Pilot for langtidsbevaring av museenes digitale kulturarv"
draft: true
date: 2025-01-28T12:00:00+01:00
description: "Nasjonalbiblioteket har, i samarbeid med KulturIT, og på oppdrag fra Kulturdepartementet, startet arbeidet med en pilot for å sikre langtidsbevaring av museenes digitale kulturarv."
tags: [Digital bevaring, Museer, Kulturarv, Pilotprosjekt, Nasjonalbiblioteket, E-ARK, REST API, S3 mellomlagring, Digital Preservation Services, OAIS, KulturIT, Kulturdepartementet, Sikkerhet, Automatisering]
authors: 
  - name: Digital Preservation Team
    image: /apple-touch-icon.png
images: 
  - dps-skisse-v2.png
---
Nasjonalbiblioteket har, i samarbeid med [KulturIT](https://kulturit.org/) og på oppdrag fra Kulturdepartementet, startet arbeidet med en pilot for å sikre langtidsbevaring av museenes digitale kulturarv.
Piloten er et ledd i arbeidet med å bevare Norges digitale kulturarv for fremtidige generasjoner.

Formålet med piloten er å teste hvordan Nasjonalbibliotekets løsning for langtidsbevaring kan integreres med KulturITs systemer, som brukes av museer til samlingsforvaltning.
Piloten har et spesielt fokus på sikkerhet, brukervennlighet og automatisering, og den vil bli evaluert ut fra et kost-/nytteperspektiv.

## Sentrale mål og tekniske elementer for piloten inkluderer

- **Teknisk integrasjon:** Opprettelse av maskin-til-maskin-kommunikasjon mellom KulturITs systemer og Nasjonalbibliotekets løsning, basert på REST API-teknologi.
Dette skal muliggjøre effektiv inn- og utlevering av arkivfiler.
- **Mellomlagring:** Etablering av en mellomlagringsplattform basert på S3-protokoll for sikker og effektiv filoverføring mellom systemene.
- **Standardiserte pakkeformater:** Bruk av E-ARK-standarder for å sikre interoperabilitet og konsistens i langtidsbevaringen av data.
- **Autentisering og autorisering:** Implementering av mekanismer som sikrer at kun autoriserte brukere og systemer får tilgang til filene og funksjonene.
- **Brukervennlighet for museene:** Et grensesnitt som gir museene mulighet til å velge hvilket materiale som skal bevares, og som gjør det enkelt å hente kopier av det bevarte materialet tilbake.

Piloten vil gjennomføres med minst to museer, og ha fokus på langtidsbevaring av digitale bilder i første omgang.
I tillegg til testing av teknisk infrastruktur, vil løsningen validere at alle arkivpakker som mottas fra museene oppfyller nødvendige krav.

## Arkitekturskisse

Arkitekturskissen nedenfor viser hvordan oppdraget tenkes løst:

{{< figure src="dps-skisse-v2.svg" alt="Et diagram som viser foreslått dataflyt i DPS-løsningen" caption="Foreslått DPS-arkitektur" >}}

- **Clients:** De som skal levere inn eller hente ut materiale som Nasjonalbiblioteket har ansvar for å bevare.
- **Intermediate storage:** Teknologiske plattformtjenester for felles mellomlagrings-løsning basert på S3.
- **Archival storage:** Bit-repository-tjenester der bevaringsdata er arkivert etter 3+2+1 prinsippet.
Det vil si tre kopier, to teknologier (disk, tape, tape), hvor en av kopiene er ligger på annen geografisk lokasjon.
- **DPS - Digital Preservation Services:** er Nasjonalbibliotekets løsning for digital bevaring. Løsningen er basert på OAIS standarden.
Den viser mellomlagringsløsning, bit-repository, API-grensesnitt og verifiseringsmekanismer som gjennomføres på digitalt materiale som mottas, og utleveres fra Nasjonalbibliotekets bevarings-omgivelse.

## Avgrensning av piloten

Det vil ikke utvikles funksjonalitet for brukskopier eller oppdatering av metadata innenfor piloten, men muligheten for å utvide løsningen til dette formålet i fremtiden vil bli vurdert.

## Organisering og rapportering

Piloten ledes av Nasjonalbiblioteket i samarbeid med KulturIT og Kulturdirektoratet.
Prosjektgruppen vil rapportere regelmessig til Kulturdepartementet.
En endelig rapport med funn, kostnadsestimater og anbefalinger for videre arbeid skal leveres innen 1. desember 2025.

Nasjonalbiblioteket ser fram til å samarbeide med KulturIT.
I fellesskap skal vi utvikle løsninger som styrker museenes mulighet til å bevare og tilgjengeliggjøre sitt digitale kulturarvsmateriale.
Denne piloten vil være et viktig steg på veien mot å sikre at Norges digitale kulturarv blir bevart for fremtiden.
