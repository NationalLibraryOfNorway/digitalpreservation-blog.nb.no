---
title: Lyd
draft: true
weight: 4
---



#### Krav til METS.xml utover generelle SIP-krav
Dette er en liste over krav til METS.xml for lydpakker som leveres til Nasjonalbiblioteket. Dette er krav utover det som er definert i [Bruk av METS.xml](https://digitalpreservation.no/nb/docs/dps/sip/1.0/mets/). <br><br>

| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:---|:---|:---|
| **NBAUDIOSIP1** | **Content Category**<br>`mets/@TYPE`<br><br>Attributtet `mets/@TYPE` **MÅ** brukes til å angi kategorien til innholdet i pakken, f.eks. "Datasets", "Websites", "Mixes" , "Other", etc. Gyldige verdier er definert i et fastsatt vokabular. Vokabularet vil oppdateres av DILCIS-styret etter hvert som tilleggsspesifikasjoner for innholdsinformasjon legges til.<br><br>For lyd brukes disse:<br>**Audio – On Tangible Medium (digital or analog):** Brukes for lyd som digitaliseres fra et fysisk medium, som en CD, kassett, minidisc eller bånd. <br> **Audio – Media-independent (digital):** Brukes for digital lyd.<br><br>Se vokabular her [E-ARK-CSIP-Content Category](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentCategory.xml). <br><br>Dette er en spesifisering av [CSIP2](https://earkcsip.dilcis.eu/#CSIP2). | **MÅ** | **1..1** |
| **NBAUDIOSIP2** | **Content Information Type Specification**<br>`mets/@csip:CONTENTINFORMATIONTYPE`<br><br>Brukes til å definere spesifikasjoner for type innholdsinformasjon som ble brukt når pakken ble opprettet. Gyldige verdier er definert i et fastsatt vokabular. Attributten er obligatorisk for METS-dokumenter på representasjonsnivå. Vokabularet vil oppdateres av DILCIS-styret etter hvert som tilleggsspesifikasjoner for innholdsinformasjon legges til.<br><br>For lyd brukes “OTHER” (en annen term enn det som finnes i det brukte vokabularet).<br><br>Se vokabular her [E-ARK-CSIP-Content Information Type](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentInformationType.xml).<br> <br>Dette er en spesifisering av [CSIP4](https://earkcsip.dilcis.eu/#CSIP4). | **MÅ** | **1..1** |
| **NBAUDIOSIP3** | **Other Content Information Type Specification**<br>`mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE`<br> <br>Når `mets/@csip:CONTENTINFORMATIONTYPE` har verdien «OTHER», **MÅ** `mets/@csip:OTHERCONTENTINFORMATIONTYPE` oppgi type innholdsinformasjon.<br> <br>OTHERCONTENTINFORMATIONTYPE for lyd **MÅ** være https://digitalpreservation.no/nb/docs/dps/sip/1.0/profiles/audio/ <br><br>Dette er en spesifisering av [CSIP5](https://earkcsip.dilcis.eu/#CSIP5). | **MÅ** | **1..1** |