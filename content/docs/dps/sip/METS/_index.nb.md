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

METS-dokumentets rotelement (`mets`) beskriver overordnet informasjonen som lagres og/eller utveksles.

| **ID**     | **Navn, METS-element, beskrivelse**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **Krav** | **Kardinalitet** |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------------|
| **NBSIP1** | **Pakkeidentifikator**<br>`mets/@OBJID`<br><br>Attributten `mets/@OBJID` er obligatorisk, verdien er en strengidentifikator for METS-fila. I METS-fila i pakkas rotmappe **MÅ** denne identifikatoren være det samme som navnet på pakkas rotmappe (se [NBSIPSTR2](/nb/docs/dps/sip/structure-requirements/#:~:text=NBSIPSTR2) for formatering). I METS-fil på de individuelle representasjonene **MÅ** denne identifikatoren være det samme som navnet på den relevante representasjonsmappa (se [NBSIPSTR11](/nb/docs/dps/sip/structure-requirements/#:~:text=NBSIPSTR11) og [NBSIPSTR12](/nb/docs/dps/sip/structure-requirements/#:~:text=NBSIPSTR12) for formatering). <br><br>Dette er en strengere, SIP-spesifikk variant av [CSIP1](https://earkcsip.dilcis.eu/#CSIP1) | **MÅ**   | **1..1**         |
| **NBSIP2** | **Pakkenavn**<br>`mets/@LABEL`<br><br>En kort tekst som oppgir tittelen eller beskrivelsen av innholdet i informasjonspakka. `mets/@LABEL` **BØR** være det samme som "title" i API-kall (se [krav til metadata](/nb/docs/dps/api/submission/metadata/)).<br><br>Dette er en strengere variant av [SIP1](https://earksip.dilcis.eu/#SIP1)                                                                                                                                                                                                                                                                                                                                                                                                                                     | **BØR**  | **1..1**         |

> [!IMPORTANT]
> I tillegg til disse kravene til rotelementene i METS, er det også et par **mediespesifikke** krav som må følges. 
> Disse kan finnes på undersidene til denne sida.

**Eksempel:**


```xml
<mets xmlns="http://www.loc.gov/METS/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:sip="https://DILCIS.eu/XML/METS/SIPExtensionMETS"
  xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS"
  xmlns:xlink="http://www.w3.org/1999/xlink" OBJID="no-nb_radio_NRKP2_199204081200"
  LABEL="no-nb_radio_NRKP2_199204081200" TYPE="Audio – On Tangible Medium (digital or analog)"
  csip:CONTENTINFORMATIONTYPE="OTHER"
  csip:OTHERCONTENTINFORMATIONTYPE="NB-METS-AUDIO-PROFILE-1.0"
  PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP-v2-2-0.xml"
  xsi:schemaLocation="http://www.loc.gov/METS/ schemas/mets1_12.xsd http://www.w3.org/1999/xlink schemas/xlink.xsd https://dilcis.eu/XML/METS/CSIPExtensionMETS schemas/DILCISExtensionMETS.xsd https://dilcis.eu/XML/METS/SIPExtensionMETS schemas/DILCISExtensionSIPMETS.xsd"
  />
```




### Bruk av METS header (`metsHdr`) 

Formålet med METS-headerseksjonen er å beskrive selve METS-dokumentet, for eksempel informasjon om oppretteren av informasjonspakken (IP).

Ingen krav utover [CSIP METS Header](https://earkcsip.dilcis.eu/#useofthemetsheaderelementmetshdr) og [E-ARK SIP METS-profil](https://earksip.dilcis.eu/#e-arksipmetsprofile2.1requirements).

**Eksempel:**

```XML
<metsHdr CREATEDATE="2026-06-19T08:47:03.115+02:00" LASTMODDATE="2026-06-19T08:47:03.115+02:00"
  RECORDSTATUS="NEW" csip:OAISPACKAGETYPE="SIP">
  <agent ROLE="CREATOR" TYPE="OTHER" OTHERTYPE="SOFTWARE">
    <name>nifi-eark-nar,no.nb.nifi.processors.dps.eark.EarkSIPGenerator</name>
    <note csip:NOTETYPE="SOFTWARE VERSION">1.0.0</note>
  </agent>
  <agent ROLE="CREATOR" TYPE="ORGANIZATION">
    <name>National Library of Norway</name>
    <note csip:NOTETYPE="IDENTIFICATIONCODE"/>
  </agent>
</metsHdr>
```



### Bruk av deskriptive metadata i METS (`dmdSec`)

Formålet med METS-seksjonen for deskriptive metadata er å referere til filer som inneholder denne typen metadata. 


| **ID**     | **Navn, METS-element, beskrivelse**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Krav** | **Kardinalitet** |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------------|
| **NBSIP3** | **Deskriptive metadata** <br>`mets/dmdSec`<br>  <br>**MÅ** brukes for å peke til tilgjengelige deskriptive metadata om informasjonspakka. Hver deskriptive metadataseksjon (`<dmdSec>`) inneholder en enkelt beskrivelse og må gjentas hvis det finnes flere beskrivelser. <br>Se også [NBSIPSTR9](/nb/docs/dps/sip/structure-requirements/#:~:text=M%C3%85-,NBSIPSTR9) der det kreves minimum én fil med deskriptive metadata.<br><br>Dette er en strengere, SIP-spesifikk variant av [CSIP17](https://earkcsip.dilcis.eu/#CSIP17).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **MÅ**   | **1..n**         |
| **NBSIP4** | **Påkrevde deskriptive metadata** <br>`mets/dmdSec`<br><br>Elementet som beskriver seksjonen for deskriptive metadata **MÅ** referere til metadatafilen(e) spesifisert i [NBSIPSTR9](nb/docs/dps/sip/structure-requirements/#:~:text=NBSIPSTR9). Den **MÅ** beskrives med `mets/dmdSec/mdRef/@MDTYPE`. Gyldige verdier: `MARC`, `MODS`, `EAD`, `DC`, `NISOIMG`, `LC-AV`, `VRA`, `TEIHDR`, `DDI`, `FGDC`, `LOM`, `PREMIS`, `PREMIS:OBJECT`, `PREMIS:AGENT`, `PREMIS:RIGHTS`, `PREMIS:EVENT`, `TEXTMD`, `METSRIGHTS`, `ISO 19115:2003 NAP`, `EAC-CPF`, `LIDO`, `OTHER`. Hvis man velger `OTHER` **BØR** man beskrive hva slags metadatatype det er med `mets/dmdSec/mdRef/@OTHERMDTYPE`. <br><br>Administrative metadata eller bevaringsmetadata kan legges ved i henhold til [CSIP31-57](https://earkcsip.dilcis.eu/#useofthemetsadministrativemetadatasectionelementamdsec). <br> Merk at noen typer metadata i form av PREMIS-eventer anbefales avlevert via submission API, se mer om det [her](/nb/docs/dps/api/submission/events/). | **MÅ**   | **1..n**         |
| **NBSIP5** | **Referanser til filer med deskriptive metadata**<br>`mets/dmdSec/mdRef`<br><br>**MÅ** brukes for å peke til filer med deskriptive metadata som befinner seg i mappa `metadata/descriptive`. Direkte embedding av metadata ved hjelp av `mets/dmdSec/mdWrap` frarådes.<br><br>Dette er en strengere, SIP-spesifikk versjon av [CSIP21](https://earkcsip.dilcis.eu/#CSIP21).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **MÅ**   | **1..n**         |
| **NBSIP6** | **Sjekksumtype**<br>`mets/dmdSec/mdRef/@CHECKSUMTYPE`<br><br>En verdi fra METS-standarden som angir hvilken algoritme som er brukt for å beregne sjekksummen for den refererte filen. Sjekksumtype **MÅ** være : `MD5`.<br><br>Dette er en strengere variant av [CSIP29](https://earkcsip.dilcis.eu/#CSIP29) og [CSIP30](https://earkcsip.dilcis.eu/#CSIP30).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **MÅ**   | **1..1**         |




**Eksempel:** 

```xml
<dmdSec ID="uuid-e1d1f6db-3851-40bf-9ffd-59277a4442dc" CREATED="2025-01-16T12:43:32.894+01:00"
  STATUS="CURRENT">
  <mdRef ID="ID-uuid-861d36a1-043f-45aa-b230-be13517823a9" LOCTYPE="URL"
    MIMETYPE="application/json" SIZE="2038" CREATED="2025-01-16T12:43:32.894+01:00"
    CHECKSUM="EB72EF8AB5B1C93801DFACBFE6AA8E27" CHECKSUMTYPE="MD5" MDTYPE="DC"
    xlink:type="simple" xlink:href="metadata/descriptive/nb_dublincore.json"/>
</dmdSec>
<dmdSec ID="uuid-EC8718B5-C417-4D8C-975B-C14CD8197E62" CREATED="2025-01-16T12:43:32.894+01:00"
  STATUS="CURRENT">
  <mdRef ID="ID-uuid-FAF602A1-AB9A-44AC-A24B-B918F7064920" LOCTYPE="URL" MIMETYPE="text/xml"
    SIZE="1903" CREATED="2025-01-16T12:43:32.894+01:00"
    CHECKSUM="50E9C929EAE5B51F20F8B86D604FD24D" CHECKSUMTYPE="MD5" MDTYPE="MODS"
    xlink:type="simple" xlink:href="metadata/descriptive/MODS.xml"/>
</dmdSec>
```





### Bruk av administrative metadata i METS (`amdSec`)

E-ARK-spesifikasjonenen legger kun føringer for hvordan man refererer til digital proveniensmetadata (`digiprovMD`-seksjonen) og rettighetsmetadata (`rightsMD`-seksjonen) i METS. Digital proveniensmetadata er informasjon om hendelser i det digitale objektets livssyklus. Dette er data som typisk formateres i PREMIS. Merk at noen typer metadata i form av PREMIS-eventer anbefales avlevert i Submission API, se mer om det her: [Eventer/bevaringsmetadata](/nb/docs/dps/api/submission/events).  Rettighetsmetadata er informasjon om immaterielle rettigheter/intellektuell eiendomsrett (IPR) knyttet til de digitale objektene.

Spesifikasjonene åpner derimot også for å oppgi tekniske (`techMD`-seksjonen) og kildematerialemetadata (`sourceMD`-seksjonen). Dette er metadata NB mener spiller en viktig rolle i forvaltningen av digitale objekter. Tekniske metadata forklarer hva dataene er for noe, mens kildematerialemetadata gir viktig kontekst for det digitale objektet, samt underbygger dets autentisitet. Se også [NBSIPSTR16](/nb/docs/dps/sip/structure-requirements/#:~:text=NBSIPSTR16) og [NBSIPSTR17](/nb/docs/dps/sip/structure-requirements/#:~:text=NBSIPSTR17).




| **ID**      | **Navn, METS-element, beskrivelse**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Krav** | **Kardinalitet** |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------------|
| **NBSIP7**  | **Kildematerialemetadata**<br>`mets/amdSec/sourceMD`<br><br>**Hvis** metadata om kildematerialet for en representasjon er tilgjengelig i informasjonspakka, **MÅ** dette elementet brukes til å beskrive dette.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **MÅ**   | **1..n**         |
| **NBSIP8**  | **Identifikator for kildematerialemetadata**<br>`mets/amdSec/sourceMD/@ID`<br><br>En `xml:id` identifikator for seksjonen for kildematerialemetadata `mets/amdSec/sourceMD` som brukes for interne referanser innenfor XML-dokumentet. Identifikatoren **MÅ** være unik innenfor XML-dokumentet.                                                                                                                                                                                                                                                                                                                                                                                                           | **MÅ**   | **1..1**         |
| **NBSIP9**  | **Status for kildematerialemetadata**<br>`mets/amdSec/sourceMD/@STATUS`<br><br>Status **MÅ** settes til `CURRENT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **MÅ**   | **1..1**         |
| **NBSIP10** | **Referanser til filer med kildematerialemetadata**<br>`mets/amdSec/sourceMD/mdRef`<br><br>**MÅ** brukes for å peke til filer med kildematerialemetadata som befinner seg i mappa metadata/source.<br> <br>Direkte embedding av metadata ved hjelp av `mets/amdSec/mdWrap` frarådes.                                                                                                                                                                                                                                                                                                                                                                                                                       | **MÅ**   | **1..1**         |
| **NBSIP11** | **Type locator**<br>`mets/amdSec/sourceMD/mdRef[@LOCTYPE='URL']`<br><br>Locatortypen er alltid brukt med verdien `URL` fra [statusvokabularet](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyStatus.xml) i E-ARK-spesifikasjonene.                                                                                                                                                                                                                                                                                                                                                                                                                                            | **MÅ**   | **1..1**         |
| **NBSIP12** | **Type lenke**<br>`mets/amdSec/sourceMD/mdRef[@xlink:type='simple']`<br><br>Attributten **MÅ** brukes med verdien `simple`. Vokabularet med mulige verdier er vedlikeholdt av xlink-standarden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **MÅ**   | **1..1**         |
| **NBSIP13** | **Filplassering**<br>`mets/amdSec/sourceMD/mdRef/@xlink:href`<br><br>Den faktiske plasseringen til fila. Den skal refereres til med URL type filepath.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **MÅ**   | **1..1**         |
| **NBSIP14** | **Type metadata**<br>`mets/amdSec/sourceMD/mdRef/@MDTYPE`<br><br>Spesifiserer typen metadata i den refererte fila. Verdiene er hentet fra METS. <br>Gyldige verdier:<br>`MARC`, `MODS`, `EAD`, `DC`, `NISOIMG`, `LC-AV`, `VRA`, `TEIHDR`, `DDI`, `FGDC`, `LOM`, `PREMIS`, `PREMIS:OBJECT`, `PREMIS:AGENT`, `PREMIS:RIGHTS`, `PREMIS:EVENT`, `TEXTMD`, `METSRIGHTS`, `ISO 19115:2003 NAP`, `EAC-CPF`, `LIDO`, `OTHER`. Hvis man velger `OTHER` **BØR** man beskrive hva slags metadatatype det er med `mets/amdSec/sourceMD/mdRef/@OTHERMDTYPE`. <br> Merk at noen typer metadata i form av PREMIS-eventer anbefales avlevert via submission API, se mer om det [her](/nb/docs/dps/api/submission/events/). | **MÅ**   | **1..1**         |
| **NBSIP15** | **Tekniske metadata**<br>`mets/amdSec/techMD`<br><br>**Hvis** tekniske metadata for datafilene i en representasjon er tilgjengelig i informasjonspakka, **MÅ** dette elementet brukes til å beskrive dette.<br><br>Direkte embedding av metadata ved hjelp av `mets/amdSec/mdWrap` frarådes.                                                                                                                                                                                                                                                                                                                                                                                                               | **BØR**  | **0..n**         |
| **NBSIP16** | **Identifikator for tekniske metadata**<br>`mets/amdSec/techMD/@ID`<br><br>En `xml:id` identifikator for seksjonen for tekniske metadata `mets/amdSec/techMD` som brukes for interne referanser innenfor XML-dokumentet. Identifikatoren **MÅ** være unik innenfor XML-dokumentet.                                                                                                                                                                                                                                                                                                                                                                                                                         | **MÅ**   | **1..1**         |
| **NBSIP17** | **Status for tekniske metadata**<br>`mets/amdSec/techMD/@STATUS`<br><br>Status **MÅ** settes til `CURRENT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **MÅ**   | **1..1**         |
| **NBSIP18** | **Referanser til filer med tekniske metadata**<br>`mets/amdSec/techMD/mdRef`<br><br>**MÅ** brukes for å peke til filer med tekniske metadata som befinner seg i mappa `metadata/technical`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **MÅ**   | **1..1**         |
| **NBSIP19** | **Type locator**<br>`mets/amdSec/techMD/mdRef[@LOCTYPE='URL']`<br><br>Locatortypen er alltid brukt med verdien `URL` fra [statusvokabularet](https://github.com/DILCISBoard/E-ARK-CSIP/blob/master/schema/CSIPVocabularyStatus.xml) i E-ARK-spesifikasjonene.                                                                                                                                                                                                                                                                                                                                                                                                                                              | **MÅ**   | **1..1**         |
| **NBSIP20** | **Type lenke**<br>`mets/amdSec/techMD/mdRef[@xlink:type='simple']`<br><br>Attributten **MÅ** brukes med verdien `simple`. Vokabularet med mulige verdier er vedlikeholdt av xlink-standarden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **MÅ**   | **1..1**         |
| **NBSIP21** | **Filplassering**<br>`mets/amdSec/techMD/mdRef/@xlink:href`<br><br>Den faktiske plasseringen til fila. Den skal refereres til med URL type filepath.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **MÅ**   | **1..1**         |
| **NBSIP22** | **Type metadata**<br>`mets/amdSec/techMD/mdRef/@MDTYPE`<br><br>Spesifiserer typen metadata i den refererte fila. Verdiene er hentet fra METS. Gyldige verdier:<br>`MARC`, `MODS`, `EAD`, `DC`, `NISOIMG`, `LC-AV`, `VRA`, `TEIHDR`, `DDI`, `FGDC`, `LOM`, `PREMIS`, `PREMIS:OBJECT`, `PREMIS:AGENT`, `PREMIS:RIGHTS`, `PREMIS:EVENT`, `TEXTMD`, `METSRIGHTS`, `ISO 19115:2003 NAP`, `EAC-CPF`, `LIDO`, `OTHER`. Hvis man velger `OTHER` **BØR** man beskrive hva slags metadatatype det er med `mets/amdSec/techMD/mdRef/@OTHERMDTYPE`.<br> Merk at noen typer metadata i form av PREMIS-eventer anbefales avlevert via submission API, se mer om det [her](/nb/docs/dps/api/submission/events/).          | **MÅ**   | **1..1**         |
| **NBSIP23** | **Sjekksumtype**<br>`mets/amdSec/digiprovMD/mdRef/@CHECKSUMTYPE, mets/amdSec/rightsMD/mdRef/@CHECKSUMTYPE, mets/amdSec/sourceMD/mdRef/@CHECKSUMTYPE, mets/amdSec/techMD/mdRef/@CHECKSUMTYPE`<br><br> Verdi fra METS-standarden som angir hvilken algoritme som er brukt for å beregne sjekksummen for den refererte filen. Sjekksumtype **MÅ** være : `MD5`.<br><br>Dette er en strengere variant av [CSIP43](https://earkcsip.dilcis.eu/#CSIP43), [CSIP44](https://earkcsip.dilcis.eu/#CSIP44), [CSIP56](https://earkcsip.dilcis.eu/#CSIP56) og [CSIP57](https://earkcsip.dilcis.eu/#CSIP57).                                                                                                             | **MÅ**   | **1..1**         |




**Eksempel:** 

```xml
<amdSec>
  <digiprovMD ID="uuid-975a7a15-140f-4e2c-a5ec-d136e86ea4e5"
    CREATED="2019-04-24T14:37:52.783+01:00">
    <mdRef LOCTYPE="URL" xlink:type="simple" xlink:href="metadata/preservation/events.xml"
      MDTYPE="PREMIS" MDTYPEVERSION="3.0" MIMETYPE="text/xml" SIZE="1211"
      CREATED="2018-04-24T14:37:52.783+01:00" CHECKSUM="dc7177d37a7de3448ee1e62da7343d72"
      CHECKSUMTYPE="MD5" LABEL="events.xml"/>
  </digiprovMD>
</amdSec>
<amdSec>
  <sourceMD ID="uuid-5d500e19-3802-49a5-92bd-7a575433ab7e"
    CREATED="2018-04-24T14:47:52.783+01:00">
    <mdRef LOCTYPE="URL" xlink:type="simple"
      xlink:href="metadata/souce/MAVIS_Carrier_12345_AE0000006261.xml" MDTYPE="OTHER"
      OTHERMDTYPE="MAVIS" MIMETYPE="text/xml" SIZE="2854"
      CREATED="2018-04-24T14:37:52.783+01:00" CHECKSUM="7ee30736137bfe72dc60afcbe374cb2a"
      CHECKSUMTYPE="MD5" LABEL="MAVIS_Carrier_12345_AE0000006261.xml"/>
  </sourceMD>
</amdSec>
```






### Bruk av METS filseksjon (`fileSec`)

`fileSec` skal beskrive alle komponenter i informasjonspakken (IP) som ikke allerede er beskrevet i elementene `amdSec` og `dmdSec`. For alle filoppføringer skal filplassering og sjekksumverdi oppgis.
METS-filseksjonen fungerer som en innholdsfortegnelse som gjør det mulig å kontrollere at alle filer er til stede og at informasjonspakken er komplett. Den gjør det også mulig å verifisere filenes integritet ved hjelp av de registrerte sjekksumverdiene.


| **ID**      | **Navn, METS-element, beskrivelse**                                                                                                                                                                                                                                                                                                                                 | **Krav** | **Kardinalitet** |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:-----------------|
| **NBSIP24** | **Sjekksumtype**<br>`mets/fileSec/fileGrp/file/@CHECKSUMTYPE`<br><br> Verdi fra METS-standarden som angir hvilken algoritme som er brukt for å beregne sjekksummen for den refererte filen. Sjekksumtype **MÅ** være : `MD5`.<br><br>Dette er en strengere variant av [CSIP71](https://earkcsip.dilcis.eu/#CSIP71) og [CSIP72](https://earkcsip.dilcis.eu/#CSIP72). | **MÅ**   | **1..1**         |



**Eksempel:** 

```xml
<fileSec ID="uuid-31FE0AB6-6140-4B5B-9B49-4D986F60192B">
  <fileGrp ID="uuid-4DE31868-267C-478A-A4DE-903D40F91B39" USE="Schemas">
    <file ID="ID-0BA063E6-7447-4B9F-A074-95B2089EFCA4" MIMETYPE="text/xml" SIZE="2038"
      CREATED="2026-06-22T10:50:04.118+02:00" CHECKSUM="EB72EF8AB5B1C93801DFACBFE6AA8E27"
      CHECKSUMTYPE="MD5">
      <FLocat LOCTYPE="URL" xlink:type="simple" xlink:href="schemas/DILCISExtensionMETS.xsd"/>
    </file>
    <file ID="ID-53F6602E-771E-4873-84C9-D51FFF0971B5" MIMETYPE="text/xml" SIZE="499"
      CREATED="2026-06-22T10:50:04.118+02:00" CHECKSUM="83DA1FF6F35ADEECE3CCCFB5E2E9F83A"
      CHECKSUMTYPE="MD5">
      <FLocat LOCTYPE="URL" xlink:type="simple" xlink:href="schemas/DILCISExtensionSIPMETS.xsd"
        />
    </file>
    <file ID="ID-72D20786-292C-47E1-82CF-63C62C83B4EF" MIMETYPE="text/xml" SIZE="137125"
      CREATED="2026-06-22T10:50:04.118+02:00" CHECKSUM="0504DEDC1251E87D7E85F9FF2DBADC0D"
      CHECKSUMTYPE="MD5">
      <FLocat LOCTYPE="URL" xlink:type="simple" xlink:href="schemas/mets1_12.xsd"/>
    </file>
    <file ID="ID-2F58420C-9FB4-4E84-B26B-DD2DF9C77201" MIMETYPE="text/xml" SIZE="3180"
      CREATED="2026-06-22T10:50:04.118+02:00" CHECKSUM="6BDC7F9459A502964F889D70A335CECE"
      CHECKSUMTYPE="MD5">
      <FLocat LOCTYPE="URL" xlink:type="simple" xlink:href="schemas/xlink.xsd"/>
    </file>
  </fileGrp>
  <fileGrp ID="uuid-783B2C36-9D26-417E-BE74-A160CB731533"
    USE="Representations/primary_20250325">
    <file ID="ID-68C498D9-D589-4372-B7D5-2FF0684788B6" MIMETYPE="text/xml" SIZE="2402"
      CREATED="2026-06-22T10:50:04.304+02:00" CHECKSUM="8E0A2C7C85D8812616CED481B9FFBD4E"
      CHECKSUMTYPE="MD5">
      <FLocat LOCTYPE="URL" xlink:type="simple"
        xlink:href="representations/primary_20250325/METS.xml"/>
    </file>
  </fileGrp>
</fileSec>
```



### Bruk av METS strukturkart (`structMap`)

METS-elementet for strukturkart (`structMap`) gir en oversikt over komponentene som er beskrevet i METS-dokumentet. Det kan også knytte elementene i strukturen til tilhørende innholdsfiler og metadata.

Ingen krav utover [CSIP METS structural map](https://earkcsip.dilcis.eu/#useofthemetsstructuralmapelementstructmap) og [E-ARK SIP METS-profil](https://earksip.dilcis.eu/#e-arksipmetsprofile2.1requirements).


**Eksempler:**

METS-eksempel på det obligatoriske strukturkartet med representasjoner:

```xml
<structMap ID="uuid-02BC407F-A6BB-4048-8DD5-757565935E3B" TYPE="PHYSICAL" LABEL="CSIP">
  <div ID="uuid-4C489BCC-1ABC-4EA6-A9B5-4B6B7052B0DB" TYPE="ORIGINAL" LABEL="primary_20140616">
    <div ID="uuid-F57F3C12-3E99-490B-ADE6-06AE3AFF8A46"
      ADMID="uuid-F1B0A220-29B4-4742-9660-5664EE2FD699 uuid-49F340DF-21E2-45B0-9C25-1ED048B4B8AE"
      LABEL="Metadata"/>
    <div ID="uuid-EEE68439-8E03-403A-A1E4-55E8E3C8E845" LABEL="Data">
      <fptr FILEID="uuid-DF9C02C3-24F9-4AC0-A033-44D8F8D739A8"/>
    </div>
  </div>
</structMap>
```
METS-eksempel på det obligatoriske strukturkartet:
```xml
<structMap ID="uuid-4589BF89-1216-49B8-9C67-C484F906706F" TYPE="PHYSICAL" LABEL="CSIP">
  <div ID="uuid-9722E574-4302-4BC2-B0A9-2B9086CB9FD7"
    LABEL="digifilm_461518_20140616_FYAL00000181">
    <div ID="uuid-21B503AA-C31A-404A-A168-DEA933F4D367"
      DMDID="uuid-AF0A86FA-2CE4-41F7-BD61-34004C216342 uuid-B40B9E66-234E-498D-B413-B772D98927D8 uuid-4A9367D6-1272-4A1D-8AD8-D32161152CF5 uuid-470C79A7-9BAB-4637-B416-1367F40A5B52 uuid-19D3CCCA-D098-4FBB-84F1-21F2947B25B2 uuid-8B34AAC6-10AC-4B3C-921D-2B4A52F3CA7E uuid-E9C6212E-12A1-4C83-B77E-FACF41990623 uuid-6E5AFBC1-A883-4FEE-82BA-CABD149FBDD6 uuid-BA48EF33-7610-41D4-9753-A132760856FF uuid-A71910DD-F472-4D9C-AE43-B7EC0C88CCA0 uuid-2EE0FB24-66F4-4365-8579-79357800AD5E uuid-158DF561-FBA5-4057-9AA2-12492230BB53"
      LABEL="Metadata"/>
    <div ID="uuid-38407EB1-9882-4C54-88BA-B6D7DECCFC8A" LABEL="Schemas">
      <fptr FILEID="uuid-4C128011-D82E-41F1-AD03-C86290173DFB"/>
    </div>
    <div ID="uuid-070E9A64-C5E9-4634-9889-91912767143F"
      LABEL="Representations/primary_20140616">
      <mptr LOCTYPE="URL" xlink:type="simple"
        xlink:href="representations/primary_20140616/METS.xml"
        xlink:title="uuid-69FDE799-1A96-4F63-ABF6-69D6EE8F7900"/>
    </div>
  </div>
</structMap>
```