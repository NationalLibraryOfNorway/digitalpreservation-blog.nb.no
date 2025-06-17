---
title: Bilder
weight: 1
---




#### Krav til METS.xml utover generelle SIP-krav
Dette er en liste over krav til METS.xml for bildepakker som leveres til Nasjonalbiblioteket. Dette er krav utover det som er definert i [Bruk av METS.xml](https://digitalpreservation.no/nb/docs/dps/sip/1.0/mets/)

<br><br>

| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:---|:---|:---|
| **NBIMAGESIP1** | **Innholdskategori (Content Category)**<br>`mets/@TYPE`<br><br>Attributtet `mets/@TYPE` **MÅ** brukes til å angi kategorien til innholdet i pakken, f.eks. "Datasets", "Websites", "Mixes" , "Other", etc. Gyldige verdier er definert i et fastsatt vokabular. Når innholdskategorien faller utenfor det definerte vokabularet, **MÅ** `mets/@TYPE` verdien settes til «OTHER» og den spesifikke verdien angis i `mets/@csip:OTHERTYPE`. Vokabularet vil oppdateres av DILCIS-styret etter hvert som tilleggsspesifikasjoner for innholdsinformasjon legges til.<br><br>For bilder brukes disse:<br>**Photographs – Print:** Brukes for en digitalisert versjon av et fysisk fotografi. <br>**Photographs – Digital:** Brukes for et digitalt fotografi. <br>**Other Graphic Images – Print:** Brukes for en digitalisert versjon av fysiske plakater, tegninger, postkort, kart, etc.<br>**Other Graphic Images – Digital:** Brukes for digitale plakater, tegninger, postkort, kart, etc.<br><br>Se vokabular her [E-ARK-CSIP-Content Category](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentCategory.xml). <br><br>Dette er en spesifisering av [CSIP2](https://earkcsip.dilcis.eu/#CSIP2). | **MÅ** | **1..1** |
| **NBIMAGESIP2** | **Content Information Type Specification**<br>`mets/@csip:CONTENTINFORMATIONTYPE`<br><br>Brukes til å definere spesifikasjoner for type innholdsinformasjon som ble brukt når pakken ble opprettet. Gyldige verdier er definert i et fastsatt vokabular. Attributten er obligatorisk for METS-dokumenter på representasjonsnivå. Vokabularet vil oppdateres av DILCIS-styret etter hvert som tilleggsspesifikasjoner for innholdsinformasjon legges til.<br><br>For bilder brukes “OTHER” (en annen term enn det som finnes i det brukte vokabularet).<br><br>Se vokabular her [E-ARK-CSIP-Content Information Type](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentInformationType.xml).<br> <br>Dette er en spesifisering av [CSIP4](https://earkcsip.dilcis.eu/#CSIP4). | **MÅ** | **1..1** |
| **NBIMAGESIP3** | **Other Content Information Type Specification**<br>`mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE`<br> <br>Når `mets/@csip:CONTENTINFORMATIONTYPE` har verdien «OTHER», **MÅ** `mets/@csip:OTHERCONTENTINFORMATIONTYPE` oppgi type innholdsinformasjon.<br> <br>OTHERCONTENTINFORMATIONTYPE for bilder **MÅ** være `https://digitalpreservation.no/nb/docs/dps/sip/1.0/profiles/images/`<br><br>Dette er en spesifisering av [CSIP5](https://earkcsip.dilcis.eu/#CSIP5). | **MÅ** | **1..1** |

<br><br>

![Eksempel på SIP for bilder](content/docs/dps/sip/1.0/profiles/EksempelBilder.png) 