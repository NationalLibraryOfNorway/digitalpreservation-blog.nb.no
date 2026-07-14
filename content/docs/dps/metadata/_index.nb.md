---
title: Metadataforvaltning
weight: 3
aliases:
  /docs/services/dps/metadata/
---

## Hva er metadata?

Metadata er strukturert informasjon som beskriver digitale objekter. Metadata gjør det mulig å identifisere, finne, forstå og forvalte digitale filer over tid. Uten metadata vil ikke en digital fil ha tilstrekkelig kontekst til å kunne tolkes, forstås eller dokumenteres. For mer informasjon om over hvordan DPS håndterer data, se [Dataforvaltning](/docs/dps/data/). 

Innen digital bevaring har metadata flere sentrale funksjoner: 

- De støtter fire grunnleggende brukeroppgaver: å **finne** innhold som tilsvarer kriteriene dine, **identifisere** riktig objekt, **velge** riktig representasjon og **hente** og tilgjengeliggjøre det digitale objektet. 
- De dokumenterer **hvem som skapte** innholdet, **når** det ble skapt, og hvilke **rettigheter** som gjelder.
- De registrerer objektets **livsløp**: hva som har skjedd med det og når. Dokumenterer hvordan og i hvilken sammenheng objektet ble til, og proveniens, slik at fremtidige brukere kan stole på hva det representerer.
- De beskriver **tekniske egenskaper** som er nødvendige for å holde filer brukbare etter hvert som formater utvikler seg.
- De gir **kontekst**: hvordan innholdet er relatert til andre objekter i (eller utenfor) samlingen 

Metadata berikes over tid. Ny informasjon legges til gjennom hele levetiden til et digitalt objekt. Noen metadata mottas ved innlevering, andre produseres når pakkene behandles i DPS, og andre bygges opp gjennom flere tiår med bevaringsaktiviteter. 

Noen metadata kan oppdateres og suppleres over tid, mens andre beskriver objektet slik det så ut da det ble avlevert, og endres ikke senere. De ulike metadataene har forskjellige formål og opprettes på ulike tidspunkt i bevaringsprosessen. Til sammen gir de en helhetlig beskrivelse av hvert digitalt objekt. 

Metadata er et grunnleggende element i digital bevaring og er nedfelt som ett av prinsippene i Nasjonalbibliotekets [Prinsipper for digital bevaring](/docs/principles/).

## Hvorfor metadata er viktige i DPS

Mange av brukerne av DPS har allerede etablerte katalog- og metadatasystemer med omfattende beskrivelser av innholdet sitt. Metadata leveres likevel også til DPS fordi de har en annen funksjon enn metadataene i de opprinnelige systemene. 

Tilgang til innhold i DPS styres gjennom bevaringsavtaler og konsumentroller. Den som leverer innhold (produsenten) er derfor ikke nødvendigvis den samme som senere skal hente det ut (konsumenten). En konsument kan ha tilgang til innhold fra mange produsenter og bevaringsavtaler, der materialet er beskrevet i ulike katalogsystemer og etter forskjellige katalogiseringsprinsipper. 

Dublin Core-metadataene etablerer et felles metadatagrunnlag i DPS. De gjør det mulig for autoriserte konsumenter å søke på tvers av alt innhold de har tilgang til, uavhengig av hvilket katalogsystem materialet kommer fra eller om de har tilgang til den opprinnelige katalogen. Et fotografi fra et museum og en film fra et kringkastingsarkiv kan dermed gjenfinnes gjennom de samme grunnleggende metadataene, selv om de opprinnelig er beskrevet på ulike måter. 

Metadata har også en viktig funksjon utover søk og gjenfinning. De gjør det mulig å forstå et digitalt objekt også når de opprinnelige katalogene eller systemene ikke lenger finnes. Dette er i tråd med prinsippene i OAIS-modellen, hvor et bevaringsobjekt bør være mest mulig selvstendig. Informasjonen som er nødvendig for å forstå og tolke innholdet følger derfor objektet inn i bevaringsløsningen, i stedet for å være avhengig av eksterne systemer. 

De mer detaljerte metadataene som følger med i SIP-en bevares som en del av bevaringspakken og kan gjøres tilgjengelige ved uthenting. De søkbare Dublin Core-metadataene brukes til å identifisere og finne riktig bevaringspakke.  

For organisasjoner som allerede forvalter metadata i egne katalogsystemer, er levering til DPS normalt en enkel prosess. Dublin Core-feltene er godt definerte, og mapping fra eksisterende metadataformater er i mange tilfeller en engangsoppgave. 

## Hvordan metadata kommer inn i DPS

Metadata brukes til ulike formål gjennom hele bevaringsprosessen. De gjør innholdet søkbart, dokumenterer objektets historie og bevarer informasjon om opphav og sammenheng. I de følgende avsnittene beskrives hvordan de ulike metadataene kommer inn i og forvaltes av DPS. 

