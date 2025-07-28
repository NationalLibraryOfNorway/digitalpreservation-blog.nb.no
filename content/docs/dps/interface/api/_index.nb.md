---
title: Submission Service API
weight: 1
draft: true
-----------

## Oversikt

Submission-tjenesten for digital bevaring tilbyr et REST-basert API for å håndtere digitale leveranser og tilhørende filer. Tjenesten lar klienter opprette leveranser, registrere filer, laste opp innhold og spore statusen gjennom hele bevaringsprosessen.

Denne dokumentasjonen kompletterer den detaljerte API-spesifikasjonen som er tilgjengelig via Swagger på [https://digitalpreservation.no/swagger/](https://digitalpreservation.no/swagger/).

## Autentisering og autorisasjon

API-et bruker OAuth 2.0 med JWT-token for autentisering, og implementerer spesifikt OAuth 2.0 Client Credentials-flyten.
Submission-tjenesten er designet for system-til-system-kommunikasjon og støtter ikke autentiseringsflyter basert på sluttbrukere (f.eks. Authorization Code-flyt).

### OAuth 2.0 Client Credentials-flyt

1. Klientapplikasjonen din autentiserer seg mot autorisasjonsserveren ved å bruke client ID og client secret
2. Autorisasjonsserveren validerer disse legitimasjonene og returnerer et access token
3. Applikasjonen inkluderer dette tokenet i Authorization-headeren i alle API-kall

All API-kommunikasjon skjer via [https://api.nb.no](https://api.nb.no), mens autentiseringsforespørsler sendes til [https://www.nb.no/authn/realms/dps/protocol/openid-connect/token](https://www.nb.no/authn/realms/dps/protocol/openid-connect/token).

Eksempel på token-forespørsel:

```http
POST /authn/realms/dps/protocol/openid-connect/token HTTP/1.1
Host: www.nb.no
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id={your_client_id}
&client_secret={your_client_secret}
```

Eksempel på API-kall med token:

```http
GET /dps-submission/v1/contracts/{your_contract_id}/submissions/{your_submission_id} HTTP/1.1
Host: api.nb.no
Authorization: Bearer {access_token}
```

### Rollebasert tilgangsstyring

Tilgang til endepunkter styres gjennom roller:

* Kontraktsspesifikke roller (`{contractId}_R`, `{contractId}_W`) gir lese- og skrivetilgang til ressurser under en spesifikk kontrakt
* Rollen `DPS_SUBMISSION_HANDLER` kreves for interne statusoperasjoner

Klientapplikasjonen må hente access token, og den utstedte JWT-en vil inneholde tildelte roller.

## Ressursmodeller

### Submission

En submission representerer en pakke med filer og metadata som skal bevares.

**Viktige egenskaper:**

* `contractId`: Kontrakts-ID i Base16 (heksadesimalt) format (4 tegn, \[0-9A-F])
* `submissionId`: Unik ID i Base62-format (22 tegn, \[A-Za-z0-9]). ID-en er case-sensitiv
* `clientId`: ID for klienten som laster opp, hentet fra JWT-token
* `objectId`: Klientdefinert ID for objektet
* `status`: Gjeldende status for submissionen
* `priority`: Prioritet for submissionen, brukt for behandlingsrekkefølge i DPS
* `metadata`: Dublin Core-basert [metadata](metadata/) for submissionen
* `sumSizeInBytes`: Total filstørrelse i bytes

### File

En fil representerer en individuell digital ressurs i en submission.

**Viktige egenskaper:**

* `contractId`: Kontrakts-ID i Base16 (4 tegn, \[0-9A-F])
* `submissionId`: Unik ID i Base62-format (22 tegn). Case-sensitiv
* `fileId`: Unik ID i Base62-format (22 tegn). Case-sensitiv
* `filePath`: Relativ filsti innen submissionen
* `s3ObjectKey`: Intern S3-nøkkel hvor filen er lagret
* `checksum`: MD5-sjekksum av filinnholdet
* `isPackaged`: Angir om filen er pakket (f.eks. ZIP eller TAR) og skal pakkes ut under behandling. Hvis `true`, vil innholdet pakkes ut og behandles individuelt.
* `uploadUrl`: Pre-signert URL for direkte opplasting til vår S3-kompatible lagring

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

### Eksempel: registrer ny submission
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

### Eksempel: registrer fil for opplasting

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
  "checksum": "d41d8cd98f00b204e9800998ecf8427e",
  "isPackaged": false,  
  "uploadUrl": "https://s3.nb.no/examplebucket/...&X-Amz-Signature=..."
}
```

### Eksempel: fullfør submission

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
      "s3ObjectKey": "myClientId/1234/8Z7x1T9rN0Xc2B5Yq4L3zP/representations/primary_20250217/data/ranablad_20250215.pdf",
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
2. **Få en pre-signert URL** i responsen (gyldig i ca. 1 time)
3. **Last opp filinnholdet** direkte til S3 ved å bruke HTTP PUT til den angitte URL-en

### Bruk av pre-signert URL

```http
PUT {pre-signed-url} HTTP/1.1
Content-Length: {file-size}

[FILE CONTENT]
```

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

## Feilhåndtering

API-et bruker vanlige HTTP-statuskoder:

* `200 OK` – Vellykket
* `201 Created` – Ressurs opprettet
* `400 Bad Request` – Feil i forespørselen
* `401 Unauthorized` – Manglende eller ugyldig token
* `403 Forbidden` – Token gyldig, men mangler rettigheter
* `404 Not Found` – Ressurs ikke funnet
* `409 Conflict` – Duplikat
* `500 Internal Server Error` – Uventet feil

Ved feil returneres et JSON-objekt med `error`:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "A descriptive error message",
    "details": "Additional details about the error"
  }
}
```

## Beste praksis

1. **Verifiser alltid sjekksum** før opplasting
2. **Bruk unike `objectId` per kontrakt**
3. **Legg ved rik metadata** for bedre søk og bevaring
4. **Håndter feil korrekt** i klientapplikasjonen

## Støtte

Trenger du hjelp eller har spørsmål, kontakt teamet for digital bevaring ved Nasjonalbiblioteket.

## API-referanse

For fullstendig informasjon om endepunkter, parametere, skjema og statuser, se [Swagger-dokumentasjonen](https://digitalpreservation.no/swagger/).
