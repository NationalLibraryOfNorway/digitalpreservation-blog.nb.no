---
title: "PREMIS uten fasit – vår tilnærming til bevaringsmetadata og eventer"
date: 2026-03-24
description: "Team digital bevaring har jobbet med hvordan vi skal dokumentere bevaringsmetadata i bevaringsomgivelsene våre, her kan du lese om jobben vi har gjort sålangt."
tags: ["Digital bevaring, Nasjonalbiblioteket, Digital Preservation, National library of Norway, metadata, bevaringsmetadata, preservation metadata, PREMIS"]
draft: false
authors: 
  - name: Lise-Lotte Melkild
    image: /apple-touch-icon.png 
---



![AI-generert illustrasjon bevaringsmetadata](/chatGPTbilde.png)

🗂️ Bevaringsmetadata beskriver opphavet til digitalt materiale, hvor det kommer fra og hvordan det er blitt til. Disse dokumenterer hvilke handlinger og hendelser (heretter kalt "eventer", på godt norsk) som har påvirket et digitalt objekt. Eksempler på dette kan være opprettelse av et objekt, formatmigrering, validering eller overføring fra et system til et annet. Denne typen metadata er særlig viktig for digitalt materiale, fordi det sikrer sporbarhet og gir dokumentasjon på hva som har blitt gjort med objektet gjennom hele livssyklusen.

🕰️ Historisk sett har det vært begrenset fokus på systematisk arbeid med bevaringsmetadata for digitalt materiale i Nasjonalbiblioteket. Etter at Team Digital Bevaring ble opprettet, har det blitt dedikert fokus på hvordan både data og metadata skal forvaltes bedre over tid. PREMIS-standarden[^1], som er utviklet for å legge til rette for strukturert beskrivelse av bevaringsmetadata, har vært diskutert i flere runder. Da det ble bestemt at vi skulle ta i bruk [E-ARK standarden](https://dilcis.eu/) for våre bevaringspakker, var det ikke lenger noen tvil, siden E-ARK også anbefaler og viser til bruk av PREMIS for denne typen metadata. 
De siste årene har vi dokumentert enkelte bevaringshendelser i en egen database, og i det pågående arbeidet med å oppgradere DPS-løsningen[^2] vår, bestemte vi oss for å samtidig se på muligheten for å ta i bruk PREMIS-eventer.

🧐Da vi hadde lite  kunnskap om PREMIS fra før, måtte vi starte jobben med å sette oss inn i hva PREMIS-standarden er, hva den er ment for og hvordan standarden kan brukes. Her fant vi fort ut at det var lite dokumentasjon som sier hvordan ting skal gjøres, og at standarden er et rammeverk som kan tolkes og løses på utallige måter. 

📊 Videre tilnærming ble en systematisk gjennomgang av [PREMIS Data Dictionary](https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf). Her gikk vi gjennom alle entiteter og samtlige semantiske enheter for å få kartlagt hva vi allerede dokumenterer, hva som vil være relevant å dokumentere på kort sikt (for å komme i gang), hva vi ønsker å implementere etterhvert, og hva vi ser på som lite relevant for vår samling. Det er hele tiden en veining mot hva som er nok dokumentasjon, uten å ende opp med unødvendig mye metadata som må lagres og forvaltes. Vi må ha i tankene at vi har mye data, mer enn de fleste, rundt 19 petabyte (19.000 terabyte) med unike data ved utgangen av 2025. Bare ved å dokumentere noen få eventer i gammel DPS-løsning, har vi allerede over 53 millioner eventer på pakkenivå og over 76 millioner eventer på filnivå. 

🔄 Videre så vi på hvilke eventer som var relevant for teamet å dokumentere internt i DPS-flyten, ved inntak av ny data og ved utlevering. I forlengelsen av arbeidet så vi en mulighet for å legge til rette for at avleverere kan levere PREMIS-eventer via API-et vårt, samtidig som de avleverer nye informasjonspakker (SIP). På denne måten kunne vi også tilby avleverer å få levert relevante bevaringsmetadata de har fra tiden før vi mottar det digitale materialet i DPS. Eventer avlevert via API bevares på samme måte som eventer opprettet i DPS. 

📋 For å bestemme hvilke eventer vi mener er relevante å dokumentere, tok vi utgangspunkt i Library of Congress sin liste over [eventTypes](https://id.loc.gov/vocabulary/preservation/eventType.html). Lista er snevret inn, og bruken av de ulike typene er spesifisert til å passe med materialet og bevaringsomgivelsene våre. Per nå er det 11 event-typer som tillates avlevert i API-et vårt, internt i DPS bruker vi noen andre typer i tillegg. Tillatte eventer avlevert i API er i første omgang utarbeidet for Nasjonalbibliotekets interne produksjonsløyper, men vil tilrettelegges for eksterne avleverere når det blir aktuelt. 

💾 Foreløpig har vi gått for en enkel modellering av PREMIS-eventene. Det som dokumenteres er objekt, event og agent. På objekt er det to nivåer som dokumenteres, intellektuell entitet (som i praksis er informasjonspakken) og på filnivå. Vi viderefører bruken av egen database  for eventer, og (per nå) ikke skrive dem til fil i informasjonspakken. Dette for å gjøre det enklere å samle informasjonen og skrive nye eventer uten å måtte oppdatere informasjonspakken. Vi skriver ikke eventer i PREMIS.xml i databasen, men i JSON-format. Vi tar høyde for at vi ved behov kan skrive eventer fra database til informasjonspakker (feks DIP ved utlevering) i PREMIS.xml. Dette gjelder også eventer som vi tar imot fra avleverere via API. For ordens skyld, så bevares våre databaser etter samme bevaringsprinsipper som data som bevares i bit-lager. 

I tillegg til at vi anbefaler avlevering av bevaringsmetadata i form av eventer i API, er det også mulig å avlevere denne type metadata i informasjonspakken (SIP). Mer om det her: [SIP 1.0 (E-ARK)](/docs/dps/sip/1.0/). 

🚀 Vi anser arbeidet vi har gjort som et utgangspunkt. Vi har valgt å dokumentere det vi vurderer som viktig nå, for å komme i gang, med en bevisst tilnærming om at vi kan justere kursen underveis. For oss er det viktigere å etablere en praksis som kan videreutvikles, enn å prøve å treffe en perfekt løsning fra start, der vi risikerer å bruke tiden på  endeløse diskusjoner - og lite praktiske løsninger. 

Det er publisert dokumentasjon på bruk av event-elementer og event-typer her: [Eventer/bevaringsmetadata](/nb/docs/dps/api/submission/events/).

Mer teknisk informasjon finnes her: [Swagger DPS Submission Service API](https://digitalpreservation.no/swagger/).

Ta gjerne kontakt hvis dere har kommentarer eller spørsmål 😊



[^1]: Preservation Metadata Implementation Strategies (PREMIS) er en metadatastandard for registrering av informasjon som er nødvendig for bevaring av digitale objekter. Standardens dokumentasjon og metadataskjema forvaltes av Library of Congress.
[^2]: Digital Preservation Services (DPS) er en samlebetegnelse for tjenster og programvarer som forvalter data i digital bevaring i Nasjonalbiblioteket. Systemet tar i mot data som skal bevares, sikrer dataintegritet og styrer tilgangen til bevarte data.