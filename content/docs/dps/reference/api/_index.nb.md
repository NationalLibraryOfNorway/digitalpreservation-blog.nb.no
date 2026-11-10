---
title: Programmeringsgrensesnitt (API)
weight: 1
aliases:
  - /docs/dps/api/
---

## Oversikt

Nasjonalbibliotekets tjenester for digital bevaring tilbyr REST-baserte API-er for å håndtere innlevering (submission) og utlevering (dissemination) av digitale objekter. Dette lar klienter integrere sine systemer med våre bevaringsløp.

Denne dokumentasjonen gir en overordnet oversikt over tilgjengelige API-er. For komplette tekniske detaljer, se vår [Swagger UI](https://digitalpreservation.no/swagger/).

Den maskinlesbare OpenAPI-spesifikasjonen (JSON) er tilgjengelig på <https://api.nb.no/dps-submission/v1/api-docs>.

Med API-et kan du:
- [**Levere materiale til bevaring**](../../how-to/submit-content/): levere digitale objekter til bevaring.
- [**Legge til bevaringseventer**](../../how-to/add-preservation-events/): legge til bevaringseventer i en innlevering.
- [**Bestille utlevering av bevart materiale**](../../how-to/retrieve-content/): bestille bevarte digitale objekter.
- [**Motta varsler**](../../how-to/receive-notifications/): få automatiske statusoppdateringer i dine systemer via webhooks.

Denne siden lister også endepunkter, felt i forespørsler og statusflyt for [innleveringer](#innleveringer) og [utleveringer](#utleveringer), og meldingene som sendes via [webhooks](#webhooks).

## Autentisering og autorisasjon

API-et bruker OAuth 2.0 med JWT-token for autentisering, og implementerer spesifikt OAuth 2.0 Client Credentials-flyten.
Tjenestene er designet for system-til-system-kommunikasjon og støtter ikke autentiseringsflyter basert på sluttbrukere (f.eks. Authorization Code-flyt).

### OAuth 2.0 Client Credentials-flyt

1. Klientapplikasjonen din autentiserer seg mot autorisasjonsserveren ved å bruke client ID og client secret.
2. Autorisasjonsserveren validerer disse legitimasjonene og returnerer et access token.
3. Applikasjonen inkluderer dette tokenet i `Authorization`-headeren i alle API-kall.

All API-kommunikasjon skjer via `https://api.nb.no`, mens autentiseringsforespørsler sendes til `https://www.nb.no/authn/realms/dps/protocol/openid-connect/token`.

**Eksempel på token-forespørsel:**
```http
POST /authn/realms/dps/protocol/openid-connect/token HTTP/1.1
Host: www.nb.no
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id={your_client_id}
&client_secret={your_client_secret}
```

**Eksempel på API-kall med token:**
```http
GET /dps-submission/v1/contracts/{your_contract_id}/submissions/{your_submission_id} HTTP/1.1
Host: api.nb.no
Authorization: Bearer {access_token}
```

### Rollebasert tilgangsstyring

Tilgang til endepunkter styres gjennom roller:

- Kontraktsspesifikke roller (`{contractId}_R`, `{contractId}_W`) gir lese- og skrivetilgang til ressurser under en spesifikk kontrakt
- Rollen `DPS_SUBMISSION_HANDLER` kreves for interne statusoperasjoner

Klientapplikasjonen må hente access token, og den utstedte JWT-en vil inneholde tildelte roller.


## Feilhåndtering

API-et bruker vanlige HTTP-statuskoder:

- `200 OK` – Vellykket
- `201 Created` – Ressurs opprettet
- `400 Bad Request` – Feil i forespørselen
- `401 Unauthorized` – Manglende eller ugyldig token
- `403 Forbidden` – Token gyldig, men mangler rettigheter
- `404 Not Found` – Ressurs ikke funnet
- `409 Conflict` – Duplikat forespørsel
- `422 Unprocessable Entity` – Ressurs finnes men er ikke bevart / ikke klar
- `500 Internal Server Error` – Uventet feil
- `502 Bad Gateway` – En tjeneste API-et er avhengig av, feilet


Feilresponser følger [RFC 9457 Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457) og returneres med medietypen `application/problem+json`:

```json
{
  "type": "https://digitalpreservation.no/problems/submission-not-found",
  "title": "Submission Not Found",
  "status": 404,
  "detail": "Submission with ID 7mVKGHwOA6w2Ot8feF9fIU was not found",
  "instance": "/v1/contracts/4eaf/submissions/7mVKGHwOA6w2Ot8feF9fIU",
  "timestamp": "2025-10-14T10:03:00.123Z",
  "errorCategory": "NOT_FOUND"
}
```

| Felt               | Beskrivelse                                                                                                                                                        |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`             | URI som identifiserer typen problem                                                                                                                                |
| `title`            | Kort, lesbar oppsummering av typen problem                                                                                                                         |
| `status`           | HTTP-statuskoden                                                                                                                                                   |
| `detail`           | Lesbar forklaring av akkurat denne feilen                                                                                                                          |
| `instance`         | URI som identifiserer akkurat denne feilen                                                                                                                         |
| `timestamp`        | Når feilen oppsto (ISO 8601)                                                                                                                                       |
| `errorCategory`    | En av `NOT_FOUND`, `CONFLICT`, `VALIDATION_ERROR`, `BUSINESS_RULE_VIOLATION`, `AUTHORIZATION_ERROR`, `INTERNAL_ERROR`, `EXTERNAL_SERVICE_ERROR`                    |
| `validationErrors` | Bare ved valideringsfeil: et objekt der hvert ugyldig felt har en liste med meldinger                                                                              |
| `currentStatus`    | Bare ved feil som skyldes ressursens tilstand: ressursens nåværende status                                                                                         |


## Innleveringer

Endepunkter for innlevering av materiale. En trinnvis gjennomgang finnes under [Levere materiale til bevaring](/nb/docs/dps/how-to/submit-content/). Alle stier er relative til `https://api.nb.no/dps-submission`.

### Endepunkter for innlevering

| Metode | Sti                                                                    | Beskrivelse                           |
|--------|------------------------------------------------------------------------|---------------------------------------|
| POST   | `/v1/contracts/{contractId}/submissions`                               | Opprett submission                    |
| GET    | `/v1/contracts/{contractId}/submissions`                               | List submissions for kontrakten       |
| GET    | `/v1/contracts/{contractId}/submissions/{submissionId}`                | Hent submission                       |
| DELETE | `/v1/contracts/{contractId}/submissions/{submissionId}`                | Slett submission                      |
| POST   | `/v1/contracts/{contractId}/submissions/{submissionId}/files`          | Registrer fil og få opplastings-URL   |
| GET    | `/v1/contracts/{contractId}/submissions/{submissionId}/files/{fileId}` | Hent fil                              |
| DELETE | `/v1/contracts/{contractId}/submissions/{submissionId}/files/{fileId}` | Slett fil                             |
| POST   | `/v1/contracts/{contractId}/submissions/{submissionId}/finalize`       | Fullfør submission                    |
| POST   | `/v1/contracts/{contractId}/submissions/{submissionId}/events`         | Send inn event, se [Bevaringseventer](/nb/docs/dps/reference/preservation-events/) |
| GET    | `/v1/contracts/{contractId}/submissions/{submissionId}/events`         | Hent eventer                          |

- **Liste over submissions:** Sortert etter når de ble opprettet, og paginert med `page` (nullbasert, standard `0`) og `size` (standard `10`). Filtrer med `objectId` og/eller `archiveId` (eksakt treff; flere filtre kombineres med OG). Hvis ingenting treffer, er responsen en tom side.
- **Hent submission:** Bruk query-parameteren `include` for å ta med relaterte data i responsen: `FILES` (registrerte filer), `DESCRIPTIVE_METADATA` (metadataene fra forespørselen) og `EVENTS` (bevaringshendelser), f.eks. `?include=FILES&include=EVENTS`.
- **Slett submission:** Bare tillatt mens submissionen har status `REGISTERED` og ikke har registrerte filer. Slett filene først; en submission som fortsatt har filer, gir `409 Conflict`.
- **Slett fil:** Bare tillatt mens submissionen har status `REGISTERED`; ellers svarer API-et med `409 Conflict`. Som standard slettes bare filregistreringen. Legg til `deleteFromS3=true` for også å slette den opplastede filen fra S3.
- **Fullfør submission:** Submissionen må ha minst én registrert fil som ikke er tom, og alle registrerte filer må ligge i S3; ellers svarer API-et med `422 Unprocessable Entity`. En submission kan bare fullføres én gang; et nytt kall gir `409 Conflict`.
- **Send inn event:** Bare tillatt mens submissionen har status `REGISTERED`. En vellykket forespørsel gir `204 No Content`.

### Felt i forespørsler om innlevering

#### Opprett submission

| Felt       | Type    | Påkrevd | Beskrivelse |
|------------|---------|---------|-------------|
| `objectId` | string  | Ja      | Klientens identifikator for innleveringsobjektet – vanligvis en ID fra kildesystemet (f.eks. en database-ID eller URN-fragment). Kobler DPS-hendelser som webhooks tilbake til objektet i ditt system. Må være unik per kontrakt (kombinasjonen `contractId` + `objectId` må være unik). Kan ikke endres etter at innleveringen er levert til DPS. Må være 3–200 tegn og kan bare inneholde `a-z`, `A-Z`, `0-9`, `-` og `_`. |
| `priority` | integer | Nei     | Prioritet for behandling i køen. Gyldige verdier: `1` (høyest) til `100` (lavest). Standard er `50` (normal prioritet), og er det som vanligvis skal brukes. Verdier over `50` angir lavere prioritet og brukes f.eks. ved rearkivering. |
| `metadata` | object  | Ja      | Beskrivende metadata om innholdet. Se [Krav til metadata](/nb/docs/dps/reference/descriptive-metadata/) for tilgjengelige elementer. |

#### Registrer fil

| Felt         | Type    | Påkrevd | Beskrivelse |
|--------------|---------|---------|-------------|
| `filePath`   | string  | Ja      | Relativ sti til filen i submissionen. Må være unik i submissionen, kan være maks 900 tegn, kan bare inneholde `a-z`, `A-Z`, `0-9`, `-`, `_`, `.`, `(`, `)` og `/`, og kan ikke starte med `/` eller `.`. |
| `checksum`   | string  | Ja      | MD5-sjekksum for filen, som 32 heksadesimale tegn med små bokstaver. |
| `isPackaged` | boolean | Nei     | Om filen er pakket midlertidig kun for overføring (for eksempel som TAR eller ZIP). Slike filer pakkes ut av bevaringsflyten. Standard er `false`. |

Responsen inneholder `fileId`, `s3ObjectKey` og en `uploadUrl` for opplasting av filinnholdet.

### Begrensninger for innlevering

| Begrensning | Verdi |
|-------------|-------|
| Maks filstørrelse ved opplasting via pre-signert URL | 5 GiB per fil |
| Gyldighet for pre-signert opplastings-URL (`uploadUrl`) | Ca. 1 time |
| Sjekksumalgoritme | MD5 |

Begrensningen i filstørrelse skyldes restriksjoner i pre-signerte S3-URL-er. Større filer kan lastes opp direkte til S3 med `s3ObjectKey`; dette er primært ment for intern bruk på Nasjonalbiblioteket.

### Statusflyt for innlevering

En submission går gjennom følgende statuser:

1. `REGISTERED` – Opprettet
2. `UPLOAD_COMPLETED` – Alle filer er lastet opp og submission er fullført
3. `PROCESSING` – Innholdet overføres til, valideres og arkiveres i bevaringssystemet
4. `PRESERVED` – Innholdet er bevart
5. `REJECTED` – Submission er avvist pga. feil

Endringer til `PRESERVED` og `REJECTED` sendes også som [webhook](/nb/docs/dps/how-to/receive-notifications/)-meldinger (`submission.preserved` og `submission.rejected`).

## Utleveringer

Endepunkter for å bestille utlevering av bevart materiale. En trinnvis gjennomgang finnes under [Bestille utlevering av bevart materiale](/nb/docs/dps/how-to/retrieve-content/). Alle stier er relative til `https://api.nb.no/dps-submission`.

### Endepunkter for utlevering

| Metode | Sti                                    | Beskrivelse           |
|--------|----------------------------------------|-----------------------|
| POST   | `/v1/disseminations`                   | Opprett ny utlevering |
| GET    | `/v1/disseminations/{disseminationId}` | Hent utlevering       |

- **Opprett utlevering:** API-et kontrollerer at klienten er autorisert, at pakken finnes og er bevart, og at forespørselen ikke er et duplikat. Hvis en utlevering allerede pågår, svarer API-et med `409 Conflict`. Forberedelsen kjører deretter i bakgrunnen, og resultatet leveres gjennom [webhooken](/nb/docs/dps/how-to/receive-notifications/) `dissemination.delivered`.

### Felt i forespørsler om utlevering

| Felt        | Type    | Påkrevd | Beskrivelse |
|-------------|---------|---------|-------------|
| `archiveId` | string  | Ja      | Unik identifikator for arkivobjektet i DPS som skal utleveres. Mottatt via `submission.preserved`-webhook. |
| `priority`  | integer | Nei     | Prioritet for behandling i køen. Gyldige verdier: `1` (høyest) til `100` (lavest). Standard er `50` (normal prioritet). |

### Statusflyt for utlevering

Foreløpige statuser (kan utvides):

1. `RECEIVED` – Mottatt
2. `QUEUED` – Lagt i kø
3. `DOWNLOADING_FROM_REPOSITORY` – Laster ned fra repository
4. `FIXITY_CHECK` – Integritetskontroll
5. `UPLOADING_TO_S3` – Laster opp til S3
6. `DISSEMINATED` – Utlevert
7. `FAILED` – Feilet
8. `REJECTED` – Avvist

Nedlastingslenkene i webhooken `dissemination.delivered` utløper på tidspunktet som er angitt i `expirationDate`. Hver nye utlevering får nye lenker.

## Webhooks

Meldinger som DPS sender til webhook-endepunktet ditt. Hvordan du setter opp og verifiserer et endepunkt, er beskrevet under [Motta varsler](/nb/docs/dps/how-to/receive-notifications/). DPS bruker [Standard Webhooks](https://www.standardwebhooks.com) for format og signering.

### Levering av webhooks

| Egenskap          | Krav                                         |
|-------------------|----------------------------------------------|
| **Protokoll**     | HTTPS (TLS 1.2 eller høyere)                 |
| **Metode**        | POST                                         |
| **Content-Type**  | `application/json`                           |
| **Autentisering** | HMAC-signatur i header (`webhook-signature`) |
| **Sertifikat**    | Gyldig TLS-sertifikat kreves                 |
| **Standard** | [Standard Webhooks](https://www.standardwebhooks.com) |
| **Respons** | `200 OK` eller `204 No Content` innen 10 sek          |
| **Retries** | Ja (eksponentiell backoff. opptil 5 døgn totalt)      |
| **Konfigurasjon** | Håndteres manuelt av NB                               |

### Webhook-headere

Alle meldinger sendes med følgende headere:

```
webhook-id: <unik id>
webhook-timestamp: <unix-sekunder>
webhook-signature: v1,<base64-signatur>
```

| Header              | Beskrivelse                                                                            |
|---------------------|----------------------------------------------------------------------------------------|
| `webhook-id`        | Unik ID for meldingen (samme ID brukes ved retries – bruk som dedup-nøkkel)            |
| `webhook-timestamp` | UNIX-tid i sekunder; bruk tidsvindu (±5–10 min) for å avvise gamle meldinger           |
| `webhook-signature` | HMAC-SHA256 av `id + "." + timestamp + "." + rå request-body`, signert med delt nøkkel |

>  **Tips:** verifiser alltid signaturen mot rå **request-body**, ikke en reserialisert JSON-struktur.

### Struktur på webhook-meldinger

Alle webhook-meldinger følger samme struktur («envelope»):

```json
{
  "type": "<event type>",
  "timestamp": "2025-09-10T00:08:11.407000+02:00",
  "data": {}
}
```

| Felt        | Type   | Beskrivelse                                                                                  |
|-------------|--------|----------------------------------------------------------------------------------------------|
| `type`      | string | Hendelsestype (se nedenfor)                                                                  |
| `timestamp` | string | Tidspunkt da hendelsen oppsto, i RFC3339/ISO 8601-format med eksplisitt offset eller UTC (Z) |
| `data`      | object | Hendelsesspesifikke felter                                                                   |

### Webhook-hendelser

DPS støtter foreløpig følgende hendelser.

#### `submission.preserved`

Webhook sendt når en SIP-innlevering er bevart og lagret permanent.

**Eksempel**
```json
{
  "type": "submission.preserved",
  "timestamp": "2025-09-10T00:08:11.407000+02:00",
  "data": {
    "contractId": "ef23",
    "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
    "archiveId": "019e404e-60ab-7457-b7c9-94c453242c69"
  }
}
```

| Felt           | Type   | Beskrivelse                                                                                                                                                                                                  |
|----------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `contractId`   | string | Identifikator for kontrakt eller avtale som innsendelsen er knyttet til                                                                                                                                      |
| `submissionId` | string | Unik identifikator for SIP-innleveringen                                                                                                                                                                     |
| `archiveId`    | string | Unik identifikator for det bevarte arkivobjektet i DPS. Tildeles når innleveringen er arkivert. Bruk denne ID-en til å referere til objektet i fremtidige forespørsler, f.eks. ved bestilling av utlevering. |

#### `submission.rejected`

Webhook sendt når en SIP-innlevering er avvist under validering eller behandling.

**Eksempel**
```json
{
  "type": "submission.rejected",
  "timestamp": "2025-09-10T00:08:11.407000+02:00",
  "data": {
    "contractId": "ef23",
    "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
    "archiveId": "019e404e-60ab-7457-b7c9-94c453242c69",
    "reasons": [
      {
        "code": "METADATA_SCHEMA_INVALID",
        "message": "Descriptive metadata did not validate against the required profile."
      },
      {
        "code": "FILE_CHECKSUM_MISMATCH",
        "message": "Checksum mismatch.",
        "filePath": "objects/issue_1942_05.pdf"
      }
    ]
  }
}
```

| Felt           | Type   | Beskrivelse                                                                                                                                    |
|----------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `contractId`   | string | Identifikator for kontrakt eller avtale som innsendelsen er knyttet til                                                                        |
| `submissionId` | string | Unik identifikator for SIP-innleveringen                                                                                                       |
| `archiveId`    | string | Unik identifikator for arkivobjektet i DPS.                                                                                                    |
| `reasons`      | array  | Liste med årsaker til avvisning. Minst én oppføring.                                                                                           |
| → `code`       | string | Maskinlesbar feilkode som identifiserer typen feil. Stabil over tid                                                                            |
| → `message`    | string | Menneskelesbar beskrivelse av feilen                                                                                                           |
| → `filePath`   | string | Relativ sti til filen feilen gjelder, dersom feilen kan knyttes til en bestemt fil. Om dette feltet mangler, gjelder feilen pakken som helhet. |

#### `dissemination.delivered`

Webhook sendt når et leveransesett (DIP) er gjort tilgjengelig for nedlasting.

**Eksempel**
```json
{
  "type": "dissemination.delivered",
  "timestamp": "2025-10-02T09:18:01.160+02:00",
  "data": {
    "archiveId": "019e404e-60ab-7457-b7c9-94c453242c69",
    "disseminationId": "5MfwdzCjkYW4c79MYorXy9",
    "objectId": "digifoto_ae0690eb-22bf-4996-a6a0-9273b7cd9256",
    "clientId": "kulturit",
    "contractId": "2d17",
    "sumSizeInBytes": "1",
    "files": [
      {
        "downloadURL": "https://minio.dev.nb.no/submission-service-stage/dissemination/5MfwdzCjkYW4c79MYorXy9/68d3a838a0be2b1d75eeef75/primary_20250325.tar?...",
        "filename": "primary_20250325.tar",
        "filesize": 3481600,
        "expirationDate": "2025-10-03T09:18:01.023897767+02:00",
        "checksum": "ae958c69059974c63980035882d2178c",
        "checksumAlgorithm": "MD5"
      }
    ]
  }
}
```

| Felt                  | Type      | Beskrivelse                                                                                                                                                          |
|-----------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `archiveId`           | string    | Unik identifikator for det bevarte arkivobjektet i DPS. Samme ID som i `submission.preserved`. Bruk den til å koble utleveringen til den opprinnelige innleveringen. |
| `disseminationId`     | string    | Unik identifikator for leveransepakke                                                                                                                                |
| `objectId`            | string    | Objektidentifikator fra avleverer – samme verdi som ble oppgitt ved oppretting av submission                                                                         |
| `clientId`            | string    | Mottaker                                                                                                                                                             |
| `contractId`          | string    | Identifikator for kontrakt eller avtale som leveransepakken er knyttet til                                                                                           |
| `sumSizeInBytes`      | integer   | Total størrelse i bytes                                                                                                                                              |
| `files`               | array     | Liste over filer i pakken                                                                                                                                            |
| → `downloadURL`       | uri       | Presignert nedlastings-URL                                                                                                                                           |
| → `filename`          | string    | Filnavn                                                                                                                                                              |
| → `filesize`          | integer   | Filstørrelse i bytes                                                                                                                                                 |
| → `expirationDate`    | date-time | Utløpsdato for URL                                                                                                                                                   |
| → `checksum`          | string    | Sjekksum                                                                                                                                                             |
| → `checksumAlgorithm` | enum      | Algoritme brukt for sjekksum                                                                                                                                         |

## Støtte

Trenger du hjelp eller har spørsmål, kontakt teamet for digital bevaring ved Nasjonalbiblioteket.

## API-referanse

For fullstendig informasjon om endepunkter, parametere, skjema og statuser, se [Swagger-dokumentasjonen](https://digitalpreservation.no/swagger/).
