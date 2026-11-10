---
title: Legge til bevaringseventer i en innlevering
linkTitle: Legge til bevaringseventer
weight: 3
---

Denne veiledningen viser hvordan du velger hvilke eventer du skal dokumentere for din arbeidsflyt, og hvordan du leverer dem via API-et som en del av en innlevering. Hva eventer er og hvorfor de er viktige, er beskrevet under [Bevaringseventer](/nb/docs/dps/understanding/metadata-management/preservation-events/). Betydning og tillatte verdier for hvert element finnes i [referansen for bevaringseventer](/nb/docs/dps/reference/preservation-events/).

## Før du starter

- Du trenger en innlevering (submission) med status `REGISTERED`. Se [Levere materiale til bevaring](/nb/docs/dps/how-to/submit-content/).
- Eventer kan bare leveres før innleveringen er fullført. Lever alle eventer først, og fullfør deretter.

## Eventtyper du kan levere

API-et godtar følgende verdier for `eventType`. Forespørsler med andre verdier blir avvist. [Referansen for bevaringseventer](/nb/docs/dps/reference/preservation-events/) beskriver hver type med retningslinjer og eksempler. Den omfatter også eventtyper som DPS registrerer selv, og som ikke kan leveres. [Swagger-dokumentasjonen](/swagger/) er den autoritative kilden for hvilke verdier API-et godtar.

