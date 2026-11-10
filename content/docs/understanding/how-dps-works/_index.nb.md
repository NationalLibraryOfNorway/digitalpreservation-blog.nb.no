---
title: Slik fungerer DPS
weight: 1
aliases:
  - /docs/dps/understanding/how-dps-works/
---

DPS tar imot informasjonspakker gjennom et offentlig API, validerer dem og lagrer data og metadata på en sikker måte. Bevart innhold utleveres gjennom det samme API-et. Denne siden beskriver referansemodellen DPS bygger på, og tjenestene DPS består av.

## OAIS som referansepunkt

OAIS (Open Archival Information System) er en referansemodell for arkivering av digital informasjon. Nasjonalbiblioteket bruker OAIS som et referansepunkt i digital bevaring, selv om kompleksiteten og utviklingen av arkitekturen vår gjør at OAIS-modellen ikke uten videre kan legges over organisasjonen vår.

{{< figure src="OAIS_Functional_Model_(en).svg" alt="OAIS-modellen" caption="" attr="Mathieualexhache (original work); Mess (SVG conversion & English translation), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0), via Wikimedia Commons" >}}

Sentrale OAIS-begreper er de forskjellige informasjonspakkene:

- **SIP** (Submission Information Package): leveres for bevaring. Inneholder innholdsdata, dokumentasjon og metadata som trengs for langsiktig bevaring og tilgang.
- **AIP** (Archival Information Package): slik den er lagret i bit-depotet. Kan være identisk med SIP-en eller inneholde ytterligere bevaringsinformasjon.
- **DIP** (Dissemination Information Package): utleveres fra bevaring. Kan bestå av hele eller deler av en AIP.

Med mindre noe annet er spesifisert, refererer vi til SIP-er når vi snakker om informasjonspakker i disse dokumentene.

## Tjenestene i DPS

DPS består av flere tjenester:

- **API-tjenesten**: Grensesnittet som brukes for både innlevering og utlevering, inkludert filoverføringer. All kommunikasjon med DPS skjer gjennom API-tjenesten.
- **Mottak**: En kjede av tjenester (overføring, validering, karakterisering, pakking, arkivering og varsling) som behandler pakker før de bevares i bit-lageret.
- **Utlevering**: En kjede av tjenester som behandler pakker for uthenting før de leveres via API-et.

**Metadatatjenesten** og **bit-lageret** utgjør kjernen i DPS. Det er her det digitale innholdet bevares og sikres.

- **Metadatatjenesten**: Databaser og objektlagring som holder oversikt over det bevarte innholdet og tilhørende metadata. De fleste tjenestene i DPS lagrer metadata i eller henter metadata fra metadatatjenesten.
- **Bit-lager**: Ulike tekniske løsninger som sørger for sikker og langsiktig lagring av det digitale innholdet.

{{< figure src="dpskonsept.drawio.svg" alt="DPS konseptuell arkitektur" caption="Konseptuell oversikt over DPS. Hele linjer representerer innlevering, stiplede linjer representerer utlevering. Dataflyt er vist i svart, metadataflyt i rødt." >}}

All tilgang og bruk styres av rollebasert tilgangskontroll knyttet til bevaringsavtaler. Se [Tilgangskontroll](/nb/docs/understanding/access-and-agreements/).

## Les mer

- [Dataforvaltning](/nb/docs/understanding/data-management/) og [Metadataforvaltning](/nb/docs/understanding/metadata-management/): hva som skjer med data og metadata i DPS.
- [DPS i Nasjonalbiblioteket](/nb/docs/understanding/preservation-at-nln/): hvordan DPS passer inn i Nasjonalbibliotekets eget systemlandskap.
