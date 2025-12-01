---
title: Text
draft: true
weight: 4
---

#### Requirements for METS.xml beyond the general SIP requirements
This is a list of requirements for the METS.xml file for text packages delivered to the National Library of Norway.
These requirements are in addition to those defined in [Use of METS.xml](https://digitalpreservation.no/nb/docs/dps/sip/1.0/mets/). <br><br>

| **ID** | **Name, METS element, description** | **Requirement** | **Cardinality** |
|:---|:---|:---|:---|
| **NBTEXTSIP1** | **Content Category**<br>`mets/@TYPE`<br><br>The attribute `mets/@TYPE` **MUST** be used to specify the category of the content within the package, e.g., "Datasets", "Websites", "Mixes", "Other", etc. Valid values are defined in a controlled vocabulary. The vocabulary will be updated by the DILCIS Board as additional content information specifications are introduced. <br><br>For text, the following values are used:<br>**Textual works – Print:** Used for the digitized version of books, journals, newspapers, sheet music, etc. <br> **Textual works – Digital:** Used for digital documents such as e-books.<br><br> See the vokabulary here [E-ARK-CSIP-Content Category](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentCategory.xml). <br><br>This is a specification of [CSIP2](https://earkcsip.dilcis.eu/#CSIP2). | **MUST** | **1..1** |
| **NBTEXTSIP2** | **Content Information Type Specification**<br>`mets/@csip:CONTENTINFORMATIONTYPE`<br><br>Used to define the specifications for the type of content information applied when the package was created. Valid values are defined in a controlled vocabulary. The attribute is mandatory for METS documents at the representation level. The vocabulary will be updated by the DILCIS Board as additional content information specifications are introduced.<br><br>For text, the value "OTHER" is used (a term different from those included in the controlled vocabulary).<br><br> See the vokabulary here [E-ARK-CSIP-Content Information Type](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentInformationType.xml).<br> <br>This is a specification of  [CSIP4](https://earkcsip.dilcis.eu/#CSIP4). | **MUST** | **1..1** |
| **NBTEXTSIP3** | **Other Content Information Type Specification**<br>`mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE`<br> <br>When `mets/@csip:CONTENTINFORMATIONTYPE` has the value "OTHER", the attribute `mets/@csip:OTHERCONTENTINFORMATIONTYPE` **MUST** specify the type of content information.<br> <br>OTHERCONTENTINFORMATIONTYPE for text **MUST** be https://digitalpreservation.no/nb/docs/dps/sip/1.0/profiles/text/ <br><br>This is a specification of [CSIP5](https://earkcsip.dilcis.eu/#CSIP5). | **MUST** | **1..1** |