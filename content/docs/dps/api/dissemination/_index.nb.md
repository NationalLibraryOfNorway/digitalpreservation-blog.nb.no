---
title: Dissemination Service
weight: 2
---

## Oversikt

Utleveringstjenesten for digital bevaring tilbyr et REST-basert API for å bestille utlevering av arkiverte og bevarte pakker (AIP-er).
Når en utleveringsforespørsel sendes inn, gjennomføres en integritetskontroll og nødvendig forberedelse før innholdet blir gjort tilgjengelig 
via en presigned URL som sendes gjennom en webhook. Dette er en prosess som tar litt tid, så alt foregår asynkront – 
og en melding vil bli sendt som en webhook når prosessen er ferdig.

For generell informasjon om autentisering og autorisasjon, se [hovedsiden for API-dokumentasjon](../).

Denne dokumentasjonen kompletterer den detaljerte API-spesifikasjonen som er tilgjengelig via Swagger på [https://digitalpreservation.no/swagger/](https://digitalpreservation.no/swagger/).


## Arbeidsflyt

1. Klient sender utleveringsforespørsel med `archiveId` (og ev. `priority`).
2. Tjenesten validerer (autorisasjon, AIP finnes, bevart status, duplikatkontroll).
3. Bakgrunnsprosess kjører integritetskontroll og forbereder data.
4. Objektet blir tilgjengelig via presigned URL avlevert på webhook.
5. Klient kan hente status ved å poll'e på `disseminationId`.


## Endepunkter

| Metode | Path                                   | Beskrivelse           |
|--------|----------------------------------------|-----------------------|
| POST   | `/v1/disseminations`                   | Opprett ny utlevering |
| GET    | `/v1/disseminations/{disseminationId}` | Hent utlevering       |

### Opprett utlevering

**Felt i forespørselen**

| Felt        | Type    | Påkrevd | Beskrivelse                                                                                                             |
|-------------|---------|---------|-------------------------------------------------------------------------------------------------------------------------|
| `archiveId` | string  | Ja      | Unik identifikator for arkivobjektet i DPS som skal utleveres. Mottatt via `submission.preserved`-webhook.              |
| `priority`  | integer | Nei     | Prioritet for behandling i køen. Gyldige verdier: `1` (høyest) til `100` (lavest). Standard er `50` (normal prioritet). |

**Forespørsel**

```http
POST /dps-submission/v1/disseminations HTTP/1.1
Host: api.nb.no
Content-Type: application/json
Authorization: Bearer eyJhbGciOxxxxxxx

{
  "archiveId": "019e404e-60ab-7457-b7c9-94c453242c69",
  "priority": 50
}
```

**Respons (201 Created)**

```json
{
  "disseminationId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
  "archiveId": "019e404e-60ab-7457-b7c9-94c453242c69",
  "clientId": "client-id",
  "contractId": "2d17",
  "objectId": "digifoto_5584a028-ba43-4ecb-bb67-7663cc802010",
  "sumSizeInBytes": 123456,
  "status": "RECEIVED",
  "priority": 50,
  "dateCreated": "2025-09-09T12:34:56.123456+01:00"
}
```

### Hent utlevering

**Forespørsel**

```http
GET /dps-submission/v1/disseminations/8Z7x1T9rN0Xc2B5Yq4L3zP HTTP/1.1
Host: api.nb.no
Content-Type: application/json
Authorization: Bearer eyJhbGciOxxxxxxx
```

**Respons (200 OK)**

```json
{
  "disseminationId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
  "archiveId": "019e404e-60ab-7457-b7c9-94c453242c69",
  "clientId": "client-id",
  "contractId": "2d17",
  "objectId": "digifoto_5584a028-ba43-4ecb-bb67-7663cc802010",
  "sumSizeInBytes": 123456,
  "status": "FIXITY_CHECK",
  "priority": 50,
  "dateCreated": "2025-09-09T12:34:56.123456+01:00"
}
```


## Statusflyt

Foreløpige statuser (kan utvides):

1. `RECEIVED` – Mottatt  
2. `QUEUED` – Lagt i kø  
3. `DOWNLOADING_FROM_REPOSITORY` – Laster ned fra repository  
4. `FIXITY_CHECK` – Integritetskontroll
5. `UPLOADING_TO_S3` – Laster opp til S3
6. `DISSEMINATED` – Utlevert
7. `FAILED` – Feilet  
8. `REJECTED` – Avvist  

## Beste praksis

1. Gjenbruk eksisterende forespørsel hvis en allerede pågår.
2. Bruk prioritet med måte – reserver lave verdier for presserende behov.
3. Lagre `disseminationId` lokalt.
4. Håndter 409 ved å hente eksisterende i stedet for å poste på nytt.
5. Poll med eksponentiell backoff.
6. Gjenbruk nedlastingslenker til de utløper; regenerer kun ved behov.

## Støtte

Kontakt teamet for digital bevaring for spørsmål eller hjelp.

## API-referanse

Se Swagger: <https://digitalpreservation.no/swagger/> for fullstendige skjema og fremtidige endepunkter.
