---
title: Krav til metadata
weight: 1
---

I tillegg til kravet om en metadatafil i informasjonspakkene (SIP), krever Nasjonalbiblioteket at et sett med metadata også leveres via submission-API-et ved avlevering. Dette skal sikre at et minimum av metadata knyttet til de avleverte representasjonene blir indeksert og søkbare.

Metadatakravene våre bygger på [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/), en internasjonal ISO-standard som er mye brukt innen arkiv, bibliotek og digitale samlinger. Dublin Core-standarden ble valgt fordi den er relativt enkel å forstå, lett å implementere, og er både fleksibel og utvidbar. Vi har supplert standarden med attributter for type, rolle og språk i enkelte felt for å gjøre metadataene mer strukturerte.

De fleste metadataelementene er valgfrie, men vi oppfordrer til å fylle dem ut så grundig som mulig. Dette gir bedre søkbarhet og forståelse av ressursene – også i et langtidsperspektiv.

For å gjøre de avleverte pakkene mest mulig selvforklarende i et bevaringsperspektiv, og for å sikre kontroll med filformater, skriver vi i tillegg metadataene til en XML-fil som legges ved arkivpakken (AIP). XML er velegnet for langtidsbevaring. Formatet er åpent, utbredt i bruk og et velkjent utvekslingsformat for metadata. For bevaring er det en fordel at formatet er tekstbasert og lesbart for både maskiner og mennesker. 
<br><br>
### Generelle retningslinjer for bruk av standarder <br>
Tegnsetting for utfylling av felter følger [UTF-8](https://snl.no/UTF-8). <br>
[ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt lang brukes.<br>
[ISO 8601-2](https://www.iso.org/obp/ui/en/#iso:std:iso:8601:-2:ed-1:v1:en) brukes som standard for angivelse av tid/dato.<br>
[ISO 3166-2](https://www.iso.org/obp/ui/en/#iso:std:iso:3166:-1:ed-4:v1:en) brukes for angivelse av land.
<br><br>
### Metadataelementer <br><br>

1
| Navn         | **Type**                                                                     |
|:--------------|:------------------------------------------------------------------------------|
| Beskrivelse  | Type ressurs/medietype. NB bruker et eget vokabular for tillatte medietyper. |
| Krav         | MÅ                                                                           |
| Kardinalitet | 1..1                                                                         | 

**Retningslinjer for bruk:**

Tillatte typer for beskrive av ressursen: Bok, Avis, Tidsskrift, Bilde, Kart, Brev, Manuskript, Noter, Musikkmanuskript, Programrapporter, Plakater, Kort, Radio, Musikk, Fjernsyn og Film. 

Det vil være muligheter for å få lagt til medietyper ved behov.

**Eksempel:**
```json
"type": "Bilde"
``` 
<br><br>
2
| Navn         | **Identifier**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Identifikatorer (type ID + ID/verdi). <br>Attributt `type` og `value` MÅ brukes for å definere type identifikator. |
| Krav         | MÅ                                                                                                                 |
| Kardinalitet | 1..n                                                                                                               |

**Retningslinjer for bruk:**

- Eksempler på identifikatorer kan være URN, PID, URI til post i en katalog/metadatasystem, dokID, hefteID, eksemplarnummer, ISBN, ISSN, ISMN, ISNI, DOI, plateetikett etc. 

- Det må defineres type identifikator. Bruk av type-attributt bør gi mening for avleverer, gjenspeile metadatakatalog/system, og bruken bør være konsekvent (standardisert skriveform). 

**Eksempel:**
```json
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