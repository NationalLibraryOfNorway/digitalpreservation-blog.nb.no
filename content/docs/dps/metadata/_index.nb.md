---
title: Metadataforvaltning
weight: 3
aliases:
  /docs/services/dps/metadata/
---

## Hva er metadata?

Metadata er strukturert informasjon om digitale objekter. Uten metadata er en digital fil bare en ugjennomsiktig sekvens av biter: du kan ikke finne den, du kan ikke forstå hva den representerer, og du kan ikke bevise at den er det den utgir seg for å være. Metadata finnes for å muliggjøre bevaring av data; for mer informasjon om over hvordan DPS håndterer data, se [Dataforvaltning](/docs/dps/data/).

Innen digital bevaring har metadata flere sentrale funksjoner:

- De støtter fire grunnleggende brukeroppgaver: å **finne** innhold som matcher kriteriene dine, **identifisere** riktig objekt blant lignende treff, **velge** riktig representasjon og **hente** det faktiske innholdet gjennom tilgjengeliggjøring
- De dokumenterer **hvem som skapte** innholdet, **når** det ble skapt, og hvilke **rettigheter** som gjelder
- De registrerer objektets **livsløp**: hva som har skjedd med det og når, og dokumenterer opprinnelse, skapelseskontekst og proveniens slik at fremtidige brukere kan stole på hva det representerer
- De fanger opp **tekniske egenskaper** som er nødvendige for å holde filer brukbare etter hvert som formater utvikler seg
- De gir **kontekst**: hvordan innholdet er relatert til andre objekter i (eller utenfor) samlingen

Rike metadata opprettes ikke på én gang. De akkumuleres gjennom levetiden til et digitalt objekt: noen metadata leveres av klienter ved innlevering, andre produseres under inmmating av pakker til DPS, og andre bygges opp gjennom flere tiår med bevaringsaktiviteter. 

Noen metadatalag er utformet for å kunne berikes over tid, mens andre er bevisste øyeblikksbilder som fryses ved innleveringstidspunktet. Hvert lag har et eget formål og opprettes på ulike stadier. Sammen danner disse lagene et helhetlig bilde av hvert digitalt objekt vi forvalter.

Metadata er så sentral for digital bevaring at de er nedfelt som et av prinsippene i Nasjonalbibliotekets [Prinsipper for digital bevaring](/docs/principles/).

## Hvorfor metadata er viktige i DPS

Mange av våre brukere har allerede omfattende katalog- og metadatasystemer. Et naturlig spørsmål er derfor: Hvis innholdet allerede er godt beskrevet i deres egne systemer, hvorfor må de levere metadata på nytt til DPS?

Svaret ligger i hvordan tilgang til bevart innhold fungerer. Tilgang til DPS styres av [bevaringsavtaler ("submission agreements") og konsumentroller](/docs/dps/access-control/) . En klient som leverer innhold (produsent) er ikke nødvendigvis den samme klienten som henter det ut igjen (konsument). For eksempel:

- Et regionalt arkiv deponerer digitaliserte fotografier
- Et universitetsbibliotek får konsumenttilgang til disse fotografiene for forskningsformål
- Forskeren kan søke etter fotografiene i DPS, selv om forskeren ikke har tilgang til det regionale arkivets interne katalog

Mer generelt kan én konsument ha tilgang til innhold som er fordelt på mange ulike innleveringsavtaler, levert av mange forskjellige innsendere. Det samme digitale innholdet kan til og med være beskrevet i flere ulike katalogsystemer på tvers av organisasjoner. Dublin Core-metadatamodellen gir en felles måte å søke på tvers av alt dette innholdet i DPS, uavhengig av hvilket katalogsystem det kommer fra, hvordan det er katalogisert, eller om det i det hele tatt er katalogisert i et annet system. 

Et fotografi kan være beskrevet på én måte i et museums samlingssystem, mens en film beskrives annerledes i et kringkastingsarkiv. Gjennom Dublin Core beskrives begge med det samme settet av attributter som et minimum: type, tittel, opphavsperson og dato. Dette gjør søk på tvers av samlinger mulig for enhver autorisert konsument.

