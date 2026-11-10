---
title: Levere materiale til bevaring
weight: 2
aliases:
  - /docs/dps/api/submission/
  - /docs/dps/how-to/submit-content/
---

Denne veiledningen viser hvordan du leverer materiale til DPS via API-et: fra en ferdig innleveringspakke (SIP) til et bevart objekt. Feltnavn, begrensninger og statuskoder er listet i [referansen for innleveringer](/nb/docs/reference/api/#innleveringer).

## Før du starter

- **Klientlegitimasjon og et tilgangstoken.** Se [Autentisering og autorisasjon](/nb/docs/reference/api/).
- **En kontrakt-ID (`contractId`)** for avtalen du leverer under, og en produsentrolle for den kontrakten.
- **Materialet klargjort som en SIP.** Se [Klargjøre materiale for levering](/nb/docs/how-to/prepare-content/).

## Steg

{{% steps %}}

### Klargjør SIP-en

Pakk materialet som en SIP, med en MD5-sjekksum for hver fil. Se [Klargjøre materiale for levering](/nb/docs/how-to/prepare-content/). Filene du registrerer i de neste stegene er filene i SIP-en, og stiene deres i API-et speiler pakkestrukturen.

### Opprett en submission

En submission representerer én informasjonspakke. Opprett den med din identifikator for objektet (`objectId`) og de deskriptive metadataene. Se [Krav til metadata](/nb/docs/reference/descriptive-metadata/) for metadataelementene.

**Forespørsel**
```http
POST /dps-submission/v1/contracts/1234/submissions HTTP/1.1
Host: api.nb.no
Content-Type: application/json
Authorization: Bearer eyJhbGciOxxxxxxx

{
  "objectId": "digavis_aabcc",
  "priority": 50,
  "metadata": {
    "type": "Artikkel",
    "identifier": [
      {
        "type": "URN",
        "value": "URN:NBN:no-nb_plfut_00001"
      }
    ],
    "title": {
      "value": "My Book Title",
      "lang": "eng"
    },
    "alternative": [
      {
        "type": "Original title",
        "value": "My Alternative Book Title",
        "lang": "eng"
      }
    ],
    "creator": [
      {
        "name": "Marek, Václav",
        "type": "person",
        "role": "Fotograf",
        "authority": {
          "source": "Example authority",
          "code": "198097",
          "uri": "https://example.com/198097"
        }
      }
    ],
    "contributor": [
      {
        "name": "Nordmann, Ola",
        "type": "person",
        "role": "Avbildet",
        "authority": {
          "source": "Example authority",
          "code": "198097",
          "uri": "https://example.com/198097"
        }
      }
    ],
    "publisher": [
      {
        "name": "Gyldendal",
        "type": "korporasjon",
        "authority": {
          "source": "Example authority",
          "code": "198097",
          "uri": "https://example.com/198097"
        }
      }
    ],
    "spatial": [
      {
        "name": "Mo i Rana",
        "type": "Place",
        "authority": {
          "source": "Example authority",
          "code": "198097",
          "uri": "https://example.com/198097"
        },
        "coordinateReferenceSystem": "EPSG:4326",
        "latitude": 67.2968,
        "longitude": 14.3974
      }
    ],
    "date": [
      {
        "type": "created",
        "value": "2023-10-27"
      }
    ],
    "language": [
      {
        "type": "Subtitles",
        "value": "swe"
      }
    ],
    "relation": [
      {
        "title": "Chronicles of Narnia",
        "lang": "eng",
        "type": "isPartOf"
      }
    ],
    "provenance": [
      {
        "value": "The collection was donated to the National Library by Václav Marek 1979-05-12",
        "lang": "eng"
      }
    ],
    "subject": [
      {
        "value": "Norge"
      }
    ],
    "description": [
      {
        "lang": "nob",
        "value": "Norge"
      }
    ]
  }
}
```

**Respons**
```json
{
  "contractId": "1234",
  "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
  "objectId": "digavis_aabcc",
  "clientId": "myClientId",
  "status": "REGISTERED",
  "priority": 50
}
```

Ta vare på `submissionId` fra responsen. Du trenger den i de neste stegene.

### Registrer hver fil

Registrer hver fil i SIP-en med stien i pakken og sjekksummen. Responsen inneholder en pre-signert `uploadUrl` for filen.

**Forespørsel**
```http
POST /dps-submission/v1/contracts/1234/submissions/8Z7x1T9rN0Xc2B5Yq4L3zP/files HTTP/1.1
Host: api.nb.no
Content-Type: application/json
Authorization: Bearer eyJhbGciOxxxxxxx

{
  "filePath": "representations/primary_20250217/data/ranablad_20250215.pdf",
  "checksum": "d41d8cd98f00b204e9800998ecf8427e",
  "isPackaged": false
}
```

**Respons**
```json
{
  "fileId": "1M0x4T9rN8Xc7B2Yq5L3zK",
  "filePath": "representations/primary_20250217/data/ranablad_20250215.pdf",
  "s3ObjectKey": "examplebucket/myClientId/1234/8Z7x1T9rN0Xc2B5Yq4L3zP/representations/primary_20250217/data/ranablad_20250215.pdf",
  "checksum": "d41d8cd98f00b204e9800998ecf8427e",
  "isPackaged": false,
  "uploadUrl": "https://s3.nb.no/examplebucket/...&X-Amz-Signature=..."
}
```

### Last opp filene

Last opp innholdet i hver fil med HTTP PUT til filens `uploadUrl`. URL-en er gyldig i ca. én time, og innholdet må ha samme MD5-sjekksum som du registrerte.

```http
PUT {uploadUrl} HTTP/1.1
Content-Length: {file-size-in-bytes}

[FILE CONTENT]
```

Hvis opplastingen feiler eller går ut på tid:

- Prøv på nytt med samme `uploadUrl` hvis den ikke er utløpt.
- Hvis den er utløpt, slett filregistreringen (`DELETE /v1/contracts/{contractId}/submissions/{submissionId}/files/{fileId}`) og registrer filen på nytt for å få en ny URL.

{{% details title="Alternativ opplasting for store filer (filer over 5 GiB)" closed="true" %}}

> [!NOTE]
> Denne funksjonaliteten er primært ment for intern bruk på Nasjonalbiblioteket, spesielt for store filer, 
> siden pre-signerte URL-er kun støtter filer med en maksimal størrelse på 5 GiB. 
> Tilgang til S3-bøtta for digital bevaring kan fås ved å kontakte Plattform-teamet.


Opplastingsprosessen følger disse stegene:
1. **Registrer en fil** ved å sende POST til `/contracts/{contractId}/submissions/{submissionId}/files`
2. **Hent ut s3ObjectKey** i responsen
3. **Last opp filinnholdet** direkte til S3, med `s3://{s3ObjectKey}` som mål. `s3ObjectKey` starter med navnet på bøtta, etterfulgt av objektnøkkelen.

Vi anbefaler å bruke AWS CLI til opplastingen. Dokumentasjon finnes her: https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html

Her er et eksempel på hvordan du kan gjøre dette:
```shell
s3 cp path/to/my_big_movie_file.mov s3://examplebucket/clientId/contract/submissionId/path/to/my_big_movie_file.mov --endpoint-url=https://s3.nb.no
```

{{% /details %}}

### Legg til bevaringseventer (valgfritt)

Hvis du har dokumentert bevaringseventer før innlevering, for eksempel digitalisering eller validering, legger du dem til nå. Eventer kan bare legges til før submissionen er fullført. Se [Legge til bevaringseventer](/nb/docs/how-to/add-preservation-events/).

### Fullfør submissionen

Når alle filene er lastet opp, fullfører du submissionen. Dette starter overføringen til DPS, og det kan ikke legges til flere filer eller eventer.

**Forespørsel**
```http
POST /dps-submission/v1/contracts/1234/submissions/8Z7x1T9rN0Xc2B5Yq4L3zP/finalize HTTP/1.1
Host: api.nb.no
Authorization: Bearer eyJhbGciOxxxxxxx
```

**Respons**
```json
{
  "contractId": "1234",
  "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
  "objectId": "digavis_aabcc",
  "clientId": "myClientId",
  "status": "UPLOAD_COMPLETED",
  "priority": 50,
  "sumSizeInBytes": 12345678,
  "files": [
    {
      "fileId": "1M0x4T9rN8Xc7B2Yq5L3zK",
      "filePath": "representations/primary_20250217/data/ranablad_20250215.pdf",
      "s3ObjectKey": "examplebucket/myClientId/1234/8Z7x1T9rN0Xc2B5Yq4L3zP/representations/primary_20250217/data/ranablad_20250215.pdf",
      "checksum": "d41d8cd98f00b204e9800998ecf8427e",
      "isPackaged": false,
      "uploadUrl": "https://s3.nb.no/examplebucket/...&X-Amz-Signature=..."
    }
  ]
}
```

### Følg statusen

Submissionen går nå gjennom `PROCESSING` til enten `PRESERVED` eller `REJECTED`. Følg den ved å [motta varsler](/nb/docs/how-to/receive-notifications/) eller ved å hente submissionen. En `200 OK` fra `finalize` bekrefter bare at opplastingen er fullført: innholdet i filene valideres etter overføringen til DPS. Når submissionen er bevart, tar du vare på `archiveId` fra meldingen `submission.preserved`. Den er materialets varige identifikator i DPS.

{{% /steps %}}

## Viktig informasjon

1. **Verifiser alltid sjekksum før opplasting.**
Kontroller at filene har forventet sjekksum før de lastes opp til DPS. Sjekksummen bekrefter at filene er intakte og ikke har blitt endret siden den ble beregnet.

1. **Gjør grundige kvalitetssjekker før innsending.**
Når en innlevering er verifisert og har fått status `PRESERVED`, kan den ikke enkelt slettes eller trekkes tilbake. Det er derfor viktig å vurdere materialet nøye og kontrollere at innhold, filer og metadata er korrekte før pakken sendes til DPS.

1. **Bruk unike `objectId` per kontrakt og ta vare på disse.**
`objectId` er koblingen mellom kildesystemet og DPS. Den returneres i API-responser og webhook-hendelser, slik at du alltid kan identifisere hvilket objekt en hendelse gjelder. `objectId` kan ikke endres.

1. **Legg ved rik metadata.**
Gode og komplette metadata gir bedre søkbarhet og bidrar til at materialet kan identifiseres og forstås over tid.

1. **Ta vare på `submissionId` og `archiveId`.**
- Ta vare på `submissionId` helt til du har mottatt meldingen `submission.preserved`. `submissionId` brukes til å slå opp innleveringen og til eventuell feilhåndtering eller korrigering.

- Meldingen `200 OK` fra `finalize` bekrefter at opplastingen er gjennomført. 
En `200 OK`-respons fra `finalize` bekrefter at filene er mottatt og sendt til S3, men betyr ikke at SIP-en er validert mot kravene for digital bevaring. API-et validerer så mye som mulig før overføring, men validering av filenes innhold skjer først etter at pakken er overført til DPS. Hvis valideringen feiler, mottar du en `submission.rejected`-melding.

- Ta vare på `archiveId`. Dette er materialets unike og varige identifikator i DPS.
  
6. **Ikke slett kildematerialet før du har mottatt meldingen `submission.preserved`.**
`submission.preserved` er bekreftelsen på at materialet er bevart i DPS og har gjennomgått nødvendig validering og verifisering. Vent derfor med å slette kildematerialet til denne meldingen er mottatt.

## Støtte

Trenger du hjelp eller har spørsmål, kontakt teamet for digital bevaring ved Nasjonalbiblioteket.