Metadata kan komme inn i DPS gjennom tre kanaler: 

### Gjennom API-et

Metadata registreres gjennom API på flere trinn i innleveringsprosessen. 

En vellykket avlevering resulterer i at det opprettes en AIP[^1] (Intellectual Entity) i databasen for bevaringsmetadata. Dersom en avlevering avvises, slettes tilhørende metadata fra databasen. 

- **Administrative metadata** registreres når en avlevering opprettes. En avtale-ID identifiserer hvilken bevaringsavtale informasjonspakken tilhører, mens en objekt-ID identifiserer objektet entydig innenfor denne avtalen. Begge verdiene lagres i databasen for bevaringsmetadata som en del av informasjonspakken.
- **Deskriptive metadata** leveres i form av Dublin Core når informasjonspakken avleveres. Metadataene lagres i databasen for deskriptive metadata og knyttes til den tilhørende informasjonspakken. Dette gjør innholdet søkbart og muliggjør kobling til eksterne systemer gjennom identifikatorer. En slik kobling gjør det mulig å identifisere systemer som inneholder mer detaljert informasjon om innholdet i informasjonspakken. Det er et mål at de deskriptive metadataene på sikt skal kunne oppdateres etter avlevering. Dette vil gjøre det mulig å korrigere, supplere og berike metadataene over tid, uten at selve AIP-en eller det bevarte innholdet endres. Obligatoriske metadata omfatter *Type* fra et kontrollert vokabular (for eksempel `Bok`, `Film` eller `Bilde`), *Tittel* og minst én *Identifikator*. I tillegg kan det registreres valgfrie metadata som: *opphavspersoner, bidragsytere, utgivere, datoer, språk, geografisk dekning, emner, beskrivelser* og *relasjoner*. Flere av disse feltene kan knyttes til autoritetsregistre. Se [Metadatakrav](/docs/dps/api/submission/metadata/) for en fullstendig spesifikasjon.
- **PREMIS-hendelser** (event'er) kan registreres som en valgfri del av avleveringen. PREMIS-hendelser som legges til ved avlevering er for å dokumentere bevaringsrelaterte aktiviteter utenfor DPS. Eksempler på slike hendelser er overføring, opprettelse, digitalisering, validering eller virusskanning. En hendelse kan knyttes til informasjonspakken som helhet eller til en spesifikk fil. Hendelsene lagres i databasen for bevaringsmetadata, med referanse til informasjonspakken og eventuelt til den aktuelle filen. Når en hendelse er registrert, kan den ikke endres eller slettes. Nye hendelser vil legges til av DPS etter hvert som objektet gjennomgår nye bevaringsrelaterte aktiviteter. Se [Bevaringsmetadata](/docs/dps/api/submission/events/) for en nærmere beskrivelse.

### Som metadatafiler i informasjonspakker (SIP)

Metadata kan også avleveres som filer direkte i informasjonspakken (SIP). Se våre [krav til pakkestruktur](/docs/dps/sip/structure-requirements/).

- **METS.xml-filer** er obligatoriske både i pakkens rotmappe og i hver representasjonsmappe. DPS analyserer METS.xml-filene ved avlevering og henter ut informasjon som brukes til å berike informasjonspakken med metadata om innhold, struktur og filer. Se [krav til METS.xml](/docs/dps/sip/mets/) for full spesifikasjon.
- **Metadatafiler** som MARC, MODS, Dublin Core XML eller domenespesifikke metadata, legges ved i informasjonspakken. DPS bevarer disse filene, identifiserer filformatet og registrerer tekniske metadata, men tolker eller indekserer ikke innholdet. Se [innføring i metadata](/docs/dps/sip/metadata/) for veiledning om plassering i informasjonspakker.

### Generert av DPS

Når en informasjonspakke mottas, beskriver DPS innholdet i henhold til objekt-elementet i PREMIS-modellen. Informasjon om Intellectual Entity, representasjoner og filer bygges opp fra metadataene som leveres (METS.xml, administrative metadata og Dublin Core), sammen med informasjon DPS selv registrerer ved mottak. Den interne PREMIS-modelleringen knytter sammen og samler denne informasjonen i databasen for bevaringsmetadata.  

Metadata som genereres ved mottak i DPS:

- **PREMIS-hendelser**: DPS oppretter en hendelse for hver operasjon som utføres: overføring, validering, verifisering, formatidentifikasjon og metadataekstraksjon. På samme måte dokumenteres bevaringsaktiviteter og utlevering av filer også etter mottaksfasen er over. Hver hendelse lagres i databasen for bevaringsmetadata med tidsstempel, resultat og agent.
- **Resultater fra formatidentifikasjon** lagres i databasen for bevaringsmetadata og identifisert format dokumenteres på filnivå.
- **Ekstraherte tekniske metadata** ekstraheres for hver fil ved bruk av analyseverktøyer (MediaInfo og ExifTool). Resultatene lagres som separate filer i en objektlagringsløsning (S3) og refererer til tilhørende filer. Metadataene beskriver filenes tekniske egenskaper, som oppløsning, bitrate og fargerom. Bruk av objektlagring legger til rette for effektiv uthenting og mulig videre bruk i analyseverktøy.

## Hvordan metadata lagres

I DPS håndteres de ulike metadataene i en egen metadatatjeneste som består av flere komponenter. Metadataene beskyttes og lagres etter de samme prinsippene som de bevarte dataene, og følger 3-2-1-prinsippet for sikker og langsiktig lagring, se [Prinsipper for digital bevaring](/docs/principles/). 

{{< figure src="metadata-service.svg" alt="Diagram som viser databasene i metadatatjenesten og relasjonene mellom dem. Databasen for bevaringsmetadata (PREMIS) inneholder intellectual entities, representasjoner, filer, hendelser, agenter og en planlagt rettighetsentitet. Databasen for deskriptive metadata inneholder Dublin Core-dokumenter. Lokasjonsdatabasen sporer depotfiler. Tekniske metadata lagres i S3-objektlagring." >}}

### Database for bevaringsmetadata

Databasen for bevaringsmetadata (MongoDB) er basert på PREMIS-datamodellen (lenke). Den inneholder metadata som dokumenterer det bevarte innholdet og bevaringsprosessen. 

Databasen lagrer blant annet informasjon om: 

- **Informasjonspakker (*Intellectual Entity*)**: Hver informasjonspakke registreres som en egen enhet med informasjon om blant annet hvilken bevaringsavtale den tilhører.
- **Representasjoner**: En informasjonspakke (*Intellectual Entity*) kan bestå av én eller flere representasjoner, for eksempel ulike versjoner eller presentasjonsformer av det samme innholdet.
- **Filer**: Alle filer som inngår i informasjonspakken (*Intellectual Entity*). For hver fil lagres blant annet resultatet av formatidentifikasjonen som utføres ved avlevering. 
- **Hendelser**: Hendelser som dokumenterer hva som har skjedd med informasjonspakken (*Intellectual Entity*) eller filene, for eksempel ved avlevering, validering eller annen behandling. Hendelsene kan være registrert av avleverer eller opprettet automatisk av DPS. 
- **Agenter**: Personer, organisasjoner eller systemer som har utført hendelsene.

### Database for deskriptive metadata

En database (MongoDB) som lagrer de deskriptive metadataene som avleveres gjennom API-et. Hver informasjonspakke (*Intellectual Entity*) er knyttet til ett sett med deskriptive metadata, basert på Dublin Core. Metadataene lagres separat fra bevaringsmetadataene, men er koblet til den samme informasjonspakken.

### Lokasjonsdatabase

En database (MongoDB) som holder oversikt over hvor filene er fysisk lagret i bevaringslageret. Ved avlevering kan DPS omorganisere filene for å tilpasse dem til lagringsløsningen. Lokasjonsdatabasen sørger for at hver fil fortsatt kan knyttes til riktig informasjonspakke og gjenfinnes. 

### Objektlagring for ekstraherte metadata

Metadata som DPS automatisk ekstraherer fra filer ved hjelp av analyseverktøy (MediaInfo og ExifTool), lagres i en egen objektlagring (S3). De ekstraherte metadataene er koblet til de tilhørende filene i metadatatjenesten. 

## Hvordan metadata kan benyttes

Tilgang til metadata skjer i dag gjennom det offentlige API-et. Følgende metadata er tilgjengelige:

### Dublin Core-metadata

API-et gir tilgang til de deskriptive Dublin Core-metadataene for hver avlevert informasjonspakke. Metadataene kan returneres sammen med informasjonspakken ved uthenting.  

### PREMIS-hendelser

PREMIS-hendelser kan hentes via API-et for hver avlevert informasjonspakke. Dette omfatter både hendelser som er registrert av avleverer, og hendelser som er opprettet av DPS.

### Filmetadata

Filmetadata kan hentes via API-et for hver fil. Dette omfatter blant annet filstier og sjekksummer.

### Oversikt over bevarte informasjonspakker

API-et kan brukes til å hente en oversikt over informasjonspakkene som er avlevert under en bestemt bevaringsavtale.  

### Utlevering

Det er mulig å bestille utlevering av bevarte informasjonspakker via API-et og følge statusen på utleveringsjobben. Selve nedlastningen av innholdet skjer utenfor API-et. Metadatafiler som inngår i bevaringspakken, følger med ved utlevering.  



[^1] Archival Information Package: En OAIS-informasjonspakke som består av innholdsinformasjonen (Content Information) og den tilhørende bevaringsbeskrivende informasjonen (Preservation Description Information, PDI).