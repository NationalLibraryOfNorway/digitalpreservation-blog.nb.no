---
title: Nettarkiv
draft: false
weight: 2
---


#### Krav til METS.xml utover generelle SIP-krav
Dette er en liste over krav til METS.xml for nettarkivpakker som leveres til Nasjonalbiblioteket. Dette er krav utover det som er definert i [Krav til METS.xml](nb/docs/dps/sip/1.0/mets/). <br><br>

| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:---|:---|:---|
| **NBWEBARCHIVESIP1** | **Content Category**<br>`mets/@TYPE`<br><br>Attributtet `mets/@TYPE` **MÅ** brukes til å angi kategorien til innholdet i pakken, f.eks. "Datasets", "Websites", "Mixes" , "Other", etc. Gyldige verdier er definert i et fastsatt vokabular. Vokabularet vil oppdateres av DILCIS-styret etter hvert som tilleggsspesifikasjoner for innholdsinformasjon legges til.<br><br>For nettarkiv brukes:<br>**Web archives** <br><br>Se vokabular her [E-ARK-CSIP-Content Category](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentCategory.xml). <br><br>Dette er en spesifisering av [CSIP2](https://earkcsip.dilcis.eu/#CSIP2). | **MÅ** | **1..1** |
| **NBWEBARCHIVESIP2** | **Content Information Type Specification**<br>`mets/@csip:CONTENTINFORMATIONTYPE`<br><br>Brukes til å definere spesifikasjoner for type innholdsinformasjon som ble brukt når pakken ble opprettet. Gyldige verdier er definert i et fastsatt vokabular. Attributten er obligatorisk for METS-dokumenter på representasjonsnivå. Vokabularet vil oppdateres av DILCIS-styret etter hvert som tilleggsspesifikasjoner for innholdsinformasjon legges til.<br><br>For nettarkiv brukes "OTHER" (en annen term enn det som finnes i det brukte vokabularet).<br><br>Se vokabular her [E-ARK-CSIP-Content Information Type](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentInformationType.xml).<br> <br>Dette er en spesifisering av [CSIP4](https://earkcsip.dilcis.eu/#CSIP4). | **MÅ** | **1..1** |
| **NBWEBARCHIVESIP3** | **Other Content Information Type Specification**<br>`mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE`<br> <br>Når `mets/@csip:CONTENTINFORMATIONTYPE` har verdien "OTHER", **MÅ** `mets/@csip:OTHERCONTENTINFORMATIONTYPE` oppgi type innholdsinformasjon.<br> <br>OTHERCONTENTINFORMATIONTYPE for nettarkiv **MÅ** være `NB-SIP-WEBARCHIVE-PROFILE-1.0`. <br><br>Dette er en spesifisering av [CSIP5](https://earkcsip.dilcis.eu/#CSIP5). | **MÅ** | **1..1** |