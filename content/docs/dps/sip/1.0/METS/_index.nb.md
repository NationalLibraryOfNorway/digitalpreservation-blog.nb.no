---
title: Krav til METS.xml
weight: 4
---

METS.xml er et XML-dokument som følger [METS-standarden](https://www.loc.gov/standards/mets/) (Metadata Encoding and Transmission Standard). Den brukes til å samle og strukturere metadata for et digitalt objekt i én fil. Filen fungerer som et kontroll- og koblingsdokument som gjør det mulig for systemer å forstå, validere og utveksle komplekse digitale objekter på en standardisert måte. 

METS.xml beskriver:
- Strukturen til objektet (for eksempel hvordan sider, kapitler eller filer henger sammen). 
- Filreferanser til de digitale filene som inngår (bilder, PDF-er, lydfiler osv). 
- Metadata som kan være både beskrivende, administrative og tekniske, ofte ved å peke til eller inkludere andre metadataformater. 

Informasjonspakker som avleveres til DPS, må inneholde en METS.xml i informasjonspakkas rotmappe, i tillegg til en METS.xml i hver representasjonsmappe. 

Begge METS.xml må validere på metskravene gitt av E-ARK-spesifikasjonene [CSIP1-119](https://earkcsip.dilcis.eu/#useofmets) og [SIP1-35](https://earksip.dilcis.eu/#e-arksipmetsprofile2.1requirements) i [E-ARK (C)SIP spesifikasjonene v2.2.0](https://dilcis.eu/specifications/), i tillegg til Nasjonalbibliotekets spesifiseringer av SIP-krav nedenfor (NBSIP).


### Bruk av rotelementer i METS (`mets`)

| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:---|:---|:---|
| **NBSIP1** | **Pakkeidentifikator**<br>`mets/@OBJID`<br><br>Attributten `mets/@OBJID` er obligatorisk, verdien er en strengidentifikator for METS-fila. I METS-fila i pakkas rotmappe **MÅ** denne identifikatoren være det samme som navnet på pakkas rotmappe (se [NBSIPSTR2](/nb/docs/dps/sip/1.0/structure-requirements/#:~:text=NBSIPSTR2) for formatering). I METS-fil på de individuelle representasjonene **MÅ** denne identifikatoren være det samme som navnet på den relevante representasjonsmappa (se [NBSIPSTR11](/nb/docs/dps/sip/1.0/structure-requirements/#:~:text=NBSIPSTR11) og [NBSIPSTR12](/nb/docs/dps/sip/1.0/structure-requirements/#:~:text=NBSIPSTR12) for formatering). <br><br>Dette er en strengere, SIP-spesifikk variant av [CSIP1](https://earkcsip.dilcis.eu/#CSIP1) | **MÅ** | **1..1** |
| **NBSIP2** | **Pakkenavn**<br>`mets/@LABEL`<br><br>En kort tekst som oppgir tittelen eller beskrivelsen av innholdet i informasjonspakka. `mets/@LABEL` **BØR** være det samme som "title" i API-kall (se [krav til metadata](/nb/docs/dps/api/submission/metadata/)).<br><br>Dette er en strengere variant av [SIP1](https://earksip.dilcis.eu/#SIP1) | **BØR** | **1..1** |

> [!IMPORTANT]
> I tillegg til disse kravene til rotelementene i METS, er det også et par **mediespesifikke** krav som må følges. 
> Disse kan finnes på undersidene til denne sida.

**Eksempel:**


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




### Bruk av METS header (`metsHdr`) 
Ingen krav utover [CSIP METS Header](https://earkcsip.dilcis.eu/#useofthemetsheaderelementmetshdr).





### Bruk av deskriptive metadata i METS (`dmdSec`)


| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:---|:---|:---|
| **NBSIP3** | **Deskriptive metadata** <br>`mets/dmdSec`<br>  <br>**MÅ** brukes for å peke til tilgjengelige deskriptive metadata om informasjonspakka. Hver deskriptive metadataseksjon (`<dmdSec>`) inneholder en enkelt beskrivelse og må gjentas hvis det finnes flere beskrivelser. <br>Se også [NBSIPSTR9](/nb/docs/dps/sip/1.0/structure-requirements/#:~:text=M%C3%85-,NBSIPSTR9) der det kreves minimum én fil med deskriptive metadata.<br><br>Dette er en strengere, SIP-spesifikk variant av [CSIP17](https://earkcsip.dilcis.eu/#CSIP17).  | **MÅ** | **1..n** |
| **NBSIP4** | **Påkrevde deskriptive metadata** <br>`mets/dmdSec`<br><br>Elementet som beskriver seksjonen for deskriptive metadata **MÅ** referere til metadatafilen(e) spesifisert i [NBSIPSTR9](nb/docs/dps/sip/1.0/structure-requirements/#:~:text=NBSIPSTR9). Den **MÅ** beskrives med `mets/dmdSec/mdRef/@MDTYPE`. Gyldige verdier: `MARC`, `MODS`, `EAD`, `DC`, `NISOIMG`, `LC-AV`, `VRA`, `TEIHDR`, `DDI`, `FGDC`, `LOM`, `PREMIS`, `PREMIS:OBJECT`, `PREMIS:AGENT`, `PREMIS:RIGHTS`, `PREMIS:EVENT`, `TEXTMD`, `METSRIGHTS`, `ISO 19115:2003 NAP`, `EAC-CPF`, `LIDO`, `OTHER`. Hvis man velger `OTHER` **BØR** man beskrive hva slags metadatatype det er med `mets/dmdSec/mdRef/@MDOTHERTYPE`. <br><br>Administrative metadata eller bevaringsmetadata kan legges ved i henhold til [CSIP31-57](https://earkcsip.dilcis.eu/#useofthemetsadministrativemetadatasectionelementamdsec). <br> Merk at noen typer metadata i form av PREMIS-eventer anbefales avlevert via submission API, se mer om det [her](/nb/docs/dps/sip/1.0/mets/nb/docs/dps/api/submission/Events).| **MÅ** | **1..n** |
| **NBSIP5** | **Referanser til filer med deskriptive metadata**<br>`mets/dmdSec/mdRef`<br><br>**MÅ** brukes for å peke til filer med deskriptive metadata som befinner seg i mappa `metadata/descriptive`. Direkte embedding av metadata ved hjelp av `mets/dmdSec/mdWrap` frarådes.<br><br>Dette er en strengere, SIP-spesifikk versjon av [CSIP21](https://earkcsip.dilcis.eu/#CSIP21). | **MÅ** | **1..n** |
| **NBSIP6** | **Sjekksumtype**<br>`mets/dmdSec/mdRef/@CHECKSUMTYPE`<br><br>En verdi fra METS-standarden som angir hvilken algoritme som er brukt for å beregne sjekksummen for den refererte filen. Sjekksumtype **MÅ** være : `MD5`.<br><br>Dette er en strengere variant av [CSIP29](https://earkcsip.dilcis.eu/#CSIP29) og [CSIP30](https://earkcsip.dilcis.eu/#CSIP30). | **MÅ** | **1..1** |




**Eksempel:** 

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





### Bruk av administrative metadata i METS (`amdSec`)

E-ARK-spesifikasjonenen legger kun føringer for hvordan man refererer til digital proveniensmetadata (`digiprovMD`-seksjonen) og rettighetsmetadata (`rightsMD`-seksjonen) i METS. Digital proveniensmetadata er informasjon om hendelser i det digitale objektets livssyklus. Dette er data som typisk formateres i PREMIS. Merk at noen typer metadata i form av PREMIS-eventer anbefales avlevert i Submission API, se mer om det her: [Eventer/bevaringsmetadata](/nb/content/docs/dps/api/submission/Events).  Rettighetsmetadata er informasjon om immaterielle rettigheter/intellektuell eiendomsrett (IPR) knyttet til de digitale objektene.

Spesifikasjonene åpner derimot også for å oppgi tekniske (`techMD`-seksjonen) og kildematerialemetadata (`sourceMD`-seksjonen). Dette er metadata NB mener spiller en viktig rolle i forvaltningen av digitale objekter. Tekniske metadata forklarer hva dataene er for noe, mens kildematerialemetadata gir viktig kontekst for det digitale objektet, samt underbygger dets autentisitet. Se også [NBSIPSTR16](/nb/docs/dps/sip/1.0/structure-requirements/#:~:text=NBSIPSTR16) og [NBSIPSTR17](/nb/docs/dps/sip/1.0/structure-requirements/#:~:text=NBSIPSTR17).




| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:---|:---|:---|
| **NBSIP7** | **Kildematerialemetadata**<br>`mets/amdSec/sourceMD`<br><br>**Hvis** metadata om kildematerialet for en representasjon er tilgjengelig i informasjonspakka, **MÅ** dette elementet brukes til å beskrive dette. | **MÅ** | **1..n** |
| **NBSIP8** | **Identifikator for kildematerialemetadata**<br>`mets/amdSec/sourceMD/@ID`<br><br>En `xml:id` identifikator for seksjonen for kildematerialemetadata `mets/amdSec/sourceMD` som brukes for interne referanser innenfor XML-dokumentet. Identifikatoren **MÅ** være unik innenfor XML-dokumentet. | **MÅ** | **1..1** |
| **NBSIP9** | **Status for kildematerialemetadata**<br>`mets/amdSec/sourceMD/@STATUS`<br><br>Status **MÅ** settes til `CURRENT` | **MÅ** | **1..1** |
| **NBSIP10** | **Referanser til filer med kildematerialemetadata**<br>`mets/amdSec/sourceMD/mdRef`<br><br>**MÅ** brukes for å peke til filer med kildematerialemetadata som befinner seg i mappa metadata/source.<br> <br>Direkte embedding av metadata ved hjelp av `mets/amdSec/mdWrap` frarådes. | **MÅ** | **1..1** |
| **NBSIP11** | **Type locator**<br>`mets/amdSec/sourceMD/mdRef[@LOCTYPE='URL']`<br><br>Locatortypen er alltid brukt med verdien `URL` fra [statusvokabularet](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyStatus.xml) i E-ARK-spesifikasjonene. | **MÅ** | **1..1** |
| **NBSIP12** | **Type lenke**<br>`mets/amdSec/sourceMD/mdRef[@xlink:type='simple']`<br><br>Attributten **MÅ** brukes med verdien `simple`. Vokabularet med mulige verdier er vedlikeholdt av xlink-standarden. | **MÅ** | **1..1** |
| **NBSIP13** | **Filplassering**<br>`mets/amdSec/sourceMD/mdRef/@xlink:href`<br><br>Den faktiske plasseringen til fila. Den skal refereres til med URL type filepath. | **MÅ** | **1..1** |
| **NBSIP14** | **Type metadata**<br>`mets/amdSec/sourceMD/mdRef/@MDTYPE`<br><br>Spesifiserer typen metadata i den refererte fila. Verdiene er hentet fra METS. <br>Gyldige verdier:<br>`MARC`, `MODS`, `EAD`, `DC`, `NISOIMG`, `LC-AV`, `VRA`, `TEIHDR`, `DDI`, `FGDC`, `LOM`, `PREMIS`, `PREMIS:OBJECT`, `PREMIS:AGENT`, `PREMIS:RIGHTS`, `PREMIS:EVENT`, `TEXTMD`, `METSRIGHTS`, `ISO 19115:2003 NAP`, `EAC-CPF`, `LIDO`, `OTHER`. Hvis man velger `OTHER` **BØR** man beskrive hva slags metadatatype det er med `mets/amdSec/sourceMD/mdRef/@MDOTHERTYPE`. <br> Merk at noen typer metadata i form av PREMIS-eventer anbefales avlevert via submission API, se mer om det [her](/nb/docs/dps/sip/1.0/mets/nb/docs/dps/api/submission/Events).| **MÅ** | **1..1** |
| **NBSIP15** | **Tekniske metadata**<br>`mets/amdSec/techMD`<br><br>**Hvis** tekniske metadata for datafilene i en representasjon er tilgjengelig i informasjonspakka, **MÅ** dette elementet brukes til å beskrive dette.<br><br>Direkte embedding av metadata ved hjelp av `mets/amdSec/mdWrap` frarådes. | **MÅ** | **1..n** |
| **NBSIP16** | **Identifikator for tekniske metadata**<br>`mets/amdSec/techMD/@ID`<br><br>En `xml:id` identifikator for seksjonen for tekniske metadata `mets/amdSec/techMD` som brukes for interne referanser innenfor XML-dokumentet. Identifikatoren **MÅ** være unik innenfor XML-dokumentet. | **MÅ** | **1..1** |
| **NBSIP17** | **Status for tekniske metadata**<br>`mets/amdSec/techMD/@STATUS`<br><br>Status **MÅ** settes til `CURRENT` | **MÅ** | **1..1** |
| **NBSIP18** | **Referanser til filer med tekniske metadata**<br>`mets/amdSec/techMD/mdRef`<br><br>**MÅ** brukes for å peke til filer med tekniske metadata som befinner seg i mappa `metadata/technical`. | **MÅ** | **1..1** |
| **NBSIP19** | **Type locator**<br>`mets/amdSec/techMD/mdRef[@LOCTYPE='URL']`<br><br>Locatortypen er alltid brukt med verdien `URL` fra [statusvokabularet](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyStatus.xml) i E-ARK-spesifikasjonene. | **MÅ** | **1..1** |
| **NBSIP20** | **Type lenke**<br>`mets/amdSec/techMD/mdRef[@xlink:type='simple']`<br><br>Attributten **MÅ** brukes med verdien `simple`. Vokabularet med mulige verdier er vedlikeholdt av xlink-standarden. | **MÅ** | **1..1** |
| **NBSIP21** | **Filplassering**<br>`mets/amdSec/techMD/mdRef/@xlink:href`<br><br>Den faktiske plasseringen til fila. Den skal refereres til med URL type filepath. | **MÅ** | **1..1** |
| **NBSIP22** | **Type metadata**<br>`mets/amdSec/techMD/mdRef/@MDTYPE`<br><br>Spesifiserer typen metadata i den refererte fila. Verdiene er hentet fra METS. Gyldige verdier:<br>`MARC`, `MODS`, `EAD`, `DC`, `NISOIMG`, `LC-AV`, `VRA`, `TEIHDR`, `DDI`, `FGDC`, `LOM`, `PREMIS`, `PREMIS:OBJECT`, `PREMIS:AGENT`, `PREMIS:RIGHTS`, `PREMIS:EVENT`, `TEXTMD`, `METSRIGHTS`, `ISO 19115:2003 NAP`, `EAC-CPF`, `LIDO`, `OTHER`. Hvis man velger `OTHER` **BØR** man beskrive hva slags metadatatype det er med `mets/amdSec/techMD/mdRef/@MDOTHERTYPE`.<br> Merk at noen typer metadata i form av PREMIS-eventer anbefales avlevert via submission API, se mer om det [her](/nb/docs/dps/sip/1.0/mets/nb/docs/dps/api/submission/Events). | **MÅ** | **1..1** |
| **NBSIP23** | **Sjekksumtype**<br>`mets/amdSec/digiprovMD/mdRef/@CHECKSUMTYPE, mets/amdSec/rightsMD/mdRef/@CHECKSUMTYPE, mets/amdSec/sourceMD/mdRef/@CHECKSUMTYPE, mets/amdSec/techMD/mdRef/@CHECKSUMTYPE`<br><br> Verdi fra METS-standarden som angir hvilken algoritme som er brukt for å beregne sjekksummen for den refererte filen. Sjekksumtype **MÅ** være : `MD5`.<br><br>Dette er en strengere variant av [CSIP43](https://earkcsip.dilcis.eu/#CSIP43), [CSIP44](https://earkcsip.dilcis.eu/#CSIP44), [CSIP56](https://earkcsip.dilcis.eu/#CSIP56) og [CSIP57](https://earkcsip.dilcis.eu/#CSIP57).  | **MÅ** | **1..1** |




**Eksempel:** 

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






### Bruk av METS filseksjon (`fileSec`)

| **ID** | **Navn, METS-element, beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:---|:---|:---|
| **NBSIP24** | **Sjekksumtype**<br>`mets/fileSec/fileGrp/file/@CHECKSUMTYPE`<br><br> Verdi fra METS-standarden som angir hvilken algoritme som er brukt for å beregne sjekksummen for den refererte filen. Sjekksumtype **MÅ** være : `MD5`.<br><br>Dette er en strengere variant av [CSIP71](https://earkcsip.dilcis.eu/#CSIP71) og [CSIP72](https://earkcsip.dilcis.eu/#CSIP72).  | **MÅ** | **1..1** |



**Eksempel:** 

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



### Bruk av METS strukturkart (`structMap`)

Ingen krav utover [CSIP METS structural map](https://earkcsip.dilcis.eu/#useofthemetsstructuralmapelementstructmap).