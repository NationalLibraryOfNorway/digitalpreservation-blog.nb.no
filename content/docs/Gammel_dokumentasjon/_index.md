---
title: Version 1.0
draft: true
weight: 1
---

Løsningen som benyttes for å motta og bevare datapakkene kalles DPS (Digital Preservation Service). DPS er basert på OAIS-modellen. En datapakke som skal bevares kalles Submission Information Package (SIP). 

## Overføring av data til DPS

### Avleveringsområde
Avleverer legger SIP som skal bevares på et filområde som DPS har tilgang til. Om DPS skal hente fra nye filområder, må det avtales med team Digital Bevaring (og team Plattform). Filområdet må monteres på DPS serverne.

### Katalogstruktur
Det skal lages én katalog pr SIP som skal bevares. Navnet på katalogen er ikke viktig for DPS, da “identifier”-feltet i Kafkameldingen brukes som unik identifikator i DPS. Når DPS har bevart SIPen - sletter vi denne katalogen fra kilden.

### Innhold i SIP

En SIP må minimum bestå av:

- **Innholdsfiler** 
	- Selve innholdet i SIP som skal bevares. Det vil typisk være en eller flere .tar filer pr SIP. 
- **checksum_transferred.md5**
- **checksum.md5**

{{< callout type="info" >}}
DPS aksepterer ikke tomme filer. SIP med tomme filer vil bli avvist dersom de er ikke pakket inn i en .tar fil eller lignende.
{{< /callout >}}

### Fil- og katalognavn
Fil- og katalognavn kan bare bestå av “Skrivbare tegn” i følge 7-bit ASCII. Dvs. 0x20 - 0x7E i ASCII tabellen. I tillegg har vi støtte for bokstavene æ, ø og å. 

{{< callout type="warning" >}} DPS har begrensninger på lengden for både filnavn og relative stier når de er kodet i ASCII 7-format. Begrensningene er spesifisert i tabellen nedenfor.
{{< /callout >}}

| Streng type | Maksimalt antall tegn for en streng kodet i 7-bits ASCII |
| --- | --- |
| Filnavn | 256 |
| Relativ sti uten filnavn | 512 |
| Relativ sti med filnavn | 768 |

### Rettigheter

For at DPS skal ha tilstrekkelig tilgang til å slette filene etter at de er bevart, må DPS-brukeren eksistere på filsystemet og være medlem av den samme gruppen som filene tilhører. Spesifikke rettigheter må også settes på katalogen med avleverte data og filene i den. Tabellen nedenfor viser de nødvendige rettighetene.

| Objekt | MRettigheter |
| --- | --- |
| Kataloger | 775 (d rwx rwx r-x) |
| Filer | (rw- rw- r--) |

Dette tilsvarer umask 0002.

{{< callout type="warning" >}}
Vi sletter ikke SIP når vi kjører i vårt stage miljø, da det ofte brukes produksjonsdata for testing.
{{< /callout >}}

#### Eksempel på filer i en SIP

```
/gluster/tekst/avis/dagensnaeringsliv/2023/dagensnaeringsliv_null_null_20230223_134_46_1/
├── meta
│   └── dagensnaeringsliv_null_null_20230223_134_46_1_meta_xml.tar
├── ocr
│   └── dagensnaeringsliv_null_null_20230223_134_46_1_ocr_xml.tar
├── pdf
│   └── dagensnaeringsliv_null_null_20230223_134_46_1_pdf.tar
├── view
│   └── dagensnaeringsliv_null_null_20230223_134_46_1_view_jp2.tar
├── checksum.md5
└── checksum_transferred.md5
```

### Sjekksumfiler
Filstiene må være relativ til rot-nivå, og kan ikke starte med punktum, skråstrek eller omvendt skråstrek. Alle filer som avleveres må være referert i checksum_transferred.md5, og motsatt - alle filer som finnes i checksum_transferred.md5 må eksistere på disk.

{{< callout type="info" >}}
Sjekksumfiler må oppfylle kravene spesifisert her: Krav til sjekksumfiler.
{{< /callout >}}

#### Innhold i checksum.md5

Dette er en sjekksumfil som inneholder sjekksum og filnavn til alle enkeltfiler før pakking i .tar filer. Som standard er denne påkrevd, men kan etter avtale gjøres unntak fra dersom filene ikke pakkes.

Sjekksumfilen må inneholde sjekksummer av alle filer som skal avleveres. 

Eksempel:
```
3fb1e6c8d4380ebacdc18cd5bfaa85e6 *pdf/dagensnaeringsliv_null_null_20230607_134_128_1-1_001_hovedavis.pdf
69f0fd05e00aca528ebacd35f7a4c6aa *pdf/dagensnaeringsliv_null_null_20230607_134_128_1-1_002_hovedavis.pdf
6a94209252d4e293813f71710db9e068 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_001_hovedavis.jp2.xml
316df33033899d189445db203218a462 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_001_hovedavis.pdf.xml
831f7bc4de22f406e33276c6ba5ef3c3 *meta/MAVIS_dagensnaeringsliv_null_null_20230607_134_128_1.xml
aafa01f48c701aa0a48c5b815a0e7ef7 *meta/MAVIS_yearTitle_dagensnaeringsliv_null_null_20230607_134_128_1.xml
7b4d09574f1cdbda1028d8831462a0e3 *meta/METS_dagensnaeringsliv_null_null_20230607_134_128_1-1_001_hovedavis.xml
583813010f2975c76e2b1db992f815c9 *meta/METS_dagensnaeringsliv_null_null_20230607_134_128_1-1_002_hovedavis.xml
74371855eea47b81144cf41841662407 *ocr/dagensnaeringsliv_null_null_20230607_134_128_1-1_001_hovedavis.xml
f30b8e0ef83b54cc34106d64f691f482 *ocr/dagensnaeringsliv_null_null_20230607_134_128_1-1_002_hovedavis.xml
```

