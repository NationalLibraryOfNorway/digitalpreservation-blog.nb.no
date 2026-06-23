---
title: METS.xml requirements
draft: false
weight: 4
---

METS.xml is an XML document that conforms to the [METS standard](https://www.loc.gov/standards/mets/) (Metadata Encoding and Transmission Standard). It is used to collect and structure metadata for a digital object within a single file. The file functions as a control and linking document that enables systems to understand, validate, and exchange complex digital objects in a standardized manner. 

METS.xml describes: 
- The structure of the object (for example, how pages, chapters, or files are related). 
- File references to the digital files included (images, PDFs, audio files, etc.). 
- Metadata, which may be descriptive, administrative, and technical, often by referencing or embedding other metadata formats.

Information packages delivered to the DPS must include a METS.xml file in the root folder of the information package, as well as a METS.xml file in each representation folder.  

Both METS.xml files must validate against the METS requirements specified by the E-ARK specifications [CSIP1-119](https://earkcsip.dilcis.eu/#useofmets) and [SIP1-35](https://earksip.dilcis.eu/#e-arksipmetsprofile2.1requirements) in the [E-ARK (C)SIP spesifikasjonene v2.2.0](https://dilcis.eu/specifications/), in addition to the National Library’s specifications of SIP requirements described below (NBSIP). 


## Use of the METS root element (`mets`)

The METS document’s root element (`mets`) describes the container for the information being stored and/or transmitted. 


| **ID** | **Name, METS element, description** | **Requirement** | **Cardinality** |
|:---|:---|:---|:---|
| **NBSIP1** | **Package Identifier**<br>`mets/@OBJID`<br><br>The `mets/@OBJID` attribute is mandatory, its value is a string identifier for the METS document. In the METS file located in the root folder of the package, this identifier **MUST** be identical to the name of the package’s root folder (see [NBSIPSTR2](/docs/dps/sip/structure-requirements/#:~:text=NBSIPSTR2) for formatting). In the METS files within the individual representation folders, this identifier **MUST** be identical to the name of the respective representation folder (see [NBSIPSTR11](/docs/dps/sip/structure-requirements/#:~:text=NBSIPSTR11) and [NBSIPSTR12](/docs/dps/sip/structure-requirements/#:~:text=NBSIPSTR12) for formatting). <br><br>This requirement is a stricter version of [CSIP1](https://earkcsip.dilcis.eu/#CSIP1) | **MUST** | **1..1** |
| **NBSIP2** | **Package name**<br>`mets/@LABEL`<br><br>A short text that provides the title or a description of the content of the information package. The value of the `mets/@LABEL` **SHOULD** match the "title" field in the API call. (see [Metadata Requirements](/docs/dps/api/submission/metadata/)).<br><br>This requirement is a stricter version of [SIP1](https://earksip.dilcis.eu/#SIP1) | **SHOULD** | **1..1** |

> [!IMPORTANT]
> In addition to these requirements for the METS root element, there are a few **media specific requirements** that needs to be adhered to. 
> These are found in the subpages below this page.

**Example:**

```xml
<mets xmlns="http://www.loc.gov/METS/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:sip="https://DILCIS.eu/XML/METS/SIPExtensionMETS"
    xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS"
    xmlns:xlink="http://www.w3.org/1999/xlink"    
    OBJID="no-nb_radio_NRKP2_199204081200"
    LABEL="no-nb_radio_NRKP2_199204081200"
    TYPE="Audio – On Tangible Medium (digital or analog)"
    csip:CONTENTINFORMATIONTYPE="OTHER"
    csip:OTHERCONTENTINFORMATIONTYPE="NB-METS-AUDIO-PROFILE-1.0"
    PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP-v2-2-0.xml"
    xsi:schemaLocation="http://www.loc.gov/METS/ schemas/mets1_12.xsd http://www.w3.org/1999/xlink schemas/xlink.xsd https://dilcis.eu/XML/METS/CSIPExtensionMETS schemas/DILCISExtensionMETS.xsd https://dilcis.eu/XML/METS/SIPExtensionMETS schemas/DILCISExtensionSIPMETS.xsd">
```




## Use of the METS header (`metsHdr`)

The purpose of the METS header section is to describe the METS document itself, for example information about the creator of the IP.

No further requirements beyond [CSIP METS Header](https://earkcsip.dilcis.eu/#useofthemetsheaderelementmetshdr) and [E-ARK SIP METS Profile](https://earksip.dilcis.eu/#e-arksipmetsprofile2.1requirements).


**Example:**

```xml
    <metsHdr CREATEDATE="2026-06-19T08:47:03.115+02:00" LASTMODDATE="2026-06-19T08:47:03.115+02:00" RECORDSTATUS="NEW" csip:OAISPACKAGETYPE="SIP">
        <agent ROLE="CREATOR" TYPE="OTHER" OTHERTYPE="SOFTWARE">
            <name>nifi-eark-nar,no.nb.nifi.processors.dps.eark.EarkSIPGenerator</name>
            <note csip:NOTETYPE="SOFTWARE VERSION">1.0.12</note>
        </agent>
        <agent ROLE="CREATOR" TYPE="ORGANIZATION">
            <name>National Library of Norway</name>
            <note csip:NOTETYPE="IDENTIFICATIONCODE"/>
        </agent>
    </metsHdr>

```





## Use of the METS descriptive metadata section (`dmdSec`)

The purpose of the METS descriptive metadata section is to refer to files containing descriptive metadata.

| **ID** | **Name, METS element, description** | **Requirement** | **Cardinality** |
|:---|:---|:---|:---|
| **NBSIP3** | **Descriptive metadata** <br>`mets/dmdSec`<br><br> **MUST** be used to refer to available descriptive metadata about the information package. Each descriptive metadata section (`<dmdSec>`) contains a single description and must be repeated if multiple descriptions exist. <br> See also [NBSIPSTR9](https://digitalpreservation.no/docs/dps/sip/structure-requirements/#:~:text=NBSIPSTR9) which requires at least one file containing descriptive metadata.<br><br>This requirement is a stricter version of [CSIP17](https://earkcsip.dilcis.eu/#CSIP17).  | **MUST** | **1..n** |
| **NBSIP4** | **Mandatory descriptive metadata** <br>`mets/dmdSec`<br><br> The element describing the descriptive metadata section **MUST** refer to the metadata file(s) specified in [NBSIPSTR9](https://digitalpreservation.no/docs/dps/sip/structure-requirements/#:~:text=NBSIPSTR9). It **MUST** be described using `mets/dmdSec/mdRef/@MDTYPE`. Valid values include: `MARC`, `MODS`, `EAD`, `DC`, `NISOIMG`, `LC-AV`, `VRA`, `TEIHDR`, `DDI`, `FGDC`, `LOM`, `PREMIS`, `PREMIS:OBJECT`, `PREMIS:AGENT`, `PREMIS:RIGHTS`, `PREMIS:EVENT`, `TEXTMD`, `METSRIGHTS`, `ISO 19115:2003 NAP`, `EAC-CPF`, `LIDO`, `OTHER`. If `OTHER` is selected, the type of metadata **SHOULD** be specified using `mets/dmdSec/mdRef/@OTHERMDTYPE`. <br><br> Administrative or preservation metadata may be included in accordance with [CSIP31-57](https://earkcsip.dilcis.eu/#useofthemetsadministrativemetadatasectionelementamdsec). <br> Note that certain types of metadata in the form of PREMIS-events are recommended to be submitted through the Submission API. You can read more about this [here](/docs/dps/api/submission/events/).| **MUST** | **1..n** |
| **NBSIP5** | **Reference to files with descriptive metadata**<br>`mets/dmdSec/mdRef`<br><br> **MUST** be used to refer to files containing descriptive metadata located in the `metadata/descriptive`. Directly embedding of metadata using `mets/dmdSec/mdWrap` is discouraged. <br><br> This requirement is a stricter version of [CSIP21](https://earkcsip.dilcis.eu/#CSIP21). | **MUST** | **1..n** |
| **NBSIP6** | **File checksum type**<br>`mets/dmdSec/mdRef/@CHECKSUMTYPE`<br><br> A value from the METS-standard which identifies the algorithm used to calculate the checksum for the referenced file. Checksum type **MUST** be : `MD5`.<br><br> This requirement is a stricter version of [CSIP29](https://earkcsip.dilcis.eu/#CSIP29) og [CSIP30](https://earkcsip.dilcis.eu/#CSIP30). | **MUST** | **1..1** |



**Example:** 

```xml
<dmdSec ID="uuid-e1d1f6db-3851-40bf-9ffd-59277a4442dc" CREATED="2025-01-16T12:43:32.894+01:00" STATUS="CURRENT">
    <mdRef ID="ID-uuid-861d36a1-043f-45aa-b230-be13517823a9" LOCTYPE="URL" MIMETYPE="application/json" SIZE="2038" CREATED="2025-01-16T12:43:32.894+01:00" 
    CHECKSUM="EB72EF8AB5B1C93801DFACBFE6AA8E27" CHECKSUMTYPE="MD5" MDTYPE="DC" xlink:type="simple" xlink:href="metadata/descriptive/nb_dublincore.json"/>
</dmdSec>
<dmdSec ID="uuid-EC8718B5-C417-4D8C-975B-C14CD8197E62" CREATED="2025-01-16T12:43:32.894+01:00" STATUS="CURRENT">
    <mdRef ID="ID-uuid-FAF602A1-AB9A-44AC-A24B-B918F7064920" LOCTYPE="URL" MIMETYPE="text/xml" SIZE="1903" CREATED="2025-01-16T12:43:32.894+01:00" 
    CHECKSUM="50E9C929EAE5B51F20F8B86D604FD24D" CHECKSUMTYPE="MD5" MDTYPE="MODS" xlink:type="simple" xlink:href="metadata/descriptive/MODS.xml"/>
</dmdSec>
```



## Use of the METS administrative metadata section (`amdSec`)

The E-ARK specification only defines how to reference digital provenance metadata (the `digiprovMD` section) and rights metadata (the `rightsMD` section) in METS.
Digital provenance metadata refers to information about events in the lifecycle of the digital object. This data is typically formatted using PREMIS. Note that certain types of metadata in the form of PREMIS-events are recommended to be submitted through the Submission API. You can read more about this here [Events/preservation metadata](/docs/dps/api/submission/events).
Rights metadata contains information about intellectual property rights (IPR) associated with the digital objects.

However, the specification also allows for the inclusion of technical metadata (`techMD` section) and source metadata (`sourceMD` section).
The National Library of Norway (NB) considers these metadata types essential for managing digital objects. Technical metadata describes the characteristics of the data itself, while source material metadata provides important context for the digital object and supports its authenticity. See also [NBSIPSTR16](/docs/dps/sip/structure-requirements/#:~:text=NBSIPSTR16) and [NBSIPSTR17](/docs/dps/sip/structure-requirements/#:~:text=NBSIPSTR17).



| **ID** | **Name, METS element, description** | **Requirement** | **Cardinality** |
|:---|:---|:---|:---|
| **NBSIP7** | **Source metadata**<br>`mets/amdSec/sourceMD`<br><br> **If** metadata about the source material for a representation is available in the information package, this element **MUST** be used to describe it. | **MUST** | **1..n** |
| **NBSIP8** | **Source metadata identifier**<br>`mets/amdSec/sourceMD/@ID`<br><br> An `xml:id` identifier for the source metadata section `mets/amdSec/sourceMD` used for internal references within the XML document. The identifier **MUST** be unique within the XML document. | **MUST** | **1..1** |
| **NBSIP9** | **Status of the source metadata**<br>`mets/amdSec/sourceMD/@STATUS`<br><br> Status **MUST** be set to `CURRENT` | **MUST** | **1..1** |
| **NBSIP10** | **Reference to files with the source metadata**<br>`mets/amdSec/sourceMD/mdRef`<br><br> **MUST** be used to reference files containing source metadata located in the `metadata/source` folder. <br><br> Direct embedding of metadata using `mets/amdSec/mdWrap` is discouraged. | **MUST** | **1..1** |
| **NBSIP11** | **Type of locator**<br>`mets/amdSec/sourceMD/mdRef[@LOCTYPE='URL']`<br><br> The locator type is always used with the value `URL` from [Vocabulary status](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyStatus.xml) in the E-ARK specifications. | **MUST** | **1..1** |
| **NBSIP12** | **Type of link**<br>`mets/amdSec/sourceMD/mdRef[@xlink:type='simple']`<br><br> The attribute **MUST** be used with the value `simple`. The vocabulary of allowed values is maintained by the XLink standard. | **MUST** | **1..1** |
| **NBSIP13** | **File location**<br>`mets/amdSec/sourceMD/mdRef/@xlink:href`<br><br> The actual location of the file. It **MUST** be referenced using a URL of the filepath type. | **MUST** | **1..1** |
| **NBSIP14** | **Type of metadata**<br>`mets/amdSec/sourceMD/mdRef/@MDTYPE`<br><br> Specifies the type of metadata in the referenced file. The values are taken from METS.<br>Valid values:<br> `MARC`, `MODS`, `EAD`, `DC`, `NISOIMG`, `LC-AV`, `VRA`, `TEIHDR`, `DDI`, `FGDC`, `LOM`, `PREMIS`, `PREMIS:OBJECT`, `PREMIS:AGENT`, `PREMIS:RIGHTS`, `PREMIS:EVENT`, `TEXTMD`, `METSRIGHTS`, `ISO 19115:2003 NAP`, `EAC-CPF`, `LIDO`, `OTHER`. If `OTHER` is chosen, the type of metadata **SHOULD** be described using `mets/amdSec/sourceMD/mdRef/@OTHERMDTYPE`. <br> Note that certain types of metadata in the form of PREMIS-events are recommended to be submitted through the Submission API. You can read more about this [here](/docs/dps/api/submission/events/).| **MUST** | **1..1** |
| **NBSIP15** | **Technical metadata**<br>`mets/amdSec/techMD`<br><br> **If** technical metadata for the data files in a representation is available in the information package, this element **MUST** be used to describe it. <br><br> Direct embedding of metadata using `mets/amdSec/mdWrap` is discouraged. | **SHOULD** | **0..n** |
| **NBSIP16** | **Technical metadata identifier**<br>`mets/amdSec/techMD/@ID`<br><br> An `xml:id` identifier for the technical metadata section `mets/amdSec/techMD` used for internal references within the XML document. The identifier **MUST** be unique within the XML document. | **MUST** | **1..1** |
| **NBSIP17** | **Status of the technical metadata**<br>`mets/amdSec/techMD/@STATUS`<br><br> Status **MUST** be set to `CURRENT` | **MUST** | **1..1** |
| **NBSIP18** | **Reference to files with the technical metadata**<br>`mets/amdSec/techMD/mdRef`<br><br> **MUST** be used to reference files containing technical metadata that are located in the folder `metadata/technical`. | **MUST** | **1..1** |
| **NBSIP19** | **Type of locator**<br>`mets/amdSec/techMD/mdRef[@LOCTYPE='URL']`<br><br> The locator type is always used with the value `URL` from [Vocabulary status](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyStatus.xml) in the E-ARK specifications. | **MUST** | **1..1** |
| **NBSIP20** | **Type of link**<br>`mets/amdSec/techMD/mdRef[@xlink:type='simple']`<br><br> The attribute **MUST** be used with the value `simple`. The vocabulary of allowed values is maintained by the XLink standard. | **MUST** | **1..1** |
| **NBSIP21** | **File location**<br>`mets/amdSec/techMD/mdRef/@xlink:href`<br><br> The actual location of the file. It **MUST** be referenced using a URL of the filepath type. | **MUST** | **1..1** |
| **NBSIP22** | **Type of metadata**<br>`mets/amdSec/techMD/mdRef/@MDTYPE`<br><br> Specifies the type of metadata in the referenced file. The values are taken from METS.<br>Valid values:<br> `MARC`, `MODS`, `EAD`, `DC`, `NISOIMG`, `LC-AV`, `VRA`, `TEIHDR`, `DDI`, `FGDC`, `LOM`, `PREMIS`, `PREMIS:OBJECT`, `PREMIS:AGENT`, `PREMIS:RIGHTS`, `PREMIS:EVENT`, `TEXTMD`, `METSRIGHTS`, `ISO 19115:2003 NAP`, `EAC-CPF`, `LIDO`, `OTHER`. If `OTHER` is chosen, the type of metadata **SHOULD** be described using `mets/amdSec/techMD/mdRef/@OTHERMDTYPE`. <br> Note that certain types of metadata in the form of PREMIS-events are recommended to be submitted through the Submission API. You can read more about this [here](/docs/dps/api/submission/events/). | **MUST** | **1..1** |
| **NBSIP23** | **File checksum type**<br>`mets/amdSec/digiprovMD/mdRef/@CHECKSUMTYPE, mets/amdSec/rightsMD/mdRef/@CHECKSUMTYPE, mets/amdSec/sourceMD/mdRef/@CHECKSUMTYPE, mets/amdSec/techMD/mdRef/@CHECKSUMTYPE`<br><br> A value from the METS-standard which identifies the algorithm used to calculate the checksum for the referenced file. Checksum type **MUST** be : `MD5`.<br><br> This requirement is a stricter version of [CSIP43](https://earkcsip.dilcis.eu/#CSIP43), [CSIP44](https://earkcsip.dilcis.eu/#CSIP44), [CSIP56](https://earkcsip.dilcis.eu/#CSIP56) og [CSIP57](https://earkcsip.dilcis.eu/#CSIP57). | **MUST** | **1..1** |



**Example:** 

```xml
<amdSec>
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
</amdSec>
```





## Use of the METS file section (`fileSec`)

The `fileSec` should describe every component of the IP not already described in the `amdSec` and `dmdSec` elements. Location and checksum values must be provided for all file entries.
The METS file section serves as a manifest, allowing users to ensure all files are present and that a package is complete, as well as testing the integrity of package files using checksum values.


|**ID** | **Name, METS element, description** | **Requirement** | **Cardinality** |
|:---|:---|:---|:---|
| **NBSIP24** | **Sjekksumtype**<br>`mets/fileSec/fileGrp/file/@CHECKSUMTYPE`<br><br> A value from the METS-standard which identifies the algorithm used to calculate the checksum for the referenced file. Checksum type **MUST** be : `MD5`.<br><br> This requirement is a stricter version of [CSIP71](https://earkcsip.dilcis.eu/#CSIP71) og [CSIP72](https://earkcsip.dilcis.eu/#CSIP72).  | **MUST** | **1..1** |



**Example:** 

```xml
<fileSec>
    <fileSec ID="file-sec-example">
        <mets:fileGrp ID="file-grp-doc" USE="Documentation">
        <mets:file ID="file-docx" 
        MIMETYPE="application/vnd.openxmlformats-officedocument.wordprocessingml.document" 
        SIZE="2554366" 
        CREATED="2012-08-15T12:08:15.432+01:00" 
        CHECKSUM="7ee30736137bfe72dc60afcbe374cb2a" CHECKSUMTYPE="MD5">
            <mets:FLocat LOCTYPE="URL" xlink:type="simple" xlink:href="documentation/File.docx">
</fileSec>
```



## Use of the METS structural map (`structMap`)

The METS structural map element provides an overview of the components described in the METS document. It can also link the elements in the structure to associated content files and metadata. 

No further requirements beyond [CSIP METS structural map](https://earkcsip.dilcis.eu/#useofthemetsstructuralmapelementstructmap) and [E-ARK SIP METS Profile](https://earksip.dilcis.eu/#e-arksipmetsprofile2.1requirements).


**Examples:**

METS example of the mandatory structural map including representations:

```xml
    <structMap ID="uuid-02BC407F-A6BB-4048-8DD5-757565935E3B" TYPE="PHYSICAL" LABEL="CSIP">
        <div ID="uuid-4C489BCC-1ABC-4EA6-A9B5-4B6B7052B0DB" TYPE="ORIGINAL" LABEL="primary_20140616">
            <div ID="uuid-F57F3C12-3E99-490B-ADE6-06AE3AFF8A46" ADMID="uuid-F1B0A220-29B4-4742-9660-5664EE2FD699 uuid-49F340DF-21E2-45B0-9C25-1ED048B4B8AE" LABEL="Metadata"/>
            <div ID="uuid-EEE68439-8E03-403A-A1E4-55E8E3C8E845" LABEL="Data">
                <fptr FILEID="uuid-DF9C02C3-24F9-4AC0-A033-44D8F8D739A8"/>
            </div>
        </div>
    </structMap>
```


METS example of the mandatory structural map:
```xml

    <structMap ID="uuid-4589BF89-1216-49B8-9C67-C484F906706F" TYPE="PHYSICAL" LABEL="CSIP">
        <div ID="uuid-9722E574-4302-4BC2-B0A9-2B9086CB9FD7" LABEL="digifilm_461518_20140616_FYAL00000181">
            <div ID="uuid-21B503AA-C31A-404A-A168-DEA933F4D367" DMDID="uuid-AF0A86FA-2CE4-41F7-BD61-34004C216342 uuid-B40B9E66-234E-498D-B413-B772D98927D8 uuid-4A9367D6-1272-4A1D-8AD8-D32161152CF5 uuid-470C79A7-9BAB-4637-B416-1367F40A5B52 uuid-19D3CCCA-D098-4FBB-84F1-21F2947B25B2 uuid-8B34AAC6-10AC-4B3C-921D-2B4A52F3CA7E uuid-E9C6212E-12A1-4C83-B77E-FACF41990623 uuid-6E5AFBC1-A883-4FEE-82BA-CABD149FBDD6 uuid-BA48EF33-7610-41D4-9753-A132760856FF uuid-A71910DD-F472-4D9C-AE43-B7EC0C88CCA0 uuid-2EE0FB24-66F4-4365-8579-79357800AD5E uuid-158DF561-FBA5-4057-9AA2-12492230BB53" LABEL="Metadata"/>
            <div ID="uuid-38407EB1-9882-4C54-88BA-B6D7DECCFC8A" LABEL="Schemas">
                <fptr FILEID="uuid-4C128011-D82E-41F1-AD03-C86290173DFB"/>
            </div>
            <div ID="uuid-070E9A64-C5E9-4634-9889-91912767143F" LABEL="Representations/primary_20140616">
                <mptr LOCTYPE="URL" xlink:type="simple" xlink:href="representations/primary_20140616/METS.xml" xlink:title="uuid-69FDE799-1A96-4F63-ABF6-69D6EE8F7900"/>
            </div>
        </div>
    </structMap>
 ```