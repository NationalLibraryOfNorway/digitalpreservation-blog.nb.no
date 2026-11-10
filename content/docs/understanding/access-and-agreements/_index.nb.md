---
title: Tilgangskontroll
tags: [Digital bevaring, OAIS-modell, Rollebasert tilgang, Bevaringsavtaler, Informasjonspakker, Autorisasjonssystemer, Tilgangsstyring, Digitale arkiv]
weight: 5
aliases:
  - /docs/services/dps/access-control/
  - /docs/dps/access-control/
  - /docs/dps/understanding/access-and-agreements/
---

Tilgang til DPS styres gjennom et offentlig API. Hvem som kan levere og hente ut innhold styres av rollebasert tilgangskontroll: hver klient tildeles spesifikke roller knyttet til bevaringsavtaler, og disse rollene bestemmer hva klienten er autorisert til å gjøre.

Modellen som styrer tilgang til å avlevere data til eller hente data fra DPS, har fire hovedkomponenter: *klienter*, *roller*, *bevaringsavtaler*, og *informasjonspakker*. For kontekst om hva som leveres og hentes, se [Dataforvaltning](/nb/docs/understanding/data-management/) og [Metadataforvaltning](/nb/docs/understanding/metadata-management/).

## Klienter
Alle brukere som skal snakke med DPS får tildelt en klient (med en klientID) av Nasjonalbiblioteket.
Med bruker mener vi en avtalepartner (REST klient) som kan kommunisere maskinelt med DPS.
Klienter kan tildeles flere roller.

## Roller
Rollene kommer i to varianter: *produsent* og *konsument*.

En produsentrolle gir klienten rettigheter til å *levere* data til DPS i form av informasjonspakker til DPS, mens en konsumentrolle gir deg tilgang til å hente informasjonspakker ut fra DPS.
Uten en rolle kan ikke klienten interagere med DPS.

Alle enkeltroller er igjen koblet til én spesifikk bevaringsavtale.
Roller tildeles klienter av Nasjonalbiblioteket, i henhold til termene spesifisert i de enkelte bevaringsavtalene.