I dette scenariet er DPS det eneste oppdagelseslaget som er tilgjengelig for konsumenten. Dublin Core-metadataene som sendes inn gjennom API-et er det som gjør innholdet søkbart. Sammen utgjør de et felles, selvstendig oppslagsgrensesnitt som fungerer for alle autoriserte konsumenter, uavhengig av om de har tilgang til den opprinnelige katalogen.

De rike metadataene du pakker inn i SIP-ene blir fortsatt bevart og gjort tilgjengelige gjennom tilgjengeliggjøring av dataene, men en konsument må først kunne finne riktig pakke for å få tilgang til dem. Det er dette de søkbare metadataene muliggjør.

Hvis du allerede forvalter slike metadata i egne katalogsystemer, er det som regel enkelt å levere dem gjennom Submission API-et. Dublin Core-feltene er godt definerte, og i mange tilfeller er mapping fra eksisterende metadataformater en engangsjobb.

Til syvende og sist muliggjør metadataene du leverer til DPS en høyere grad av selvbetjening for brukere av DPS. Autoriserte konsumenter kan finne og hente innholdet de leter etter på egenhånd, uten å måtte gå gjennom mellomledd, enten det er den opprinnelige innsenderen, et katalogteam eller en samlingsforvalter. De søkbare og uthentbare metadatalagene gjør DPS til en selvstendig plattform for gjenfinning og tilgang.

DPS er først og fremst et system for å sikre *data* (se [Dataforvaltning](/docs/dps/data/)). Metadata er det som gjør disse dataene søkbare, troverdige og brukbare over tid.

## Hvordan metadata kommer inn i DPS

Hver type metadata har et spesifikt formål i bevaringssyklusen, fra å gjøre innhold søkbart, til å bygge revisjonsspor, samt bevare konteksten rundt en innlevering. De følgende avsnittene beskriver hvordan forskjellige metadata kommer inn i DPS og hvor de ender opp i metadatatjenesten ("metadata service").

Metadata kan komme inn i DPS gjennom tre kanaler:

### Gjennom Submission API-et

Metadata kommer inn gjennom Submission API-et på flere tidspunkt i innleveringsprosessen.

Den typiske sekvensen er: opprett en avlevering ("submission") → registrer filene som utgjør SIP-en → send inn eventuelle PREMIS-hendelser → fullfør avlevering for å starte innmating.

En vellykket avlevering fører til at det opprettes en "Intellectual Entity" (AIP) opprettes i databasen for bevaringsmetadata. En avvist avlevering slettes fra databasen.

- **Administrative metadata** leveres når du oppretter en avlevering. En kontrakt-ID identifiserer hvilken bevaringsavtale som gjelder for den avleverte informasjonspakken (se [rollebasert tilgangskontroll](/docs/dps/access-control/)), og en objekt-ID identifiserer objektet unikt innenfor bevaringsavtalen. Begge lagres i databasen for bevaringsmetadata og beriker Intellectual Entity-dokumentet.
- **Dublin Core-metadata** leveres også når en informasjonspakke avleveres. De lagres i databasen for deskriptive metadata, koblet til Intellectual Entity, og gjør innholdet søkbart. Dublin Core gjør det også mulig å knytte en pakke til en post i et eksternt fagsystem, slik at alle som henter ut pakken ut vet hvilke systemer som inneholder mer detaljert informasjon om dens innhold. Obligatoriske felter inkluderer en type fra et kontrollert vokabular (for eksempel `Bok`, `Film`, `Bilde`), en tittel og minst én identifikator. Valgfrie felter gjør det mulig å registrere opphavspersoner, bidragsytere, utgivere, datoer, språk, geografisk dekning, emner, beskrivelser og relasjoner, mange med støtte for autoritetsregistre. Se [Metadatakrav](/docs/dps/api/submission/metadata/) for full spesifikasjon.
- **PREMIS-hendelser** kan valgfritt sendes inn i løpet av avleveringen. Hver hendelse dokumenterer en bevaringsaktivitet som har skjedd utenfor DPS, for eksempel overføring, opprettelse, digitalisering, validering eller virusskanning, og kan valgfritt referere til en spesifikk fil i den avleverte informasjonspakka. De lagres i databasen for bevaringsmetadata som event-dokumenter, koblet til IE og eventuelt en fil. Se [eventer/bevaringsmetadata](/docs/dps/api/submission/events/) for mer detaljer.

