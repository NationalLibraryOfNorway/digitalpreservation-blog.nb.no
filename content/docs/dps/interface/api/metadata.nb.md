---
title: Krav til metadata
weight: 1
---

I tillegg til kravet om en metadatafil i informasjonspakkene (SIP), krever Nasjonalbiblioteket at et sett med metadata også leveres via submission-API-et ved avlevering. Dette skal sikre at et minimum av metadata knyttet til de avleverte representasjonene blir indeksert og søkbare.

Metadatakravene bygger på [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/), en internasjonal ISO-standard som er mye brukt innen arkiv, bibliotek og digitale samlinger. Dublin Core-standarden ble valgt fordi den er relativt enkel å forstå, lett å implementere, og er både fleksibel og utvidbar. Standarden er supplert med attributter i feltene for å gjøre metadataene mer strukturerte.

De fleste metadataelementene er valgfrie, men det oppfordres til å fylle dem ut så grundig som mulig. Dette gir bedre søkbarhet og forståelse av ressursene – også i et langtidsperspektiv.

For å gjøre de avleverte pakkene mest mulig selvforklarende i et bevaringsperspektiv, og for å sikre kontroll med filformater, skrives i tillegg metadataene til en XML-fil etter mottak og legges ved arkivpakken (AIP). XML er velegnet for langtidsbevaring. Formatet er åpent, utbredt i bruk og et velkjent utvekslingsformat for metadata. For bevaring er det en fordel at formatet er tekstbasert og lesbart for både maskiner og mennesker. 
<br><br>
### Generelle retningslinjer for bruk av standarder 
Tegnsetting for utfylling av felter følger [UTF-8](https://snl.no/UTF-8). <br>
[ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes.<br>
[ISO 8601-2](https://www.iso.org/obp/ui/en/#iso:std:iso:8601:-2:ed-1:v1:en) brukes som standard for angivelse av tid/dato.<br>
[ISO 3166-2](https://www.iso.org/obp/ui/en/#iso:std:iso:3166:-1:ed-4:v1:en) brukes for angivelse av land.
<br><br>
### Metadataelementer 
<br>
1. 

| Navn         | **Type**                                                                     |
|:--------------|:------------------------------------------------------------------------------|
| Beskrivelse  | Type ressurs/medietype. NB bruker et eget vokabular for tillatte medietyper.<br>Attributt `lang` BØR brukes for å definere språkkode. |
| Krav         | MÅ                                                                           |
| Kardinalitet | 1..1                                                                         | 

**Retningslinjer for bruk:**

- Tillatte typer for beskrive av ressursen: 

  **Tekst:** Bok, Avis, Tidsskrift, Artikkel, Småtrykk, Brev, Epost, Manuskript, Musikkmanuskript, Noter, Programrapport, Programstatistikk. 

  **Bilder:** Bilde, Kart, Plakat, Postkort, Referansemateriale. 

  **Lyd:** Lydbok, Musikk, Radio.

  **Levende bilder:** Film, Fjernsyn.

 
  Det vil være muligheter for å få lagt til medietyper ved behov.
- Språkkode bør angis. [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes.
  
**Eksempel:**
```json
{"type":"Bilde",
"lang": "nor"}
``` 
<br>
2. 

| Navn         | **Identifier**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Identifikatorer (type ID + ID/verdi). <br>Attributt `type` og `value` MÅ brukes for å definere type identifikator.<br>Attributt `lang` BØR brukes for å definere språkkode.
| Krav         | MÅ                                                                                                                 |
| Kardinalitet | 1..n                                                                                                               |

**Retningslinjer for bruk:**

- Eksempler på identifikatorer kan være URN, PID, URI til post i en katalog/metadatasystem, dokID, hefteID, eksemplarnummer, ISBN, ISSN, ISMN, ISNI, DOI, plateetikett etc. 

- Det må defineres type identifikator. Bruk av type-attributt bør gi mening for avleverer, gjenspeile metadatakatalog/system, og bruken bør være konsekvent (standardisert skriveform). 
- Språkkode bør angis. [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes.

**Eksempler:**
```json
{"identifier": [
  {
    "type": "URN",
    "value": "URN:NBN:no-nb_digifoto_20220311_00191_NB_PE_VM_M_05_09_01_036"
  },
  {
    "lang": "nor",
    "type": "bilde-id",
    "value": "NB_PE_VM_M_05_09_01_036"
  },
  {
    "lang": "nor",
    "type": "hyllesignatur",
    "value": "POEL00003975"
  }
]}
```
<br>
3. 

| Navn         | **Title**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Navn gitt til ressursen. Der tittel mangler er anbefalt praksis å gi ressursen en “meningsbærende” tittel. <br> Attributt `lang` BØR brukes for å definere språkkode. |
| Krav         | MÅ                                                                                                                 |
| Kardinalitet | 1..1                                                                                                               |

**Retningslinjer for bruk:**

- En del ressurser har allerede en forhåndsdefinert tittel, som bøker, tidsskrift, artikler, malte verk, kunstfoto osv. Der tittel mangler er anbefalt praksis å gi ressursen en “meningsbærende” tittel. Med meningsbærende menes noe som gir mening for gjenkjennelse og identifikasjon av ressursen (navn som gir mening for avleverer). 

- Språkkode bør angis. [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes. 

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
4. 

| Navn         | **Alternative**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Alternativ tittel (originaltittel, undertittel etc). <br>Attributt `type` MÅ brukes for å definere type tittel. <br> Attributt `lang` BØR brukes for å definere språkkode. |
| Krav         | BØR                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

- For å bedre muligheter for søk på tittel anbefales det å legge til alternativ tittel der tittelen inneholder tall og/eller spesialtegn, eller der tall opprinnelig er skrevet som tekst. 
  Eksempler:
  <br> `title`: 1-2-3 Matematikk = `alternative`: en to tre matematikk.
  <br> `title`: Kari & Bjarne på fisketur = `alternative`: Kari og Bjarne på fisketur. 
  <br> `title`: Tusen fjelltopper = `alternative`: 1000 fjelltopper.  

- Det kreves forklaring til hvilken type tittel som oppgis. Bruk av type-attributt bør gi mening for avleverer, gjenspeile metadatakatalog/system, og bruken bør være konsekvent (standardisert skriveform).

- Språkkode bør angis. [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes. 

**Eksempel:**
```json
{"alternative": [
  {
    "type": "originaltittel",
    "value": "Ola and Kari on fishing trip in Rondane",
    "lang": "eng"
  }
]}
```
<br>
5. 

| Navn         | **Creator**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Navn/korporasjon som opptrer i sentral rolle (forfatter, komponist, filmregissør, fotograf, ukjent etc.). <br>Attributt `role` BØR brukes for å definere rolle. <br>Attributt `type` BØR brukes for å angi type. Tillatte typer: *Person, Organization, Personal Name, Corporate Name, Meeting Name, Uniform Title*. <br>Attributt `authority` BØR brukes for å angi autoritet. <br>Attributt `lang` BØR brukes for å definere språkkode.  |
| Krav         | BØR                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

- Det anbefales bruk av autoritetsregister i de tilfeller dette finnes, både for personnavn og korporasjoner. Det må oppgis hvilket autoritetsregister som er benyttet. Et eksempel på autoritetsregister er [Felles autoritetsregister for personer og korporasjoner](https://bibliotekutvikling.no/kunnskapsorganisering/vokabularer-utkast/felles-autoritetsregister-for-personer-og-korporasjoner/).

- Creator identiseres i tillegg ved å skrives ut i sin fulle form (navn, etternavn/korporasjon). Fødselsår - dødsår kan legges til bak navnet i parentes. Eksempler: *Nesbø, Jo (1960-  ), Shakespeare, William (1564-1616)*. 

- Det bør oppgis om det er snakk om personnavn eller korporasjon. Dette er løst på ulike måter i ulike metadatakataloger og autoritetsregistre. Foreløpig er disse verdiene tillat for angivelse av navn/korporasjon (type), men det er mulig å få lagt til flere typer ved behov: *Person, Organization, Personal Name, Corporate Name, Meeting Name* (konferanse), *Uniform Title* (traktat, kontrakt).  

- Det bør oppgis hvilken rolle (role) navn/korporasjoner har. Eksempler på roller er: forfatter, komponist, filmregissør, fotograf, skaper etc. 

- Bruk av role-attributt bør gi mening for avleverer, gjenspeile metadatakatalog/system, og bruken bør være konsekvent (standardisert skriveform). 
- Språkkode bør angis. [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes.

**Eksempler:**
```json
{"creator": [
  {
    "lang": "nor",
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
    "lang": "nor",
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
6.  

| Navn         | **Contributor**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Navn som opptrer i sentral rolle (illustratør, fotograf, medforfatter). <br>Attributt `role` BØR brukes for å definere rolle. <br>Attributt `type` BØR brukes for å angi type autoritet. Tillatte typer: *Person, Organization, Personal Name, Corporate Name, Meeting Name, Uniform Title.* <br>Attributt `lang` BØR brukes for å definere språkkode.|
| Krav         | BØR                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

- Regler for utfylling av Contributor-feltet er de samme som Creator-feltet. Eksempler på roller for Contributor kan være: bidragsyter, avbildet, illustratør, modell, redaktør, designer etc.  
- Språkkode bør angis. [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes.


**Eksempler:**
```json
{"contributor": [
  {
    "role": "avbildet",
    "type": "Person",
    "name": "Nordmann, Ola",
    "lang": "nor"
  },
  {
    "role": "avbildet",
    "name": "Nordmann, Kari",
    "lang": "nor"
  }
]}
```
```json
{"contributor": [
  {
    "lang": "nor",
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
```
<br>
7.  

| Navn         | **Publisher**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Navn som opptrer i sentral rolle (Organisasjonen eller enheten som har publisert ressursen). <br> Attributt `type` BØR brukes for å definer type autoritet. Tillatte typer: *Person, Organization, Personal Name, Corporate Name, Meeting Name, Uniform Title.*<br>Attributt `lang` BØR brukes for å definere språkkode. |
| Krav         | BØR                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

- Det anbefales å bruke autoritetsregister hvis det finnes. Det må oppgis hvilket autoritetsregister som er benyttet, og hvilken type autoritet det er (type): *Person, Organization, Personal Name, Corporate Name, Meeting Name* (konferanse), *Uniform Title* (traktat, kontrakt). Ved bruk av autoritetsregister bør utgiver i tillegg skrives ut i sin fulle form. Sted og/eller år for utgivelse kan legges til i parantes bak navnet. Eksempel: Nasjonalbiblioteket (Oslo, 1984). 
  
- Språkkode bør angis. [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes.

**Eksempel:**
```json
{"publisher": [
  {
    "lang": "nor",
    "name": "Nasjonalbiblioteket (Oslo, 1984)",
    "type": "Organization",
    "authority": {
      "source": "Felles autoritetsregister (BARE)",
      "code": "90362181",
      "uri": "https://bibsys-almaprimo.hosted.exlibrisgroup.com/permalink/f/nelpa2/AUTREG90362181"
    }
  }
]}
```
<br>
8.  

| Navn         | **Spatial**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Relevante stedsnavn for ressursen. Kan referere til geografiske steder som land, regioner og byer som har betydning for ressursen. <br> Det BØR angis `type` for hvilket sted som oppgis.<br>Attributt `lang` BØR brukes for å definere språkkode.  |
| Krav         | BØR                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

- Bruk [ISO 3166-2](https://www.iso.org/obp/ui/en/#iso:std:iso:3166:-1:ed-4:v1:en) for angivelse av land. Landekoder skrives bak landet i parentes (NO). 

- Vi anbefaler bruk av stedsnavstjenester/registre for angivelse av norske stedsnavn. Et eksempel er [Sentralt stedsnavnregister](https://www.kartverket.no/api-og-data/stedsnavndata) (SSR) fra kartverket. Det må oppgis hvilket register som er benyttet.  

- Ved bruk av autoritetsregistre for å angi Spatial, bør man skrive plassering/navn i sin fulle form i tillegg. Brukes ikke register, skrives plassering/navn fortrinnsvis land;region/fylke;kommune;sted;gate;. 

- Det er mulig å oppgi koordinater i form av lengde- og breddegrader. Det skal brukes på denne måten: `latitude`=61.85401 `longitude`=9.80856

- Eksempler på `type` sted kan være utgiversted, innspillingssted, handlingssted, trykkested, fødested osv. Bruk av type-attributt her bør gi mening for avleverer, gjenspeile metadatakatalog/system, og bruken bør være konsekvent (standardisert skriveform).  

- Språkkode bør angis. [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes.

**Eksempel:**
```json
{"spatial": [
  { 
    "lang": "nor",
    "name": "Norge (NO);Innlandet;Stor-Elvdal;Rondane gjestegård",
    "type": "Avbildet sted",
    "authority": {
      "source": "Kulturnav",
      "code": "1031636c-0717-4d12-8895-fb88a7d4e952",
      "uri": "http://kulturnav.org/1031636c-0717-4d12-8895-fb88a7d4e952"
    },    
    "coordinateReferenceSystem": "EPSG:4326",
    "latitude": 61.788453,
    "longitude": 10.224725
  },
  { 
    "name": "Norge (NO);Innlandet;Lillehammer;Lillehammer"
  }  
]}
```
<br>
9.  

| Navn         | **Date**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Relevante datoer for ressursen (utgivelse, copyright, opprettelse/digitaliseringsdato etc., type årstall + årstall/verdi).  <br> Attributt `type` MÅ brukes for å definere type dato.<br>Attributt `lang` BØR brukes for å definere språkkode.   |
| Krav         | BØR                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

- Det må angis type årstall + årstall/verdi. [ISO 8601-2](https://www.iso.org/obp/ui/en/#iso:std:iso:8601:-2:ed-1:v1:en) brukes som standard.  

- Bruke av type-attributt bør gi mening for avleverer, gjenspeile metadatakatalog/system, og bruken bør være konsekvent (standardisert skriveform). 

- Språkkode bør angis. [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes.

**Eksempler:**
```json
{"date": [
  {
    "type": "motivdato",
    "value": "1938",
    "lang": "nor"
  },
  {
    "type": "digitalisert",
    "value": "2022-03-05T14:28:12+02:00",
    "lang": "nor"
  },
  {
    "type": "publisert",
    "value": "2022-03-12",
    "lang": "nor"
  }
]}
```
<br>
10.   

| Navn         | **Language**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Språk som er relevant for ressursen. <br> Attributt `lang` MÅ brukes for å definere språkkode. <br> Attributt `type` MÅ brukes for å definere hva språket representerer (undertekster, talespråk, skriftspråk etc.).   |
| Krav         | BØR                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

- [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes.

- Det må angis type for hva språket representerer. Eksempler på type som språket representerer kan være undertekster, talespråk, skriftspråk etc.  

- Bruk av type-attributt bør gi mening for avleverer, gjenspeile metadatakatalog/system, og bruken bør være konsekvent (standardisert skriveform). 

**Eksempler:**
```json
{"language": [
  {
    "type": "undertekster",
    "value": "engelsk",
    "lang": "nor"
  }
]}
```
```json
{"language": [
  {
    "type": "skriftspråk",
    "value": "fransk",
    "lang": "nor"
  }
]}
```
<br>
11.  

| Navn         | **Relation**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | En relatert ressurs der den beskrevne ressursen er fysisk eller logisk inkludert (tittel på overordnet verk, samling, serie, del).<br>Det MÅ brukes attributter for `title` + `type` ELLER `id` + `type`.<br>Attributt `URI` BØR brukes. <br> Attributt `lang` BØR brukes for å definere språkkode.   |
| Krav         | BØR                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

- Bruk av attributter kan varieres, men det kreves alltid bruk av `type` OG enten `title` eller `id`.

- Attributt `title` angir tittel på relatert ressurs. 

- Attributt `type` angir hvilken type relasjon det er mellom ressurser. Bruk av termer fra Dublin Core anbefales (conformsTo, hasFormat, hasPart, hasVersion, isFormatOf, isPartOf, isReferencedBy, isReplacedBy, isRequiredBy, isVersionOf, references, replaces, requires). 
Hvis andre termer brukes bør de gi mening for avleverer, gjenspeile metadatakatalog/system, og bruken bør være konsekvent (standardisert skriveform).

- Eksempel på bruk av attributt `id` er henvisning til en seriepost, verkspost, eller andre ressurser i samme i serie/verk.

- Attributt `URI` brukes for å angi lenke til relatert ressurs (katalogpost, nettside).  

- Språkkode bør angis (lang-attributt). [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes.

**Eksempler:**
```json
{"relation": [
  {
    "title": "Norge på langs med Ola og Kari",
    "type": "IsPartOf",
    "id": "987654321",
    "URI": "https://www.nb.no/items/eb57e3c314894b0120cf631104065e74?page",
    "lang": "nor"
  }
]}
```
```json
{"relation": [
  {
    "title": "Chronicles of Narnia",
    "type": "IsPartOf",
    "lang": "eng"
  }
]}
```
```json
{"relation": [
  {
    "title": "20161203.jpg",
    "type": "hasPart",
    "URI": "https://www.nb.no/items/83af9a36b005c5737aa33d1fb64f429d?page"
  }
]}
```

<br>
12.   

| Navn         | **Provenance**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Informasjon om eventuelle endringer som har betydning for ressursens autentisitet, integritet og tolkning (eierskap, forvaltning etc). <br> Attributt `lang` BØR brukes for å definere språkkode.   |
| Krav         | BØR                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

- Språkkode bør angis (lang-attributt). [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes.

**Eksempel:**
```json
{"provenance": [
  {
    "value": "Samlingen ble donert til Nasjonalbiblioteket av Václav Marek 1979-05-12",
    "lang": "nor"
  }
]}
```
<br>
13.  

| Navn         | **Subject**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Emneord knyttet til ressursen. <br> Attributt `lang` BØR brukes for å definere språkkode.   |
| Krav         | KAN                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

- Feltet brukes for å beskrive hva ressursen inneholder/handler om. Eksempler på dette er ord eller uttrykk som forteller noe om emne, tema, hendelser, landemerker, bygninger eller tidsperioder som har betydning for ressursen. 

- Desimalklassifikasjon er også gyldige verdier.

- Det kan brukes henvisning til autoritetsregistre der det er relevant. Der det brukes autoritetsregister må emneord skrives i sin fulle form i tillegg.

- Språkkode bør angis (lang-attributt). [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes.

**Eksempler:**
```json
{"subject": [
  {
    "lang": "nor",
    "value": "rondane"
  },
  {
    "lang": "nor",
    "value": "fisketur"
  },
  {
    "lang": "nor",
    "value": "natur"
  }
]}
```

```json
{"subject": [
  { 
    "lang": "nor",
    "value": "natur",
    "authority": {
      "source": "Kulturnav",
      "code": "1031536c-0717-4d12-8895-fb88a7d4e952",
      "uri": "http://kulturnav.org/1031636c-0717-4d32-8895-fb88a7d4e952"
    }
  }
]}
```

<br>
14.   

| Navn         | **Description**                                                                                                     |
|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| Beskrivelse  | Beskrivelse av ressursen. Beskrivelsen kan inkludere, men er ikke begrenset til: et sammendrag, en innholdsfortegnelse, en grafisk representasjon eller en fritekst om ressursen.  <br> Attributt `lang` BØR brukes for å definere språkkode.   |
| Krav         | KAN                                                                                                                 |
| Kardinalitet | 0..n                                                                                                               |

**Retningslinjer for bruk:**

- Beskrivelsen kan inkludere, men er ikke begrenset til: et sammendrag, en innholdsfortegnelse, en grafisk representasjon eller en fritekst om ressursen. 

- Språkkode bør angis (lang-attributt). [ISO 639-2](https://www.iso.org/obp/ui/#iso:std:iso:639:-2:ed-1:v1:en) brukes som standard for å angi språk når attributt `lang` brukes.

**Eksempel:**
```json
{"description": [
  {
    "value": "Bildet er en del av samlingen etter Václav Marek, der han fulgte Ola og Kari Nordmann Norge på langs. Václav Marek var en engelskmann som var interessert i Norge og norsk natur.",
    "lang": "nor"
  }
]}
```
<br> **Eksempel som inneholder alle metadataelementene:**

```json
{
  "objectId": "av_6e8bc430-9c3a11d9",
  "priority": 50,
  "metadata": {
    "type": "Bilde",
    "lang": "nor"
    }
    "identifier": [
      {
        "type": "URN",
        "value": "URN:NBN:no-nb_digifoto_20220311_00191_NB_PE_VM_M_05_09_01_036"
      },
      {
        "type": "bilde-id",
        "value": "NB_PE_VM_M_05_09_01_036",
        "lang": "nor"
      },
      {
        "type": "hyllesignatur",
        "value": "POEL00003975",
        "lang": "nor"
      }
    ],
    "title": {
      "value": "Ola og Kari på fisketur i Rondane",
      "lang": "nor"
    },
    "alternative": [
      {
        "type": "originaltittel",
        "value": "Ola and Kari on fishing trip in Rondane",
        "lang": "eng"
      }
    ],
    "creator": [
      {
        "lang": "nor",
        "name": "Marek, Václav",
        "type": "Person",
        "role": "fotograf",
        "authority": {
          "source": "Felles autoritetsregister (BARE)",
          "code": "90362181",
          "uri": "https://bibsys-almaprimo.hosted.exlibrisgroup.com/permalink/f/nelpa2/AUTREG90362181"
        }
      }
    ],
    "contributor": [
      {
        "role": "avbildet",
        "type": "Person",
        "name": "Nordmann, Ola",
        "lang": "nor"
      },
      {
        "lang": "nor",
        "role": "avbildet",
        "type": "Person",
        "name": "Solberg, Erna",
        "authority": {
          "source": "Kulturnav",
          "code": "e762d909-5cce-4d2b-892b-258272514fde",
          "uri": "https://kulturnav.org/e762d909-5cce-4d2b-892b-258272514fde"
        }
      }
    ],
    "publisher": [
      {
        "lang": "nor",
        "name": "Nasjonalbiblioteket",
        "type": "Organization",
        "authority": {
          "source": "Felles autoritetsregister (BARE)",
          "code": "90362181",
          "uri": "https://bibsys-almaprimo.hosted.exlibrisgroup.com/permalink/f/nelpa2/AUTREG90362181"
        }
      }
    ],
    "spatial": [
      { 
        "lang": "nor",
        "name": "Norge (NO);Innlandet;Stor-Elvdal;Rondane gjestegård",
        "type": "Avbildet sted",
        "authority": {
          "source": "Kulturnav",
          "code": "1031636c-0717-4d12-8895-fb88a7d4e952",
          "uri": "http://kulturnav.org/1031636c-0717-4d12-8895-fb88a7d4e952"
        },    
        "coordinateReferenceSystem": "EPSG:4326",
        "latitude": 61.788453,
        "longitude": 10.224725
      },
      { 
        "name": "Norge (NO);Innlandet;Lillehammer;Lillehammer"
      }  
    ],
    "date": [
      {
        "type": "motivdato",
        "value": "1938", 
        "lang": "nor"
      },
      {
        "type": "digitalisert",
        "value": "2022-03-05T14:28:12+02:00",
        "lang": "nor"
      },
      {
        "type": "publisert",
        "value": "2022-03-12",
        "lang": "nor"
      }
    ],
    "language": [
      {
        "type": "undertekster",
        "value": "engelsk",
        "lang": "nor"
      }
    ],
    "relation": [
     {
    "title": "Norge på langs med Ola og Kari",
    "type": "IsPartOf",
    "id": "987654321",
    "URI": "https://www.nb.no/items/eb57e3c314894b0120cf631104065e74?page",
    "lang": "nor"
  }
    ],
    "provenance": [
      {
        "value": "Samlingen ble donert til Nasjonalbiblioteket av Václav Marek 1979-05-12",
        "lang": "nor"
      }
    ],
    "subject": [
      {
        "lang": "nor",
        "value": "rondane"
      },
      {
        "lang": "nor",
        "value": "fisketur"
      },
    { 
    "lang": "nor",
    "value": "natur",
    "authority": {
      "source": "Kulturnav",
      "code": "1031536c-0717-4d12-8895-fb88a7d4e952",
      "uri": "http://kulturnav.org/1031636c-0717-4d32-8895-fb88a7d4e952"
    }
  }
    ],
    "description": [
      {
        "value": "Bildet er en del av samlingen etter Václav Marek, der han fulgte Ola og Kari Nordmann Norge på langs. Václav Marek var en engelskmann som var interessert i Norge og norsk natur.",
        "lang": "nor"
      }
    ]
  }
```
