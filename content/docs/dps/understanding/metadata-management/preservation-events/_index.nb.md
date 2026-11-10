---
title: Bevaringseventer
weight: 1
---

Bevaringseventer er en type bevaringsmetadata. En event dokumenterer en handling eller hendelse som har påvirket et digitalt objekt, for eksempel opprettelse, migrering, validering eller overføring. Sammen utgjør eventene en oversikt over hva som er gjort med et objekt gjennom hele livssyklusen, av hvem, og med hvilket resultat. [Metadataforvaltning](/nb/docs/dps/understanding/metadata-management/) beskriver hvordan eventer kommer inn i DPS, både fra produsenten og fra DPS selv. Denne siden forklarer hvordan eventer er modellert, hvorfor vi anbefaler å levere dem via API-et, og hvor mye som bør dokumenteres.

## Hvordan eventer er modellert

DPS baserer eventene sine på [PREMIS-datamodellen](https://www.loc.gov/standards/premis/) for bevaringsmetadata. Hver event knytter sammen tre ting:

- **Objektet** eventen gjelder: enten hele informasjonspakken (den intellektuelle entiteten) eller en enkelt fil i den.
- **Selve eventen**: hva slags handling det var, når den skjedde, hva som ble gjort, og hva utfallet ble.
- **Agenten** som utførte den: programvare, maskinvare, en organisasjon eller en person.

PREMIS er et fleksibelt rammeverk mer enn en fast oppskrift, og det finnes lite veiledning i hvordan det skal brukes i praksis. Nasjonalbiblioteket har valgt en bevisst enkel modell i første omgang, og regner med å utvide den over tid. Bakgrunnen for valgene er beskrevet i blogginnlegget [PREMIS uten fasit](/nb/blog/2026-03-24-premis-without-a-single-right-answer-our-approach-to-preservation-metadata-and-events/).

Eventtyper hentes fra et kontrollert vokabular. Nasjonalbiblioteket tar utgangspunkt i Library of Congress sin liste over [eventtyper](https://id.loc.gov/vocabulary/preservation/eventType.html), innskrenket og spesifisert for å passe vårt materiale og våre bevaringsomgivelser.

## Eventer i API-et og i SIP-en

Eventer lagres i databasen for bevaringsmetadata i stedet for å skrives som filer i informasjonspakken. Det gjør det mulig å legge til nye eventer gjennom hele levetiden til et objekt uten å endre den bevarte pakken. Eventer som produsenten leverer, bevares på lik linje med eventene DPS registrerer selv, slik at hele historikken til et objekt er samlet på ett sted når det hentes ut.

Bevaringsmetadata kan også legges som filer i informasjonspakken (SIP). Slike filer bevares som en del av pakken, men de er ikke tilgjengelige som eventer gjennom API-et. Derfor anbefaler vi å levere eventer via API-et. Hvis praktiske eller tekniske grunner gjør det umulig, er det likevel bedre å legge informasjonen i SIP-en enn å utelate den. Informasjon om proveniens kan også oppgis i elementet *Provenance* i de [deskriptive metadataene](/nb/docs/dps/reference/descriptive-metadata/).

## Bevisst dokumentasjon

Flere eventer betyr ikke nødvendigvis bedre dokumentasjon. Mange eventer som sier det samme gjør historikken vanskeligere å lese, og øker mengden metadata som må forvaltes over tid. Som hovedregel knyttes eventer til informasjonspakken som helhet, og til enkeltfiler bare når en handling eller et avvik på filnivå må dokumenteres. Det viktigste er å ha et bevisst forhold til hva som dokumenteres, hvorfor, og på hvilket nivå.

Eventer bør utformes med tanke på framtidig forvaltning og bruk, slik at informasjonen er forståelig og etterprøvbar over tid.

## Les mer

- [Legge til bevaringseventer](/nb/docs/dps/how-to/add-preservation-events/): hvilke eventer du bør registrere for din arbeidsflyt, og hvordan du leverer dem.
- [Referanse for bevaringseventer](/nb/docs/dps/reference/preservation-events/): event-elementer, eventtyper og eksempler.
