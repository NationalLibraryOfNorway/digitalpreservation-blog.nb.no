---
title: Eventer/ bevaringsmetadata
weight: 2
draft: false
---

> ⚠️ **Disse sidene er under arbeid** ⚠️



I digital bevaring dokumenterer en “event” en handling eller hendelse som har påvirket et digitalt objekt, for eksempel opprettelse, migrering, validering eller overføring. Dette anses som viktig bevaringsmetadata og gir sporbarhet og bevis for hva som er gjort med objektet gjennom hele livssyklusen. 

Avlevering av eventer er ikke et krav, men vi anbefaler at det opprettes hvis man har slik informasjon tilgjengelig. Eventer som legges til i APIet vil bevares i egen event-database, på lik linje med hendelser som skjer på innsiden av bevaringsomgivelsene (DPS). Ved utlevering gir det enklere oversikt over hendelser knyttet til et objekt. Hvis det er ønskelig å legge til andre typer bevaringsmetadata, er det er også mulig å avlevere bevaringsmetadata i informasjonspakken (SIP). Se mer om det under  [metadataveiledning](/docs/dps/sip/1.0/metadata/) og [krav til pakkestruktur](/docs/dps/sip/1.0/structure-requirements/). Informasjon som går direkte på proveniens kan legges til i [krav til metadata](/docs/dps/api/submission/metadata/).

Eventer kan være knyttet til hele informasjonspakken eller til enkelte filer. Generelt bør eventer knyttes til pakkenivå, Intellektuell entitet (IE), der det er mulig. Dette for å unngå store mengder eventer som i utgangspunktet sier det samme. Det er åpent for å legge eventer på filer der det er behov for å dokumentere hendelser på enkeltfiler. Det viktigste er at man har et bevisst forhold til hva som dokumenteres, hvorfor det dokumenteres, og på hvilket nivå. 

Det anbefales at eventene skrives på norsk der det er mulig. Eventene bør utformes med hensyn til framtidig forvaltning og bruk, slik at informasjonen er mest mulig forståelig og etterprøvbar over tid.

