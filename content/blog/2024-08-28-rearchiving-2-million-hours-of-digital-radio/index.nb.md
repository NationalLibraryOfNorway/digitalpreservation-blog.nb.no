---  
title: "Rearkivering av 2 millioner timer digital radio – en omfattende prosess"
description: "Lær hvordan Nasjonalbiblioteket lyktes med å migrere 2,2 millioner timer med digitalt radioarkiv (1 petabyte) fra et bitlager fra 2007 til et moderne digitalt bevaringssystem – inkludert de tekniske utfordringene, forbedringene og erfaringene som ble gjort under dette omfattende bevaringsprosjektet."
date: 2024-08-28  
tags: ["Digital Bevaring", "Radioarkiv", "Datamigrering", "HPSS", "DPS", "Oracle HSM", "Lydbevaring", "Kringkasting,"]  
authors: 
  - name: Digital Preservation Team
    image: /apple-touch-icon.png
draft: false
images: 
  - radio.jpg
---

Nasjonalbiblioteket er i gang med å modernisere bitlageret sitt fra 2007 og erstatte det med et nytt, moderne system for digital bevaring. Den nye løsningen er basert på et egenutviklet system kalt DPS (Digital Preservation Services), som bruker IBM-HPSS som underliggende lagringssystem. Overgangen forventes å pågå i et par år, og er nødvendig for å sikre langtidsbevaring og tilgjengeliggjøring av Nasjonalbibliotekets digitale samling.

![Gammel radio](/radio.jpg)

## Overgang til ny bevaringsløsning

I 2023 ble all ny tilvekst av data overført til den nye DPS-bevaringsløsningen. Det gamle bit-lageret inneholdt på dette tidspunktet over 14 petabyte med digitalisert og pliktavlevert materiale, som må rearkiveres til DPS. En viktig del av prosessen innebærer å analysere og pakke om det historiske materialet for å oppfylle de nye kravene i DPS.

## Historisk pliktavlevert radio

Materialet som skal rearkiveres omfatter 2,2 millioner timer digital radio – det tilsvarer 2,5 millioner filer og totalt 1 petabyte data. Dette inkluderer både digitalt fødte- og digitaliserte radioprogrammer fra perioden 1993–2022.

I 1993 var det fire radiokanaler som leverte 16 500 timer med radio. Innen 2022 hadde antallet kanaler økt til 30, som samlet leverte 150 000 timer radio. Med utfasing av det gamle bitlageret ble det nødvendig å flytte dette materialet over til den nye bevaringsløsningen.

## DSM til DPS: En grundig prosess

DSM (Digital Longterm Storage) har vært Nasjonalbibliotekets interne system for håndtering av pliktavlevert radio de siste 20 årene. Dataene har vært lagret i et Oracle HSM-bitlager i tre instanser (disk, tape, tape), og radiomaterialet ble hentet daglig fra ulike kringkastere. Noen sendinger var lagret som mp3- og wav-filer med tilhørende sjekksumfiler. Andre sendinger var kun lagret som mp3.

Før rearkiveringsprosessen startet, ble det tatt en avgjørelse om å generere nye MP4-avspillingsfiler fra WAV-filene for å erstatte de varierende kvalitetsnivåene i de gamle MP3-filene. De nye MP4-filene skal ikke arkiveres i DPS, siden de er sikret på visningsplattformen Wowza. Det nye avspillingsformatet som ble valgt, var 160 kbit AAC i M4A-container (audio). Som kodek ble det brukt Fraunhofer FDK AAC (libfdk_aac).

## Tekniske forbedringer og metadata

