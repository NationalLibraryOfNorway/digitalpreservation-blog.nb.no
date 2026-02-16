---
title: Krav for levende bilder
draft: false
weight: 3
---

---
#### Krav til METS.xml utover generelle SIP-krav
Dette er en liste over krav til METS.xml for levende bilder-pakker som leveres til Nasjonalbiblioteket. Dette er krav utover det som er definert i [Krav til METS.xml](/nb/docs/dps/sip/1.0/mets/). <br><br>

| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|---|---|---|---|
| **NBMOVINGIMAGESIP1** |**Content Category**<br>`mets/@TYPE`<br><br>Attributtet `mets/@TYPE` **MÅ** brukes til å angi kategorien til innholdet i pakken, f.eks. "Datasets", "Websites", "Mixes" , "Other", etc. Gyldige verdier er definert i et fastsatt vokabular. Når innholdskategorien faller utenfor det definerte vokabularet, **MÅ** `mets/@TYPE` verdien settes til `Other` og den spesifikke verdien angis i `mets/@csip:OTHERTYPE`. Vokabularet vil oppdateres av DILCIS-styret etter hvert som tilleggsspesifikasjoner for innholdsinformasjon legges til.<br><br>For levende bilder brukes: <br> `Other` : En annen term enn det som finnes i det brukte vokabularet.<br><br>Se vokabular her [E-ARK-CSIP-Content Category](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentCategory.xml). <br><br>Dette er en spesifisering av [CSIP2](https://earkcsip.dilcis.eu/#CSIP2). | **MÅ** | **1..1** |
| **NBMOVINGIMAGESIP2** | **Other content category**<br>`mets[@csip:TYPE='OTHER']/@csip:OTHERTYPE`<br><br>Når `mets/@TYPE` har verdien `Other` **MÅ** `mets/@csip:OTHERTYPE` brukes for å oppgi innholdskategori for pakken/representasjonen. <br><br>For levende bilder brukes:<br>`Moving images - on tangible media` : Brukes for levende bilder som er digitalisert fra en analog kilde. <br>`Moving images - digital` : Brukes for levende bilder som er født digitalt eller kommer fra digitale kilder.<br> <br>Dette er en spesifisering av [CSIP3](https://earkcsip.dilcis.eu/#CSIP3). | **MÅ** | **1..1** |
| **NBMOVINGIMAGESIP3** | **Content Information Type Specification**<br>`mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE`<br> <br>Brukes til å definere spesifikasjoner for type innholdsinformasjon som ble brukt når pakken ble opprettet. Gyldige verdier er definert i et fastsatt vokabular. Attributten er obligatorisk for METS-dokumenter på representasjonsnivå. <br> <br> For levende bilder brukes `OTHER` (en annen term enn det som finnes i det brukte vokabularet).<br><br> Se vokabular her [E-ARK-CSIP-Content Information Type](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentInformationType.xml). <br><br>Dette er en spesifisering av [CSIP4](https://earkcsip.dilcis.eu/#CSIP4). | **MÅ** | **1..1** |
| **NBMOVINGIMAGESIP4** | **Other Content Information Type Specification**<br>`mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE`<br> <br>Når `mets/@csip:CONTENTINFORMATIONTYPE` har verdien `OTHER`, **MÅ** `mets/@csip:OTHERCONTENTINFORMATIONTYPE` oppgi type innholdsinformasjon.<br> <br>OTHERCONTENTINFORMATIONTYPE for levende bilder MÅ være `NB-SIP-MOVINGIMAGES-PROFILE-1.0`.<br><br>Dette er en spesifisering av [CSIP5](https://earkcsip.dilcis.eu/#CSIP5). |**MÅ**  | **1..1** |



### Eksempel: 


```XML
<mets:mets xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS" 
    xmlns:mets="http://www.loc.gov/METS/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xlink="http://www.w3.org/1999/xlink" 
    OBJID="no-nb_fjernsyn_NRK_NRK-Tegnsprak_202204081200" 
    LABEL="no-nb_fjernsyn_NRK_NRK-Tegnsprak_202204081200" 
    TYPE="OTHER" 
    csip:OTHERTYPE="Moving images - digital" 
    csip:CONTENTINFORMATIONTYPE="OTHER" 
    csip:OTHERCONTENTINFORMATIONTYPE="NB-SIP-MOVINGIMAGES-PROFILE-1.0" 
    PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP-v2-2-0.xml" 
    xsi:schemaLocation="http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/mets.xsd http://www.w3.org/1999/xlink http://www.loc.gov/standards/mets/xlink.xsd https://DILCIS.eu/XML/METS/CSIPExtensionMETS https://earkcsip.dilcis.eu/schema/DILCISExtensionMETS.xsd">
</mets:mets>