---
title: Requirements for audio
draft: false
weight: 4
---

#### Requirements for METS.xml beyond the general SIP requirements
This is a list of requirements for the METS.xml file for audio packages delivered to the National Library of Norway.
These requirements are in addition to those defined in [METS.xml requirements](/docs/dps/sip/1.0/mets/). <br><br>

| **ID** | **Name, METS element, description** | **Requirement** | **Cardinality** |
|:---|:---|:---|:---|
| **NBAUDIOSIP1** | **Content Category**<br>`mets/@TYPE`<br><br>The attribute `mets/@TYPE` **MUST** be used to specify the category of the content within the package, e.g., "Datasets", "Websites", "Mixes", "Other", etc. Valid values are defined in a controlled vocabulary. The vocabulary will be updated by the DILCIS Board as additional content information specifications are introduced. <br><br>For audio, the following values are used:<br>`Audio – On Tangible Medium (digital or analog)` : Used for audio digitized from a physical medium such as a CD, cassette, MiniDisc, or tape. <br>`Audio – Media-independent (digital)` : Used for born-digital audio.<br><br> See the vokabulary here [E-ARK-CSIP-Content Category](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentCategory.xml). <br><br>This is a specification of [CSIP2](https://earkcsip.dilcis.eu/#CSIP2). | **MUST** | **1..1** |
| **NBAUDIOSIP2** | **Content Information Type Specification**<br>`mets/@csip:CONTENTINFORMATIONTYPE`<br><br>Used to define the specifications for the type of content information applied when the package was created. Valid values are defined in a controlled vocabulary. The attribute is mandatory for METS documents at the representation level. The vocabulary will be updated by the DILCIS Board as additional content information specifications are introduced.<br><br>For audio, the value `OTHER` is used (a term different from those included in the controlled vocabulary).<br><br> See the vokabulary here [E-ARK-CSIP-Content Information Type](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentInformationType.xml).<br> <br>This is a specification of  [CSIP4](https://earkcsip.dilcis.eu/#CSIP4). | **MUST** | **1..1** |
| **NBAUDIOSIP3** | **Other Content Information Type Specification**<br>`mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE`<br> <br>When `mets/@csip:CONTENTINFORMATIONTYPE` has the value `OTHER`, the attribute `mets/@csip:OTHERCONTENTINFORMATIONTYPE` **MUST** specify the type of content information.<br> <br>OTHERCONTENTINFORMATIONTYPE for audio **MUST** be `NB-METS-AUDIO-PROFILE-1.0`. <br><br>This is a specification of [CSIP5](https://earkcsip.dilcis.eu/#CSIP5). | **MUST** | **1..1** |


### Example
```xml
<mets:mets xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS" 
xmlns:mets="http://www.loc.gov/METS/" 
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:xlink="http://www.w3.org/1999/xlink" 
OBJID="no-nb_radio_NRKP2_199204081200" 
LABEL="no-nb_radio_NRKP2_199204081200" 
TYPE="Audio – On Tangible Medium (digital or analog)" 
csip:CONTENTINFORMATIONTYPE="OTHER" 
csip:OTHERCONTENTINFORMATIONTYPE="NB-METS-AUDIO-PROFILE-1.0" 
PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP-v2-2-0.xml" 
xsi:schemaLocation="http://www.loc.gov/METS/ http://www.loc.gov/standards/mets/mets.xsd http://www.w3.org/1999/xlink http://www.loc.gov/standards/mets/xlink.xsd https://DILCIS.eu/XML/METS/CSIPExtensionMETS https://earkcsip.dilcis.eu/schema/DILCISExtensionMETS.xsd">
</mets:mets> 