---
title: Use of METS.xml 
draft: false
weight: 2
---

## Requirements for the use of METS.xml (SIP)

Information packages delivered to the DPS must contain a file named `METS.xml` in the root folder of the information package, as well as a `METS.xml` in each representation folder.

Both `METS.xml` files must validate against the METS requirements specified by the E-ARK specifications [CSIP1-119](https://earkcsip.dilcis.eu/#useofmets) and [SIP1-35](https://earksip.dilcis.eu/#e-arksipmetsprofile2.1requirements) in the [E-ARK (C)SIP spesifikasjonene v2.2.0](https://dilcis.eu/specifications/).
<br><br>

### Use of the METS root element (`mets`)

<br>

| **ID** | **Name, METS element, description** | **Requirement** | **Cardinality** |
|:---|:---|:---|:---|
| **NBSIP1** | **Package Identifier**<br>`mets/@OBJID`<br><br>The `mets/@OBJID` attribute is mandatory, its value is a string identifier for the METS document. In the METS file located in the root folder of the package, this identifier **MUST** be identical to the name of the package’s root folder (see [NBSIPSTR2](https://digitalpreservation.no/docs/dps/sip/1.0/structure-requirements/) for formatting). In the METS files within the individual representation folders, this identifier **MUST** be identical to the name of the respective representation folder (see [NBSIPSTR11](https://digitalpreservation.no/docs/dps/sip/1.0/structure-requirements/#:~:text=1..1-,NBSIPSTR11) and [NBSIPSTR12](https://digitalpreservation.no/docs/dps/sip/1.0/structure-requirements/#:~:text=1..1-,NBSIPSTR12) for formatting). <br><br>This requirement is a stricter version of [CSIP1](https://earkcsip.dilcis.eu/#CSIP1) | **MUST** | **1..1** |
| **NBSIP2** | **Package name**<br>`mets/@LABEL`<br><br>A short text that provides the title or a description of the content of the information package. The value of the `mets/@LABEL` **SHOULD** match the "title" field in the API call. (see [Metadata Requirements](https://digitalpreservation.no/docs/dps/interface/api/metadata/)).<br><br>This requirement is a stricter version of [SIP1](https://earksip.dilcis.eu/#SIP1) | **SHOULD** | **1..1** |


<br>

**Example:**


```xml
{<mets xmlns="http://www.loc.gov/METS/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:sip="https://DILCIS.eu/XML/METS/SIPExtensionMETS"
    xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS"
    xmlns:xlink="http://www.w3.org/1999/xlink"    
    OBJID="no-nb_fjernsyn_NRK_NRK-Tegnsprak_202204081200"
    LABEL="no-nb_fjernsyn_NRK_NRK-Tegnsprak_202204081200"
    TYPE="Video – File-based and Physical Media"
    csip:CONTENTINFORMATIONTYPE="OTHER"
    csip:OTHERCONTENTINFORMATIONTYPE="Digital Library Object"
    PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP-v2-2-0.xml"
    xsi:schemaLocation="http://www.loc.gov/METS/ schemas/mets1_12.xsd http://www.w3.org/1999/xlink schemas/xlink.xsd https://dilcis.eu/XML/METS/CSIPExtensionMETS schemas/DILCISExtensionMETS.xsd https://dilcis.eu/XML/METS/SIPExtensionMETS schemas/DILCISExtensionSIPMETS.xsd">}
```






<br><br><br>


### Use of the METS header (`metsHdr`)
<br>

| **ID** | **Name, METS element, description** | **Requirement** | **Cardinality** | 
|:---|:---|:---|:---|
| **NBSIP3** | **Submission agreement**<br>`metsHdr/altRecordID`<br><br>The submission agreement under which the package is delivered **MUST** be referenced. `@TYPE` **MUST** be set to the value “SUBMISSONAGREEMENT”. (An example of this will be provided). <br><br>This requirement is a stricter version of [SIP5](https://earksip.dilcis.eu/#SIP5) | **MUST** | **1..1** |  |  |
| **NBSIP4** | **Submitting agent**<br>`metsHdr/agent` <br><br>This is a wrapper element that allows you to specify the name of the organization or individual who delivered the information package to the National Library of Norway. The deliverer does not have to be the same as the package owner, as specified in the submission agreement.<br><br>This is a more detailed specification of [SIP15](https://earksip.dilcis.eu/#SIP15) | **MUST** | **1..1** |  |  |
| **NBSIP5** | **Submitting agent role**<br>`metsHdr/agent/@ROLE`<br><br>Specifies the role of the organization or individual who submitted the information package to the National Library of Norway. The attributes must be set to role=`”OTHER”` and otherrole=`”SUBMITTER”`.<br><br>This requirement is a stricter version of [SIP16](https://earksip.dilcis.eu/#SIP16) | **MUST** | **1..1** |  |  |
| **NBSIP6** | **Submitting agent name**<br>`metsHdr/agent/name`<br><br>The name of the organization or individual who submitted the information package to the National Library of Norway. <br> Personal names should be written in inverted form. Organization names are written in the original language (as commonly used). <br><br>This is a more detailed specification of [SIP18](https://earksip.dilcis.eu/#SIP18) | **MUST** | **1..1** |  |  |
| **NBSIP7** | **Submitting agent additional information**<br>`metsHdr/agent/note`<br><br> This is a note field where a unique identification code for the submitter of the information package **SHOULD** be provided. For organizations, the organization number should be given. For individuals, we require an identifier from the[Norwegian Authority File](https://bibliotekutvikling.no/kunnskapsorganisering/vokabularer-utkast/felles-autoritetsregister-for-personer-og-korporasjoner/) for persons and corporations, [ISNI](https://isni.org/), [VIAF](https://viaf.org/en) or [ORCID](https://orcid.org/).<br><br>This requirement is a stricter version of [SIP19](https://earksip.dilcis.eu/#SIP19) | **SHOULD** | **0..1** |  |  |

<br>

**Example:** 


```xml
{<metsHdr CREATEDATE="2025-03-18T22:53:09.977+01:00" LASTMODDATE="2025-03-18T22:53:09.977+01:00" RECORDSTATUS="NEW" csip:OAISPACKAGETYPE="SIP">
    <agent ROLE="CREATOR" TYPE="OTHER" OTHERTYPE="SOFTWARE">
        <name>RODA Commons IP</name>
        <note csip:NOTETYPE="SOFTWARE VERSION">2.2.0</note>
    </agent>
    <agent ROLE="CREATOR" TYPE="INDIVIDUAL">
        <name>PEDERSEN, TORBJORN BAKKEN</name>
        <note csip:NOTETYPE="IDENTIFICATIONCODE">https://orcid.org/0009-0005-3523-5728</note>
    </agent>
    <agent ROLE="OTHER" OTHERROLE="SUBMITTER" TYPE="ORGANIZATION">
        <name>Nasjonalbiblioteket</name>
        <note csip:NOTETYPE="IDENTIFICATIONCODE">Organisasjonsnummer:123456789</note>
    </agent>
    <altRecordID TYPE="SUBMISSIONAGREEMENT">https://submissionagreement.nb.no/SA-XXXXXX</altRecordID>
</metsHdr>}
```





<br><br><br>

### Use of the METS descriptive metadata section (`dmdSec`)
<br>

| **ID** | **Name, METS element, description** | **Requirement** | **Cardinality** |
|:---|:---|:---|:---|
| **NBSIP8** | **Descriptive metadata** <br>`mets/dmdSec`<br><br> **MUST** be used to refer to available descriptive metadata about the information package. Each descriptive metadata section (<dmdSec>) contains a single description and must be repeated if multiple descriptions exist. <br> See also [NBSIPSTR9](https://digitalpreservation.no/docs/dps/sip/1.0/structure-requirements/#:~:text=NBSIPSTR9) which requires at least one file containing descriptive metadata.<br><br>This requirement is a stricter version of [CSIP17](https://earkcsip.dilcis.eu/#CSIP17).  | **MUST** | **1..n** |
| **NBSIP9** | **Mandatory descriptive metadata** <br>`mets/dmdSec`<br><br> The element describing the descriptive metadata section **MUST** refer to the metadata file(s) specified in [NBSIPSTR9](https://digitalpreservation.no/docs/dps/sip/1.0/structure-requirements/#:~:text=NBSIPSTR9). It **MUST** be described using `mets/dmdSec/mdRef/@MDTYPE`. Valid values include: MARC, MODS, EAD, DC, NISOIMG, LC-AV, VRA, TEIHDR, DDI, FGDC, LOM, PREMIS, PREMIS:OBJECT, PREMIS:AGENT, PREMIS:RIGHTS, PREMIS:EVENT, TEXTMD, METSRIGHTS, ISO 19115:2003 NAP, EAC-CPF, LIDO, OTHER. If '`OTHER`' is selected, the type of metadata **SHOULD** be specified using `mets/dmdSec/mdRef/@MDOTHERTYPE`. <br><br> Administrative or preservation metadata may be included in accordance with [CSIP31-57](https://earkcsip.dilcis.eu/#useofthemetsadministrativemetadatasectionelementamdsec). | **MUST** | **1..n** |
| **NBSIP10** | **Reference to files with descriptive metadata**<br>`mets/dmdSec/mdRef`<br><br> **MUST** be used to refer to files containing descriptive metadata located in the `metadata/descriptive`. Directly embedding of metadata using `mets/dmdSec/mdWrap` is discouraged. <br><br> This requirement is a stricter version of [CSIP21](https://earkcsip.dilcis.eu/#CSIP21). | **MUST** | **1..n** |
| **NBSIP11** | **File checksum type**<br>`mets/dmdSec/mdRef/@CHECKSUMTYPE`<br><br> A value from the METS-standard which identifies the algorithm used to calculate the checksum for the referenced file. Checksum type **MUST** be : CHECKSUMTYPE="MD5".<br><br> This requirement is a stricter version of [CSIP29](https://earkcsip.dilcis.eu/#CSIP29) og [CSIP30](https://earkcsip.dilcis.eu/#CSIP30). | **MUST** | **1..1** |

<br>


**Example:** 

```xml
{<dmdSec ID="uuid-e1d1f6db-3851-40bf-9ffd-59277a4442dc" CREATED="2025-01-16T12:43:32.894+01:00" STATUS="CURRENT">
    <mdRef ID="ID-uuid-861d36a1-043f-45aa-b230-be13517823a9" LOCTYPE="URL" MIMETYPE="application/json" SIZE="2038" CREATED="2025-01-16T12:43:32.894+01:00" 
    CHECKSUM="EB72EF8AB5B1C93801DFACBFE6AA8E27" CHECKSUMTYPE="MD5" MDTYPE="DC" xlink:type="simple" xlink:href="metadata/descriptive/nb_dublincore.json"/>
</dmdSec>
<dmdSec ID="uuid-EC8718B5-C417-4D8C-975B-C14CD8197E62" CREATED="2025-01-16T12:43:32.894+01:00" STATUS="CURRENT">
    <mdRef ID="ID-uuid-FAF602A1-AB9A-44AC-A24B-B918F7064920" LOCTYPE="URL" MIMETYPE="text/xml" SIZE="1903" CREATED="2025-01-16T12:43:32.894+01:00" 
    CHECKSUM="50E9C929EAE5B51F20F8B86D604FD24D" CHECKSUMTYPE="MD5" MDTYPE="MODS" xlink:type="simple" xlink:href="metadata/descriptive/MODS.xml"/>
</dmdSec>}
```




<br><br><br>


### Use of the METS administrative metadata section (`amdSec`)

The E-ARK specification only defines how to reference digital provenance metadata (the `digiprovMD` section) and rights metadata (the `rightsMD` section) in METS.
Digital provenance metadata refers to information about events in the lifecycle of the digital object. This data is typically formatted using PREMIS.
Rights metadata contains information about intellectual property rights (IPR) associated with the digital objects.

However, the specification also allows for the inclusion of technical metadata (`techMD` section) and source metadata (`sourceMD` section).
The National Library of Norway (NB) considers these metadata types essential for managing digital objects. Technical metadata describes the characteristics of the data itself, while source material metadata provides important context for the digital object and supports its authenticity. See also [NBSIPSTR16](https://digitalpreservation.no/docs/dps/sip/1.0/structure-requirements/#:~:text=NBSIPSTR16) and [NBSIPSTR17](https://digitalpreservation.no/docs/dps/sip/1.0/structure-requirements/#:~:text=NBSIPSTR17).

<br>
<br>



| **ID** | **Name, METS element, description** | **Requirement** | **Cardinality** |
|:---|:---|:---|:---|
| **NBSIP12** | **Source metadata**<br>`mets/amdSec/sourceMD`<br><br> **If** metadata about the source material for a representation is available in the information package, this element **MUST** be used to describe it. | **MUST** | **1..n** |
| **NBSIP13** | **Source metadata identifier**<br>`mets/amdSec/sourceMD/@ID`<br><br> An `xml:id` identifier for the source metadata section `mets/amdSec/sourceMD` used for internal references within the XML document. The identifier **MUST** be unique within the XML document. | **MUST** | **1..1** |
| **NBSIP14** | **Status of the source metadata**<br>`mets/amdSec/sourceMD/@STATUS`<br><br> Status **MUST** be set to `'CURRENT'` | **MUST** | **1..1** |
| **NBSIP15** | **Reference to files with the source metadata**<br>`mets/amdSec/sourceMD/mdRef`<br><br> **MUST** be used to reference files containing source metadata located in the `metadata/source` folder. <br><br> Direct embedding of metadata using `mets/amdSec/mdWrap` is discouraged. | **MUST** | **1..1** |
| **NBSIP16** | **Type of locator**<br>`mets/amdSec/sourceMD/mdRef[@LOCTYPE='URL']`<br><br> The locator type is always used with the value `'URL'` from [Vocabulary status](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyStatus.xml) in the E-ARK specifications. | **MUST** | **1..1** |
| **NBSIP17** | **Type of link**<br>`mets/amdSec/sourceMD/mdRef[@xlink:type='simple']`<br><br> The attribute **MUST** be used with the value '`simple`'. The vocabulary of allowed values is maintained by the XLink standard. | **MUST** | **1..1** |
| **NBSIP18** | **File location**<br>`mets/amdSec/sourceMD/mdRef/@xlink:href`<br><br> The actual location of the file. It **MUST** be referenced using a URL of the filepath type. | **MUST** | **1..1** |
| **NBSIP19** | **Type of metadata**<br>`mets/amdSec/sourceMD/mdRef/@MDTYPE`<br><br> Specifies the type of metadata in the referenced file. The values are taken from METS.<br>Valid values:<br> MARC, MODS, EAD, DC, NISOIMG, LC-AV, VRA, TEIHDR, DDI, FGDC, LOM, PREMIS, PREMIS:OBJECT, PREMIS:AGENT, PREMIS:RIGHTS, PREMIS:EVENT, TEXTMD, METSRIGHTS, ISO 19115:2003 NAP, EAC-CPF, LIDO, OTHER. If '`OTHER`' is chosen, the type of metadata **SHOULD** be described using `mets/amdSec/sourceMD/mdRef/@MDOTHERTYPE`.| **MUST** | **1..1** |
| **NBSIP20** | **Technical metadata**<br>`mets/amdSec/techMD`<br><br> **If** technical metadata for the data files in a representation is available in the information package, this element **MUST** be used to describe it. <br><br> Direct embedding of metadata using `mets/amdSec/mdWrap` is discouraged. | **MUST** | **1..n** |
| **NBSIP21** | **Technical metadata identifier**<br>`mets/amdSec/techMD/@ID`<br><br> An `xml:id` identifier for the technical metadata section `mets/amdSec/techMD` used for internal references within the XML document. The identifier **MUST** be unique within the XML document. | **MUST** | **1..1** |
| **NBSIP22** | **Status of the technical metadata**<br>`mets/amdSec/techMD/@STATUS`<br><br> Status **MUST** be set to '`CURRENT`' | **MUST** | **1..1** |
| **NBSIP23** | **Reference to files with the technical metadata**<br>`mets/amdSec/techMD/mdRef`<br><br> **MUST** be used to reference files containing technical metadata that are located in the folder `metadata/technical`. | **MUST** | **1..1** |
| **NBSIP24** | **Type of locator**<br>`mets/amdSec/techMD/mdRef[@LOCTYPE='URL']`<br><br> The locator type is always used with the value `'URL'` from [Vocabulary status](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyStatus.xml) in the E-ARK specifications. | **MUST** | **1..1** |
| **NBSIP25** | **Type of link**<br>`mets/amdSec/techMD/mdRef[@xlink:type='simple']`<br><br> The attribute **MUST** be used with the value '`simple`'. The vocabulary of allowed values is maintained by the XLink standard. | **MUST** | **1..1** |
| **NBSIP26** | **File location**<br>`mets/amdSec/techMD/mdRef/@xlink:href`<br><br> The actual location of the file. It **MUST** be referenced using a URL of the filepath type. | **MUST** | **1..1** |
| **NBSIP27** | **Type of metadata**<br>`mets/amdSec/techMD/mdRef/@MDTYPE`<br><br> Specifies the type of metadata in the referenced file. The values are taken from METS.<br>Valid values:<br> MARC, MODS, EAD, DC, NISOIMG, LC-AV, VRA, TEIHDR, DDI, FGDC, LOM, PREMIS, PREMIS:OBJECT, PREMIS:AGENT, PREMIS:RIGHTS, PREMIS:EVENT, TEXTMD, METSRIGHTS, ISO 19115:2003 NAP, EAC-CPF, LIDO, OTHER. If '`OTHER`' is chosen, the type of metadata **SHOULD** be described using `mets/amdSec/techMD/mdRef/@MDOTHERTYPE`.  | **MUST** | **1..1** |
| **NBSIP28** | **File checksum type**<br>`mets/amdSec/digiprovMD/mdRef/@CHECKSUMTYPE, mets/amdSec/rightsMD/mdRef/@CHECKSUMTYPE, mets/amdSec/sourceMD/mdRef/@CHECKSUMTYPE, mets/amdSec/techMD/mdRef/@CHECKSUMTYPE`<br><br> A value from the METS-standard which identifies the algorithm used to calculate the checksum for the referenced file. Checksum type **MUST** be : CHECKSUMTYPE="MD5".<br><br> This requirement is a stricter version of [CSIP43](https://earkcsip.dilcis.eu/#CSIP43), [CSIP44](https://earkcsip.dilcis.eu/#CSIP44), [CSIP56](https://earkcsip.dilcis.eu/#CSIP56) og [CSIP57](https://earkcsip.dilcis.eu/#CSIP57). | **MUST** | **1..1** |

<br>

**Example:** 

```xml
{<amdSec>
    <digiprovMD ID="uuid-975a7a15-140f-4e2c-a5ec-d136e86ea4e5" CREATED="2019-04-24T14:37:52.783+01:00">
        <mdRef LOCTYPE="URL" xlink:type="simple" xlink:href="metadata/preservation/events.xml"
            MDTYPE="PREMIS" MDTYPEVERSION="3.0" MIMETYPE="text/xml" SIZE="1211"
            CREATED="2018-04-24T14:37:52.783+01:00" CHECKSUM="dc7177d37a7de3448ee1e62da7343d72"
            CHECKSUMTYPE="MD5" LABEL="events.xml"/>
    </digiprovMD>
</amdSec>
<amdSec>
    <sourceMD ID="uuid-5d500e19-3802-49a5-92bd-7a575433ab7e" CREATED="2018-04-24T14:47:52.783+01:00">
        <mdRef LOCTYPE="URL" xlink:type="simple"
            xlink:href="metadata/souce/MAVIS_Carrier_12345_AE0000006261.xml" MDTYPE="OTHER"
            OTHERMDTYPE="MAVIS" MIMETYPE="text/xml" SIZE="2854"
            CREATED="2018-04-24T14:37:52.783+01:00" CHECKSUM="7ee30736137bfe72dc60afcbe374cb2a"
            CHECKSUMTYPE="MD5" LABEL="MAVIS_Carrier_12345_AE0000006261.xml"/>
    </sourceMD>
</amdSec>}
```



<br><br><br>


### Use of the METS file section (`fileSec`)

| **ID** | **Name, METS element, description** | **Requirement** | **Cardinality** |
|:---|:---|:---|:---|
| **NBSIP29** | **File checksum type**<br>`mets/fileSec/fileGrp/file/@CHECKSUMTYPE`<br><br> A value from the METS-standard which identifies the algorithm used to calculate the checksum for the referenced file. Checksum type **MUST** be : CHECKSUMTYPE="MD5".<br><br> This requirement is a stricter version of [CSIP71](https://earkcsip.dilcis.eu/#CSIP71) og [CSIP72](https://earkcsip.dilcis.eu/#CSIP72). | **MUST** | **1..1** |

<br>

**Example:**

```xml
{<fileSec>
    <fileSec ID="file-sec-example">
        <mets:fileGrp ID="file-grp-doc" USE="Documentation">
        <mets:file ID="file-docx" 
            MIMETYPE="application/vnd.openxmlformats-officedocument.wordprocessingml.document" SIZE="2554366" 
            CREATED="2012-08-15T12:08:15.432+01:00" 
            CHECKSUM="7ee30736137bfe72dc60afcbe374cb2a" CHECKSUMTYPE="MD5">
                <mets:FLocat LOCTYPE="URL" xlink:type="simple" xlink:href="documentation/File.docx">
</fileSec>}
```

<br><br><br>

### Use of the METS structural map (`structMap`)

No further requirements beyond [CSIP](https://earkcsip.dilcis.eu/#useofthemetsstructuralmapelementstructmap).