#### Innhold i checksum_transferred.md5

Dette er en sjekksumfil som er laget etter tar-pakking av alle enkeltfiler, og inneholder sjekksum på alle filer som skal overføres til DPS (inkludert checksum.md5 filen). Dette er en påkrevd fil.

{{< callout type="warning" >}}
Merk at vi ønsker å få med checksum.md5 her
{{< /callout >}}

Eksempel:
```
ffff5ab4c72e87589ed7cd10a5e6a6a5 *meta/dagensnaeringsliv_null_null_20230607_134_128_1_meta_xml.tar
0c1af21bf8ec7883f1347f72b95fc4d7 *ocr/dagensnaeringsliv_null_null_20230607_134_128_1_ocr_xml.tar
ae4ab3e5ba01d84c44cd3c91ed4b6962 *pdf/dagensnaeringsliv_null_null_20230607_134_128_1_pdf.tar
a593473d499d3f62d646b10230a1438e *view/dagensnaeringsliv_null_null_20230607_134_128_1_view_jp2.tar
e31bfe7c4aaa5019ae11353d606885b9 *checksum.md5
```

### Prioritering
DPS tildeler en standard prioritet basert på hvilket område den henter SIPene fra. Denne er mulig å overstyre ved å sette egen prioritet i Kafkameldingen.

### Bruk av Apache Kafka i DPS
Apache Kafka brukes som asynkron kommunikasjonskanal mellom avleverer og DPS. Dedikerte Kafka-topics er opprettet spesielt for dette formålet. 

Her er nærmere informasjon om hvilke Kafka topics og meldingsformat DPS bruker.

#### Kafka-meldinger til DPS når SIP er klar for bevaring
Når avleverer har kopiert SIP til avleveringsområdet, og satt riktige rettiheter - må det sendes én Kafka-melding pr SIP til topic: `digitalpreservation_dps_transfer`. DPS vil da umiddelbart starte validering av SIP som en del av bevaringsprosessen. 

{{< callout type="warning" >}}
Obs: Når en Kafka-melding er sendt til `digitalpreservation_dps_transfer topicen, regnes SIP som låst av Digital Bevaring, og ingen endringer av SIP er tillatt. Eventuelle endringer som gjøres på SIP etter at meldingen er sendt, blir ikke nødvendigvis fanget opp av DPS. DPS vil slette SIP når den er bevart, og eventuelle endringer vil da bli slettet uten å ha blitt bevart.
{{< /callout >}}

#### Kafka-meldinger fra DPS når SIP er bevart
Etter at SIP er blitt bevart i DPS, sender DPS en bekreftelse i form av en Kafka-melding på `digitalpreservation_dps_confirm` topicen. Denne topicen er felles for alle avleverere, og man må derfor filtrere ut de meldingene som er relevante for seg selv.

#### Kafka-meldinger fra DPS om en SIP har blitt avvist
Hvis valideringen av SIP feiler, får avleverer informasjon om dette i form av en Kafka-melding på `digitalpreservation_dps_reject` topicen. Denne topicen er felles for alle avleverere, og man må derfor filtrere ut de meldingene som er relevante for seg selv.

DPS stopper da prosesseringen, og gjør ikke noe mer med SIP. Katalogen blir IKKE slettet fra avleveringsområdet, og det forventes at avleverer korrigerer feilen og sender ny Kafka-melding.

#### Versjonering/endring av en SIP
{{< callout type="info" >}}
I noen tilfeller kan det være behov for å endre en SIP etter at den er bevart. Dette kan skyldes at nye filer er skapt, eller at eksisterende filer er korrigerte. Dette løses ved versjonering av bevaringspakkene. Så langt ser det ut til at OCFL er en mekanisme som egner seg godt til dette. Dette er imidlertid ikke implementert i DPS enda.
{{< /callout >}}

Inntil vi har fått etablert versjonering kan objekter bevares på nytt på følgende måte:

- Eksisterende versjon av SIP må være fullstendig bevart i DPS, dvs. at avleverer må ha mottatt Kafka-melding på digitalpreservation_dps_confirm topic.
- Ny komplett SIP må legges på avleveringsområdet
- SIP slettes i DPS ved bruk av egen DPS Delete-tjeneste. Kontakt team Digital Bevaring for mer informasjon om dette.
- Ny Kafka-melding sendes til digitalpreservation_dps_transfer topic.

{{< callout type="error" >}}
Merk: All historikk og sporing av opprinnelig SIP vil bli slettet i DPS, og vi vil ikke ha noen informasjon om at ny SIP tidligere har vært bevart. Dette bør derfor ikke gjøres med mindre det er strengt nødvendig.
{{< /callout >}}