Alle objekter ble pakket i henhold til [E-ARK-standarden](https://earkaip.dilcis.eu/), og metadata ble generert i MODS-format. Filidentifisering ble utført med verktøyet Siegfried, og teknisk metadata ble ekstrahert med [Mediainfo](https://mediaarea.net/en/MediaInfo). Hver fil ble behandlet og dokumentert nøye, og det ble opprettet “eventer” som beskrev hva som var gjort. Disse ble lagret i DPS-databasen.

## Tidslinje og erfaringer

Høsten 2023 ble det gjennomført forarbeid og kartlegging. I desember samme år startet utviklingen av arbeidsflyten for rearkiveringen, den ble basert på Apache NiFi. Første versjon ble satt i drift 27. februar 2024, og innen 24. juni 2024 var rearkiveringen av 2,2 millioner radioprogrammer fullført.

Å lage de nye MP4-filene tok lang tid, men fordi vi kunne kjøre 35 prosesser samtidig, klarte vi likevel å rearkivere opptil 9 terabyte data per dag.

## Funn og erfaringer

Under prosessen ble det funnet avvik i 577 av 2,2 millioner objekter. Ingen av feilene oppsto mens dataene var lagret i Oracle HSM-bitlageret. De fleste feil skyldtes mangelfulle kontrollrutiner ved første mottak og arkivering av materialet.

### Sjekksum-avvik (4 tilfeller)

**Årsak**: Objekter feilet på grunn av sjekksumavvik mellom registrert og faktisk beregnet sjekksum under rearkivering.
**Tiltak**: Alle tre kopier i Oracle HSM ble kontrollert og viste seg å være identiske. Avviket må derfor ha oppstått før første arkivering. For disse fire objektene valgte vi å beholde MP3-filen i bevaringsobjektet, siden den hadde korrekt sjekksum. I tillegg ble det registrert en “event” som forklarer hvorfor MP3-filen også ble bevart.

### Null-byte-fil (1 tilfelle)

**Årsak**: En wav-fil med null bytes førte til sjekksumavvik.
**Tiltak**: Alle tre kopier var identiske, så avviket må ha skjedd før lagring i HSM. Det ble registrert en “event” som forklarer hvorfor MP3-filen ble bevart.

### Korrupt fil (1 tilfelle)

**Årsak**: Filen hadde korrekt sjekksum, men manglende informasjon om varighet i Mediainfo avslørte at den var korrupt.
**Tiltak**: Filen ble arkivert i mangel på alternativer, og "event" ble dokumentert.

### Feil ved URN-validering (507 tilfeller)

**Årsak**: Objekter med URN i et annet format enn forventet. Valideringsverktøyet kunne derfor ikke hente data korrekt for MODS-generering. Feilen ser ut til å skyldes leveringsproblemer hos en kringkaster i en kort periode i oktober 2011.
**Tiltak**: URN-ene ble korrigert.

### Duplikatfiler (48 tilfeller)

**Årsak**: 48 objekter fra DSM var allerede arkivert i DPS som følge av overgangsprosessen 21. mars 2023. De første datasettene ble manuelt lastet inn i DPS og ved en feil også fanget opp og arkivert i DSM.
**Tiltak**: Ingen tiltak nødvendig – dataene er riktig arkivert i DPS.

### Duplikatfiler (16 tilfeller)

**Årsak**: Etter rearkiveringen sto 16 objekter igjen i køen som ikke-arkiverte, selv om de faktisk var arkivert i DPS. Dette er hovedsakelig knyttet til opprydding etter en backup-hendelse 1. mars 2024.
**Tiltak**: Ingen tiltak nødvendig – dataene er riktig arkivert i DPS.

## Statistikk og resultater

Rearkiveringsprosessen resulterte i 2,1 millioner nye MP4-filer, til sammen 143 TB avspillingsfiler på nb.no, som erstatter 40 TB av de gamle MP3-filene. Totalt ble 2 183 478 arkivpakker rearkivert i det nye DPS-bevaringsmiljøet.

Dette arbeidet representerer en betydelig forbedring av Nasjonalbibliotekets evne til å bevare og tilgjengeliggjøre digitalt radiomateriale for framtidige generasjoner.

# Tall

**Statistikk fra DSM (gammel bevaringsomgivelse)**

| MimeType    |  Quantity |                 Bytes | TiB |    TB |
| ----------- | --------: | --------------------: | --: | ----: |
| audio/mpeg  |    24 997 |     1 436 936 706 369 |   1 |     1 |
| audio/x-wav | 2 158 485 | 1 053 241 022 424 650 | 958 | 1 053 |
| text/plain  |   358 462 |            12 177 323 |   0 |     0 |



**Statistikk fra DPS (ny bevaringsomgivelse)**

| Type     |  Num AIPs |                 Bytes | TiB |    TB |
| -------- | --------: | --------------------: | --: | ----: |
| radio-DK |   350 929 |    47 733 509 049 163 |  43 |    48 |
| radio    | 1 832 549 | 1 007 674 770 422 690 | 916 | 1 007 |
| Total    | 2 183 478 | 1 055 408 279 471 850 | 959 | 1 055 |



*TiB (tebibyte) er byte/1024, som er den nøyaktige måleenheten for datavolum.*

*TB (terabyte) er byte/1000, som er den mest brukte måleenheten for omtrentlige datavolum.*

Det ble produsert 2,1 millioner nye MP4- (M4A-) filer, som til sammen utgjorde 130 TiB / 143 TB med nye tilgangsfiler på nb.no. Dette erstattet omtrent 40 TB med gamle MP3-tilgangsfiler.

![Timer med radio per år](/radiohours.webp)