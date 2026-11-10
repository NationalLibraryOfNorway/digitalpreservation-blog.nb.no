---
title: Bevaringseventer
weight: 4
draft: false
aliases:
  - /docs/dps/api/submission/events/
  - /docs/dps/reference/preservation-events/
---

Denne siden spesifiserer elementene i en bevaringsevent og eventtypene som brukes i DPS. Hva eventer er og hvorfor de er viktige, er beskrevet under [Bevaringseventer](/nb/docs/understanding/metadata-management/preservation-events/). Hvordan du velger og leverer eventer, er beskrevet under [Legge til bevaringseventer](/nb/docs/how-to/add-preservation-events/).

## Event-elementer

**Tillatte elementer er:**

**Agent (`agent`):**\*

- **agentName**\*
- **agentType**\*
- **agentVersion**
- **agentNote**

**Event (på toppnivå):**

- **eventDateTime**\*
- **eventType**\*
- **eventDetail**
- **fileRef** (med **relativePath**\* når `fileRef` brukes)
- **outcome**\*
- **outcomeDetail**

Elementer merket med \* er påkrevde.


## Agent

Agent beskriver den aktøren (hvem eller hva) som utførte handlingen. Dette kan være programvare, en organisasjon eller en person. 
Informasjonen skal være tilstrekkelig presis til å kunne identifisere hvilken aktør og konfigurasjon som ble brukt.

### AgentName

Navn på aktøren som utførte handlingen. Navnet skal være entydig og konsekvent brukt.

**Eksempler:**

- "Apache NiFi"
- "Nasjonalbiblioteket – Team digital bevaring"
- "Ola Nordmann"
- "JHOVE"

### AgentType

