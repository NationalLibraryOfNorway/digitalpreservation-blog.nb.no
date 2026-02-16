---
title: Requirements for Moving images
draft: false
weight: 3
---

#### Requirements for METS.xml beyond the general SIP requirements
This is a list of requirements for the METS.xml file for moving image packages delivered to the National Library of Norway. These are additional requirements beyond what is defined in [METS.xml requirements](/docs/dps/sip/1.0/mets/). <br><br>

| **ID** | **Name, METS Element, description** | **Requirement** | **Cardinality** |
|---|---|---|---|
| **NBMOVINGIMAGESIP1** | **Content Category**<br>The attribute `mets/@TYPE` **MUST** be used to specify the category of the content within the package, e.g., "Datasets", "Websites", "Mixes", "Other", etc. Valid values are defined in a controlled vocabulary. When the content category falls outside the defined vocabulary, the `mets/@TYPE` value **MUST** be set to `Other`, and the specific value must be specified in `mets/@csip:OTHERTYPE`. The vocabulary will be updated by the DILCIS Board as additional content information specifications are added.<br><br>For moving images, use: <br>`Other` : A term different from those included in the controlled vocabulary. <br><br><br>See the vokabulary here [E-ARK-CSIP-Content Category](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentCategory.xml). <br><br>This is a spesification of [CSIP2](https://earkcsip.dilcis.eu/#CSIP2). | **MUST** | **1..1** |
| **NBMOVINGIMAGESIP2** | **Other content category**<br>`mets[@csip:TYPE='OTHER']/@csip:OTHERTYPE`<br><br> When `mets/@TYPE` uses the value `Other`, `mets/@csip:OTHERTYPE` **MUST** be used to specify the content category of the package/representation. <br><br>For moving images, use: <br>`Moving images - on tangible media` : Used for moving images that have been digitized from an analog source. <br>`Moving images - digital` : Used for moving images that are born-digital or originate from digital sources.<br> <br>This is a spesification of [CSIP3](https://earkcsip.dilcis.eu/#CSIP3). | **MUST** | **1..1** |
| **NBMOVINGIMAGESIP3** | **Content Information Type Specification** <br> `mets[@csip:CONTENTINFORMATIONTYPE`<br> <br>Used to define the specifications for the type of content information that were applied when the package was created. Valid values are defined in a controlled vocabulary. The attribute is mandatory for METS documents at the representation level.<br> <br>For moving images, the value `OTHER` is used (indicating a value not currently covered by the vocabulary).<br><br>This is a spesification of [CSIP4](https://earkcsip.dilcis.eu/#CSIP4). | **MUST** | **1..1** |
| **NBMOVINGIMAGESIP4** | **Other Content Information Type Specification**<br>`mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE`<br> <br>When `mets/@csip:CONTENTINFORMATIONTYPE` uses the value `OTHER`, `mets/@csip:OTHERCONTENTINFORMATIONTYPE` **MUST** be used to specify the type of content information.<br> <br>OTHERCONTENTINFORMATIONTYPE for moving images **MUST** be set to `NB-SIP-MOVINGIMAGES-PROFILE-1.0`. <br><br>This is a spesification of [CSIP5](https://earkcsip.dilcis.eu/#CSIP5). |**MUST**  | **1..1** |


### Example:
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
    csip:OTHERCONTENTINFORMATIONTYPE="NB-METS-MOVINGIMAGES-PROFILE-1.0" 
    PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP-v2-2-0.xml" 
    xsi:schemaLocation="http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/mets.xsd http://www.w3.org/1999/xlink http://www.loc.gov/standards/mets/xlink.xsd https://DILCIS.eu/XML/METS/CSIPExtensionMETS https://earkcsip.dilcis.eu/schema/DILCISExtensionMETS.xsd">
</mets:mets>