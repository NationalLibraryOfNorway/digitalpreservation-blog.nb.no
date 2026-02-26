---
title: Bruk av event-elementer
weight: 2
draft: false
---

For formatering av eventer, se teknisk dokumentasjon her: [Swagger DPS Submission Service API](https://digitalpreservation.no/swagger/).

**Tillatte elementer er:** 

Agent:*
- agentName*
- agentType*
- agentVersion
- agentNotes

Event:*
- eventDateTime*
- eventType*
- eventDetail
- outcome*
- outcomeDetail

Elementer merket med * er påkrevde. 
<br><br>

# Forklaring til bruk av event-elementer:

## Agent: 
Agent beskriver den aktøren som utførte handlingen. Dette kan være programvare, en organisasjon eller en person.

### AgentName
Navn på aktøren som utførte handlingen. Navnet skal være entydig og konsekvent brukt.

**Eksempler:**
- "Apache NiFi"
- "Nasjonalbiblioteket – Team digital bevaring"
- "Ola Nordmann"
- "JHOVE"


### AgentType
Angir hvilken type aktør som utførte handlingen.

**Tillatte verdier:**
- "software"
- "organization"
- "person"


### AgentVersion
Versjonsnummer på agenten dersom det er programvare. Agentversjon brukes for å sikre sporbarhet og mulighet for reproduksjon, ulike versjoner av samme verktøy kan gi ulike resultater. 

**Eksempler:**
- "1.15.0"
- "3.2"
- "1.11.0; DROID_SignatureFile_V116.xml; container-signature-20231127.xml"



### AgentNotes
Tilleggsinformasjon om agenten som utførte handlingen. Elementet skal dokumentere egenskaper, kontekst eller oppsett av agenten, ikke hva agenten gjorde i et spesifikt event. 

**Dette kan inkludere:**
- Hva agenten er, og hva den gjør generelt
- Hvordan agenten er konfigurert eller installert
- Operativ kontekst eller ansvar
  
**Eksempler:**
- "Siegfried is a file format identification tool using PRONOM signatures. Installed with signature set v95 for PDF, TIFF, JPEG, and XML formats."
- "Apache NiFi is a dataflow automation tool that enables the design and management of complex data pipelines. "
- "JHOVE custom installation with PDF, TIFF and JPEG modules enabled. Running under Java 17 runtime environment."
- "Institution with formal responsibility for digital preservation, ingest, and long-term management of archival materials."

> [!NOTE]
> Bruk AgentNotes så konsekvent som mulig for samme agent. Ved skriveforskjeller i AgentNotes opprettes ny Agent i registeret.


## Event:
Event beskriver selve handlingen som ble utført på objektet.

### EventDateTime
Tidspunktet hendelsen fant sted. Skal angis etter ISO 8601-standarden, med tidssone.

**Eksempel:**
- "2026-02-23T10:45:00+01:00 "


### EventType
Angir hvilken type handling som ble utført. Elementet beskriver hva slags prosess hendelsen representerer.
Verdien skal være en kontrollert og konsekvent brukt betegnelse – [liste med tillatte typer](/nb/docs/dps/api/submission/events/eventType/).


### EventDetail
En presis beskrivelse av hva som ble gjort i hendelsen. Dette utdyper EventType og beskriver selve operasjonen.

**Eksempler:**
- "MD5 checksum generated"
- "Migrated from TIFF to JPEG2000"
- "Validated against PDF/A-2b standard"



### Outcome
Overordnet resultat av hendelsen. Dette elementet angir om hendelsen ble gjennomført som forventet, mislyktes eller ble fullført med avvik.

**Tillatte verdier:**
- "success"
- "failure"
- "warning"


### OutcomeDetail
En konkret og presis beskrivelse av resultatet av hendelsen.
Dette elementet skal dokumentere hva som faktisk ble oppnådd eller hvilke avvik som ble identifisert. Beskrivelsen skal være kortfattet og forståelig. Det er ikke alle hendelser som er nødvendig å dokumentere utover success/failure/warning, da holder det å bruke «outcome»-elementet. 

**Eksempler:**
- "Identified as fmt/353 (TIFF 6.0)."
- "Validated against profile E-ARK-SIP-v2-2-0, NB-SIP-STRUCTURE-1.0 and NB-SIP-MOVINGIMAGES-PROFILE-1.0."






