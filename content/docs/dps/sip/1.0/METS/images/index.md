---
title: Requirements for images
weight: 1
Draft: false
---


#### Requirements for METS.xml beyond the general SIP requirements
This is a list of requirements for the METS.xml file for image packages delivered to the National Library of Norway. These are additional requirements beyond what is defined in [METS.xml requirements](/docs/dps/sip/1.0/mets/). <br><br>

| **ID** | **Name, METS Element, Description** | **Requirement** | **Cardinality** |
|:---|:---|:---|:---|
| **NBIMAGESIP1** | **Content Category**<br>`mets/@TYPE`<br><br>The `mets/@TYPE`attribute **MUST** be used to specify the content category of the package, e.g., "Datasets", "Websites", "Mixes", "Other", etc. Valid values are defined in a controlled vocabulary. The vocabulary will be updated by the DILCIS Board as new content information specifications are added.<br><br>For images, the following values are used:<br>`Photographs – Print` : Used for a digitized version of a physical photograph. <br>`Photographs – Digital` : Used for a born-digital photograph. <br>`Other Graphic Images – Print`: Used for digitized versions of posters, drawings, postcards, maps, etc.<br>`Other Graphic Images – Digital` : Used for digital posters, drawings, postcards, maps, etc.<br><br>See the vokabulary here [E-ARK-CSIP-Content Category](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentCategory.xml). <br><br>This is a specification of [CSIP2](https://earkcsip.dilcis.eu/#CSIP2). | **MUST** | **1..1** |
| **NBIMAGESIP2** | **Content Information Type Specification**<br>`mets/@csip:CONTENTINFORMATIONTYPE`<br><br>Used to define the type specification of content information applied when the package was created. Valid values are defined in a controlled vocabulary. The attribute is mandatory for METS documents at the representation level. The vocabulary will be updated by the DILCIS Board as new content information specifications are added.<br><br>For images, the value `OTHER` is used (indicating a value not currently covered by the vocabulary).<br><br>See the vokabulary here [E-ARK-CSIP-Content Information Type](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentInformationType.xml).<br> <br>This is a spesification of [CSIP4](https://earkcsip.dilcis.eu/#CSIP4). | **MUST** | **1..1** |
| **NBIMAGESIP3** | **Other Content Information Type Specification**<br>`mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE`<br> <br>When the value of `mets/@csip:CONTENTINFORMATIONTYPE` is `OTHER`, the `mets/@csip:OTHERCONTENTINFORMATIONTYPE` **MUST** specify the type of content information.<br> <br>For images the value of OTHERCONTENTINFORMATIONTYPE **MUST** be: `NB-METS-IMAGES-PROFILE-1.0`.<br><br>This is a specification of [CSIP5](https://earkcsip.dilcis.eu/#CSIP5). | **MUST** | **1..1** |


### Example
```xml
<mets:mets xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS" 
    xmlns:mets="http://www.loc.gov/METS/" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xlink="http://www.w3.org/1999/xlink" 
    OBJID="no-nb_digifoto_20170215_00280_NB_MIT_GNR_02053" 
    LABEL="no-nb_digifoto_20170215_00280_NB_MIT_GNR_02053" 
    TYPE="Photographs – Print" 
    csip:CONTENTINFORMATIONTYPE="OTHER" 
    csip:OTHERCONTENTINFORMATIONTYPE="NB-METS-IMAGES-PROFILE-1.0" 
    PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP-v2-2-0.xml" 
    xsi:schemaLocation="http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/mets.xsd http://www.w3.org/1999/xlink http://www.loc.gov/standards/mets/xlink.xsd https://DILCIS.eu/XML/METS/CSIPExtensionMETS https://earkcsip.dilcis.eu/schema/DILCISExtensionMETS.xsd">
</mets:mets> 