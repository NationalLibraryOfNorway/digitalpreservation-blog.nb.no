---
title: DPS sin rolle i NB
weight: 1
draft: true
aliases:
  - /systemarkitektur
  - /forvaltningsarkitektur
  - /docs/dps/architecture/
---

Digital Preservation Services (DPS) er Nasjonalbibliotekets system for langsiktig digital bevaring.
DPS opererer ikke i et vakuum: det er ett av tre systemdomener som deler ansvaret for digitale objekter i Nasjonalbiblioteket. Disse domenene opererer selvstendig, men hvert domens ansvar påvirker de andre.
Denne siden beskriver konteksten DPS ble bygget i, og hvordan denne konteksten former systemet.

De tre systemdomenene som beskrives her, gjenspeiler Nasjonalbibliotekets interne driftslandskap.

Eksterne klienter samhandler med DPS direkte gjennom API-et og bringer sine egne identifikatorer, metadata og omfangsdefinisjoner.

{{< figure src="onioncontext.svg" alt="DPS innenfor NBs organisatoriske kontekst" caption="DPS innenfor NBs organisatoriske kontekst" >}}

## De tre systemdomenene

Internt i Nasjonalbibliotekets egne samlinger er ansvaret for digitale objekter[^1] fordelt mellom tre systemdomener, som hver forvalter forskjellige aspekter ved objektene:

### Metadatasystemer

Biblioteksystemer, kataloger, registre og forvaltningssystemer (som Alma, Mavis og Hanske). De er hovedkilden for deskriptive metadata og utsteder unike identifikatorer (UID-er, typisk URN-er) for digitale objekter. Disse systemene forvalter et bredt spekter av entiteter; kun en delmengde beskriver digitale objekter relevante for digital bevaring.

Det er her intellektuelle entiteter defineres: valget av hva som utgjør en bevaringsverdig informasjonspakke starter her, ikke i DPS. Én URN tilsvarer typisk én pakke. For detaljer om pakkeomfang, se [Pakke-, representasjons- og dataomfang](/docs/dps/sip/scope/).

### Digital Preservation Services (DPS)

Bevaringssystemet. Forvalter bevaringsdata med en PREMIS-basert datamodell (intellektuelle entiteter, representasjoner, filer, eventer, agenter). DPS tilbyr "kald" langtidslagring med asynkron tilgang, designet for bevaring fremfor umiddelbar uthenting. DPS er hovedkilden for tekniske metadata på filnivå i Nasjonalbiblioteket. DPS er ikke hovedkilden for deskriptive metadata: systemet holder metadataene det trenger for å operere selvstendig, uten å gjenskape metadatasystemenes fulle katalogstrukturer.

For eksterne produsenter og konsumenter fungerer DPS som en selvstendig tjeneste: du leverer dine egne identifikatorer og metadata gjennom API-et, og DPS håndterer bevaringen uavhengig. For detaljer om hvordan data og metadata håndteres i DPS, se [Dataforvaltning](/docs/dps/data/) og [Metadataforvaltning](/docs/dps/metadata/).

### Offentlige tilgangstjenester

Nettbiblioteket og Oria. Forvalter en høstet delmengde av deskriptive metadata og tilbyr tilgangskopier utledet fra bevaringsfiler. Disse tjenestene tilbyr "varm" lagring med umiddelbar tilgang, i motsetning til bevaringslagringen til DPS.

De offentlige tilgangstjenestene transformerer de høstede metadataene til en flatere struktur, med én enkelt representasjon per intellektuell entitet. De intellektuelle entitetene som finnes på nett, speiler derfor ikke nødvendigvis entitetene i metadatasystemene.

En UID, forvaltet av metadatasystemene, binder de tre domenene sammen. Den må være unik på tvers av systemene og bør ikke gjenbrukes.

## Data- og metadataflyt

Diagrammet under er en idealisert og forenklet fremstilling av hvordan data og metadata beveger seg mellom domenene:

