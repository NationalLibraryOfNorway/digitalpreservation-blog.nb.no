---
title: Krav for datasett
draft: true
weight: 5
---

#### Krav til METS.xml utover generelle SIP-krav
Dette er en liste over krav til METS.xml for pakker med datasett og databaser som leveres til Nasjonalbiblioteket. Dette er krav utover det som er definert i [Krav til METS.xml](/nb/docs/dps/sip/mets/). <br><br>

> [!NOTE]
> E-ARK har egne Content Information Type-spesifikasjoner for [relasjonsdatabaser med SIARD (CITS SIARD)](https://dilcis.eu/content-types/cs-siard) og [geodata (CITS Geospatial)](https://dilcis.eu/content-types/cs-geospatial-data). Nasjonalbiblioteket har ennå ikke full oversikt over hvorvidt disse spesifikasjonene er forenlige med våre øvrige SIP-krav. Ønsker du å avlevere geodata eller SIARD-strukturert data, ta kontakt med teamet for digital bevaring før leveranse.

| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:---|:---|:---|
| **NBDATASETSIP1** | **Content Category**<br>`mets/@TYPE`<br><br>Attributtet `mets/@TYPE` **MÅ** brukes til å angi kategorien til innholdet i pakken, f.eks. "Datasets", "Websites", "Mixes" , "Other", etc. Gyldige verdier er definert i et fastsatt vokabular. Vokabularet vil oppdateres av DILCIS-styret etter hvert som tilleggsspesifikasjoner for innholdsinformasjon legges til.<br><br>For datasett og databaser **MÅ** `mets/@TYPE` være én av følgende verdier:<br>`Datasets` : Brukes for data kodet i en definert struktur, f.eks. datadumper og dataeksporter i formater som CSV, JSON, XML eller Parquet. <br>`Databases` : Brukes for et komplett sett av innholdet i en database, f.eks. databasedumper eller eksporter.<br><br>Se vokabular her [E-ARK-CSIP-Content Category](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentCategory.xml). <br><br>Dette er en spesifisering av [CSIP2](https://earkcsip.dilcis.eu/#CSIP2). | **MÅ** | **1..1** |
| **NBDATASETSIP2** | **Content Information Type Specification**<br>`mets/@csip:CONTENTINFORMATIONTYPE`<br><br>Brukes til å definere spesifikasjoner for type innholdsinformasjon som ble brukt når pakken ble opprettet. Gyldige verdier er definert i et fastsatt vokabular. Attributten er obligatorisk for METS-dokumenter på representasjonsnivå. Vokabularet vil oppdateres av DILCIS-styret etter hvert som tilleggsspesifikasjoner for innholdsinformasjon legges til.<br><br>For datasett og databaser brukes `OTHER` (en annen term enn det som finnes i det brukte vokabularet).<br><br>Se vokabular her [E-ARK-CSIP-Content Information Type](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentInformationType.xml).<br> <br>Dette er en spesifisering av [CSIP4](https://earkcsip.dilcis.eu/#CSIP4). | **MÅ** | **1..1** |
| **NBDATASETSIP3** | **Other Content Information Type Specification**<br>`mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE`<br> <br>Når `mets/@csip:CONTENTINFORMATIONTYPE` har verdien `OTHER`, **MÅ** `mets/@csip:OTHERCONTENTINFORMATIONTYPE` oppgi type innholdsinformasjon.<br> <br>OTHERCONTENTINFORMATIONTYPE for datasett og databaser **MÅ** være `NB-SIP-DATASETS-PROFILE-1.0`. <br><br>Dette er en spesifisering av [CSIP5](https://earkcsip.dilcis.eu/#CSIP5). | **MÅ** | **1..1** |


### Eksempel
```xml
<mets:mets xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS"
  xmlns:mets="http://www.loc.gov/METS/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:xlink="http://www.w3.org/1999/xlink" OBJID="no-nb_datasett_0209202600042"
  LABEL="no-nb_datasett_0209202600042" TYPE="Datasets" csip:CONTENTINFORMATIONTYPE="OTHER"
  csip:OTHERCONTENTINFORMATIONTYPE="NB-SIP-DATASETS-PROFILE-1.0"
  PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP-v2-2-0.xml"
  xsi:schemaLocation="http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/mets.xsd http://www.w3.org/1999/xlink http://www.loc.gov/standards/mets/xlink.xsd https://DILCIS.eu/XML/METS/CSIPExtensionMETS https://earkcsip.dilcis.eu/schema/DILCISExtensionMETS.xsd"
  />
```
