---
title: Digital Preservation Services (DPS)
weight: 4
aliases:
  - /docs/services/dps/
  - /docs/services/
---

DPS (Digital Preservation Services) refererer til Nasjonalbibliotekets tjenester for bevaring av digitalt kulturarvmateriale. Med digitalt kulturarvmateriale menes både digitalisert og «digitalt født» materiale. Det omfatter både materiale som er underlagt pliktavleveringsloven, digitalt innhold som anses å være en del av nasjonal kulturarv, og materiale som på andre måter anses å være digitalt bevaringsverdig. DPS er basert på OAIS-modellen.

{{% details title="OAIS-terminologi" closed="true" %}}

OAIS (Open Archival Information System) er en referansemodell for arkivering av digital informasjon. Nasjonalbiblioteket bruker OAIS som et referansepunkt i digital bevaring, selv om kompleksiteten og utviklingen av arkitekturen vår gjør at OAIS-modellen ikke uten videre kan legges over organisasjonen vår.

{{< figure src="OAIS_Functional_Model_(en).svg" alt="OAIS-modellen" caption="" attr="Mathieualexhache (original work); Mess (SVG conversion & English translation), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0), via Wikimedia Commons" >}}

Sentrale OAIS-begreper er de forskjellige informasjonspakkene:

- **SIP** (Submission Information Package): leveres for bevaring. Inneholder innholdsdata, dokumentasjon og metadata som trengs for langsiktig bevaring og tilgang.
- **AIP** (Archival Information Package): slik den er lagret i bit-depotet. Kan være identisk med SIP-en eller inneholde ytterligere bevaringsinformasjon.
- **DIP** (Dissemination Information Package): utleveres fra bevaring. Kan bestå av hele eller deler av en AIP.

Med mindre noe annet er spesifisert, refererer vi til SIP-er når vi snakker om informasjonspakker i disse dokumentene.

{{% /details %}}

## Hvem kan bruke DPS

DPS er offentlig tilgjengelig, men tilgang krever en avtale med Nasjonalbiblioteket. For detaljer, se [Dataforvaltning](/docs/dps/data/).

## Hva DPS gjør

DPS bruker et offentlig API både for innlevering og utlevering av informasjon. Systemet tar imot informasjonspakker (SIP-er), validerer dem og lagrer data og metadata på en sikker måte. Systemet tilbyr utlevering gjennom det samme API-et. All tilgang og bruk styres av rollebasert tilgangskontroll knyttet til bevaringsavtaler. 

DPS består av flere tjenester: 

- **API-tjenesten**: Grensesnittet som brukes for både innlevering og utlevering, inkludert filoverføringer. All kommunikasjon med DPS skjer gjennom API-tjenesten.
- **Mottak**: En kjede av tjenester (overføring, validering, karakterisering, pakking, arkivering og varsling) som behandler pakker før de bevares i bit-lageret.
- **Utlevering**: En kjede av tjenester som behandler pakker for uthenting før de leveres via API-et.

**Metadatatjenesten** og **bit-lageret** utgjør kjernen i DPS. Det er her det digitale innholdet bevares og sikres. 

- **Metadatatjenesten**: Databaser og objektlagring som holder oversikt over det bevarte innholdet og tilhørende metadata. De fleste tjenestene i DPS lagrer metadata i eller henter metadata fra metadatatjenesten.
- **Bit-lager**: Ulike tekniske løsninger som sørger for sikker og langsiktig lagring av det digitale innholdet.
- **API-tjeneste**: All kommunikasjon med DPS skjer gjennom API-tjenesten.


{{< figure src="dpskonsept.drawio.svg" alt="DPS konseptuell arkitektur" caption="Konseptuell oversikt over DPS. Hele linjer representerer innlevering, stiplede linjer representerer utlevering. Dataflyt er vist i svart, metadataflyt i rødt." >}}

## DPS sin rolle i NB

DPS er ett av tre systemdomener som deler ansvaret for digitale objekter i Nasjonalbiblioteket. Disse domenene forvalter forskjellige aspekter ved objektene. Domenene opererer selvstendig, men påvirker hverandre.

## De tre systemdomenene:

### Metadatasystemer