### Som metadatafiler i informasjonspakker (SIP)

Metadata kan også avleveres som filer direkte i SIP-strukturen, der de følger innholdsfilene. Se [krav til SIP-struktur](/docs/dps/sip/structure-requirements/) for fullstendige krav pakkestruktur.

- **METS.xml-filer** er obligatoriske både i pakkas rotmappe og i hver representasjonsmappe. I motsetning til de andre metadatafilene i SIP-en blir METS.xml analysert av DPS ved avlevering. DPS henter metadata fra METS-headeren for å berike Intellectual Entity-dokumentet, og henter filer og sjekksummer fra filseksjonen for å opprette Representation- og File-dokumenter i databasen for bevaringsmetadata. Se [krav til METS.xml](/docs/dps/sip/mets/) for full spesifikasjon.
- **Rike metadatafiler**, som MARC, MODS, Dublin Core XML eller domenespesifikke metadata, kan også legges inn i SIP-strukturen som filer sammen med innholdsfilene, både på pakke- og representasjonsnivå. DPS behandler disse filene som enhver annen datafil: de modelleres som File-dokumenter i databasen for bevaringsmetadata og gjennomgår formatidentifikasjon og tekniske metadata ekstraheres fra dem. Innholdet i disse filene derimot **hverken tolkes eller indekseres av DPS**. Se [innføring i metadata](/docs/dps/sip/metadata/) for veiledning om plassering i informasjonspakker.

### Generert av DPS

Når en informasjonspakke mottas, beskriver DPS pakkas innhold PREMIS-objektmodellen i databasen for bevaringsmetadata. Intellectual Entity-, representasjon- og fil-dokumenter fylles med dataene du leverer (METS.xml, administrative metadata og Dublin Core) kombinert med det DPS dokumenterer i innmatingsprosessen. Denne interne modellen binder alt sammen. Den er ikke noe du forholder deg direkte med. Det nærmeste man kommer er å levere PREMIS-hendelser i riktig format gjennom API-et.

Flere typer metadata genereres også automatisk under innmating:

- **PREMIS-hendelser**: DPS oppretter en hendelse for hver operasjon som utføres under innmating: overføring, validering, innmating, formatidentifikasjon og metadataekstraksjon. På samme måte dokumenteres bevaringsaktiviteter og tilgjengeliggjøring av filer også etter innmatings-fasen er over. Hver hendelse lagres i databasen for bevaringsmetadata som et event-dokument, koblet til IE og eventuelt en fil, med tidsstempel, resultat og agent.
- **Resultater fra formatidentifikasjon** lagres i databasen for bevaringsmetadata og beriker File-dokumentene med identifisert format.
- **Ekstraherte tekniske metadata** produseres for hver fil ved hjelp av MediaInfo og ExifTool. Resultatene lagres som filer i S3-objektlagringen og refereres fra File-dokumentene. De fanger opp filenes tekniske egenskaper, som oppløsning, bitrate, fargerom og mer. De lagres i objektlagring for enklere uthenting og mulig bruk i analyseverktøy.

## Hvordan metadata lagres

Metadata i DPS håndteres av metadatatjenesten, som består av flere komponenter. På samme måte som data i DPS beskyttes metadata av den samme 3-2-1-lagringspolicyen (se [Prinsipper for digital bevaring](/docs/principles/)). 

{{< figure src="metadata-service.svg" alt="Diagram som viser databasene i metadatatjenesten og relasjonene mellom dem. Databasen for bevaringsmetadata (PREMIS) inneholder intellectual entities, representasjoner, filer, hendelser, agenter og en planlagt rettighetsentitet. Databasen for deskriptive metadata inneholder Dublin Core-dokumenter. Lokasjonsdatabasen sporer depotfiler. Tekniske metadata lagres i S3-objektlagring." >}}

### Database for bevaringsmetadata

En MongoDB-database basert på PREMIS-datamodellen. Den inneholder følgende dokumenttyper:

