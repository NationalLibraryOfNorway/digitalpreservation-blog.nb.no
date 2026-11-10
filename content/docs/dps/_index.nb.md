---
title: Digital Preservation Services (DPS)
weight: 2
aliases:
  - /docs/services/dps/
  - /docs/services/
---

DPS (Digital Preservation Services) refererer til Nasjonalbibliotekets tjenester for bevaring av digitalt kulturarvmateriale. Med digitalt kulturarvmateriale menes både digitalisert og «digitalt født» materiale. Det omfatter både materiale som er underlagt pliktavleveringsloven, digitalt innhold som anses å være en del av nasjonal kulturarv, og materiale som på andre måter anses å være digitalt bevaringsverdig. DPS er basert på OAIS-modellen.

## Hvem kan bruke DPS

DPS er offentlig tilgjengelig, men tilgang krever en bevaringsavtale med Nasjonalbiblioteket. Hvordan avtaler og roller styrer tilgang, er beskrevet under [Tilgangskontroll](/nb/docs/dps/understanding/access-and-agreements/).

## Hva DPS gjør

DPS bruker et offentlig API både for innlevering og utlevering av informasjon. Systemet tar imot informasjonspakker (SIP-er), validerer dem og lagrer data og metadata på en sikker måte. Systemet tilbyr utlevering av informasjonspakker (DIP-er) gjennom det samme API-et. All tilgang og bruk styres av rollebasert tilgangskontroll knyttet til bevaringsavtaler.

[Slik fungerer DPS](/nb/docs/dps/understanding/how-dps-works/) beskriver tjenestene DPS består av, og [DPS sin rolle i NB](/nb/docs/dps/understanding/preservation-at-nln/) beskriver hvordan DPS henger sammen med Nasjonalbibliotekets andre systemer.

## Forstå DPS

Disse sidene forklarer konsepter, ansvarsområder og hvordan DPS fungerer:

{{< cards >}}
  {{< card link="understanding/how-dps-works" title="Slik fungerer DPS" subtitle="OAIS, tjenestene i DPS og hvordan de henger sammen" icon="cube" >}}
  {{< card link="understanding/preservation-at-nln" title="DPS sin rolle i NB" subtitle="De tre systemdomenene og hvordan data og metadata flyter mellom dem" icon="map" >}}
  {{< card link="understanding/information-packages" title="Informasjonspakker" subtitle="Hva en pakke inneholder, typer metadata og pakkens omfang" icon="archive" >}}
  {{< card link="understanding/data-management" title="Dataforvaltning" subtitle="Hvordan data bevares, lagres og uthentes i DPS" icon="database" >}}
  {{< card link="understanding/metadata-management" title="Metadataforvaltning" subtitle="Hvordan metadata kommer inn, lagres og brukes i DPS" icon="tag" >}}
  {{< card link="understanding/access-and-agreements" title="Tilgangskontroll" subtitle="Hvordan roller, bevaringsavtaler og tillatelser styrer tilgang" icon="shield-check" >}}
{{< /cards >}}

## Bruke DPS

Trinnvise veiledninger for produsenter og konsumenter:

{{< cards >}}
  {{< card link="how-to/prepare-content" title="Klargjøre materiale for levering" subtitle="Pakk materialet som en SIP som oppfyller kravene" icon="archive" >}}
  {{< card link="how-to/submit-content" title="Levere materiale til bevaring" subtitle="Registrer en innlevering, last opp filer og fullfør" icon="upload" >}}
  {{< card link="how-to/add-preservation-events" title="Legge til bevaringseventer" subtitle="Velg og legg til bevaringseventer i en innlevering" icon="collection" >}}
  {{< card link="how-to/retrieve-content" title="Bestille utlevering av bevart materiale" subtitle="Bestill utlevering av bevart materiale og last det ned" icon="download" >}}
  {{< card link="how-to/receive-notifications" title="Motta varsler" subtitle="Få statusoppdateringer i egne systemer via webhooks" icon="bell" >}}
{{< /cards >}}

## Referanse

Spesifikasjoner og API-referanse:

{{< cards >}}
  {{< card link="reference/api" title="Programmeringsgrensesnitt (API)" subtitle="Autentisering, roller og feilhåndtering" icon="code" >}}
  {{< card link="reference/sip" title="SIP-spesifikasjoner" subtitle="E-ARK pakkestruktur, METS.xml-krav og eksempler" icon="archive" >}}
  {{< card link="reference/descriptive-metadata" title="Krav til metadata" subtitle="Dublin Core-elementer som leveres med hver pakke" icon="tag" >}}
  {{< card link="reference/preservation-events" title="Bevaringseventer" subtitle="Event-elementer, agenter og eventtyper" icon="collection" >}}
{{< /cards >}}

