---
title: Krav til metadata
weight: 1
---

I tillegg til kravet om en metadatafil i informasjonspakkene (SIP), krever Nasjonalbiblioteket at et sett med metadata også leveres via submission-API-et ved avlevering. Dette skal sikre at et minimum av metadata knyttet til de avleverte representasjonene blir indeksert og søkbare.

Metadatakravene våre bygger på Dublin Core, en internasjonal ISO-standard som er mye brukt innen arkiv, bibliotek og digitale samlinger. Dublin Core-standarden ble valgt fordi den er relativt enkel å forstå, lett å implementere, og er både fleksibel og utvidbar. Vi har supplert standarden med attributter for type, rolle og språk i enkelte felt for å gjøre metadataene mer strukturerte.

De fleste metadataelementene er valgfrie, men vi oppfordrer til å fylle dem ut så grundig som mulig. Dette gir bedre søkbarhet og forståelse av ressursene – også i et langtidsperspektiv.

For å gjøre de avleverte pakkene mest mulig selvforklarende i et bevaringsperspektiv, og for å sikre kontroll med filformater, skriver vi i tillegg metadataene til en XML-fil som legges ved arkivpakken (AIP). XML er velegnet for langtidsbevaring. Formatet er åpent, utbredt i bruk og et velkjent utvekslingsformat for metadata. For bevaring er det en fordel at formatet er tekstbasert og lesbart for både maskiner og mennesker. 
<br><br>
### Metadataelementer

| Navn         | **Type**                                                                     |
|:--------------|:------------------------------------------------------------------------------|
| Beskrivelse  | Type ressurs/medietype. NB bruker et eget vokabular for tillatte medietyper. |
| Krav         | MÅ                                                                           |
| Kardinalitet | 1..1                                                                         | 

**Retningslinjer for bruk:**

Tillatte typer for beskrive av ressursen: Bok, Avis, Tidsskrift, Bilde, Kart, Brev, Manuskript, Noter, Musikkmanuskript, Programrapporter, Plakater, Kort, Radio, Musikk, Fjernsyn og Film. 

Det vil være muligheter for å få lagt til medietyper ved behov.

**Eksempel:**
```
"type": "Bilde"
``` 
<br><br>
| Navn         | **Identifier**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Identifikatorer (type ID + ID/verdi). <br>Attributt `type` og `value` MÅ brukes for å definere type identifikator. |
| Krav         | MÅ                                                                                                                 |
| Kardinalitet | 1..n                                                                                                               |

**Retningslinjer for bruk:**

- Eksempler på identifikatorer kan være URN, PID, URI til post i en katalog/metadatasystem, dokID, hefteID, eksemplarnummer, ISBN, ISSN, ISMN, ISNI, DOI, plateetikett etc. 

- Det må defineres type identifikator. Bruk av type-attributt bør gi mening for avleverer, gjenspeile metadatakatalog/system, og bruken bør være konsekvent (standardisert skriveform). 

**Eksempel:**
```
"identifier": [
  {
    "type": "URN",
    "value": "URN:NBN:no-nb_digifoto_20220311_00191_NB_PE_VM_M_05_09_01_036"
  },
  {
    "type": "bilde-id",
    "value": "NB_PE_VM_M_05_09_01_036"
  },
  {
    "type": "hyllesignatur",
    "value": "POEL00003975"
  }
]
```