---
title: Dissemination service API
weight: 2
---

## Oversikt

Dissemination-tjenesten gjør det mulig for klienter å bestille utlevering av arkiverte og bevarte pakker (AIP-er). Når en utleveringsforespørsel sendes inn, gjennomføres en integritetskontroll og nødvendig forberedelse før innholdet blir gjort tilgjengelig via en presigned URL som sendes gjennom en webhook.

Denne dokumentasjonen utfyller den detaljerte API-spesifikasjonen som finnes i Swagger på <https://digitalpreservation.no/swagger/>

For detaljer om autentisering og roller, se Submission Service API.

## Ressursmodell: Dissemination

En dissemination representerer en forespørsel om å utlevere et allerede bevart objekt.

**Viktige egenskaper:**

- `disseminationId`: Unik Base62-ID (22 tegn, case-sensitiv)
- `archiveId`: Intern arkiv-ID (AIP-identifikator)
- `clientId`: Klienten som forespørr
- `contractId`: Kontraktstilknytning
- `objectId`: objekt indentifikator
- `sumSizeInBytes`: Total størrelse
- `status`: Gjeldende status
- `priority`: Prioritet (heltall; lavere = raskere planlegging)
- `dateCreated`: Tidsstempel (RFC 3339)

## Arbeidsflyt

1. Klient sender disseminasjonsforespørsel med `archiveId` (og ev. `priority`).
2. Tjenesten validerer (autorisasjon, AIP finnes, bevart status, duplikatkontroll).
3. Bakgrunnsprosess kjører integritetskontroll og forbereder data.
4. objektet blir tilgjengelig via presigned URL avlevert på webhook.
5. Klient kan hente status ved å poll'e på `disseminationId`.

### Intern prosess (NiFi)

Interne komponenter (NiFi) koordinerer tekniske steg:

1. Hent neste forespørsel (`GET /v1/disseminations/next`).
2. Hent filplasseringer fra LocationDB.
3. Hent filer fra HPSS / annet arkivlag.
4. Kontroller sjekksum (fixity).
5. Skriv filer (eller samlet pakke) til S3.
6. Generer pre-signerte URL-er via API.
7. Ferdigstill (sett disseminated og eksponer lenker).
8. Send varsel (Notify) ved suksess eller feil.

## Endepunkter

| Metode | Path | Beskrivelse | Rolle |
| ------ | ---- | ----------- | ----- |
| POST | `/v1/disseminations` | Opprett ny disseminasjon | `{contractId}_R` |
| GET | `/v1/disseminations/{disseminationId}` | Hent disseminasjon | `{contractId}_R` |

## Opprett disseminasjon

`POST /v1/disseminations`

### Forespørsel (body)

```json
{
  "archiveId": "68cd11bce080fe9cdf1dac1d",
  "priority": 50
}
```

### Respons (201 Created)

```json
{
  "disseminationId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
  "archiveId": "68d3a83aa0be2b1d75eeef77",
  "clientId": "client-id",
  "contractId": "2d17",
  "objectId": "digifoto_5584a028-ba43-4ecb-bb67-7663cc802010",
  "sumSizeInBytes": 123456,
  "status": "FIXITY_CHECK",
  "priority": 50,
  "dateCreated": "2025-09-09T12:34:56.123456+01:00"
}
```

### Feil (opprettelse)

- `400 Bad Request` – Ugyldig input
- `401 Unauthorized` – Manglende/ugyldig token
- `403 Forbidden` – Mangler nødvendig rolle
- `404 AIP not found` – Ukjent `archiveId`
- `409 Conflict` – Allerede en disseminasjon i gang for samme `archiveId` og klient
- `422 Unprocessable Entity` – AIP finnes men er ikke bevart / ikke klar

## Hent dissemination

`GET /v1/disseminations/{disseminationId}`

### Respons (200)

```json
{
  "disseminationId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
  "archiveId": "68d3a83aa0be2b1d75eeef77",
  "clientId": "client-id",
  "contractId": "2d17",
  "objectId": "digifoto_5584a028-ba43-4ecb-bb67-7663cc802010",
  "sumSizeInBytes": 123456,
  "status": "FIXITY_CHECK",
  "priority": 50,
  "dateCreated": "2025-09-09T12:34:56.123456+01:00"
}
```

### Feil (henting)

- `401 Unauthorized`
- `403 Forbidden`
- `404 Dissemination not found`

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
2. Bruk prioritet med måte – reserver høye verdier for presserende behov.
3. Poll med eksponentiell backoff.
4. Lagre `disseminationId` lokalt.
5. Håndter 409 ved å hente eksisterende i stedet for å poste på nytt.
6. Unngå tett polling; bruk eksponentiell backoff.
7. Gjenbruk nedlastingslenker til de utløper; regenerer kun ved behov.

## Støtte

Kontakt teamet for digital bevaring for spørsmål eller hjelp.

## API-referanse

Se Swagger: <https://digitalpreservation.no/swagger/> for fullstendige skjema og fremtidige endepunkter.