- **Intellectual Entities (IE-er)**: Hver informasjonspakke (AIP) beskrives som ett IE-dokument som representerer rotnivået i pakken. Hver IE har en identifikator for bevaringsavtalen som gjelder for pakken. Det er planlagt en egen rettighetsentitet for å lagre denne informasjonen i fremtiden.
- **Representasjoner**: Hver IE inneholder minst én representasjon.
- **Filer**: Filene i hver representasjon. Resultater fra formatidentifikasjon under innmating lagres her og beriker hvert fildokument med identifisert format.
- **Hendelser**: PREMIS-hendelser ("events"), både innsendt av klienter og generert av DPS. Hver hendelse er knyttet til en IE og kan valgfritt også knyttes til en spesifikk fil.
- **Agenter**: Personene, organisasjonene, programvaren eller utstyret som utførte hver hendelse.

For ytterligere definisjoner av disse PREMIS-entitetstypene, se [DPS sin rolle i NLN](/docs/dps/context/).

### Database for deskriptive metadata

En MongoDB-database. Hver IE er koblet til nøyaktig ett Dublin Core-dokument. Dette er metadataene du sender inn gjennom Submission API-et, lagret separat fra bevaringsmetadataene, men koblet til de samme IE-ene.

### Lokasjonsdatabase

En MongoDB-database. DPS pakker om og reorganiserer filene som sendes inn i SIP-er for bedre utnyttelse av det til det gjeldende bitlageret vårt. Denne databasen sporer hvor filene er fysisk lagret. Hvert depotfildokument er koblet til både et IE-dokument og fildokumentene det inneholder.

### Objektlagring for ekstraherte metadata

Resultatene fra metadataekstraksjonsverktøyene (MediaInfo og ExifTool) lagres som filer i en S3-bøtte for objektlagring. Fildokumentene i databasene refererer til stiene i denne bøtta.

## Hvordan metadata kan benyttes

Tilgang til metadata skjer i dag gjennom det offentlige API-et. Følgende data er tilgjengelige:

### Dublin Core-metadata

Kan hentes per avleverte informasjonspakke gjennom API-et. Når du ber om en spesifikk informasjonspakke, kan du inkludere de deskriptive metadataene som ble sendt inn sammen med den.

### PREMIS-hendelser

Kan hentes per avleverte informasjonspakke gjennom API-et. Både hendelser innsendt av klienter og hendelser generert av DPS kan hentes for en gitt informasjonspakke.

### Filmetadata

Kan hentes per fil gjennom API-et, inkludert filstier og sjekksummer.

### Utlisting av bevarte objekter

Du kan hente en paginert liste over avleverte informasjonspakker innenfor en gitt kontrakt gjennom API-et.

### Utlevering ("dissemination")

Du kan bestille utlevering av bevarte informasjonspakker og sjekke statusen på utleveringsjobben gjennom API-et. Selve nedlastingen av innhold skjer utenfor API-et. Metadatafilene i SIP-en bevares på samme måte som dataene og kan hentes ut på denne måten.

---

Metadata som lagres, men som foreløpig ikke er tilgjengelige gjennom API-et:

- **Ekstraherte tekniske metadata** lagres i S3-objektlagring, men er ennå ikke tilgjengelige for klienter gjennom API-et.

Vi arbeider for å muliggjøre søl på tvers av intellectual entiteter i bevaringsdatabasen, og der hendelser og andre metadata kan hentes i konteksten av IE-er. Denne sida beskriver hva som er tilgjengelig i dag. DPS er under aktiv utvikling.

## Hvordan metadata endrer seg over tid

Metadata i DPS følger tre ulike oppdateringsmodeller. Noen er implementert, mens andre er planlagt:

- **Versjoneres** (planlagt): Dublin Core-metadata skal kunne oppdateres gjennom API-et, med hver endring håndtert som en versjon hendelse. Dette er ikke implementert enda.
- **Tillegg**: PREMIS-hendelser kan bare legges til, aldri endres. Nye hendelser kobles til de relevante entitetene, og dokumenter slik det som har skjedd med objektet over tid. En forvalter kan utløse ny ekstraksjon av tekniske metadata for enkeltfiler, noe som produserer et nytt ekstraksjonsresultat samtidig som det gamle bevares.
- **Uforanderlige**: Metadatafilene i SIP-en fryses ved innlevering og kan ikke endres per nå.