{{< figure src="context.svg" alt="architecture diagram" caption="Data- og metadataflyt mellom systemer i NB" >}}

SIP-en bærer bevaringsdata og en kopi av deskriptive metadata fra metadatasystemene. DPS bevarer ikke tilgangskopier som kan utledes automatisk fra bevaringsfiler; slike kopier forvaltes av de offentlige tilgangstjenestene.

## PREMIS-entiteter og overlappende ansvar

DPS bruker PREMIS som sin bevaringsmetadatamodell. Verken metadatasystemene eller de offentlige tilgangstjenestene bruker PREMIS direkte, men PREMIS-begrepene hjelper med å forklare hvor ansvarsområdene begynner og slutter på tvers av de tre domenene i NB. Denne kartleggingen forklarer hvorfor DPS ble utformet slik det ble, ikke hvordan eksterne brukere bør modellere sine egne data[^2].

{{% details title="PREMIS-terminologi" closed="true" %}}

### Intellektuelle entiteter (IE)

> An **Intellectual Entity** is a distinct intellectual or artistic creation that is considered relevant to a designated community in the context of digital preservation: for example, a particular book, map, photograph, database, or hardware or software. An intellectual Entity can include other Intellectual Entities[...]

I vår implementering er det et én-til-én-forhold mellom SIP og IE. IE-en er entiteten som identifiseres av UID-en som binder de tre systemdomenene sammen. Vanligvis er dette den **minste** beskrevne enheten i våre metadatasystemer. For detaljer om hvordan dette former pakkeomfang, se [Pakke-, representasjons- og dataomfang](/docs/dps/sip/scope/).

Metadata på pakkerota beskriver IE-en som SIP-en inneholder representasjoner av. Representasjonene er ulike datagjengivelser av IE-en og har ikke egne beskrivende metadata.

### Representasjoner

> A **Representation** is the set of all file objects needed to render an Intellectual Entity.

En pakke kan inneholde flere representasjoner. For de aller fleste SIP-er i Nasjonalbiblioteket er det én enkelt representasjon per pakke. Metadataene på SIP-ens kjerne beskriver hele pakken og alle representasjonene likt.

### Filer

> A **File** is a named and ordered sequence of bytes that is known to an operating system. A File can be zero or more bytes and has a File format, access permissions, and File system characteristics such as size and last modification date.

{{% /details %}}

Innenfor NB er PREMIS-entiteter fordelt på de tre systemdomenene. For eksterne brukere forvalter DPS sin egen datamodell (intellektuelle entiteter, representasjoner og filer) og omfang defineres av klienten. Rollene til de to andre domenene fylles av dine egne systemer.

- **Metadatasystemer**: internt i NB er det her intellektuelle entiteter defineres og identifiseres. Representasjonsnivået er typisk *ikke* beskrevet i disse systemene. De definerer representasjoner implisitt gjennom representasjonens én-til-én-forhold til IE-en.
- **Digital Preservation Services (DPS)**: forvalter den fulle PREMIS-datamodellen: intellektuelle entiteter, representasjoner og filer. DPS gjenskaper ikke metadatasystemenes fulle deskriptive metadatastrukturer. Systemet tilbyr søk basert på metadata som leveres til og genereres av DPS. For detaljer, se [Metadataforvaltning](/docs/dps/metadata/).
- **Offentlige tilgangstjenester**: forvalter og formidler en høstet delmengde av intellektuelle entiteter, tilgangsrepresentasjoner og filer.


[^1]: "Digitale objekter" omfatter både *enkle digitale objekter* (individuelle enkeltfiler) og *komplekse digitale objekter* (grupper av filer). Eksempler på enkle digitale objekter kan være enkeltbilder i TIFF-format, mens komplekse digitale objekter kan være en DCP (en mappe med bilde- og lydstrømmer i MXF-containere og XML-filer).
[^2]: *PREMIS Data Dictionary (full document)*, Version 3.0, Nov. 2015, [https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf](https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf)
