---
title: Metadataveiledning
weight: 2
---

Denne siden beskriver hvilke typer metadata som finnes, hvor de plasseres i en informasjonspakke, og hvordan de refereres til i METS.
En pakke kan ha ett sett metadatafiler på rotnivået av pakka og ett sett metadatafiler per representasjon på representasjonsnivået av pakka.

## Pakkemetadata (hele pakka)

### Deskriptive metadata

Deskriptive metadata beskriver det intellektuelle objektet som pakka representerer (typisk et eksemplar av et verk eller lignende). 
Kan brukes til identifikasjon og gjenfinning av det intellektuelle innholdet i pakka, og beskriver ikke spesifikke filer.

| Plassering i SIP         | Eksempelfiler                  |  METS-element | 
| ------------------------ | ------------------------------ | --------------- | 
| `/metadata/descriptive/` | <ul><li> MODS.xml<br><li> mavisTitle.xml</ul> |  `dmdSec` | 

### Bevarings- og digitaliseringsmetadata

Kort definisjon fra E-ARK CSIP:
> Digital provenance metadata [...] records digital preservation information, e.g. audit information covering a digital library object’s life-cycle.

Bevaringsmetadata på en **pakkes rotnivå** beskriver opphavet til en **pakke**, hvor den kommer fra og hvordan den er fremstilt. 
Typisk vil dette være beskrivelser av digitale prosesser, handlinger, hendelser og resultatene av disse. 


| Plassering i SIP        | Eksempelfiler                  | METS-element | 
| ------------------------ | ------------------------------ | -------------- | 
| `/representations/*/metadata/preservation/` | <ul><li> ScanityTransfer.xml<br><li> MAVIS_film_carrier.xml (ved digitalisering)<br><li> MAVIS_sound_carrier_*.xml (ved digitalisering)<br><li> PREMIS events</ul> | `digiprovMD` |


## Representasjonsmetadata (per representasjon)

### Kildemetadata

Kort definisjon fra E-ARK CSIP:
> Source metadata [...] records descriptive, technical or rights metadata for an analog source for a digital library object[^1].

Kildemetadata beskriver objektet en representasjon er utledet fra. 
Typisk vil dette være metadata om et originalt fysisk eller digitalt kildemateriale (for eksempel en bok, et bilde, en filmrull) og dets tilstand ved digitaliseringtidspunktet. 
På samme måte kan det være metadata om et digitalt objekt som er blitt brukt til å utlede et annet digitalt objekt.

| Plassering i SIP        | Eksempelfiler                  | METS-element | 
| ------------------------ | ------------------------------ | -------------- | 
| `/representations/*/metadata/source/` | <ul><li> mavisAnalogCarrier.xml<br><li> mavisAnalogComponent.xml<br><li> mavisDigitalCarrier.xml<br><li> mavisDigitalComponent.xml<br><li> mavisSoundTrackCarrier.xml<br><li> mavisSoundTrackComponent.xml</ul> | `sourceMD` |


### Tekniske metadata

Kort definisjon fra E-ARK CSIP:
> [Technical metadata describes] technical details of the data themselves.

Tekniske metadata dokumenterer målbare, systemgenererte tekniske egenskaper ved de digitale filene i en representasjon. 
Teknisk metadata beskriver hva de digitale filene faktisk er, basert på filanalyse.
Tekniske metadata er ** ikke** beskrivelser av hva det intellektuelle innholdet i fila er, eller hva som er gjort med den/prosesshistorikk.

| Plassering i SIP        | Eksempelfiler                  | METS-element | 
| ------------------------ | ------------------------------ | -------------- | 
| `/representations/*/metadata/technical/` | <ul><li> FITS<br><li> MediaInfo<br><li> ExifTool<br><li> JHOVE</ul> | `techMD` |


### Bevarings- og digitaliseringsmetadata

Kort definisjon fra E-ARK CSIP:
> Digital provenance metadata [...] records digital preservation information, e.g. audit information covering a digital library object’s life-cycle.

Bevaringsmetadata beskriver opphavet til filene i en representasjon, hvor de kommer fra og hvordan de er fremstilt. 
Typisk vil dette være beskrivelser av digitaliseringsprosesser, handlinger, hendelser og resultatene av disse. 
Hvis metadata beskriver hvordan, når eller av hvilket system de digitale filene ble skapt eller registrert, er det typisk bevaringsmetadata.

| Plassering i SIP        | Eksempelfiler                  | METS-element | 
| ------------------------ | ------------------------------ | -------------- | 
| `/representations/*/metadata/preservation/` | <ul><li> ScanityTransfer.xml<br><li> MAVIS_film_carrier.xml (ved digitalisering)<br><li> MAVIS_sound_carrier_*.xml (ved digitalisering)<br><li> PREMIS events</ul> | `digiprovMD` |

<!-- {{< callout >}} 
**Kort huskeregel:**
- **Deskriptive metadata (descriptive)**: hva pakka intellektuelt er for noe
- **Kilde (source)**: hva som ble digitalisert
- **Teknisk (technical)**: hva filene er
- **Bevaring (preservation)**: hvordan filene ble skapt
{{< /callout >}}  -->

[^1]: [Common Specification for Information Packages
v2.2.0 : Use of the METS administrative metadata section (element amdSec)](https://earkcsip.dilcis.eu/#useofthemetsadministrativemetadatasectionelementamdsec)
