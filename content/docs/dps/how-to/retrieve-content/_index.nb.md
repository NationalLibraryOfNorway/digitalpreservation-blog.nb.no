---
title: Bestille utlevering av bevart materiale
weight: 3
aliases:
  - /docs/dps/api/dissemination/
---

Denne veiledningen viser hvordan du bestiller utlevering av materiale som er bevart i DPS, og hvordan du laster det ned. Utleveringen skjer asynkront: DPS kontrollerer og klargjør materialet først, og varsler deg når det er klart. Feltnavn og statuser er listet i [API-referansen](/nb/docs/dps/reference/api/#utleveringer).

## Før du starter

- **Klientlegitimasjon og et tilgangstoken**, med en konsumentrolle for kontrakten materialet tilhører. Se [Autentisering og autorisasjon](/nb/docs/dps/reference/api/#autentisering-og-autorisasjon).
- **`archiveId`** for materialet du vil ha. Den sendes i webhooken `submission.preserved` når materialet er bevart.
- **Et webhook-endepunkt** for å motta meldingen `dissemination.delivered` med nedlastingslenkene. Se [Motta varsler](/nb/docs/dps/how-to/receive-notifications/).

## Steg

{{% steps %}}

### Bestill utlevering

Opprett en utlevering (dissemination) med `archiveId`. Bruk standard prioritet med mindre behovet er presserende.

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

Lagre `disseminationId` fra responsen. Hvis en utlevering av det samme materialet allerede pågår, svarer API-et med `409 Conflict`: hent den eksisterende utleveringen i stedet for å opprette en ny.

### Vent til materialet er klargjort

DPS henter materialet fra repositoriet, kontrollerer integriteten og gjør det tilgjengelig for nedlasting. Dette kan ta litt tid. Når materialet er klart, mottar du en webhook-melding `dissemination.delivered`.

Du kan også følge statusen ved å hente utleveringen. Unngå hyppig polling; bruk eksponentiell backoff.

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

### Last ned og kontroller filene

Meldingen [`dissemination.delivered`](/nb/docs/dps/reference/api/#disseminationdelivered) inneholder en liste `files`. Last ned hver fil fra `downloadURL` og sammenlign den med `checksum`, med algoritmen som er angitt i `checksumAlgorithm`.

Last ned filene før lenkene utløper (`expirationDate`). Hvis lenkene utløper, send en ny forespørsel om utlevering; hver utlevering får nye lenker.

{{% /steps %}}

## Beste praksis

1. Gjenbruk eksisterende forespørsel hvis en allerede pågår.
2. Bruk prioritet med måte – reserver lave verdier for presserende behov.
3. Lagre `disseminationId` lokalt.
4. Håndter 409 ved å hente eksisterende i stedet for å poste på nytt.
5. Poll med eksponentiell backoff.
6. Last ned filene før lenkene utløper (`expirationDate` i webhooken `dissemination.delivered`). Hvis lenkene utløper, send en ny forespørsel om dissemination; hver dissemination får nye lenker.

## Støtte

Kontakt teamet for digital bevaring for spørsmål eller hjelp.
