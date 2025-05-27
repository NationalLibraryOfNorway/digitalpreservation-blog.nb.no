---
title: Krav til metadata
weight: 1
---

I tillegg til kravet om en metadatafil i informasjonspakkene (SIP), krever Nasjonalbiblioteket at et sett med metadata også leveres via submission-API-et ved avlevering. Dette skal sikre at et minimum av metadata knyttet til de avleverte representasjonene blir indeksert og søkbare.

Metadatakravene våre bygger på [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/), en internasjonal ISO-standard som er mye brukt innen arkiv, bibliotek og digitale samlinger. Dublin Core-standarden ble valgt fordi den er relativt enkel å forstå, lett å implementere, og er både fleksibel og utvidbar. Vi har supplert standarden med attributter for type, rolle og språk i enkelte felt for å gjøre metadataene mer strukturerte.

De fleste metadataelementene er valgfrie, men vi oppfordrer til å fylle dem ut så grundig som mulig. Dette gir bedre søkbarhet og forståelse av ressursene – også i et langtidsperspektiv.

For å gjøre de avleverte pakkene mest mulig selvforklarende i et bevaringsperspektiv, og for å sikre kontroll med filformater, skriver vi i tillegg metadataene til en XML-fil som legges ved arkivpakken (AIP). XML er velegnet for langtidsbevaring. Formatet er åpent, utbredt i bruk og et velkjent utvekslingsformat for metadata. For bevaring er det en fordel at formatet er tekstbasert og lesbart for både maskiner og mennesker. 
<br><br>
### Generelle retningslinjer for bruk av standarder 
Tegnsetting for utfylling av felter følger [UTF-8](https://snl.no/UTF-8). <br>
[ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt lang brukes.<br>
[ISO 8601-2](https://www.iso.org/obp/ui/en/#iso:std:iso:8601:-2:ed-1:v1:en) brukes som standard for angivelse av tid/dato.<br>
[ISO 3166-2](https://www.iso.org/obp/ui/en/#iso:std:iso:3166:-1:ed-4:v1:en) brukes for angivelse av land.
<br><br>
### Metadataelementer 
<br>
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
{"type":"Bilde"}
``` 
<br>
2

| Navn         | **Identifier**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Identifikatorer (type ID + ID/verdi). <br>Attributt `type` og `value` MÅ brukes for å definere type identifikator. |
| Krav         | MÅ                                                                                                                 |
| Kardinalitet | 1..n                                                                                                               |

**Retningslinjer for bruk:**

- Eksempler på identifikatorer kan være URN, PID, URI til post i en katalog/metadatasystem, dokID, hefteID, eksemplarnummer, ISBN, ISSN, ISMN, ISNI, DOI, plateetikett etc. 

- Det må defineres type identifikator. Bruk av type-attributt bør gi mening for avleverer, gjenspeile metadatakatalog/system, og bruken bør være konsekvent (standardisert skriveform). 

**Eksempler:**
```json
{"identifier": [
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
]}
```
<br>
3

| Navn         | **Title**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Navn gitt til ressursen. Der tittel mangler er anbefalt praksis å gi ressursen en “meningsbærende” tittel. <br> Attributt `lang` BØR brukes for å definere språkkode. |
| Krav         | MÅ                                                                                                                 |
| Kardinalitet | 1..1                                                                                                               |

**Retningslinjer for bruk:**

- En del ressurser har allerede en forhåndsdefinert tittel, som bøker, tidsskrift, artikler, malte verk, kunstfoto osv. Der tittel mangler er anbefalt praksis å gi ressursen en “meningsbærende” tittel. Med meningsbærende menes noe som gir mening for gjenkjennelse og identifikasjon av ressursen (navn som gir mening for avleverer). 

- Språkkode må angis for titler oppgitt på andre språk enn norsk (lang-attributt). [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes. 

**Eksempler:**
```json
{"title": {
  "value": "Ola og Kari på fisketur i Rondane",
  "lang": "nor"
}}
```
```json
{"title": {
  "value": "Negativopptak fra juni 1972 [bilde 394]",
  "lang": "nor"
}}
```
```json
{"title": {
  "value": "20131007.jpg"
}}
```
<br>
4

| Navn         | **Alternative**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Alternativ tittel (originaltittel, undertittel etc). <br>Attributt `type` MÅ brukes for å definere type tittel. <br> Attributt `lang` MÅ brukes for å definere språkkode. |
| Krav         | BØR                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

- For å bedre muligheter for søk på tittel anbefales det å legge til alternativ tittel der tittelen inneholder tall og/eller spesialtegn, eller der tall opprinnelig er skrevet som tekst. 
  Eksempler:
  `title`: 1-2-3 Matematikk = `alternative`: en to tre matematikk.
  `title`: Kari & Bjarne på fisketur = `alternative`: Kari og Bjarne på fisketur. 
  `title`: Tusen fjelltopper = `alternative`: 1000 fjelltopper.  

- Det kreves forklaring til hvilken type tittel som oppgis. Bruk av type-attributt bør gi mening for avleverer, gjenspeile metadatakatalog/system, og bruken bør være konsekvent (standardisert skriveform).

- Bruk av lang-attributt. [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt lang brukes. 

**Eksempler:**
```json
{"alternative": [
  {
    "type": "original tittel",
    "value": "Ola and Kari on fishing trip in Rondane",
    "lang": "eng"
  }
]}
```
<br>
5

| Navn         | **Creator**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Navn/korporasjon som opptrer i sentral rolle (forfatter, komponist, filmregissør, fotograf, ukjent etc.). <br>Attributt `role` BØR brukes for å definere rolle. <br>Attributt `type` BØR brukes for å angi type. Tillatte typer: *Person, Organization, Personal Name, Corporate Name, Meeting Name, Uniform Title*. <br>Attributt `authority` BØR brukes for å angi autoritet. |
| Krav         | BØR                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

- Det anbefales bruk av autoritetsregister i de tilfeller dette finnes, både for personnavn og korporasjoner. Det må oppgis hvilket autoritetsregister som er benyttet. Et eksempel på autoritetsregister er [Felles autoritetsregister for personer og korporasjoner](https://bibliotekutvikling.no/kunnskapsorganisering/vokabularer-utkast/felles-autoritetsregister-for-personer-og-korporasjoner/).

- Creator identiseres i tillegg ved å skrives ut i sin fulle form (navn, etternavn/korporasjon). Fødselsår - dødsår kan legges til bak navnet i parentes. Eksempler: *Nesbø, Jo (1960-  ), Shakespeare, William (1564-1616)*. 

- Det bør oppgis om det er snakk om personnavn eller korporasjon. Dette er løst på ulike måter i ulike metadatakataloger og autoritetsregistre. Foreløpig er disse verdiene tillat for angivelse av navn/korporasjon (type), men det er mulig å få lagt til flere typer ved behov: *Person, Organization, Personal Name, Corporate Name, Meeting Name* (konferanse), *Uniform Title* (traktat, kontrakt).  

- Det bør oppgis hvilken rolle (role) navn/korporasjoner har. Eksempler på roller er: forfatter, komponist, filmregissør, fotograf, skaper etc. 

- Bruk av role-attributt bør gi mening for avleverer, gjenspeile metadatakatalog/system, og bruken bør være konsekvent (standardisert skriveform). 

**Eksempler:**
```json
{"creator": [
  {
    "name": "Marek, Václav (1908-1994)",
    "type": "Person",
    "role": "fotograf",
    "authority": {
      "source": "Felles autoritetsregister (BARE)",
      "code": "90169632",
      "uri": "https://bibsys-almaprimo.hosted.exlibrisgroup.com/permalink/f/nelpa2/AUTREG90169632"
    }
  }
]}
```
```json
{"creator": [
  {
    "name": "Shakespeare, William (1564-1616)",
    "type": "Person",
    "role": "forfatter",
    "authority": {
      "source": "Felles autoritetsregister (BARE)",
      "code": "9016555",
      "uri": "https://bibsys-almaprimo.hosted.exlibrisgroup.com/permalink/f/nelpa2/AUTREG9016555"
    }
  }
]}
```
<br>
6 

| Navn         | **Contributor**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Navn som opptrer i sentral rolle (illustratør, fotograf, medforfatter). <br>Attributt `role` BØR brukes for å definere rolle. <br>Attributt `type` BØR brukes for å angi type autoritet. Tillatte typer: *Person, Organization, Personal Name, Corporate Name, Meeting Name, Uniform Title.* |
| Krav         | BØR                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

Regler for utfylling av Contributor-feltet er de samme som Creator-feltet. Eksempler på roller for Contributor kan være: bidragsyter, avbildet, illustratør, modell, redaktør, designer etc.  

**Eksempler:**
```json
{"contributor": [
  {
    "role": "avbildet",
    "type": "Person",
    "name": "Nordmann, Ola"
  },
  {
    "role": "avbildet",
    "name": "Nordmann, Kari"
  }
]}
```
```json
{"contributor": [
  {
    "role": "illustratør",
    "type": "Person",
    "name": "Solberg, Erna",
    "authority": {
      "source": "Kulturnav",
      "code": "e762d909-5cce-4d2b-892b-258272514fde",
      "uri": "https://kulturnav.org/e762d909-5cce-4d2b-892b-258272514fde"
    }
  }
]}