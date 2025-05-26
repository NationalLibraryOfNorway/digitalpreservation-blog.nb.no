---
title: Bilder
weight: 1
---





## Krav til METS.xml utover generelle SIP-krav
Dette er en liste over krav til METS.xml for bildepakker som leveres til Nasjonalbiblioteket. Dette er krav utover det som er definert i [Bruk av METS.xml](https://digitalpreservation.no/nb/docs/dps/sip/1.0/mets/)


| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:---|:---|:---|
| **CSIP2** | **Content Category**  <br>`mets/@TYPE`<br><br>Attributtet `mets/@TYPE` **MÅ** brukes til å angi kategorien til innholdet i pakken, f.eks. "Datasets", "Websites", "Mixes" , "Other", etc. Gyldige verdier er definert i et fastsatt vokabular. Når innholdskategorien faller utenfor det definerte vokabularet, **MÅ** `mets/@TYPE` verdien settes til «OTHER» og den spesifikke verdien angis i `mets/@csip:OTHERTYPE`. Vokabularet vil oppdateres av DILCIS-styret etter hvert som tilleggsspesifikasjoner for innholdsinformasjon legges til. | **MÅ** | **1..1** |
| **NBIMAGESIP1** | **Innholdskategori (Content Category)**<br>`mets/@TYPE`<br><br>Attributten brukes til å definere innholdet i informasjonspakka. For bilder brukes disse:<br><br>**Photographs – Print:** Brukes for en digitalisert versjon av et fysisk fotografi. <br>**Photographs – Digital:** Brukes for et digitalt fotografi. <br>**Other Graphic Images – Print:** Brukes for en digitalisert versjon av fysiske plakater, tegninger, postkort, kart, etc.<br>**Other Graphic Images – Digital:** Brukes for digitale plakater, tegninger, postkort, kart, etc.<br><br>[DILCISBoard/E-ARK-CSIP-Content Category](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentCategory.xml) | **MÅ** | **1..1** |
| **CSIP4** | **Content Information Type Specification**<br>`mets/@csip:CONTENTINFORMATIONTYPE`<br><br>Brukes til å definere spesifikasjoner for type innholdsinformasjon som ble brukt når pakken ble opprettet. Gyldige verdier er definert i et fastsatt vokabular. Attributten er obligatorisk for METS-dokumenter på representasjonsnivå. Vokabularet vil oppdateres av DILCIS-styret etter hvert som tilleggsspesifikasjoner for innholdsinformasjon legges til. | **MÅ** | **1..1** |
| **NBIMAGESIP2** | **Content Information Type Specification**<br>`mets/@csip:CONTENTINFORMATIONTYPE` <br><br>For bilder brukes “OTHER” (en annen term enn det som finnes i det brukte vokabularet).<br><br>[DILCISBoard/E-ARK-CSIP-Content Information Type](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentInformationType.xml) <br>  | **MÅ** | **1..1** |
| **CSIP5** | **Other Content Information Type Specification** <br>`mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE`<br><br>Når `mets/@csip:CONTENTINFORMATIONTYPE` har verdien «OTHER», **MÅ** `mets/@csip:OTHERCONTENTINFORMATIONTYPE` oppgi type innholdsinformasjon.  | **MÅ** | **1..1** |
| **NBIMAGESIP3** | **Other Content Information Type Specification**<br>`mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE` <br><br>`OTHERCONTENTINFORMATIONTYPE` for bilder **MÅ** være (https://digitalpreservation.no/nb/docs/dps/sip/1.0/profiles/images/)  | **MÅ** | **1..1** |