---
title: Bruk av METS.xml
weight: 2
---

## Krav til bruk av METS.xml (SIP)

Informasjonspakker som avleveres til DPS, skal inneholde en fil kalt `METS.xml` i informasjonspakkas rotmappe, samt en `METS.xml` i hver representasjonsmappe.

Begge `METS.xml` må validere på metskravene gitt av E-ARK-spesifikasjonene [CSIP1-119](https://earkcsip.dilcis.eu/#useofmets) og [SIP1-35](https://earksip.dilcis.eu/#e-arksipmetsprofile2.1requirements) i [E-ARK (C)SIP spesifikasjonene v2.2.0](https://dilcis.eu/specifications/)
<br><br>

### Bruk av rotelementer i METS (`mets`)

<br>

| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:---|:---|:---|
| **NBSIP1** | **Pakkeidentifikator**<br>`mets/@OBJID`<br><br>Attributten `mets/@OBJID` er obligatorisk, verdien er en strengidentifikator for METS-fila. I METS-fila i pakkas rotmappe **MÅ** denne identifikatoren være det samme som navnet på pakkas rotmappe (se [NBSIPSTR2](https://digitalpreservation.no/nb/docs/dps/sip/1.0/structure/) for formatering). I METS-fil på de individuelle representasjonene **MÅ** denne identifikatoren være det samme som navnet på den relevante representasjonsmappa (se [NBSIPSTR11](https://digitalpreservation.no/nb/docs/dps/sip/1.0/structure-requirements/#:~:text=1..1-,NBSIPSTR11) og [NBSIPSTR12](https://digitalpreservation.no/nb/docs/dps/sip/1.0/structure-requirements/#:~:text=1..1-,NBSIPSTR12) for formatering). <br><br>Dette er en strengere, SIP-spesifikk variant av [CSIP1](https://earkcsip.dilcis.eu/#CSIP1) | **MÅ** | **1..1** |
| **NBSIP2** | **Pakkenavn**<br>`mets/@LABEL`<br><br>En kort tekst som oppgir tittelen eller beskrivelsen av innholdet i informasjonspakka. `mets/@LABEL` **BØR** være det samme som "title" i API-kall (se [krav til metadata](https://digitalpreservation.no/nb/docs/dps/interface/api/metadata/)).<br><br>Dette er en strengere variant av [SIP1](https://earksip.dilcis.eu/#SIP1) | **BØR** | **1..1** |


<br>

**Eksempel:**


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


### Bruk av METS header (`metsHdr`)
<br>

| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** | 
|:---|:---|:---|:---|
| **NBSIP3** | **Bevaringsavtale**<br>`metsHdr/altRecordID`<br><br>Det **MÅ** refereres til bevaringsavtalen pakka er levert innenfor. `@TYPE` må settes til verdien “SUBMISSONAGREEMENT”. (Eksempel på dette kommer). <br><br>Dette er en strengere variant av [SIP5](https://earksip.dilcis.eu/#SIP5) | **MÅ** | **1..1** |  |  |
| **NBSIP4** | **Avleverer-agent**<br>`metsHdr/agent` <br><br>Dette er et wrapper-element som lar deg oppgi navnet på organisasjonen eller personen som har avlevert informasjonspakka til Nasjonalbiblioteket. Avleverer trenger ikke være det samme som pakkeeier, som er presisert i bevaringsavtalen.<br><br>Dette er en spesifisering av [SIP15](https://earksip.dilcis.eu/#SIP15) | **MÅ** | **1..1** |  |  |
| **NBSIP5** | **Rolle for avleverer-agent (submitting agent)**<br>`metsHdr/agent/@ROLE`<br>  <br>Rollen til organisasjonen eller personen som har levert informasjonspakka til Nasjonalbiblioteket. Skal være satt til role=`”OTHER”` otherrole=`”SUBMITTER”`.<br><br>Dette er en strengere variant av [SIP16](https://earksip.dilcis.eu/#SIP16) | **MÅ** | **1..1** |  |  |
| **NBSIP6** | **Navn på avleverer-agent**<br>`metsHdr/agent/name`<br>  <br>Navnet på organisasjonen eller personen som har levert informasjonspakka til Nasjonalbiblioteket. <br>Personnavn skrives i invertert form. Organisasjonsnavn oppgis på originalspråk (slik som det vanligvis brukes). <br><br>Dette er en spesifisering av [SIP18](https://earksip.dilcis.eu/#SIP18) | **MÅ** | **1..1** |  |  |
| **NBSIP7** | **Tilleggsinformasjon om avleverer**<br>`metsHdr/agent/note`<br>  <br>Dette er et notatfelt der det **BØR** oppgis en unik identifikasjonskode for informasjonspakkas avleverer. For organisasjoner bør det oppgis organisasjonsnummer. For personer vil vi ha identifikator fra [Felles autoritetsregister](https://bibliotekutvikling.no/kunnskapsorganisering/vokabularer-utkast/felles-autoritetsregister-for-personer-og-korporasjoner/) for personer og korporasjoner, [ISNI](https://isni.org/), [VIAF](https://viaf.org/en) eller [ORCID](https://orcid.org/).<br><br>Dette er en strengere variant av [SIP19](https://earksip.dilcis.eu/#SIP19) | **BØR** | **0..1** |  |  |

<br>

**Eksempel:** 


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

### Bruk av deskriptive metadata i METS (`dmdSec`)
<br>

| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:---|:---|:---|
| **NBSIP8** | **Deskriptive metadata** <br>`mets/dmdSec`<br>  <br>**MÅ** brukes for å peke til tilgjengelige deskriptive metadata om informasjonspakka. Hver deskriptive metadataseksjon (`<dmdSec>`) inneholder en enkelt beskrivelse og må gjentas hvis det finnes flere beskrivelser. <br>Se også [NBSIPSTR9](https://digitalpreservation.no/nb/docs/dps/sip/1.0/structure-requirements/#:~:text=M%C3%85-,NBSIPSTR9) der det kreves minimum én fil med deskriptive metadata.<br><br>Dette er en strengere, SIP-spesifikk variant av [CSIP17](https://earkcsip.dilcis.eu/#CSIP17).  | **MÅ** | **1..n** |
| **NBSIP9** | **Påkrevde deskriptive metadata** <br>`mets/dmdSec`<br><br>Elementet som beskriver seksjonen for deskriptive metadata **MÅ** referere til metadatafilen(e) spesifisert i [NBSIPSTR9](https://digitalpreservation.no/nb/docs/dps/sip/1.0/structure-requirements/#:~:text=NBSIPSTR9). Den **MÅ** beskrives med `mets/dmdSec/mdRef/@MDTYPE`. Gyldige verdier: MARC, MODS, EAD, DC, NISOIMG, LC-AV, VRA, TEIHDR, DDI, FGDC, LOM, PREMIS, PREMIS:OBJECT, PREMIS:AGENT, PREMIS:RIGHTS, PREMIS:EVENT, TEXTMD, METSRIGHTS, ISO 19115:2003 NAP, EAC-CPF, LIDO, OTHER. Hvis man velger '`OTHER`' **BØR** man beskrive hva slags metadatatype det er med `mets/dmdSec/mdRef/@MDOTHERTYPE`. <br><br>Administrative metadata eller bevaringsmetadata kan legges ved i henhold til [CSIP31-57](https://earkcsip.dilcis.eu/#useofthemetsadministrativemetadatasectionelementamdsec). | **MÅ** | **1..n** |
| **NBSIP10** | **Referanser til filer med deskriptive metadata**<br>`mets/dmdSec/mdRef`<br><br>**MÅ** brukes for å peke til filer med deskriptive metadata som befinner seg i mappa `metadata/descriptive`. Direkte embedding av metadata ved hjelp av `mets/dmdSec/mdWrap` frarådes.<br><br>Dette er en strengere, SIP-spesifikk versjon av [CSIP21](https://earkcsip.dilcis.eu/#CSIP21). | **MÅ** | **1..n** |
| **NBSIP11** | **Sjekksumtype**<br>`mets/dmdSec/mdRef/@CHECKSUMTYPE`<br><br>En verdi fra METS-standarden som angir hvilken algoritme som er brukt for å beregne sjekksummen for den refererte filen. Sjekksumtype **MÅ** være: CHECKSUMTYPE="MD5".<br><br>Dette er en strengere variant av [CSIP29](https://earkcsip.dilcis.eu/#CSIP29) og [CSIP30](https://earkcsip.dilcis.eu/#CSIP30). | **MÅ** | **1..1** |

<br>


**Eksempel:** 

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


### Bruk av administrative metadata i METS (`amdSec`)

E-ARK-spesifikasjonenen legger kun føringer for hvordan man refererer til digital proveniensmetadata (`digiprovMD`-seksjonen) og rettighetsmetadata (`rightsMD`-seksjonen) i METS. Digital proveniensmetadata er informasjon om hendelser i det digitale objektets livssyklus. Dette er data som typisk formateres i PREMIS. Rettighetsmetadata er informasjon om immaterielle rettigheter/intellektuell eiendomsrett (IPR) knyttet til de digitale objektene.

Spesifikasjonene åpner derimot også for å oppgi tekniske (`techMD`-seksjonen) og kildematerialemetadata (`sourceMD`-seksjonen). Dette er metadata NB mener spiller en viktig rolle i forvaltningen av digitale objekter. Tekniske metadata forklarer hva dataene er for noe, mens kildematerialemetadata gir viktig kontekst for det digitale objektet, samt underbygger dets autentisitet. Se også [NBSIPSTR16](https://digitalpreservation.no/nb/docs/dps/sip/1.0/structure-requirements/#:~:text=NBSIPSTR16) og [NBSIPSTR17](https://digitalpreservation.no/nb/docs/dps/sip/1.0/structure-requirements/#:~:text=NBSIPSTR17).

<br>
<br>



| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:---|:---|:---|
| **NBSIP12** | **Kildematerialemetadata**<br>`mets/amdSec/sourceMD`<br><br>**Hvis** metadata om kildematerialet for en representasjon er tilgjengelig i informasjonspakka, **MÅ** dette elementet brukes til å beskrive dette. | **MÅ** | **1..n** |
| **NBSIP13** | **Identifikator for kildematerialemetadata**<br>`mets/amdSec/sourceMD/@ID`<br><br>En `xml:id` identifikator for seksjonen for kildematerialemetadata `mets/amdSec/sourceMD` som brukes for interne referanser innenfor XML-dokumentet. Identifikatoren **MÅ** være unik innenfor XML-dokumentet. | **MÅ** | **1..1** |
| **NBSIP14** | **Status for kildematerialemetadata**<br>`mets/amdSec/sourceMD/@STATUS`<br><br>Status **MÅ** settes til `'CURRENT'` | **MÅ** | **1..1** |
| **NBSIP15** | **Referanser til filer med kildematerialemetadata**<br>`mets/amdSec/sourceMD/mdRef`<br><br>**MÅ** brukes for å peke til filer med kildematerialemetadata som befinner seg i mappa metadata/source.<br> <br>Direkte embedding av metadata ved hjelp av `mets/amdSec/mdWrap` frarådes. | **MÅ** | **1..1** |
| **NBSIP16** | **Type locator**<br>`mets/amdSec/sourceMD/mdRef[@LOCTYPE='URL']`<br><br>Locatortypen er alltid brukt med verdien `'URL'` fra [statusvokabularet](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyStatus.xml) i E-ARK-spesifikasjonene. | **MÅ** | **1..1** |
| **NBSIP17** | **Type lenke**<br>`mets/amdSec/sourceMD/mdRef[@xlink:type='simple']`<br><br>Attributten **MÅ** brukes med verdien '`simple`'. Vokabularet med mulige verdier er vedlikeholdt av xlink-standarden. | **MÅ** | **1..1** |
| **NBSIP18** | **Filplassering**<br>`mets/amdSec/sourceMD/mdRef/@xlink:href`<br><br>Den faktiske plasseringen til fila. Den skal refereres til med URL type filepath. | **MÅ** | **1..1** |
| **NBSIP19** | **Type metadata**<br>`mets/amdSec/sourceMD/mdRef/@MDTYPE`<br><br>Spesifiserer typen metadata i den refererte fila. Verdiene er hentet fra METS. <br>Gyldige verdier:<br>MARC, MODS, EAD, DC, NISOIMG, LC-AV, VRA, TEIHDR, DDI, FGDC, LOM, PREMIS, PREMIS:OBJECT, PREMIS:AGENT, PREMIS:RIGHTS, PREMIS:EVENT, TEXTMD, METSRIGHTS, ISO 19115:2003 NAP, EAC-CPF, LIDO, OTHER. Hvis man velger '`OTHER`' **BØR** man beskrive hva slags metadatatype det er med `mets/amdSec/sourceMD/mdRef/@MDOTHERTYPE`.| **MÅ** | **1..1** |
| **NBSIP20** | **Tekniske metadata**<br>`mets/amdSec/techMD`<br><br>**Hvis** tekniske metadata for datafilene i en representasjon er tilgjengelig i informasjonspakka, **MÅ** dette elementet brukes til å beskrive dette.<br><br>Direkte embedding av metadata ved hjelp av `mets/amdSec/mdWrap` frarådes. | **MÅ** | **1..n** |
| **NBSIP21** | **Identifikator for tekniske metadata**<br>`mets/amdSec/techMD/@ID`<br><br>En `xml:id` identifikator for seksjonen for tekniske metadata `mets/amdSec/techMD` som brukes for interne referanser innenfor XML-dokumentet. Identifikatoren **MÅ** være unik innenfor XML-dokumentet. | **MÅ** | **1..1** |
| **NBSIP22** | **Status for tekniske metadata**<br>`mets/amdSec/techMD/@STATUS`<br><br>Status **MÅ** settes til '`CURRENT`' | **MÅ** | **1..1** |
| **NBSIP23** | **Referanser til filer med tekniske metadata**<br>`mets/amdSec/techMD/mdRef`<br><br>**MÅ** brukes for å peke til filer med tekniske metadata som befinner seg i mappa `metadata/technical`. | **MÅ** | **1..1** |
| **NBSIP24** | **Type locator**<br>`mets/amdSec/techMD/mdRef[@LOCTYPE='URL']`<br><br>Locatortypen er alltid brukt med verdien '`URL`' fra [statusvokabularet](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyStatus.xml) i E-ARK-spesifikasjonene. | **MÅ** | **1..1** |
| **NBSIP25** | **Type lenke**<br>`mets/amdSec/techMD/mdRef[@xlink:type='simple']`<br><br>Attributten **MÅ** brukes med verdien '`simple`'. Vokabularet med mulige verdier er vedlikeholdt av xlink-standarden. | **MÅ** | **1..1** |
| **NBSIP26** | **Filplassering**<br>`mets/amdSec/techMD/mdRef/@xlink:href`<br><br>Den faktiske plasseringen til fila. Den skal refereres til med URL type filepath. | **MÅ** | **1..1** |
| **NBSIP27** | **Type metadata**<br>`mets/amdSec/techMD/mdRef/@MDTYPE`<br><br>Spesifiserer typen metadata i den refererte fila. Verdiene er hentet fra METS. Gyldige verdier:<br>MARC, MODS, EAD, DC, NISOIMG, LC-AV, VRA, TEIHDR, DDI, FGDC, LOM, PREMIS, PREMIS:OBJECT, PREMIS:AGENT, PREMIS:RIGHTS, PREMIS:EVENT, TEXTMD, METSRIGHTS, ISO 19115:2003 NAP, EAC-CPF, LIDO, OTHER. Hvis man velger '`OTHER`' **BØR** man beskrive hva slags metadatatype det er med `mets/amdSec/techMD/mdRef/@MDOTHERTYPE`.  | **MÅ** | **1..1** |
| **NBSIP28** | **Sjekksumtype**<br>`mets/amdSec/digiprovMD/mdRef/@CHECKSUMTYPE, mets/amdSec/rightsMD/mdRef/@CHECKSUMTYPE, mets/amdSec/sourceMD/mdRef/@CHECKSUMTYPE, mets/amdSec/techMD/mdRef/@CHECKSUMTYPE`<br><br> Verdi fra METS-standarden som angir hvilken algoritme som er brukt for å beregne sjekksummen for den refererte filen. Sjekksumtype **MÅ** være: CHECKSUMTYPE="MD5".<br><br>Dette er en strengere variant av [CSIP43](https://earkcsip.dilcis.eu/#CSIP43), [CSIP44](https://earkcsip.dilcis.eu/#CSIP44), [CSIP56](https://earkcsip.dilcis.eu/#CSIP56) og [CSIP57](https://earkcsip.dilcis.eu/#CSIP57).  | **MÅ** | **1..1** |

<br>

**Eksempel:** 

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


### Bruk av METS filseksjon (`fileSec`)

| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:---|:---|:---|
| **NBSIP29** | **Sjekksumtype**<br>`mets/fileSec/fileGrp/file/@CHECKSUMTYPE`<br><br> Verdi fra METS-standarden som angir hvilken algoritme som er brukt for å beregne sjekksummen for den refererte filen. Sjekksumtype **MÅ** være: CHECKSUMTYPE="MD5".<br><br>Dette er en strengere variant av [CSIP71](https://earkcsip.dilcis.eu/#CSIP71) og [CSIP72](https://earkcsip.dilcis.eu/#CSIP72) | **MÅ** | **1..1** |

<br>

**Eksempel:**

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

### Bruk av METS strukturkart (`structMap`)

Ingen Krav utover [CSIP](https://earkcsip.dilcis.eu/#useofthemetsstructuralmapelementstructmap).