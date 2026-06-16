---
title: Digital Preservation Services (DPS)
weight: 4
aliases:
  - /docs/services/dps/
  - /docs/services/
---

DPS (Digital Preservation Services) refererer til Nasjonalbibliotekets tjenester for bevaring av digitalt kulturarvmateriale. Med digitalt kulturarvmateriale menes både digitalisert og «digitalt født» materiale. Det omfatter både materiale som er underlagt pliktavleveringsloven, digitalt innhold som anses å være en del av nasjonal kulturarv, og materiale som på andre måter anses å være digitalt bevaringsverdig. DPS er et OAIS-arkiv.

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

Gjennom disse sidene refererer vi til *klienter*: organisasjonene og systemene som samhandler med DPS. En klient kan opptre som **produsent** (leverer data) eller **konsument** (henter data), i tråd med etablert OAIS-terminologi. En enkelt klient kan være både produsent og konsument.

DPS er offentlig tilgjengelig, men tilgang krever en avtale med Nasjonalbiblioteket. For detaljer, se [Datahåndtering](/docs/dps/data/).

## Hva DPS gjør

DPS tar imot informasjonspakker (SIP-er), validerer dem, lagrer data og metadata på en sikker måte, og tilbyr utlevering gjennom et offentlig API. Alt styres av rollebasert tilgangskontroll knyttet til bevaringsavtaler.

Under panseret består DPS av flere tjenester:

- **API service**: det offentlige grensesnittet som klienter bruker for både innlevering og utlevering, inkludert filoverføringer.
- **Ingest pipeline**: en kjede av tjenester (transfer, validation, characterization, packaging, archive, notification) som prosesserer pakker før de går inn i bit-depotet.
- **Dissemination pipeline**: en kjede av tjenester som prosesserer pakker for uthenting før de leveres gjennom API-et.

Sammen utgjør **metadata service** og **bit repository** DPS sin kjerne (gjerne kalt **DPS core**). Disse holder innholdet vi bevarer og sikrer. Tjenestene rundt dem kan byttes ut. Selve DPS-kjernen kan også byttes ut, men innholdet må da migreres:

- **Metadata service**: databasene og objektlagringen som holder oversikt over alt. De fleste tjenestene i DPS sender metadata til eller benytter seg av metadata fra denne tjenesten.
- **Bit repository**: teiprobotbibliotek og diskbibliotek for trygg og langsiktig lagring.

Du har bare grensesnitt mot DPS gjennom API service.

{{< figure src="dpskonsept.drawio.svg" alt="DPS konseptuell arkitektur" caption="Konseptuell oversikt over DPS. Hele linjer representerer innlevering, stiplede linjer representerer utlevering. Dataflyt er vist i svart, metadataflyt i rødt." >}}

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