Teknisk dokumentasjon for avlevering i API og formatering av eventer finnes her: [Swagger DPS Submission Service API](https://digitalpreservation.no/swagger/)

<br>
<br>

# Bruk av event-elementer

**Tillatte elementer er:** 

**Agent:***
- **agentName***
- **agentType***
- **agentVersion**
- **agentNotes**

**Event:***
- **eventDateTime***
- **eventType***
- **eventDetail**
- **outcome***
- **outcomeDetail**

Elementer merket med * er påkrevde. 
<br><br>

## Forklaring til bruk av event-elementer:

## Agent:
Agent beskriver den aktøren som utførte handlingen. Dette kan være programvare, en organisasjon eller en person.

### AgentName
Navn på aktøren som utførte handlingen. Navnet skal være entydig og konsekvent brukt.

**Eksempler:**
- "Apache NiFi"
- "Nasjonalbiblioteket – Team digital bevaring"
- "Ola Nordmann"
- "JHOVE"


### AgentType
Angir hvilken type aktør som utførte handlingen.

**Tillatte verdier:**
- "software"
- "organization"
- "person"


### AgentVersion
Versjonsnummer på agenten dersom det er programvare. Agentversjon brukes for å sikre sporbarhet og mulighet for reproduksjon, ulike versjoner av samme verktøy kan gi ulike resultater. 

**Eksempler:**
- "1.15.0"
- "3.2"
- "1.11.0; DROID_SignatureFile_V116.xml; container-signature-20231127.xml"



### AgentNotes
Tilleggsinformasjon om agenten som utførte handlingen. Elementet skal dokumentere egenskaper, kontekst eller oppsett av agenten, ikke hva agenten gjorde i et spesifikt event. 

**Dette kan inkludere:**
- Hva agenten er, og hva den gjør generelt.
- Hvordan agenten er konfigurert eller installert.
- Operativ kontekst eller ansvar.
  
**Eksempler:**
- "Verktøy for identifisering av filformater som bruker PRONOM-signaturer. Installert med signatursett versjon 95, som støtter formatene PDF, TIFF, JPEG og XML."
- "Verktøy for automatisering av dataflyt som gjør det mulig å designe og administrere komplekse datapipelines."
- "Installert i en tilpasset konfigurasjon med aktiverte moduler for PDF, TIFF og JPEG. Løsningen kjører i kjøremiljø Java 17."
- "Institusjon med formelt ansvar for digital bevaring, mottak og langsiktig forvaltning av arkivmateriale."

> [!NOTE]
> Bruk AgentNotes så konsekvent som mulig for samme agent. Ved skriveforskjeller i AgentNotes opprettes ny Agent i registeret.


## Event:
Event beskriver selve handlingen som ble utført på objektet.

### EventDateTime
Tidspunktet hendelsen fant sted. Skal angis etter ISO 8601-standarden, med tidssone.

**Eksempel:**
- "2026-02-23T10:45:00+01:00 "


### EventType
Angir hvilken type handling som ble utført. Elementet beskriver hva slags prosess hendelsen representerer.
Verdien skal være en kontrollert og konsekvent brukt betegnelse – se liste med tillatte typer nedenfor.


### EventDetail
En presis beskrivelse av hva som ble gjort i hendelsen. Dette utdyper EventType og beskriver selve operasjonen.

**Eksempler:**
- "MD5-sjekksum generert."
- "Migrert fra TIFF til JPEG2000."
- "Validert mot PDF/A-2b-standarden."



### Outcome
Overordnet resultat av hendelsen. Dette elementet angir om hendelsen ble gjennomført som forventet, mislyktes eller ble fullført med avvik.

**Tillatte verdier:**
- "success"
- "failure"
- "warning"


### OutcomeDetail
En konkret og presis beskrivelse av resultatet av hendelsen.
Dette elementet skal dokumentere hva som faktisk ble oppnådd eller hvilke avvik som ble identifisert. Beskrivelsen skal være kortfattet og forståelig. Det er ikke alle hendelser som er nødvendig å dokumentere utover success/failure/warning, da holder det å bruke «outcome»-elementet. 

**Eksempler:**
- "Formatet er identifisert som fmt/353 (TIFF 6.0)."
- "Pakken er validert mot profilene E-ARK-SIP-v2-2-0, NB-SIP-STRUCTURE-1.0 og NB-SIP-MOVINGIMAGES-PROFILE-1.0."

<br>
<br>

# Event-typer 

Nasjonalbiblioteket har tatt utgangspunkt i [Library of Congress](https://www.loc.gov/) sin liste over [EventTypes](https://id.loc.gov/vocabulary/preservation/eventType.html). Lista har blitt innskrenket, og bruken av de ulike typene er spesifisert til å passe våre behov og bevaringsomgivelser. Andre typer enn det som er spesifisert i lista nedenfor blir ikke godkjent i API.


## EventTypes


### Capture

| Navn 	| **capture** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen der en agent (organisasjon, team, rolle, system, tjeneste, automatisert prosess) aktivt tilegner seg et objekt gjennom andre mekanismer enn overføring fra skaper eller giver. 	|
| Omfang 	| IE, Fil 	|


**Retningslinjer for bruk:**
- Brukes når det høstes nettsteder ved hjelp av crawling.


**Eksempler:**
```json
    {
        "agent": {
            "agentName": "Heritrix Web Crawler",
            "agentType": "software",
            "agentVersion": "3.5.0",
            "agentNotes": "Brukt til nettarkivering for å høste inn nettsteder; HTML, bilder, skript og lenkede ressurser."
        },
        "event": {
            "eventDateTime": "2026-02-03T07:14:01.716+01:00",
            "eventType": "capture",
            "eventDetail": "Høstet nettstedet 'https://example.no'; alle sider, bilder, PDF-er og lenkede ressurser, i henhold til automatisk periodisk webhøsting.",
            "outcome": "success",
            "outcomeDetail": "Totalt antall sider høstet: 234; total datastørrelse: 1,2 GB; alle URL-er arkivert i WARC-format."
        }
    }
```


### Creation 


 | Navn 	| **creation** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen der et nytt objekt opprettes. 	|
| Omfang 	| Fil 	|


**Retningslinjer for bruk:**
- Brukes for å dokumentere det digitale objektet i en informasjonspakke. 
-	Brukes til å dokumentere opprinnelsen til filen eller den Intellektuelle Entiteten (IE), og beskriver metoden og prosessen for å opprette filen/IE. Se også eventType "imaging". 
  

**Eksempler:**
```json
    {
        "agent": {
            "agentName": "Pyramix",
            "agentType": "software",
            "agentVersion": "15.0.8",
            "agentNotes": "Programvare for innspilling, redigering, mixing og mastering av lyd."
        },
        "event": {
            "eventDateTime": "2026-02-03T07:14:01.716+01:00",
            "eventType": "creation",
            "eventDetail": "En digital representasjon av det fysiske materialet ble opprettet gjennom en digitaliseringsprosess.",
            "outcome": "success",
            "outcomeDetail": "De resulterende WAV-filene ble lagret på disk på lydstudioets arbeidsstasjon."
        }
    }
```


### Filename change 


 | Navn 	| **filename change** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen der et filnavn endres.  	|
| Omfang 	| Fil 	|


**Retningslinjer for bruk:**
-	Relevant ved endring av navn på en født digital fil, eller når for eksempel en fil må gis nytt navn for å oppfylle kravene til lagringssystemet. 
-	Enten fjerning av forbudte tegn eller delvis/hel erstatning av det opprinnelige filnavnet. Dette kan brukes for å dokumentere endringer som fjerning av tegn, eller der et system fjerner filnavnet helt og erstatter det med et systemgenerert navn.



**Eksempler:**
 ```json
    {
        "agent": {
            "agentName": "Apache NiFi",
            "agentType": "software",
            "agentVersion": "2.4.0",
            "agentNotes": "Programvare for automatisering av dataflyter som muliggjør utforming og administrasjon av komplekse datapipelines."
        },
        "event": {
            "eventDateTime": "2026-02-03T10:47:29.332+01:00",
            "eventType": "filename change",
            "eventDetail": "Filnavn ble endret for å følge gjeldende filnavnstandard.",
            "fileRef": {
                "fileId": "a1b2c3d4e5f67890123456789abcdef0",
                "relativePath": "representations/rep-text_20230219/data/document_001.pdf"
            },
            "outcome": "success",
            "outcomeDetail": "Filnavn endret fra NN_TR_2011_01_31_18_40.mp4 til NRK_TR_2011_01_31_18_40.mp4."
        }
    }
```


 ### Fixity check 


 | Navn 	| **fixity check** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen med å verifisere at et objekt ikke har blitt endret i en gitt periode.	|
| Omfang 	| IE, Fil 	|


**Retningslinjer for bruk:**
-	Eventen bør knyttes til IE når det er mulig. Knyttes kun til fil dersom det er behov for å dokumentere avvik.
-	Vil mest sannsynlig inneholde resultatene fra eventen «message digest calculation».
- Spesielt viktig når sjekksummer mottas fra eksterne. 


**Eksempler:**
```json
    {
        "agent": {
            "agentName": "md5sum (GNU coreutils)",
            "agentType": "software",
            "agentVersion": "8.32",
            "agentNotes": "Beregner MD5-sjekksummer og verifiserer dem mot lagret sjekksumoversikt."
        },
        "event": {
            "eventDateTime": "2026-02-03T12:05:48.210+01:00",
            "eventType": "fixity check",
            "eventDetail": "MD5-sjekksummer ble beregnet for alle filer i pakken og kontrollert mot lagrede verdier i oversiktsfilen.",
            "outcome": "success"
        }
    } 
```


 ### Imaging 


 | Navn 	| **imaging** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen med å hente ut et diskbilde fra et fysisk informasjonsmedium.	|
| Omfang 	| IE 	|


**Retningslinjer for bruk:**
-	Brukes for å dokumentere prosessen med å lage en eksakt digital kopi (diskbilde) av et lagringsmedium, inkludert alle filer, metadata, filsystemstruktur og noen ganger også ledig plass og slettede data.
-	Der det er relevant, skal denne eventen brukes i stedet for, ikke i tillegg til, «creation»-eventen. 


**Eksempler:**



### Message digest calculation 


 | Navn 	| **message digest calculation** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen der en sjekksum (checksum) opprettes.	|
| Omfang 	| IE, Fil	|


**Retningslinjer for bruk:**
-	Eventen bør knyttes til IE når det er mulig. Knyttes kun til fil dersom det er behov for å dokumentere avvik.
-	Eventen «fixity check» kontrollerer Sjekksummen.
- Brukes ved opprettelse av nye sjekksummer. Hvis sjekksummer opprettes lokalt, er det ikke behov for å bruke eventen "fixity check" i tillegg til event "message digest calculation". Se også EventType "fixity check". 


**Eksempler:**
```json
    {
        "agent":{
            "agentName": "md5sum (GNU coreutils)",
            "agentType": "software",
            "agentVersion": "8.32",
            "agentNotes": "Beregner MD5-sjekksummer og verifiserer dem mot lagret sjekksumoversikt."
        },
        "event":{
            "eventDateTime": "2026-02-03T13:36:42.455+01:00",
            "eventType": "message digest calculation",
            "eventDetail": "MD5-sjekksummer ble beregnet for alle filer i pakken.",
            "outcome": "success"
        }
    }
```


### Metadata extraction 


 | Navn 	| **metadata extraction** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen med å hente ut metadata fra et objekt. Dette inkluderer tekniske, administrative og beskrivende metadata.	|
| Omfang 	| Fil	|


**Retningslinjer for bruk:**
- Brukes når metadata hentes ut av en fil og resulterer i en eller flere metadatafiler. 
- Filen(e) som utledes må referere til opprinnelsesfila. 


**Eksempler:**
```json
    {
        "agent":{
            "agentName": "ExifTool",
            "agentType": "software",
            "agentVersion": "12.60",
            "agentNotes": "Brukt for å utlede metadata fra bilde- og videofiler."
        },
        "event":{
            "eventDateTime": "2026-02-19T11:45:32.123+01:00",
            "eventType": "metadata extraction",
            "eventDetail": "Utledet tekniske og deskriptive metadata fra bildefil: DSC_0456.JPG.",
            "fileRef": {
                "fileId": "b1c2d3e4f567890123456789abcdef01",
                "relativePath": "representations/rep-images_20230908/data/DSC_0456.JPG"
            },
            "outcome": "success",
            "outcomeDetail": "Bilde: format JPEG, oppløsning 6000x4000 piksler, 24-bit farge; Kamera: Nikon D850; Linse: 24-70mm f/2.8; Eksponering: 1/125 sec at f/8; ISO: 100; Filstørrelse: 18.2 MB."
        }
    }
```
```json
    {
        "agent":{
            "agentName": "Audioinspector",
            "agentType": "software",
            "agentVersion": "5.5",
            "agentNotes": "Programvare for automatisk analyse, kvalitetskontroll, og metadatahåndtering av lydfiler."
        },
        "event":{
            "eventDateTime": "2026-02-11T12:01:08Z",
            "eventType": "metadata extraction",
            "eventDetail": "Wav-filer ble analysert for kvalitetskontroll og dokumentasjon.",
            "fileRef":{
                "relativePath": "representations/primary_20250325/data/something.wav"
            },
            "outcome": "success",
            "outcomeDetail": "Utledet en XML-metadatafil som inneholder detaljert analyse."
        }
    }
```


### Migration


 | Navn 	| **migration** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen der et objekt konverteres fra ett filformat til ett eller flere andre filformater.	|
| Omfang 	| IE, Fil	|


**Retningslinjer for bruk:**
-	Eventen bør knyttes til IE når det er mulig, for eksempel dersom filene er konvertert på samme måte til samme format.
-	Brukes ved endring av filformat, ikke til å dokumentere komprimering som del av lagringsoptimalisering. Se også eventType «compression».
-	Migration-events skal alltid resultere i en ny pakke eller fil. 
- Filen(e) som migreres må referere til opprinnelsesfila. 


**Eksempler:**
```json
    {
        "agent":{
            "agentName": "FFmpeg",
            "agentType": "software",
            "agentVersion": "6.0",
            "agentNotes": "Brukt for mediekonvertering og koding."
        },
        "event":{
            "eventDateTime": "2026-02-03T15:09:55.774+01:00",
            "eventType": "migration",
            "eventDetail": "Konverterte MOV-filer til MXF/Op1a-format med JPEG2000, videokodek og PCM lydkodek.",
            "outcome": "success",
            "outcomeDetail": "command=ffmpeg -i input.mov -c:v jpeg2000 -c:a pcm_s16le output.mxf; container=MXF/Op1a; videoCodec=JPEG2000; audioCodec=PCM; integrityChecked=yes"
        }
    }
```


### Transfer 


 | Navn 	| **transfer** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen med å overføre metadata og/eller digitale objekter mellom systemer. 	|
| Omfang 	| IE	|


**Retningslinjer for bruk:**
-	Brukes ved overføring av objekter inn eller ut av bevaringsområdet eller midlertidige arbeidsområder. Dette inkluderer for eksempel flytting mellom bit-lagre, fra bit-lager til arbeidsområde for bearbeiding, eller fra arbeidsområde til bit-lager.


**Eksempler:**
```json
    {
        "agent":{
            "agentName": "Apache NiFi",
            "agentType": "software",
            "agentVersion": "2.2.0",
            "agentNotes": "Programvare for automatisering av dataflyter som muliggjør utforming og administrasjon av komplekse datapipelines."
        },
        "event":{
            "eventDateTime": "2026-02-18T14:02:33Z",
            "eventType": "transfer",
            "eventDetail": "Overført pakke fra Oracle HSM(SAM-FS) til lokalt arbeidsområde for videre behandling; Opprinnelige sjekksummer verifisert ved opplasting; Opprettet E-ARK SIP.",
            "outcome": "success",
            "outcomeDetail": "Verifiserte sjekksummer med md5sum (GNU coreutils); Opprettet E-ARK SIP med commons-ip2 2.12.0."
        }
    }
```


### Validation 


 | Navn 	| **validation** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen med å sammenligne et objekt med en standard og registrere samsvar eller avvik. 	|
| Omfang 	| IE, Fil	|


**Retningslinjer for bruk:**
-	Objektet som valideres kan være en fil eller en Intellektuell enhet. Eventen bør knyttes til IE når det er mulig. For eksempel hvis filene er validert på samme måte med samme verktøy, eller strukturen er validert for hele pakken. 
-	Det kan være hensiktsmessig å lage én event for hele valideringen der man heller beskriver hvilke verktøy som er brukt i de ulike stegene, i stedet for å lage flere eventer for flere valideringer. 


**Eksempler:**
```json
    {
        "agent":{
            "agentName": "JHOVE",
            "agentType": "software",
            "agentVersion": "1.32.1",
            "agentNotes": "Et fleksibelt rammeverk for programvare som brukes til å identifisere, validere, og karakterisere digitale objekter."
        },
        "event":{
            "eventDateTime": "2026-02-03T17:30:39.662+01:00",
            "eventType": "validation", 
            "eventDetail": "Validerte at lydfiler samsvarer med spesifikasjonene til WAVE-formatet.",
            "outcome": "success"
        }
    }
```
```json
    {
        "agent":{
            "agentName": "Apache NiFi",
            "agentType": "software",
            "agentVersion": "2.4.0",
            "agentNotes": "Programvare for automatisering av dataflyter som muliggjør utforming og administrasjon av komplekse datapipelines."
        },
        "event":{
            "eventDateTime": "2026-02-03T17:30:39.662+01:00",
            "eventType": "validation", 
            "eventDetail": "Validerte E-ARK SIP ved bruk av DPS Validation workflow v.a00f683: nifi-nb-eark-nar,EarkSIPValidator 1.0.7; org.roda-community,commons-ip2 2.12.0.",
            "outcome": "success",
            "outcomeDetail": "Validert mot profilene E-ARK-SIP-v2-2-0, NB-SIP-STRUCTURE-1.0 and NB-SIP-MOVINGIMAGES-PROFILE-1.0."
        }
    }
```


### Virus check 


 | Navn 	| **virus check** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen der en fil skannes for virus eller skadelig programvare. 	|
| Omfang 	| IE, Fil	|


**Retningslinjer for bruk:**
-	Eventen bør knyttes til IE når det er mulig. Knyttes kun til fil dersom det er behov for å dokumentere avvik.


**Eksempler:**
```json
    {
        "agent":{
            "agentName": "ClamAV",
            "agentType": "software",
            "agentVersion": "1.8.7",
            "agentNotes": "Antivirusprogram utviklet for å oppdage skadelig programvare."
        },
        "event":{
            "eventDateTime": "2026-02-03T18:27:53.842+01:00",
            "eventType": "virus check",
            "eventDetail": "Alle filer i pakken ble skannet før overføring.",
            "outcome": "success",
            "outcomeDetail": "Ingen infiserte filer oppdaget."
        }
    }
```
```json
    {
        "agent":{
            "agentName": "ClamAV",
            "agentType": "software",
            "agentVersion":"1.8.7",
            "agentNotes": "Antivirusprogram utviklet for å oppdage skadelig programvare."
        },
        "event":{
            "eventDateTime": "2026-02-03T07:14:01.716+01:00",
            "eventType": "virus check",
            "eventDetail": "Alle filer i pakken ble skannet før overføring.",
            "outcome": "success",
            "outcomeDetail": "Oppdaget signaturen Win.Trojan.MacroVirus-12345 i file_2026.xml."
        }
    }
```



