---
title: Dataforvaltning
weight: 2
aliases:
 /docs/services/dps/data/
---

## Hva er data?

DPS er et sett med tjenester utviklet for å bevare data. I DPS-sammenheng snakker vi om *data* og *metadata*. Data er innholdet som bevares: de digitale filene du avleverer til DPS. Metadataene i DPS eksisterer for å muliggjøre bevaring og gi tilgang til disse dataene. Uten data finnes det ingenting å bevare. DPS tar ikke imot metadata uten data.

For å avlevere data må dataene pakkes i en SIP, strukturert i henhold til våre [SIP-spesifikasjoner](/docs/dps/sip/). I SIP-en ligger dataene i `data/`-mappa i hver representasjon. METS.xml-filene, metadata-mappene, skjemaene og dokumentasjonen utenfor data-mappene utgjør "emballasjen" som gjør innholdet maskinlesbart og verifiserbart. [E-ARK-spesifikasjonene](https://dilcis.eu/specifications) definerer hvilke typer filer som hører hjemme hvor, slik at framtidige brukere som henter ut dataene vet hvor de skal lete etter hva.

Hvis du ønsker å bevare metadata i DPS (for eksempel metadatafiler eksportert fra bibliotekkataloger), behandles disse som *data* i DPS-sammenheng og legges i `data/`-mappa i SIP-en. DPS vil da på samme måte kreve metadata som beskriver disse dataene. DPS tillater dette, men hvorvidt dette er en hensiktsmessig måte å sikre metadata kan diskuteres.

Formålet med digital bevaring er å sikre at digitalt innhold forblir uendret og kan benyttes over tid. DPS forvalter i dag petabyte med bevarte data. Når data først har kommet inn i DPS, er vi forpliktet til å bevare innholdet så lenge klienten og bevaringsavtalen vurderer dataene som bevaringsverdige. Dersom ikke annet er avtalt, betyr dette i praksis i "evig" tid. DPS er ikke ment som midlertidig lager for filer.

## Valg av hva som skal bevares

DPS og teamet for digital bevaring avgjør **ikke** hva som er bevaringsverdig. Utvelgelsen skjer på to nivåer:

- **Avtalenivå**: Nasjonalbiblioteket og klientorganisasjonen inngår en avtale om bruk av DPS. Én kontrakt kan resultere i flere bevaringsavtaler, som hver styrer hvilke klienter som kan avlevere og få tilgang til innholdet.
- **Objektnivå**: Utvalgskriteriene ligger fullt og helt hos klienten. Det er dere som avgjør hvilke objekter som skal inn i DPS, og hvilke som skal holdes utenfor.

På avtalenivå definerer bevaringsavtalen hvilke typer innhold som kan avleveres og på hvilke vilkår. Vi har i dag ikke mulighet til å automatisk validere at hvert enkelt objekt samsvarer med innholdet i avtalen, og er derfor avhengige av at klienten følger sine forpliktelser.

På objektnivå er valget klientens. Når bevaringsavtalen først er inngått, er vår rolle ikke å vurdere hva som fortjener bevaring. Vår oppgave er å sikre at det dere overlater til oss forblir uendret og tilgjengelig, uavhengig av hvilke filer dere velger å bevare.

Vi anbefaler sterkt at klienter gjør informerte vurderinger på objektnivå, i tråd med [Prinsipper for digital bevaring](/docs/principles/). Særlig anbefaler vi:

- **Bruk av veldokumenterte og åpne filformater**: Dette øker sannsynligheten for at filene forblir brukbare over tid (prinsipp 2). Se [Anbefalte filformater](/docs/formats) for våre anbefalinger.
- **Unngå unødvendig store filer**: Hver eneste bit som lagres i DPS medfører en varig kostnad knyttet til lagring og forvaltning (prinsipp 1). Unødvendig store filer gir økte kostnader uten å tilføre verdi. Ved å avlevere den minste fornuftige versjonen av hvert digitalt objekt bidrar du til å holde systemet bærekraftig.
- **Unngå unødvendig duplisering av data**: Filer som kan genereres automatisk fra bevarte masterfiler (for eksempel tilgangskopier eller lavoppløselige derivater) bør ikke avleveres (prinsipp 1). DPS fokuserer på å bevare kildematerialet som andre versjoner kan produseres fra.
- **Analyser filene før avlevering**: Generer sjekksummer tidlig, bekreft filformatene og verifiser at innholdet er det det utgir seg for å være (prinsipp 4). DPS krever at alle filer avleveres med sjekksum i SIP-en.

## Hvordan data kommer inn i DPS

Data kommer inn i DPS gjennom avlevering av informasjonspakker (SIPer) som sendes inn via avleveringstjenesten. Du autentiserer deg mot API-et, som verifiserer at du har rettigheter til å avlevere under den aktuelle bevaringsavtalen (se [rollebasert tilgangskontroll](/docs/dps/access-control/)).

Avleveringsflyten er: opprett en avlevering → registrer filene som utgjør SIP-en → last opp filinnholdet → fullfør avleveringen for å starte innmating i DPS.

Filene bevares dersom de validerer mot [krav til SIP-struktur](/docs/dps/sip/structure-requirements/), [krav til METS.xml](/docs/dps/sip/mets/) og [krav til Submission API-et](/docs/dps/api/submission/). Avleveringer som ikke oppfyller kravene vil bli avvist. 

## Hvordan data bevares i DPS

Når data først er kommet inn i DPS, er prinsippet enkelt: Det du avleverer er det du får tilbake, uendret. Bevaringen skjer på to nivåer:

### Passiv bevaring

Passiv bevaring sikrer at bitene overlever. Den krever ingen forståelse av innholdet, bare at filene forblir uendret.

- **Bevaring på bitnivå**: Originalfilene bevares. Data lagres som en tro kopi av det som ble mottatt, uten konvertering, komprimering eller andre endringer som påvirker bitinnholdet. DPS krever at filer leveres med sjekksummer i SIP-en. Disse lagres, verifiseres under innmating og kontrolleres på nytt ved utlevering. Dersom et avvik oppdages, dokumenteres dette og de øvrige kopiene kontrolleres for å gjenopprette en uskadd versjon. I praksis fungerer dette i stor skala: over 16 millioner filer har blitt sjekksumverifisert gjennom fem teknologiske generasjonsskifter over 20 år, uten at en eneste endring på bitnivå er påvist.
- **Redundant lagring**: Data beskyttes av 3-2-1-prinsippet: tre kopier, på to ulike lagringsteknologier, hvorav én kopi oppbevares på en annen geografisk plassering. Dersom én kopi går tapt eller blir korrupt, sikrer de andre kopiene at dataene overlever. Flere kopier gjør også integritetskontrollen meningsfull: når et avvik oppdages, fungerer de uskadde kopiene som fasit for hvilken versjon som er korrekt.

Alle data lagres i bitlageret. Den fysiske plasseringen til hver fil dokumenteres og kobles til det digitale objektet filen tilhører. DPS kan pakke om filer internt for å oppnå mer effektiv lagring, men dette er transparent: ved utlevering mottar du innholdet i sin opprinnelige form.

### Aktiv bevaring

Aktiv bevaring handler om mer enn å lagre biter. Den aktive bevaringen handler delvis om å bygge opp kunnskap om innholdet slik at DPS kan håndtere det over tid.

Som del av innmatingsprosessen utfører DPS formatidentifikasjon og ekstrahering av tekniske metadata for alle filer. Dette gir oversikt over hvilke filer som finnes i depotet, hvilke formater de har og hvilke tekniske egenskaper de besitter. Samtidig avdekkes potensielle problemer: dersom DPS finner noe som kan være galt med en fil, selv etter at SIP-strukturen er validert, dokumenteres dette, klienten informeres om feilen, før filen bevares som vanlig. En framtidig bruker som oppdager en feil kan dermed se at DPS allerede registrerte problemet ved innmating, og at filens integritet har vært uendret siden.

Denne kunnskapen danner grunnlaget for bevaringsplanlegging ("preservation planning"). Kunnskap om hvilke filformater som finnes i bitlageret og i hvilke mengder, gjør det mulig å overvåke utsatte formater og vurdere når tiltak kan bli nødvendige. Periodiske integritetskontroller verifiserer at filene ikke har endret seg. Alle operasjoner dokumenteres og danner et "revisjonsspor" som viser hva som skjedde med hver fil og når.

Teamet for digital bevaring opprettholder kompetanse om ulike filformater, deres styrker og svakheter, og konsekvensene av å migrere fra ett format til et annet. Dette gjør oss i stand til å hjelpe klienter med å ta informerte beslutninger om hvilke tiltak som bør gjennomføres dersom et format skulle bli truet på en eller annen måte. For en detaljert gjennomgang av hvordan metadataene forvaltes, se [Metadatahåndtering](/docs/dps/metadata/).

## Hvordan data kan benyttes

Data i DPS lagres "kaldt". Tilgangen er ikke umiddelbar. DPS er bygget på en asynkron arkitektur, og utleveringsforespørsler behandles som bakgrunnsjobber med innebygde forsinkelser. Dette er et bevisst valg: bitlageret er optimalisert for langsiktig sikkerhet og kostnadseffektivitet fremfor rask uthenting.

Data hentes ut gjennom utlevering. For å hente ut data må du ha en konsumentrolle knyttet til den aktuelle bevaringsavtalen (se [rollebasert tilgangskontroll](/docs/dps/access-control/)):

- Du oppretter en utleveringsforespørsel gjennom API-et og angir DPS-ID-en til innholdet du ønsker å hente ut (se [Dissemination API](/docs/dps/api/dissemination/)).
- Det utføres en integritetskontroll som del av utleveringsprosessen for å verifisere at innholdet ikke har blitt endret siden det ble lagret.
- Når innholdet er klart, gjøres det tilgjengelig gjennom en presigned URL som leveres via webhook.
- Du kan også sjekke status på forespørselen gjennom API-et mens DPS klargjør innholdet.

Når innhold utleveres, returneres filene i sin opprinnelige form. Ompakkingen som skjer internt i lagringssystemet er transparent for brukeren.

## Hvordan data endrer seg over tid

I dag er data i DPS uforanderlige. Når filer først er bevart, kan originalene ikke endres. Hvis du trenger å oppdatere eller erstatte innhold, må du avlevere en ny versjon gjennom en ny avlevering. Originalen bevares side om side med den oppdaterte versjonen. Bevaringsaktiviteter som formatmigrering eller integritetskontroller dokumenteres og kan resultere i nye derivater, men de endrer ikke de bevarte originalfilene.

DPS er fortsatt under utvikling. Vi diskuterer aktivt hvordan versjonering og tillegg av nye data til eksisterende informasjonspakker kan støttes i framtiden. Dette er ikke implementert ennå, men gjenspeiler et kontinuerlig arbeid for å gjøre systemet mer fleksibelt over tid.
