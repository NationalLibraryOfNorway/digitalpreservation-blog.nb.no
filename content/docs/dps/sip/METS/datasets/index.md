---
title: Requirements for dataset
weight: 5
---

#### Requirements for METS.xml beyond the general SIP requirements
This is a list of requirements for the METS.xml file for packages containing datasets and databases to be delivered to the National Library of Norway.
These requirements are in addition to those defined in [METS.xml requirements](/docs/dps/sip/mets/). <br><br>

> [!NOTE]
> E-ARK provides dedicated Content Information Type Specifications for [relational databases using SIARD (CITS SIARD)](https://dilcis.eu/content-types/cs-siard) and [geospatial data (CITS Geospatial)](https://dilcis.eu/content-types/cs-geospatial-data). The National Library of Norway has not yet fully assessed how these specifications align with its own SIP requirements. If you want to submit geodata or SIARD-structured data, please contact the digital preservation team before delivery.

| **ID** | **Name, METS element, description** | **Requirement** | **Cardinality** |
|:---|:---|:---|:---|
| **NBDATASETSIP1** | **Content Category**<br>`mets/@TYPE`<br><br>The attribute `mets/@TYPE` **MUST** be used to specify the category of the content within the package, e.g., "Datasets", "Websites", "Mixes", "Other", etc. Valid values are defined in a controlled vocabulary. The vocabulary will be updated by the DILCIS Board as additional content information specifications are introduced. <br><br>For datasets and databases, `mets/@TYPE` **MUST** be one of the following values:<br>`Datasets` : Used for data encoded in a defined structure, e.g. data dumps and data exports in formats such as CSV, JSON, XML, or Parquet. <br>`Databases` : Used for a complete set of the content contained within a database, e.g. database dumps or exports.<br><br> See the vocabulary here [E-ARK-CSIP-Content Category](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentCategory.xml). <br><br>This is a specification of [CSIP2](https://earkcsip.dilcis.eu/#CSIP2). | **MUST** | **1..1** |
| **NBDATASETSIP2** | **Content Information Type Specification**<br>`mets/@csip:CONTENTINFORMATIONTYPE`<br><br>Used to define the specifications for the type of content information applied when the package was created. Valid values are defined in a controlled vocabulary. The attribute is mandatory for METS documents at the representation level. The vocabulary will be updated by the DILCIS Board as additional content information specifications are introduced.<br><br>For datasets and databases, the value `OTHER` is used (a term different from those included in the controlled vocabulary).<br><br> See the vocabulary here [E-ARK-CSIP-Content Information Type](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyContentInformationType.xml).<br> <br>This is a specification of  [CSIP4](https://earkcsip.dilcis.eu/#CSIP4). | **MUST** | **1..1** |
| **NBDATASETSIP3** | **Other Content Information Type Specification**<br>`mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE`<br> <br>When `mets/@csip:CONTENTINFORMATIONTYPE` has the value `OTHER`, the attribute `mets/@csip:OTHERCONTENTINFORMATIONTYPE` **MUST** specify the type of content information.<br> <br>OTHERCONTENTINFORMATIONTYPE for datasets and databases **MUST** be `NB-SIP-DATASETS-PROFILE-1.0`. <br><br>This is a specification of [CSIP5](https://earkcsip.dilcis.eu/#CSIP5). | **MUST** | **1..1** |


### Example
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
