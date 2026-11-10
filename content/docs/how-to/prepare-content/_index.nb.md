---
title: Klargjøre materiale for levering
weight: 1
aliases:
  - /docs/dps/how-to/prepare-content/
---

Denne veiledningen viser hvordan du pakker materiale som en innleveringspakke (SIP) som DPS godtar. Hvert steg lenker til kravene det dekker; kravsidene er normative, og denne veiledningen gjentar dem ikke. Hva en pakke inneholder, og hvorfor, er forklart under [Informasjonspakker](/nb/docs/understanding/information-packages/).

## Før du starter

- **Innholdsfilene**, helst i et av de [foretrukne filformatene](/nb/policies/formats/).
- **Deskriptive metadata** for materialet, for eksempel en eksport av en katalogpost.
- **En identifikator for pakken.** Den brukes som navn på pakkens rotmappe.
- **Medietypen** til materialet: bilder, lyd, levende bilder, tekst, nettarkiv eller datasett. Hver av dem har egne [krav til METS.xml](/nb/docs/reference/sip/mets/).

## Steg

{{% steps %}}

### Avgjør pakkens omfang

En pakke beskriver nøyaktig én intellektuell entitet ([NBSIPSTR1](/nb/docs/reference/sip/structure-requirements/#:~:text=NBSIPSTR1)). Vi anbefaler å avgrense en pakke til ett bestemt digitalt eksemplar, for eksempel én skanning av et fotografi eller én digitalisering av en bok. En teknisk variant av det samme eksemplaret, for eksempel et avledet visningsformat, er en ny representasjon i samme pakke, ikke en ny pakke. Se [Ny pakke eller ny representasjon?](/nb/docs/understanding/information-packages/#ny-pakke-eller-ny-representasjon)

### Lag mappestrukturen

Lag en rotmappe med pakkens identifikator som navn, med bare bokstavene `A–Z`, `a–z`, sifre, `-` og `_`. Den samme identifikatoren brukes som `@OBJID` i rot-`METS.xml` ([NBSIPSTR2](/nb/docs/reference/sip/structure-requirements/#:~:text=NBSIPSTR2)). Gi den denne strukturen:

```text
<pakkeidentifikator>/
├── METS.xml
├── metadata/
│   └── descriptive/
├── representations/
│   └── primary_ÅÅÅÅMMDD/
│       ├── METS.xml
│       ├── data/
│       └── metadata/
└── schemas/
```

Pakken kan bare inneholde mapper som kravene tillater ([NBSIPSTR20](/nb/docs/reference/sip/structure-requirements/#:~:text=NBSIPSTR20)). [Hva en pakke inneholder](/nb/docs/understanding/information-packages/#hva-en-pakke-inneholder) forklarer hva hver mappe er til.

### Legg til innholdsfilene

Legg innholdsfilene i `representations/primary_ÅÅÅÅMMDD/data/` ([NBSIPSTR11](/nb/docs/reference/sip/structure-requirements/#:~:text=NBSIPSTR11), [NBSIPSTR13](/nb/docs/reference/sip/structure-requirements/#:~:text=NBSIPSTR13)), der `ÅÅÅÅMMDD` er datoen mappen ble opprettet. Hvis pakken har mer enn én representasjon, får hver ekstra representasjon sin egen mappe, navngitt med et meningsfullt navn og datoen, for eksempel `processed_20251214` ([NBSIPSTR12](/nb/docs/reference/sip/structure-requirements/#:~:text=NBSIPSTR12)).

### Legg til metadatafilene

Legg minst én fil med deskriptive metadata i `metadata/descriptive/` ([NBSIPSTR9](/nb/docs/reference/sip/structure-requirements/#:~:text=NBSIPSTR9)). Legg kilde-, tekniske og bevaringsmetadata i representasjonen de hører til. [Plassering av metadata i korte trekk](/nb/docs/reference/sip/structure-requirements/#plassering-av-metadata-i-korte-trekk) viser hvor hver type skal ligge.

Bevaringseventer, for eksempel digitalisering eller validering, leveres heller via API-et enn som filer. Se [Legge til bevaringseventer](/nb/docs/how-to/add-preservation-events/).

### Legg til skjemaer og dokumentasjon

Legg alle XML-skjemaer for de strukturerte metadataene i pakken i `schemas/` ([NBSIPSTR18](/nb/docs/reference/sip/structure-requirements/#:~:text=NBSIPSTR18)). Hvis det trengs tilleggsdokumentasjon for å nyttiggjøre seg innholdet, legger du den i `documentation/` ([NBSIPSTR19](/nb/docs/reference/sip/structure-requirements/#:~:text=NBSIPSTR19)).

### Skriv METS-filene

Skriv en `METS.xml` i rotmappa ([NBSIPSTR4](/nb/docs/reference/sip/structure-requirements/#:~:text=NBSIPSTR4)) og én i hver representasjonsmappe ([NBSIPSTR14](/nb/docs/reference/sip/structure-requirements/#:~:text=NBSIPSTR14)). De må oppfylle [kravene til METS.xml](/nb/docs/reference/sip/mets/) og tilleggskravene for medietypen din, som blant annet angir innholdskategori og hvilken profil som skal oppgis.

Nasjonalbibliotekets [DPS E-ARK SIP Generator](https://github.com/NationalLibraryOfNorway/dps-eark-generator) kan generere METS-filene og legge til XML-skjemaene ut fra en mappestruktur som den over. Den er bygget på [commons-ip](https://github.com/keeps/commons-ip), et åpent bibliotek og kommandolinjeverktøy for å lage og validere E-ARK-informasjonspakker. Kontroller at resultatet oppfyller kravene for medietypen, for eksempel profilen som oppgis.

### Beregn sjekksummer

Beregn en MD5-sjekksum for hver fil i pakken. Du registrerer hver fil med sjekksummen når du leverer, og DPS verifiserer sjekksummene ved mottak. Kontroller sjekksummene på nytt rett før du leverer, for å sikre at filene ikke er endret.

### Kontroller pakken

Kontroller pakken mot kravene før du leverer den. [commons-ip](https://github.com/keeps/commons-ip) og handlingen `validate` i [DPS E-ARK SIP Generator](https://github.com/NationalLibraryOfNorway/dps-eark-generator) kontrollerer pakken mot E-ARK-spesifikasjonene, men ikke mot Nasjonalbibliotekets tilleggskrav. DPS validerer pakken mot både E-ARK-kravene og Nasjonalbibliotekets krav etter at den er overført; hvis den ikke oppfyller dem, avvises innleveringen med en liste over årsaker.

{{% /steps %}}

## Neste steg

- [Levere materiale til bevaring](/nb/docs/how-to/submit-content/) via API-et.
- Se [eksemplene](/nb/docs/reference/sip/examples/) på komplette pakker for ulike medietyper.