I API-et vises rollene i tilgangstokenet som `{contractId}_W` (produsent, skrivetilgang) og `{contractId}_R` (konsument, lesetilgang) for hver bevaringsavtale. Se [Rollebasert tilgangsstyring](/nb/docs/reference/api/#rollebasert-tilgangsstyring).

## Bevaringsavtaler (submission agreement)
Bevaringsavtaler sier noe om forvaltningspremissene for en gitt informasjonspakke. 
Bevaringsavtaler opprettes mellom produsenter (OAIS) og Nasjonalbiblioteket.
Bevaringsavtalen er Nasjonalbibliotekets variant av konseptet "submission agreement", som stammer fra OAIS. 
Submission agreements oppsummeres slik i E-ARK-SIP-spesifikasjonene:[^1]

> Interactions between Producers and the OAIS are often guided by a Submission Agreement, which establishes specific details about how these interactions should take place, e.g. the type of information expected to be exchanged, the metadata the Producer is expected to deliver, the logistics of the actual transfer, statements regarding access restrictions on the submitted material, etc.

I konteksten rollebasert tilgang, er det ikke detaljene i disse bevaringsavtalene som er viktig, men det at bevaringsavtalene er opprettet i systemene våre.

Produsent-/konsument-roller relatert til bevaringsavtalen opprettes i systemene våre.
En bevaringsavtale må eksistere *før* avlevering av informasjonspakker til DPS kan skje.

Bevaringsavtaler er knyttet til én eller flere informasjonspakker. I API-et identifiseres en bevaringsavtale med kontrakt-ID-en (`contractId`).

## Informasjonspakker
Når data eller metadata skal leveres til eller hentes ut fra DPS, gjøres dette i form av informasjonspakker[^2].
Individuelle informasjonspakker er knyttet til én (og kun én) bevaringsavtale.

## Arkiv-ID
DPS tildeler en arkiv-ID (`archiveId`) til hver informasjonspakke som bevares.
Arkiv-ID-en er unik innenfor våre systemer, og er pakkens varige identifikator i DPS.
Arkiv-ID-en sendes til den som har avlevert informasjonspakken når pakken er bevart, i meldingen `submission.preserved`.

{{< figure src="tilgangskontroll.svg" alt="Et diagram som viser relasjonene mellom komponentene som er relevante for tilgangsstyring" caption="Komponentene som styrer rollebasert tilgang" >}}

## Eksempel: Innlevering av informasjonspakker
En klient som skal levere en informasjonspakke til DPS, er nødt til å spesifisere hvilken bevaringsavtale som skal gjelde for pakka.
Man kan kun levere informasjonspakker knyttet til bevaringsavtaler man er autorisert til å *produsere*.
Hvis man har de riktige rollene, registrerer DPS innleveringen og returnerer en innleverings-ID (`submissionId`) som kvittering. Når pakken er bevart, tildeler DPS en arkiv-ID og sender den til klienten.

```mermaid
sequenceDiagram
    participant C as Client
    participant K as AuAu System
    participant DPS as DPS API
    
    C->>K: 1. Request token with client credentials
    K-->>C: 2. Return JWT with roles
    
    C->>DPS: 3. Submit ingest request with contract ID<br>of the preservation agreement
    
    DPS-->>K: 4. Validate JWT
    K-->>DPS: 
    DPS->>DPS: 5. Verify producer role matches<br/>contract ID
    
    alt Valid JWT & Authorized Producer
        DPS->>DPS: 6a. Register submission
        DPS-->>C: 7a. Return submission ID as receipt
    else Invalid JWT or Unauthorized
        DPS-->>C: 6b. Return error message
    end
```

## Eksempel: Uthenting av informasjonspakker
En klient som vil hente denne informasjonspakka ut igjen, vil måtte spesifisere hvilken informasjonspakke som skal hentes ut ved hjelp av arkiv-ID-en.
Hvis klienten har en konsumentrolle knyttet til bevaringsavtalen som gjelder for den relevante informasjonspakka, vil DPS starte utleveringsprosessen.

```mermaid
sequenceDiagram
    participant C as Client
    participant K as AuAu System
    participant DPS as DPS API
    
    C->>K: 1. Request token with client credentials
    K-->>C: 2. Return JWT with roles
    
    C->>DPS: 3. Request dissemination using archive ID
    
    DPS-->>K: 4. Validate JWT
    K-->>DPS: 
    DPS->>DPS: 5. Verify consumer role matches<br/>contract ID for IP <br>with requested archive ID
    
    alt Valid JWT & Authorized Consumer
        DPS->>DPS: 6a. Begin dissemination process
        DPS-->>C: 7a. Return dissemination start message
    else Invalid JWT or Unauthorized
        DPS-->>C: 6b. Return error message
    end
```

## Eksempel: Søk
En klient som vil gjøre oppslag i DPS, vil kunne gjøre oppslag på alle informasjonspakker koblet til bevaringsavtalene vedkommende har en konsumentrolle for.

```mermaid
sequenceDiagram
    participant C as Client
    participant K as AuAu System
    participant DPS as DPS API
    
    C->>K: 1. Request token with client credentials
    K-->>C: 2. Return JWT with roles
    
    C->>DPS: 3. Submit search query
    
    DPS-->>K: 4. Validate JWT
    K-->>DPS: 
    DPS->>DPS: 5. Extract client roles and match<br> with contract IDs
    
    alt Valid JWT & Has Consumer Roles
        DPS->>DPS: 6a. Execute search on IPs with relevant<br> contract IDs
        DPS-->>C: 7a. Return search results
    else Invalid JWT or No Consumer Roles
        DPS-->>C: 6b. Return error message
    end
```

[^1]: [E-ARK SIP: 4.1. Submission Agreements](https://earksip.dilcis.eu/#submissionagreements)
[^2]: For mer informasjon om informasjonspakker se [OAIS-terminologien](/nb/docs/understanding/how-dps-works/#oais-som-referansepunkt).
