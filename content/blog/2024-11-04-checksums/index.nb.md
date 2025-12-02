---
title: "Bedre sent enn aldri: Slik la vi til sjekksummer for 16 millioner allerede bevarte filer"
date: 2024-11-06T12:45:00+01:00 
description: "Under migrering fra gammelt til nytt lagringssystem, ble det gjennomført verifisering av 2,5 petabyte data. Her er en besrkivelse av hvordan det ble brukt sjekksummer for å validere 16 millioner filer, på tvers av flere lagringskopier."
tags: ["Digital Preservation", "Checksums", "Data Migration", "Data Integrity", "Digital Storage", "File Verification", "Legacy Systems", "Digital Archives", "SAM-FS", "Long-term Storage", "digital bevaring", "sjekksummer", "kulturarv"]  
authors: 
  - name: Digital Preservation Team
    image: /apple-touch-icon.png
images: 
  - cover.jpg
aliases: /checksum-generation
---

Nasjonalbiblioteket har brukt SAM-FS[^1] som system for langtidslagring og arkivering av store datamengder siden 2007. Systemet inneholder i dag 14 petabyte data og nærmer seg nå «end-of-life» som produkt.

I 2022 besluttet Nasjonalbiblioteket å erstatte SAM-FS med en mer moderne bevaringsløsning for digitalt materiale. Den nye løsningen bygger på egenutviklet programvare kalt DPS (Digital Preservation Services) og bruker IBM-HPSS som underliggende lagringssystem. 

De siste ti årene har Nasjonalbiblioteket brukt sjekksummer[^2] som metode for å verifisere bevarte data. En sjekksum er en beregnet hash-verdi som brukes til å kontrollere at en fil ikke har blitt endret. Vanlige sjekksumalgoritmer inkluderer MD5, SHA-1, SHA-256 og SHA-512. Nasjonalbiblioteket bruker MD5[^3].

## Manglende sjekksummer
Mange av de eldste filene i SAM-FS **manglet** sjekksummer da de ble lagret. Siden alle filer i systemet er lagret i tre eksemplarer, betyr det at de tre kopiene i praksis eksisterer uavhengig av hverandre når det ikke finnes en opprinnelig sjekksum. Hvis det skulle oppstå et avvik mellom kopiene, ville vi ikke hatt noen referanseverdi å kontrollere mot. 

{{< figure src="checksum1.svg" alt="Diagram showing the data flow in and out of SAM-FS" caption="Data stored in SAM-FS in 3 instances" >}}

Som en del av migreringen fra SAM-FS til DPS ble det derfor bestemt å opprette og lagre sjekksummer for alle filer som manglet dette. 

## Utfordringer
Hvordan kunne vi sikre at filene som ble overført fra SAM-FS til DPS var identiske med det som opprinnelig var arkivert, når ingen sjekksummer fantes for verifisering? De eldste filene var mer enn 20 år gamle og hadde allerede gjennomgått opptil fem hardware/plattformmigreringer (se figur 4). 

Hvilken av de tre filene i SAM-FS skulle vi velge som utgangspunkt? Hvordan kunne vi vite at dette var den «riktige» filen uten å lese og sammenligne alle tre kopiene? Det ble vanskelig å gjøre en full sammenligning, siden det ville innebære å lese og prosessere flere petabyte[^4] data i samme tekniske miljø som også håndterte den daglige drifta. 

## Løsningen
At filene fantes i flere eksemplarer viste seg å være en fordel da vi skulle generere sjekksummer for de «gamle» filene for første gang. Ett eksemplar lå på disk, mens to lå på tape. 

{{< figure src="checksum2.svg" alt="Diagram showing data flow in checksum generation" caption="Checksum calculation" >}}

Først ble det utviklet et skript som hentet ut alle filer uten sjekksum fra én av tapekopiene (steg 2). For hver fil ble det beregnet en sjekksum og lagret i en database. 

Denne prosessen tok litt over to måneder for et datasett på 2,5 petabyte.

{{< figure src="checksum3.svg" alt="Diagram showing data flow in checksum verification and data transfer to the DPS" caption="Checksum verification and transfer to DPS" >}}

Da alle tapefilene var lest og sjekksummer lagret, startet selve migreringen til DPS. 

Hver fil ble først hentet fra diskeksemplaret i SAM-FS, og det ble beregnet en sjekksum som ble sammenlignet med tapekopiens sjekksum (steg 3). Hvis de stemte overens, betydde det at minst to av tre kopier var identiske. 

Filen ble da godkjent og overført til DPS, sammen med den nye sjekksummen (steg 4). Hvis sjekksummene ikke samsvarte, betydde det at enten disk- eller tapekopien var feil. Dette ble registrert som en feil og måtte undersøkes manuelt ved å sjekke den tredje kopien for å avgjøre hvilken som var korrekt. 

## Resultat og erfaringer
Ingen av de 16 millioner filene i datasettet på 2,5 petabyte hadde avvikende sjekksummer. Metoden var både tid- og ressurskrevende, men sørget for at filene som ble overført til DPS var autentiske. 

En viktig lærdom var at man i stor grad kan stole på tekniske lagringssystemer når det gjelder å bevare bitmønstre over tid. Vi verifiserte 16 millioner filer med sjekksum, filer som gjennom 20 år hadde vært gjennom inntil fem teknologimigreringer – uten å finne én eneste bitendring. 

### Plattform- og teknologigenerasjoner i SAM-FS
Oversikt over teknologiskiftene i Nasjonalbibliotekets langtidslagringssystem SAM-FS. TB-verdien angir lagringskapasitet per enhet (disk/tape):

| **Tidsperiode** | **Disk** | **Tapekopi 1** | **Tapekopi 2** |
|----|----|----|----|
| 2007-2009 | SUN 6140 (1TB) | SUN SL8500 – T10kA (500GB) | SUN SL8500 – T10kA (500GB) |
| 2009-2011 | SUN 6180 (2TB) | SUN SL8500 – T10kB (1TB) | SUN SL8500 – T10kB (1TB) |
| 2012-2016 | Nexsan (3TB) | SUN SL8500 – T10kC (5TB) | SUN SL8500 – T10kC (5TB) |
| 2016-2019 | Nexsan (8TB) | *as above* | *as above* |
| 2020-2022 | Fujitsu (16TB) | SUN SL8500 – LTO8 (12TB) | SUN SL8500 – LTO8 (12TB) |

[^1]: Hierarkisk lagringsstyringssystem, SAM-FS, også kjent som Oracle HSM

[^2]: https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums

[^3]: https://no.wikipedia.org/wiki/MD5

[^4]: 1 Petabyte = 1.000 Terrabyte
