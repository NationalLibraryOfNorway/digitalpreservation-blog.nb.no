---
title: Submission Service
weight: 1
---

## Oversikt

Submission-tjenesten for digital bevaring tilbyr et REST-basert API for å håndtere digitale leveranser og tilhørende filer. 
Tjenesten lar klienter opprette leveranser, registrere filer, laste opp innhold og spore statusen gjennom hele bevaringsprosessen.

For generell informasjon om autentisering og autorisasjon, se [hovedsiden for API-dokumentasjon](../).

Denne dokumentasjonen kompletterer den detaljerte API-spesifikasjonen som er tilgjengelig via Swagger på [https://digitalpreservation.no/swagger/](https://digitalpreservation.no/swagger/).

**Filstørrelsesbegrensning:**

* Maks filstørrelse: 5 GB per fil
* Begrensningen skyldes restriksjoner i pre-signerte S3-URL-er

## Leveringsflyt

Hele prosessen for å levere innhold ser slik ut:

1. **Opprett en submission** med metadata
2. **Registrer filer** for å få pre-signerte opplastingslenker
3. **Last opp filer** via disse lenkene
4. **Fullfør submissionen** for å starte bevaringsbehandling
5. Spor **submission-status** etter hvert som den behandles (statusoppdatering kommer i senere versjon)


## Eksempel på API-bruk

### Registrer ny submission
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
        "type": "Person",
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
        "type": "Person",
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
        "type": "Organization",
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
        "value": "Swedish",
        "lang": "eng"
      }
    ],
    "isPartOf": [
      {
        "value": "Chronicles of Narnia",
        "lang": "eng"
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
        "lang": "nob",
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

### Registrer fil for opplasting

`isPackaged` angir om filer er pakket midlertidig kun for overføringsformål. Disse filene pakkes for å lette overføringen, og pakkes ut av bevaringsflyten.

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
  "s3ObjectKey": "examplebucket/clientId/contract/submissionId/path/to/file.txt",
  "checksum": "d41d8cd98f00b204e9800998ecf8427e",
  "isPackaged": false,
  "uploadUrl": "https://s3.nb.no/examplebucket/...&X-Amz-Signature=..."
}
```

### Fullfør submission

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
      "s3ObjectKey": "bucket/myClientId/1234/8Z7x1T9rN0Xc2B5Yq4L3zP/representations/primary_20250217/data/ranablad_20250215.pdf",
      "checksum": "d41d8cd98f00b204e9800998ecf8427e",
      "isPackaged": false,
      "uploadUrl": "https://s3.nb.no/examplebucket/...&X-Amz-Signature=..."
    }
  ]
}
```


## Filopplasting

Opplastingsprosessen følger disse stegene:
1. **Registrer en fil** ved å sende POST til `/contracts/{contractId}/submissions/{submissionId}/files`
2. **Hent pre-signert URL** fra responsen. Feltet heter `uploadUrl`, og  er gyldig i ca. 1 time.
3. **Last opp filinnholdet** direkte til S3 ved å bruke HTTP PUT til den angitte URL-en


### Opplasting av fil med bruk av pre-signert URL

```http
PUT {uploadUrl} HTTP/1.1
Content-Length: {file-size-in-bytes}

[FILE CONTENT]
```


{{% details title="Alternativ opplasting for store filer (filer over 5 GiB)" closed="true" %}}

> [!NOTE]
> Denne funksjonaliteten er primært ment for intern bruk på Nasjonalbiblioteket, spesielt for store filer, 
> siden pre-signerte URL-er kun støtter filer med en maksimal størrelse på 5 GiB. 
> Tilgang til S3-bøtta for digital bevaring kan fås ved å kontakte Plattform-teamet.


Opplastingsprosessen følger disse stegene:
1. **Registrer en fil** ved å sende POST til `/contracts/{contractId}/submissions/{submissionId}/files`
2. **Hent ut s3ObjectKey** i responsen
3. **Last opp filinnholdet** direkte til S3 ved å bruke s3ObjectKey som object-nøkkel

Vi anbefaler å bruke AWS CLI til opplastingen. Dokumentasjon finnes her: https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html

Her er et eksempel på hvordan du kan gjøre dette:
```shell
s3 cp path/to/my_big_movie_file.mov s3://examplebucket/clientId/contract/submissionId/path/to/my_big_movie_file.mov --endpoint-url=https://s3.nb.no
```

{{% /details %}}


### Krav til opplasting
- Filen må lastes opp via oppgitt pre-signert URL
- Filinnholdet må ha samme MD5-sjekksum som oppgitt ved registrering

### Håndtering av feil

- Hvis opplasting feiler eller går ut på tid, kan du prøve på nytt med samme URL (hvis gyldig)
- Hvis URL-en er utløpt, slett filregistreringen og registrer på nytt for å få en ny URL

## Statusflyt

En submission går gjennom følgende statuser:

1. `REGISTERED` – Opprettet
2. `UPLOAD_COMPLETED` – Alle filer er lastet opp og submission er fullført
3. `TRANSFERRING` – Innhold overføres til bevaringssystemet
4. `VALIDATING` – Innholdet valideres
5. `ARCHIVING` – Innholdet arkiveres
6. `PRESERVED` – Innholdet er bevart
7. `REJECTED` – Submission er avvist pga. feil


## Beste praksis

1. **Verifiser alltid sjekksum** før opplasting
2. **Bruk unike `objectId` per kontrakt**
3. **Legg ved rik metadata** for bedre søk og bevaring
4. **Håndter feil korrekt** i klientapplikasjonen

## Støtte

Trenger du hjelp eller har spørsmål, kontakt teamet for digital bevaring ved Nasjonalbiblioteket.

## API-referanse

For fullstendig informasjon om endepunkter, parametere, skjema og statuser, se [Swagger-dokumentasjonen](https://digitalpreservation.no/swagger/).