Biblioteksystemer, kataloger, registre og forvaltningssystemer (som Alma, Mavis og Hanske). De er hovedkilden for deskriptive metadata og utsteder unike identifikatorer (UID-er, typisk URN-er) for digitale objekter. Disse systemene forvalter et bredt spekter av ressurser.  

Det er her intellektuelle entiteter[^1] defineres: valget av hva som utgjør en bevaringsverdig informasjonspakke starter her, ikke i DPS. Én URN tilsvarer typisk én pakke. For detaljer om pakkeomfang, se [Pakke-, representasjons- og dataomfang](/docs/dps/sip/scope/).  

### Digital Preservation Services (DPS)

Bevaringssystemet. Forvalter bevaringsdata med en PREMIS-basert datamodell[^2] (intellektuelle entiteter, representasjoner, filer, eventer, agenter). DPS tilbyr langtidslagring med asynkron tilgang. DPS er hovedkilden for tekniske metadata på filnivå i Nasjonalbiblioteket. DPS er ikke hovedkilden for deskriptive metadata: systemet holder metadataene det trenger for å operere selvstendig, uten å gjenskape metadatasystemenes fulle katalogstrukturer.  

DPS fungerer som en selvstendig tjeneste: identifikatorer og metadata leveres gjennom API-et, og DPS håndterer bevaringen. For detaljer om hvordan data og metadata håndteres i DPS, se [Dataforvaltning](/docs/dps/data/) og [Metadataforvaltning](/docs/dps/metadata/).

### Offentlige tilgangstjenester

Nasjonalbibliotekets nettbaserte tjenester. Forvalter en delmengde deskriptive metadata og tilbyr umiddelbar tilgang til visningskopier utledet fra bevaringsfiler.  

De offentlige tilgangstjenestene tilpasser de høstede metadataene til en flatere struktur, med én enkelt representasjon per intellektuell entitet. De intellektuelle entitetene som finnes på nett, speiler derfor ikke nødvendigvis entitetene i metadatasystemene.  

En UID, forvaltet av metadatasystemene, binder de tre domenene sammen. Den må være unik på tvers av systemene og bør ikke gjenbrukes.  

## Data- og metadataflyt

Diagrammet under er en forenklet fremstilling av hvordan data og metadata beveger seg mellom systemdomenene i Nasjonalbiblioteket: 

{{< figure src="context.svg" alt="architecture diagram" caption="Data- og metadataflyt mellom systemer i NB" >}}

SIP-en inneholder bevaringsdata og en kopi av deskriptive metadata fra metadatasystemene. DPS bevarer ikke tilgangskopier som kan utledes automatisk fra bevaringsfiler; slike kopier forvaltes av de offentlige tilgangstjenestene.

## Forstå DPS

Disse sidene forklarer konsepter, ansvarsområder og hvordan DPS fungerer:

{{< cards >}}
  {{< card link="context" title="DPS sin rolle i NB" subtitle="Systemkonteksten DPS ble bygget i og hvordan den former tjenesten" icon="view-grid" >}}
  {{< card link="data" title="Datahåndtering" subtitle="Hvordan data bevares, lagres og uthentes i DPS" icon="database" >}}
  {{< card link="metadata" title="Metadatahåndtering" subtitle="Hvordan metadata kommer inn, lagres og brukes i DPS" icon="tag" >}}
  {{< card link="access-control" title="Tilgangskontroll" subtitle="Hvordan roller, bevaringsavtaler og tillatelser styrer tilgang" icon="shield-check" >}}
{{< /cards >}}

## Bruke DPS

Disse sidene er spesifikasjoner og API-referanser for produsenter og konsumenter:

{{< cards >}}
  {{< card link="api" title="Submission Service API" subtitle="Endepunkter for innlevering, utlevering og webhooks" icon="code" >}} 
  {{< card link="sip" title="SIP-spesifikasjoner" subtitle="E-ARK pakkestruktur, METS.xml-krav og eksempler" icon="archive" >}}
{{< /cards >}}

[^1]: [Intellektuelle entiteter og innhold](https://digitalpreservation.no/nb/docs/dps/sip/scope/#intellektuelle-entiteter-og-innhold)
[^2]: *PREMIS Data Dictionary (full document)*, Version 3.0, Nov. 2015, [https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf](https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf)