- [`capture`](/nb/docs/dps/reference/preservation-events/#capture)
- [`creation`](/nb/docs/dps/reference/preservation-events/#creation)
- [`filename change`](/nb/docs/dps/reference/preservation-events/#filename-change)
- [`fixity check`](/nb/docs/dps/reference/preservation-events/#fixity-check)
- [`imaging`](/nb/docs/dps/reference/preservation-events/#imaging)
- [`information package creation`](/nb/docs/dps/reference/preservation-events/#information-package-creation)
- [`message digest calculation`](/nb/docs/dps/reference/preservation-events/#message-digest-calculation)
- [`metadata extraction`](/nb/docs/dps/reference/preservation-events/#metadata-extraction)
- [`migration`](/nb/docs/dps/reference/preservation-events/#migration)
- [`transfer`](/nb/docs/dps/reference/preservation-events/#transfer)
- [`validation`](/nb/docs/dps/reference/preservation-events/#validation)
- [`virus check`](/nb/docs/dps/reference/preservation-events/#virus-check)

## Velg hvilke eventer du skal dokumentere

Denne veiledningen er basert på Nasjonalbibliotekets interne arbeidsflyter og er ikke nødvendigvis dekkende for alle typer bevaringsprosesser. Innspill til forbedringer, presiseringer og ytterligere brukstilfeller mottas gjerne.


### Digitalisering av fysiske kilder 

**Minimum:** 

- **Creation eller Imaging (Bruk én av disse):** Når filen(e) faktisk opprettes.<br>
**Creation** brukes når digitale filer opprettes gjennom digitalisering eller produksjon, for 	eksempel ved skanning, digitalisering av lyd eller overføring av video fra analog kilde.<br>
**Imaging** brukes når det opprettes et komplett diskbilde (bit-for-bit kopi) av et fysisk 	lagringsmedium, som harddisk, diskett, CD eller minnekort. Imaging omfatter hele 		mediet, inkludert filsystemstruktur, metadata, ledig plass og eventuelt slettede data.

- **Message digest calculation:** Opprettelse av sjekksummer. Det anses ikke som nødvendig å dokumentere verifisering av sjekksummene rett etter at de er opprettet. Gjerne verifiser dem før de sendes videre, men ikke lag en event på det. 
  
- **Information package creation:** Opprettelsen av en SIP. Dokumenterer gjeldende pakkestandard (E-ARK).
  

**Kan være relevant:**

- **Validation:** Validering av kvalitet og/eller format mot en standard.
- **Metadata extraction:** Hente ut tekniske, administrative og/eller deskriptive metadata fra fil. Uttrekk må beskrives i "OutcomeDetail" eller resultere i ny fil som legges i bevaringspakken.


### Digitalt født materiale

**Minimum:**

- **Transfer:** Fra avleverer til intern produksjonsløype/internt område. 
- **Message digest calculation eller fixity check:** Hvis filer avleveres med sjekksum, må disse verifiseres. Hvis filene mangler sjekksum, må det opprettes. 
- **Information package creation:** Opprettelsen av en SIP. Dokumenter gjeldende pakkestandard (E-ARK).


**Kan være relevant:**

- **Virus check:** Lag én event for alle filer (hele pakken), eventuelle avvik dokumenteres på filnivå. 
- **Validation:** Validering av kvalitet og/eller format mot en standard.
- **Metadata extraction:** Hente ut tekniske, administrative og/eller deskriptive metadata fra fil. Uttrekk må beskrives i "OutcomeDetail" eller resultere i ny fil som legges i bevaringspakken.
- **Filename change:** Hvis filnavn endres etter mottak av filene.
- **Migration:** Hvis filformat endres. 


### Overføring av materiale fra tidligere lagringssystem til DPS

**Minimum:**

- **Transfer:** Fra tidligere lagringssystem. 
- **Fixity check eller message digest calculation:** Kontroll av eksisterende sjekksummer. Hvis materialet mangler sjekksummer, må det opprettes. 
- **Information package creation:** Opprettelsen av en SIP. Dokumenter gjeldende pakkestandard (E-ARK). Denne er relevant kun når bevaringspakkene endres.
  
Merk at det kan være én event med event-type «transfer» som inkluderer sjekksumverifisering: transfer fra X til Y, med sjekksumverifisering på veien. 


**Kan være relevant:**

- **Creation:** Hvis opprettelse av filene ikke er dokumentert tidligere, og man har denne informasjonen tilgjengelig. 
- **Filename change:** Hvis filnavn endres etter at det er flyttet fra tidligere lagringssystem. 
- **Migration:** Hvis filformat endres. 


### Netthøsting (web-arkiv)

**Minimum:**

- **Capture:** Selve innhøstingen/crawl. 
- **Creation:** Hvis det lages for eksempel nye WARC-filer.
- **Message digest calculation:** Opprettelse av sjekksummer. Det anses ikke som nødvendig å dokumentere verifisering av sjekksummene rett etter at de er opprettet. Gjerne verifiser dem før de sendes videre, men ikke lag en event. 
- **Information package creation:** Opprettelsen av en SIP. Dokumenter gjeldende pakkestandard (E-ARK). 


**Kan være relevant:**
- **Validation:** Validering av kvalitet og/eller format mot en standard.
- **Virus check:** Lag én event for alle filer (hele pakken), eventuelle avvik dokumenteres på filnivå. 
- **Metadata extraction:** Hente ut tekniske, administrative og/eller deskriptive metadata fra fil. Uttrekk må beskrives i "OutcomeDetail" eller resultere i ny fil som legges i bevaringspakken.

## Kobling av eventer til objekt

Eventer sendes inn via API:

`POST /v1/contracts/{contractId}/submissions/{submissionId}/events`

Et event knyttes alltid til en submission, som representerer en Intellektuell entitet (IE).

Eventer kan bare sendes inn mens submissionen har status `REGISTERED`, altså før submissionen er fullført. En vellykket forespørsel gir `204 No Content`. Feltet `isUserInitiated` settes automatisk til `true` for eventer som sendes inn via API-et, og trenger ikke å være med.

Innsendte eventer kan hentes med `GET /v1/contracts/{contractId}/submissions/{submissionId}/events`.

### Nivå og referanse til fil

Eventer knyttes alltid til en submission (IE). De kan enten gjelde hele informasjonspakken (IE-nivå) eller en spesifikk fil (filnivå).

Dette styres av `fileRef`:

- Uten `fileRef` → eventet gjelder hele informasjonspakken (IE)
- Med `fileRef` → eventet gjelder en spesifikk fil

`fileRef` identifiserer filen ved hjelp av `relativePath`:

- Referansen baseres på filens relative sti i informasjonspakken
- `fileId` genereres internt i DPS og skal ikke oppgis i API-kallet
- Det kan kun angis én `fileRef` per event

**Eksempel (filnivå):**

```json
{
  "fileRef": {
    "relativePath": "representations/rep-images/data/DSC_0456.JPG"
  }
}
```

I dette eksemplet gjelder eventet filen `DSC_0456.JPG` i representasjonen `rep-images`.

## Struktur på JSON-payload

Et event sendes inn som ett JSON-objekt. Feltene som beskriver selve handlingen og resultatet ligger på toppnivå. Aktøren som utførte handlingen, beskrives i objektet `agent`.

`fileRef` er valgfritt og brukes bare når eventet gjelder en spesifikk fil. Hvis `fileRef` ikke er angitt, gjelder eventet hele informasjonspakken (IE-nivå).

**Forenklet struktur:**

```json
{
  "agent": {
    "agentName": "...",
    "agentType": "...",
    "agentVersion": "...",
    "agentNote": "..."
  },
  "eventDateTime": "...",
  "eventType": "...",
  "eventDetail": "...",
  "fileRef": {
    "relativePath": "..."
  },
  "outcome": "...",
  "outcomeDetail": "..."
}
```


Eventer kan registreres både på pakkenivå og filnivå. Som hovedregel bør eventer knyttes til pakkenivå, Intellektuell entitet (IE), der det er mulig. Dette for
å unngå store mengder eventer som i utgangspunktet sier det samme. Det er åpent for å legge eventer på filer der det er behov for å dokumentere hendelser på
enkeltfiler. Det viktigste er at man har et bevisst forhold til hva som dokumenteres, hvorfor det dokumenteres, og på hvilket nivå.

Det anbefales at eventene skrives på norsk der det er mulig. Eventene bør utformes med hensyn til framtidig forvaltning og bruk, slik at informasjonen er mest
mulig forståelig og etterprøvbar over tid.

Teknisk dokumentasjon for avlevering i API og formatering av eventer finnes her: [Swagger DPS Submission Service API](https://digitalpreservation.no/swagger/)

Den maskinlesbare OpenAPI-spesifikasjonen (JSON) er tilgjengelig på <https://api.nb.no/dps-submission/v1/api-docs>. Eventer er beskrevet i skjemaet `SubmitEventDto`.