Angir hvilken type aktør som utførte handlingen. 
Verdiene er hentet fra [Library of Congress sitt vokabular for agentType](https://id.loc.gov/vocabulary/preservation/agentType.html).

**Tillatte verdier:**

- "software"
- "organization"
- "person"
- "hardware"

### AgentVersion

Angir agentens versjon eller revisjon. Feltet er **kun** relevant for agenter av typen programvare og maskinvare. Agentversjon brukes for å sikre sporbarhet og mulighet for reproduksjon, ulike versjoner av samme verktøy
kan gi ulike resultater.

**Eksempler:**

- "1.15.0"
- "3.2"
- "1.11.0; DROID\_SignatureFile\_V116.xml; container-signature-20231127.xml"

### AgentNote

Tilleggsinformasjon om agenten som utførte handlingen. Elementet skal dokumentere egenskaper, kontekst eller oppsett av agenten, ikke hva agenten gjorde i et
spesifikt event.

**Dette kan inkludere:**

- Hva agenten er, og hva den gjør generelt.
- Hvordan agenten er konfigurert eller installert.
- Operativ kontekst eller ansvar.

**Eksempler:**

- "Verktøy for identifisering av filformater som bruker PRONOM-signaturer. Installert med signatursett versjon 95, som støtter formatene PDF, TIFF, JPEG og
  XML."
- "Programvare for automatisering av dataflyter som muliggjør utforming og administrasjon av komplekse datapipelines."
- "Installert i en tilpasset konfigurasjon med aktiverte moduler for PDF, TIFF og JPEG. Løsningen kjører i kjøremiljø Java 17."
- "Institusjon med formelt ansvar for digital bevaring, mottak og langsiktig forvaltning av arkivmateriale."

> [!NOTE]
> Bruk konsekvente formuleringer i agentNote når du beskriver samme agent.

## Event

Event beskriver selve handlingen som ble utført på objektet.

### EventDateTime

Tidspunktet hendelsen fant sted. Skal angis etter ISO 8601-standarden, med tidssone.

**Eksempel:**

- "2026-02-23T10:45:00+01:00"

### EventType

Angir hvilken type handling som ble utført. Elementet beskriver hva slags prosess hendelsen representerer. Verdien skal være en kontrollert og konsekvent brukt
betegnelse – se liste med tillatte typer nedenfor.

### EventDetail

En presis beskrivelse av hva som ble gjort i hendelsen. 
Beskrivelsen bør angi hvilken operasjon som ble utført, på hvilket objekt, og eventuelt hvilken metode, standard eller prosess som ble brukt.

**Eksempler:**

- "MD5-sjekksum generert."
- "Migrert fra TIFF til JPEG2000."
- "Validert mot PDF/A-2b-standarden."

### Outcome

Overordnet resultat av hendelsen. 
Dette elementet angir om hendelsen ble gjennomført som forventet, mislyktes eller ble fullført med avvik. 
Verdien skal være konsistent og brukes likt for tilsvarende hendelser.
Verdiene er hentet fra [Library of Congress sitt vokabular for eventOutcome](https://id.loc.gov/vocabulary/preservation/eventOutcome.html).

**Tillatte verdier:**

- "success" – hendelsen ga det tiltenkte resultatet.
- "warning" – hendelsen ga en advarsel som må vurderes. Dette omfatter også delvis vellykkede hendelser, for eksempel en validering som rapporterer brudd på et BØR-krav.
- "fail" – hendelsen ga ikke det tiltenkte resultatet.

### OutcomeDetail

Dette elementet brukes bare der det er behov for å dokumentere ytterligere informasjon om utfallet. I mange tilfeller er det tilstrekkelig å bruke «outcome»-elementet (success, warning, fail).
"OutcomeDetail" er en konkret og presis beskrivelse av resultatet av hendelsen. 
Feltet bør brukes når resultatet inneholder informasjon som er relevant for videre bruk, kontroll eller dokumentasjon. 
Dette elementet skal dokumentere hva som faktisk ble oppnådd eller hvilke avvik som ble identifisert. 
Beskrivelsen skal være kortfattet og forståelig. 


**Eksempler:**

- "Formatet er identifisert som fmt/353 (TIFF 6.0)."
- "Pakken er validert mot profilene E-ARK-SIP-v2-2-0, NB-SIP-STRUCTURE-1.0 og NB-SIP-MOVINGIMAGES-PROFILE-1.0 med én advarsel: CSIPSTR13 representasjonsmappen primary_20250325 mangler undermappen metadata (BØR-krav). Behandlingen fortsatte."


## Eventtyper som godtas via API-et

Nasjonalbiblioteket har tatt utgangspunkt i [Library of Congress](https://www.loc.gov/) sin liste
over [EventTypes](https://id.loc.gov/vocabulary/preservation/eventType.html). Lista har blitt innskrenket, og bruken av de ulike typene er spesifisert til å
passe våre behov og bevaringsomgivelser. Andre typer enn det som er spesifisert i lista nedenfor blir ikke godkjent i API.

### Capture

| Navn          | **capture**                                                                                                                                                                                |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Beskrivelse 	 | Prosessen der en agent (organisasjon, team, rolle, system, tjeneste, automatisert prosess) aktivt tilegner seg et objekt gjennom andre mekanismer enn overføring fra skaper eller giver. Innhenting av eksisterende digitale data.	 |
| Omfang        | IE, Fil                                                                                                                                                                                    |

**Retningslinjer for bruk:**

- Brukes når det høstes nettsteder ved hjelp av crawling.

**Eksempel:**

```json
{
  "agent": {
    "agentName": "Heritrix Web Crawler",
    "agentType": "software",
    "agentVersion": "3.5.0",
    "agentNote": "Brukt til nettarkivering for å høste inn nettsteder; HTML, bilder, skript og lenkede ressurser."
  },
  "eventDateTime": "2026-02-03T07:14:01.716+01:00",
  "eventType": "capture",
  "eventDetail": "Høstet nettstedet 'https://example.org'; alle sider, bilder, PDF-er og lenkede ressurser, i henhold til automatisk periodisk webhøsting.",
  "outcome": "success",
  "outcomeDetail": "Totalt antall sider høstet: 234; total datastørrelse: 1,2 GB; alle URL-er arkivert i WARC-format."
}

```

### Creation

| Navn        | **creation**                            |
|:------------|:----------------------------------------|
| Beskrivelse | Prosessen der et nytt objekt opprettes. En ny fil eller et digitalt objekt skapes, for eksempel ved digitalisering. |
| Omfang      | IE, Fil                                 |

**Retningslinjer for bruk:**

- Brukes for å dokumentere opprettelse av et digitalt objekt.
- Brukes til å dokumentere opprinnelsen til filen eller den Intellektuelle Entiteten (IE), og beskriver metoden og prosessen for å opprette filen/IE. Se også
  eventType "imaging".

**Eksempel:**

```json
{
  "agent": {
    "agentName": "Pyramix",
    "agentType": "software",
    "agentVersion": "15.0.8",
    "agentNote": "Programvare for innspilling, redigering, miksing og mastering av lyd."
  },
  "eventDateTime": "2026-02-03T08:02:17.304+01:00",
  "eventType": "creation",
  "eventDetail": "Digitalisering av fysisk bærer, 1/4-tommes lydbånd, til WAV/BWF ved bruk av Pyramix og A/D-konverter. Opptak gjort i sanntid fra analog kilde via ekstern konverter. Verifisert opptakskvalitet.",
  "outcome": "success"
}
```

### Filename change

| Navn        | **filename change**              |
|-------------|----------------------------------|
| Beskrivelse | Prosessen der et filnavn endres. |
| Omfang      | Fil                              |

**Retningslinjer for bruk:**

- Brukes ved endring av filnavnet på en digitalt født fil.
- Dokumenterer hel eller delvis endring av det opprinnelige filnavnet, for eksempel ved fjerning av forbudte tegn eller mellomrom, tilpasning til gjeldende filnavnstandard eller korrigering av feil i filnavnet.

**Eksempel:**

```json
{
  "agent": {
    "agentName": "Apache NiFi",
    "agentType": "software",
    "agentVersion": "2.4.0",
    "agentNote": "Programvare for automatisering av dataflyter som muliggjør utforming og administrasjon av komplekse datapipelines."
  },
  "eventDateTime": "2026-02-03T10:47:29.332+01:00",
  "eventType": "filename change",
  "eventDetail": "Filnavnet ble endret fra NN_TR_2011_01_31_18_40.mp4 til NRK_TR_2011_01_31_18_40.mp4 for å følge gjeldende filnavnstandard. Filnavnprefikset angir hvilken radiokanal filen stammer fra. Det opprinnelige prefikset NN var feil og ble erstattet med NRK.",
  "fileRef": {
    "relativePath": "representations/primary_20250325/data/NRK_TR_2011_01_31_18_40.mp4"
  },
  "outcome": "success"
}
```

### Fixity check

| Navn        | **fixity check**                         |
|-------------|------------------------------------------|
| Beskrivelse | Prosessen der det verifiseres at et objekt ikke er endret ved å kontrollere sjekksum(er). |
| Omfang      | IE, Fil                                  |


**Retningslinjer for bruk:**
- Brukes til å verifisere at et digitalt objekt ikke er endret ved å kontrollere og sammenligne objektets sjekksum med en tidligere registrert sjekksum.
- Eventen bør knyttes til IE når det er mulig. Knyttes kun til fil dersom det er behov for å dokumentere avvik.
- Vil mest sannsynlig inneholde resultatene fra eventen «message digest calculation».
- Spesielt viktig når sjekksummer mottas fra eksterne.


**Eksempel:**

```json
{
  "agent": {
    "agentName": "md5sum (GNU coreutils)",
    "agentType": "software",
    "agentVersion": "8.32",
    "agentNote": "Verktøy brukt til å beregne og verifisere sjekksummer for å kontrollere dataintegritet over tid."
  },
  "eventDateTime": "2026-02-03T12:05:48.210+01:00",
  "eventType": "fixity check",
  "eventDetail": "MD5-sjekksummer ble kontrollert mot tidligere registrerte verdier for alle filer i pakken.",
  "outcome": "success"
}
```

### Imaging

| Navn        | **imaging**                                                             |
|-------------|-------------------------------------------------------------------------|
| Beskrivelse | Prosessen med å hente ut et diskbilde fra et fysisk informasjonsmedium. |
| Omfang      | IE                                                                      |

**Retningslinjer for bruk:**

- Brukes for å dokumentere prosessen med å lage en eksakt digital kopi (diskbilde) av et lagringsmedium, inkludert alle filer, metadata, filsystemstruktur og
  noen ganger også ledig plass og slettede data.
- Som hovedregel brukes denne eventen i stedet for «creation»-eventen, ikke i tillegg til. I enkelte tilfeller kan det likevel være relevant å benytte begge eventene.

**Eksempel:**

```json
{
  "agent": {
    "agentName": "GNU ddrescue",
    "agentType": "software",
    "agentVersion": "1.27",
    "agentNote": "Verktøy brukt for å opprette bit-for-bit diskbilder fra fysiske lagringsmedier."
  },
  "eventDateTime": "2026-02-03T09:00:00+01:00",
  "eventType": "imaging",
  "eventDetail": "Opprettet bit-for-bit diskbilde fra ekstern harddisk. Diskbildet inkluderer filsystemstruktur og tilhørende metadata fra originalmediet.",
  "outcome": "success"
}
```

### Information package creation

| Navn        | **information package creation**                                                             |
|-------------|-------------------------------------------------------------------------|
| Beskrivelse | Prosessen med å opprette en informasjonspakke (SIP, AIP eller DIP).     |
| Omfang      | IE                                                                      |

**Retningslinjer for bruk:**
- Brukes når en SIP, AIP eller DIP opprettes som en ny informasjonspakke, inkludert etablering av pakkestruktur, metadata og tilhørende filer i henhold til gjeldende pakkestandard (f.eks. E-ARK).
- Skal ikke brukes ved ren kopiering eller flytting av eksisterende pakker uten endring av pakkestruktur eller metadata.
- Hvis det brukes SIP-generator utviklet av Nasjonalbiblioteket, uten endringer, bruk agent fra første eksempel. 

**Eksempel:**


```json
{
  "agent": {
    "agentName": "nifi-nb-eark-nar.EarkSIPGenerator",
    "agentType": "software",
    "agentVersion": "1.0.11",
    "agentNote": "Apache NiFi-prosessor utviklet av Nasjonalbiblioteket for opprettelse av E-ARK SIP. Bruker commons-ip, et Java-bibliotek for opprettelse og håndtering av E-ARK-informasjonspakker."
  },
  "eventDateTime": "2026-02-03T16:42:15+01:00",
  "eventType": "information package creation",
  "eventDetail": "Opprettet SIP i henhold til Nasjonalbibliotekets profil SIP 1.0.",
  "outcome": "success"
}
```

```json
{
  "agent": {
    "agentName": "org.roda-community:commons-ip2",
    "agentType": "software",
    "agentVersion": "2.12.0",
    "agentNote": "Java-bibliotek for opprettelse og håndtering av E-ARK-informasjonspakker."
  },
  "eventDateTime": "2026-02-03T16:58:03+01:00",
  "eventType": "information package creation",
  "eventDetail": "Opprettelse av E-ARK SIP i henhold til E-ARK Common Specification (CSIP) V.2.2.0, E-ARK SIP V.2.2.0 og Nasjonalbibliotekets spesifikasjoner SIP 1.0 (E-ARK).",
  "outcome": "success"
}
```


### Message digest calculation

| Navn        | **message digest calculation** |
|-------------|--------------------------------|
| Beskrivelse | Opprettelsen av sjekksum(er).            |
| Omfang      | IE, Fil                        |

**Retningslinjer for bruk:**

- Brukes ved opprettelse av nye sjekksummer. Hvis sjekksummer opprettes lokalt, er det ikke behov for å bruke eventen "fixity check" i tillegg til event "message digest calculation". Se også EventType "fixity check".
- Eventen «fixity check» dokumenterer kontroll av sjekksum(er).
- Eventen bør knyttes til IE når det er mulig. Dersom det er behov for å dokumentere avvik, skal avviket knyttes til den aktuelle filen.


**Eksempel:**

```json
{
  "agent": {
    "agentName": "md5sum (GNU coreutils)",
    "agentType": "software",
    "agentVersion": "8.32",
    "agentNote": "Verktøy brukt til å beregne og verifisere sjekksummer for å kontrollere dataintegritet over tid."
  },
  "eventDateTime": "2026-02-03T13:36:42.455+01:00",
  "eventType": "message digest calculation",
  "eventDetail": "MD5-sjekksummer ble beregnet for alle filer i pakken.",
  "outcome": "success"
}
```

### Metadata extraction

| Navn          | **metadata extraction**                                                                                |
|:--------------|:-------------------------------------------------------------------------------------------------------|
| Beskrivelse 	 | Uttrekk av metadata fra et objekt. Dette inkluderer tekniske, administrative og beskrivende metadata.	 |
| Omfang        | Fil                                                                                                    |

**Retningslinjer for bruk:**

- Brukes når metadata hentes ut av en fil. 
- Utledet metadata må referere til opprinnelsesfila i `"fileRef"`.
- Hvis uttrekk resulterer i en eller flere metadatafiler, må `"OutcomeDetail"` inkludere referanse (relativ filsti) til utledet/generert metadatafil.

**Eksempler:**

Eksempel på metadatauttrekk dokumentert i outcomeDetail:
```json
{
  "agent": {
    "agentName": "ExifTool",
    "agentType": "software",
    "agentVersion": "12.60",
    "agentNote": "Utleder tekniske metadata fra filer."
  },
  "eventDateTime": "2026-02-19T11:45:32.123+01:00",
  "eventType": "metadata extraction",
  "eventDetail": "Utledet tekniske metadata fra bildefil.",
  "fileRef": {
    "relativePath": "representations/rep-images_20230908/data/DSC_0456.JPG"
  },
  "outcome": "success",
  "outcomeDetail": "Bilde: format JPEG, oppløsning 8256x5504 piksler, 24-bit farge; Kamera: Nikon D850; Linse: 24-70mm f/2.8; Eksponering: 1/125 s ved f/8; ISO: 100; Filstørrelse: 18,2 MB."
}
```

Eksempel på metadatauttrekk resulterende i en ny fil:
```json
{
  "agent": {
    "agentName": "Audioinspector",
    "agentType": "software",
    "agentVersion": "5.5",
    "agentNote": "Programvare for automatisk analyse, kvalitetskontroll og metadatahåndtering av lydfiler."
  },
  "eventDateTime": "2026-02-11T12:01:08Z",
  "eventType": "metadata extraction",
  "eventDetail": "WAV-filen ble analysert for kvalitetskontroll og dokumenta++sjon.",
  "fileRef": {
    "relativePath": "representations/primary_20250325/data/something.wav"
  },
  "outcome": "success",
  "outcomeDetail": "Utledet en XML-metadatafil som inneholder detaljert analyse: representations/primary_20250325/metadata/technical/audioinspector/metadata.xml"
}
```

### Migration

| Navn        | **migration**                    |
|-------------|----------------------------------|
| Beskrivelse | Konvertering til nytt filformat. |
| Omfang      | IE, Fil                          |

**Retningslinjer for bruk:**

- Brukes når en eller flere filer konverteres til et annet filformat. 
- Eventen bør knyttes til IE når det er mulig, for eksempel dersom filene er konvertert på samme måte til samme format.
- Migration-events skal alltid resultere i en ny fil(er) eller pakke.
- Relevante parametere som beskriver migreringsprosessen, bør dokumenteres i `eventDetail`.
- Filen(e) som migreres må referere til opprinnelsesfila i `fileRef` når enkeltfiler migreres (når eventen ikke er knyttet til IE).
- `OutcomeDetail` må inkludere referanse (relativ filsti) til migrert fil(er).

**Eksempel:**

```json
{
  "agent": {
    "agentName": "FFmpeg",
    "agentType": "software",
    "agentVersion": "6.0",
    "agentNote": "Mediekonvertering og koding av AV-filer."
  },
  "eventDateTime": "2026-02-03T15:09:55.774+01:00",
  "eventType": "migration",
  "eventDetail": "Batch-migrering av alle MOV-filer i pakken (25 filer) til MXF/Op1a-format med tapsfri JPEG2000-videokodek og 24-bit PCM-lydkodek. Brukte parametere: command=ffmpeg -i input.mov -c:v jpeg2000 -pred dwt53 -c:a pcm_s24le output.mxf; container=MXF/Op1a; videoCodec=JPEG2000 (tapsfri, dwt53); audioCodec=PCM 24-bit; integrityChecked=yes",
  "outcome": "success",
  "outcomeDetail": "Resulterende MXF-filer lagret i representations/primary_20250325/data/."
}
```

### Transfer

| Navn        | **transfer**                                                                  |
|-------------|-------------------------------------------------------------------------------|
| Beskrivelse | Prosessen med å overføre metadata og/eller digitale objekter mellom systemer. |
| Omfang      | IE                                                                            |

**Retningslinjer for bruk:**

- Brukes ved overføring av materiale mellom ulike systemer eller organisatoriske kontekster, for eksempel fra produsent til bevaringssystem eller mellom ulike lagringsmiljøer. Skal ikke brukes for interne arbeidsflyter eller interne prosesseringssteg.
- Ikke bruk transfer-event for flytting av materiale inn i DPS (avlevering via API), systemet oppretter en event ved mottak.  
  
**Eksempel:**

```json
{
  "agent": {
    "agentName": "Apache NiFi",
    "agentType": "software",
    "agentVersion": "2.4.0",
    "agentNote": "Programvare for automatisering av dataflyter som muliggjør utforming og administrasjon av komplekse datapipelines."
  },
  "eventDateTime": "2026-02-18T14:02:33+01:00",
  "eventType": "transfer",
  "eventDetail": "Overført pakke fra bevaringslageret Oracle HSM (SAM-FS) til lokalt arbeidsområde for videre behandling; opprinnelige sjekksummer verifisert med md5sum (GNU coreutils) ved opplasting.",
  "outcome": "success"
}
```

### Validation

| Navn        | **validation**           |
|-------------|--------------------------|
| Beskrivelse | Validering mot standard. |
| Omfang      | IE, Fil                  |

**Retningslinjer for bruk:**

- Brukes når en pakke eller fil kontrolleres for å verifisere at den er i samsvar med en bestemt standard, profil, spesifikasjon eller andre definerte krav.
- Objektet som valideres, kan være en enkelt fil eller en intellektuell enhet (IE). Eventen bør knyttes til IE når det er mulig, for eksempel når flere filer er validert på samme måte og med samme verktøy, eller når pakkens struktur er validert som en helhet. Det bør også fremgå hva valideringen er utført mot, for eksempel en standard, profil, spesifikasjon eller andre definerte krav.
- Det kan være hensiktsmessig å lage én event for hele valideringen der man heller beskriver hvilke verktøy som er brukt i de ulike stegene, i stedet for å lage flere eventer for flere valideringer.

**Eksempler:**

```json
{
  "agent": {
    "agentName": "JHOVE",
    "agentType": "software",
    "agentVersion": "1.32.1",
    "agentNote": "Verktøy brukt til identifikasjon, validering og karakterisering av digitale objekter."
  },
  "eventDateTime": "2026-02-03T17:30:39.662+01:00",
  "eventType": "validation",
  "eventDetail": "Validerte alle PDF-filer i pakken (35 filer) med JHOVE for å kontrollere at filene samsvarer med spesifikasjonene for PDF 1.7.",
  "outcome": "success"
}
```

```json
{
  "agent": {
    "agentName": "Apache NiFi",
    "agentType": "software",
    "agentVersion": "2.4.0",
    "agentNote": "Programvare for automatisering av dataflyter som muliggjør utforming og administrasjon av komplekse datapipelines."
  },
  "eventDateTime": "2026-02-03T17:41:12.508+01:00",
  "eventType": "validation",
  "eventDetail": "Validerte E-ARK SIP ved bruk av DPS Validation workflow v.a00f683: nifi-nb-eark-nar.EarkSIPValidator 1.0.7; org.roda-community:commons-ip2 2.12.0. Validert mot profilene E-ARK-SIP-v2-2-0, NB-SIP-STRUCTURE-1.0 og NB-SIP-MOVINGIMAGES-PROFILE-1.0.",
  "outcome": "success"
}
```

Eksempel på validering med avvik som ikke stoppet behandlingen:

```json
{
  "agent": {
    "agentName": "Apache NiFi",
    "agentType": "software",
    "agentVersion": "2.4.0",
    "agentNote": "Programvare for automatisering av dataflyter som muliggjør utforming og administrasjon av komplekse datapipelines."
  },
  "eventDateTime": "2026-02-03T17:48:05.219+01:00",
  "eventType": "validation",
  "eventDetail": "Validerte E-ARK SIP ved bruk av DPS Validation workflow v.a00f683: nifi-nb-eark-nar.EarkSIPValidator 1.0.7; org.roda-community:commons-ip2 2.12.0.",
  "outcome": "warning",
  "outcomeDetail": "Validert mot profilene E-ARK-SIP-v2-2-0 og NB-SIP-STRUCTURE-1.0 med én advarsel: CSIPSTR13 – representasjonsmappen primary_20250325 mangler undermappen metadata (BØR-krav). Behandlingen fortsatte."
}
```

### Virus check

| Navn          | **virus check**                                                      |
|:--------------|:---------------------------------------------------------------------|
| Beskrivelse 	 | Prosessen der en fil skannes for virus eller skadelig programvare. 	 |
| Omfang        | IE, Fil                                                              |

**Retningslinjer for bruk:**

- Eventen bør knyttes til IE når det er mulig. Knyttes kun til fil dersom det er behov for å dokumentere avvik.
- Hvis det blir funnet virus eller annen skadelig programvare, skal `outcome` være `fail`. Knytt eventen til den berørte filen med `fileRef`, og beskriv funnet i `outcomeDetail`.

**Eksempler:**

```json
{
  "agent": {
    "agentName": "ClamAV",
    "agentType": "software",
    "agentVersion": "1.4.2",
    "agentNote": "Antivirusprogram brukt til å oppdage skadelig programvare. Virussignatur: daily.cvd, versjon 27890; main.cvd, versjon 12345."
  },
  "eventDateTime": "2026-02-03T18:27:53.842+01:00",
  "eventType": "virus check",
  "eventDetail": "Alle filer i pakken ble skannet for virus og annen skadelig programvare før videre behandling.",
  "outcome": "success"
}
```

```json
{
  "agent": {
    "agentName": "ClamAV",
    "agentType": "software",
    "agentVersion": "1.4.2",
    "agentNote": "Antivirusprogram brukt til å oppdage skadelig programvare. Virussignatur: daily.cvd, versjon 27890; main.cvd, versjon 12345."
  },
  "eventDateTime": "2026-02-03T08:51:40.127+01:00",
  "eventType": "virus check",
  "eventDetail": "Filen ble skannet for virus og annen skadelig programvare før overføring.",
  "fileRef": {
    "relativePath": "representations/primary_20250325/data/file_2026.xml"
  },
  "outcome": "fail",
  "outcomeDetail": "Oppdaget signaturen Win.Trojan.MacroVirus-12345."
}
```

## Eventer som genereres av DPS

> [!NOTE]
> Denne delen er under arbeid. Den vil liste eventtypene DPS registrerer selv, når hver av dem registreres, og hvilken agent som brukes.

DPS registrerer egne eventer under mottak, under bevaring og når innhold hentes ut. Dette omfatter eventer for overføring, validering, verifisering, filformatidentifisering og uttrekk av teknisk metadata. Noen av disse eventtypene brukes bare internt og kan ikke leveres via API-et.
