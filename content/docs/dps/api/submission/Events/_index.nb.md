---
title: Eventer/bevaringsmetadata
weight: 2
draft: false
---

> ⚠️ **Disse sidene er under arbeid** ⚠️



I digital bevaring dokumenterer en “event” en handling eller hendelse som har påvirket et digitalt objekt, for eksempel opprettelse, migrering, validering eller overføring. Dette anses som viktig bevaringsmetadata og gir sporbarhet og bevis for hva som er gjort med objektet gjennom hele livssyklusen. 

Avlevering av eventer er ikke et krav, men vi anbefaler at det opprettes hvis man har slik informasjon tilgjengelig. Eventer som legges til i APIet vil bevares i egen event-database, på lik linje med hendelser som skjer på innsiden av bevaringsomgivelsene (DPS). Ved utlevering gir det enklere oversikt over hendelser knyttet til et objekt. Hvis det er ønskelig å legge til andre typer bevaringsmetadata, er det er også mulig å avlevere bevaringsmetadata i informasjonspakken (SIP). Se mer om det under  [metadataveiledning](/nb/docs/dps/sip/1.0/metadata/) og [krav til pakkestruktur](/nb/docs/dps/sip/1.0/structure-requirements/). Informasjon som går direkte på proveniens kan legges til i [krav til metadata](/nb/docs/dps/api/submission/metadata/).

Eventer kan være knyttet til hele informasjonspakken eller til enkelte filer. Generelt bør eventer knyttes til pakkenivå, Intellektuell entitet (IE), der det er mulig. Dette for å unngå store mengder eventer som i utgangspunktet sier det samme. Det er åpent for å legge eventer på filer der det er behov for å dokumentere hendelser på enkeltfiler. Det viktigste er at man har et bevisst forhold til hva som dokumenteres, hvorfor det dokumenteres, og på hvilket nivå. 

Teknisk dokumentasjon for avlevering i API finnes her: [Swagger DPS Submission Service API](https://digitalpreservation.no/swagger/)

Her finnes forklaring til bruk av de ulike elementene en event er bygd opp av, og til de ulike event-typene: 

{{< cards >}}
  {{< card link="event_elements" title="Bruk av event-elementer" icon="document-text" >}} 
  {{< card link="event_type" title="Event-typer" icon="document-text" >}}
{{< /cards >}}