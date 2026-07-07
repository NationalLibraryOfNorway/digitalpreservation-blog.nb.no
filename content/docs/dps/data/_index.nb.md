---
title: Dataforvaltning
weight: 2
aliases:
 /docs/services/dps/data/
---

## Hva er data?

DPS er et sett med tjenester utviklet for å bevare data. I DPS-sammenheng snakker vi om *data og metadata*. **Data** er ressursen som skal bevares, for eksempel dokumenter, bilder, lyd- og filmopptak eller databasedumper. **Metadata** beskriver dataene og gir informasjon om innhold, struktur, kontekst og forvaltning. DPS tar ikke imot metadata uten data. 

For å avlevere data må dataene pakkes i en SIP, strukturert i henhold til våre [SIP-spesifikasjoner](/docs/dps/sip/). I en SIP ligger representasjoner i egen mappe for data. METS.xml-filene, metadata-mappene, skjemaene og dokumentasjonen utenfor data-mappene utgjør strukturen som gjør innholdet maskinlesbart og verifiserbart.[E-ARK-spesifikasjonene](https://dilcis.eu/specifications) definerer hvor de ulike filtypene skal plasseres i bevaringspakken. Dette gjør det enklere å finne, tolke og gjenbruke innholdet i framtiden. 

## Valg av hva som skal bevares

DPS og teamet for digital bevaring vurderer ikke hvilke digitale objekter som er bevaringsverdige. Ansvar for utvelgelse ligger hos Produsenten og skjer på to nivåer: 

- **Avtalenivå**: Nasjonalbiblioteket og produsenten inngår en avtale om bruk av DPS. Én bevaringsavtale kan omfatte flere tilgangsavtaler, som definerer hvem som kan avlevere materiale og hvem som har tilgang til det bevarte innholdet.
- **Objektnivå**: Produsenten avgjør hvilke digitale objekter som skal avleveres til DPS for bevaring.

På avtalenivå fastsetter bevaringsavtalen hvilke typer innhold som kan avleveres og hvilke vilkår som gjelder. DPS har ikke funksjonalitet for automatisk å kontrollere at hvert enkelt objekt er i samsvar med bevaringsavtalen. Systemet forutsetter derfor at avleveringer skjer i tråd med de avtalte rammene. 

Når materiale er avlevert i henhold til en bevaringsavtale, er DPS sin oppgave å sikre at innholdet bevares uendret, autentisk og tilgjengelig over tid, uavhengig av hvilke filer Produsenten har valgt å avlevere.

Ved valg av objekter og filformater anbefales det å følge [Prinsipper for digital bevaring](/docs/principles/). 

## Hvordan data kommer inn i DPS

Data kommer inn i DPS gjennom avlevering av informasjonspakker (SIPer) som sendes inn via avleveringstjenesten. Avleverer autentiserer seg mot API-et. API-et verifiserer at avleverer har de nødvendige rettigheter i henhold til inngått bevaringsavtale (se [rollebasert tilgangskontroll](/docs/dps/access-control/)). 

Avleveringsflyten er: opprett en avlevering → registrer filene som utgjør SIP-en → last opp filinnholdet → fullfør avleveringen for å starte behandling i DPS. 

Filene bevares dersom de validerer mot [krav til SIP-struktur](/docs/dps/sip/structure-requirements/), [krav til METS.xml](/docs/dps/sip/mets/) og krav til [Submission API-et](/docs/dps/api/submission/). Avleveringer som ikke oppfyller kravene vil bli avvist. 

## Hvordan data bevares i DPS

Når data først er kommet inn i DPS, er prinsippet enkelt: Det du avleverer er det du får tilbake, uendret. Bevaringen skjer på to nivåer: 

### Passiv bevaring

Passiv bevaring sikrer at data er uforandret. Den krever ingen forståelse av innholdet, bare at filene forblir uendret. 

- **Bevaring på bit-nivå**: Originalfilene bevares. Data lagres som det ble mottatt, uten konvertering, komprimering eller andre endringer som påvirker bit-innholdet. DPS krever at filer leveres med sjekksummer i SIP-en. Disse lagres, verifiseres under mottak og kontrolleres på nytt ved utlevering. Dersom et avvik oppdages, dokumenteres dette og de øvrige kopiene kontrolleres for å gjenopprette en uskadd versjon.
- **Redundant lagring**: Data beskyttes av 3-2-1-prinsippet: tre kopier, på to ulike lagringsteknologier, hvorav én kopi oppbevares på en annen geografisk plassering. Dersom én kopi går tapt eller blir korrupt, sikrer de andre kopiene at dataene overlever. Flere kopier gjør også integritetskontrollen meningsfull: når et avvik oppdages på én kopi, fungerer de andre kopiene som fasit for hvilken versjon som er korrekt.

Alle data lagres i bit-lageret. Den fysiske plasseringen til hver fil dokumenteres og kobles til det digitale objektet filen tilhører. DPS kan pakke om filer internt for å oppnå mer effektiv lagring, men dette er transparent: ved utlevering mottar du innholdet i sin opprinnelige form. 

### Aktiv bevaring

Aktiv bevaring omfatter mer enn sikker lagring av digitale objekter. Formålet er også å etablere og vedlikeholde kunnskap om innholdet, slik at det kan forvaltes og bevares over tid. 

Som en del av mottaksprosessen gjør DPS formatidentifikasjon og ekstraherer tekniske metadata for alle filer. Dette gir oversikt over hvilke filer som er lagret i DPS, hvilke filformater de har, og hvilke tekniske egenskaper de inneholder. Prosessen kan også avdekke avvik eller potensielle problemer. Dersom DPS identifiserer forhold som kan indikere feil i en fil etter at SIP-strukturen er validert, dokumenteres dette og produsenten informeres. Filen bevares deretter som en del av DPS. Dersom noen på et senere tidspunkt oppdager den samme feilen, vil dokumentasjonen vise at avviket allerede var registrert ved mottaket, og at filens integritet har vært uendret siden dette tidspunktet. 

Informasjonen som samles inn danner grunnlaget for bevaringsplanlegging. Kunnskap om hvilke filformater som finnes i DPS, og i hvilket omfang de forekommer, gjør det mulig å overvåke formater som kan være utsatt for teknologisk foreldelse og vurdere når bevaringstiltak kan bli nødvendige. Periodiske integritetskontroller verifiserer at filene ikke har blitt endret over tid. Alle operasjoner dokumenteres og viser hvilke handlinger som er utført på hver fil og når de fant sted. 

For en nærmere beskrivelse av hvordan metadata forvaltes, se [Metadataforvaltning](/docs/dps/metadata/).

## Hvordan data kan benyttes

Innholdet i DPS er ikke tilgjengelig for umiddelbar uthenting. Systemet er basert på en asynkron arkitektur. Lagringsløsningen er utformet for å prioritere langsiktig bevaringssikkerhet og kostnadseffektiv drift fremfor lav responstid ved utlevering. Tilgang og utlevering reguleres av egne avtaler. Forespørsler behandles via API'et. (se [rollebasert tilgangskontroll](/docs/dps/access-control/)).

## Hvordan data endrer seg over tid

Data som er bevart i DPS er uforanderlige. Når en informasjonspakke er avlevert og bevart, kan de opprinnelige filene ikke endres. Dersom innhold må oppdateres eller erstattes, må dette skje gjennom en ny avlevering. Den opprinnelige versjonen bevares sammen med den nye, slik at begge versjoner er tilgjengelige. 

Bevaringsaktiviteter, som formatmigrering og integritetskontroller, dokumenteres som en del av bevaringsprosessen. Slike aktiviteter kan resultere i nye derivater, men påvirker ikke de bevarte originalfilene. 

DPS er under kontinuerlig utvikling. Det pågår arbeid med å vurdere hvordan muligheten for å legge til nye data i eksisterende informasjonspakker kan støttes i framtiden. Denne funksjonaliteten er foreløpig ikke implementert.
