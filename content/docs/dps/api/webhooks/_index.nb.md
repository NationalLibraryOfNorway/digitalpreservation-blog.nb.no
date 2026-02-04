---
title: Webhooks
weight: 3
---

# Webhooks fra Digital Preservation System (DPS)

Nasjonalbiblioteket kan sende hendelsesvarsler direkte til dine systemer via webhooks.  
DPS bruker **Standard Webhooks**[^1] for format og signering,
slik at varsler kan valideres sikkert og behandles automatisk.

Dette lar deg motta automatiske meldinger når innleveringer eller utleveringer endrer status – uten å måtte spørre API-et vårt kontinuerlig.

For å motta disse varslene må du ha et **endepunkt (en URL)** som kan ta imot **HTTPS POST**-forespørsler med **JSON-data** fra DPS.  
Nasjonalbiblioteket registrerer foreløpig alle webhook-endepunkter manuelt i samarbeid med hver partner.

---

## Formål

- Varsle om statusendringer i innleveringer
- Varsle om fullførte utleveringer
- Sikre trygg og forutsigbar levering med tydelige kontrakter

---

## Hvordan det fungerer

Når en hendelse oppstår i DPS:

1. DPS sender en **HTTP POST**-forespørsel til URL-en du har oppgitt
2. Meldingen inneholder informasjon om hendelsen i **JSON-format**, i henhold til *Standard Webhooks*
3. Ditt system mottar meldingen, validerer at den kommer fra DPS, og svarer med **HTTP 200 OK**

## Tekniske krav

### Transport og format

| Egenskap          | Krav                                         |
|-------------------|----------------------------------------------|
| **Protokoll**     | HTTPS (TLS 1.2 eller høyere)                 |
| **Metode**        | POST                                         |
| **Content-Type**  | `application/json`                           |
| **Autentisering** | HMAC-signatur i header (`webhook-signature`) |
| **Responstid**    | Maks 10 sekunder                             |
| **Sertifikat**    | Gyldig TLS-sertifikat kreves                 |

### Endepunkt-oppsett

Du må eksponere en offentlig tilgjengelig URL, for eksempel:

```http
https://partner.example.com/api/dps/webhook
```

**Anbefalinger:**

- Bruk IP-allowlist (vi kan oppgi faste utgående IP-er ved behov)
- Sett opp overvåkning og varsling av at tjenesten din er operativ
- Valider signaturen for hver melding før behandling

---

## HTTP-headere (Standard Webhooks-format)

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

---

## Svar på meldingen

Webhook-mottakeren må:

- svare med HTTP **200 OK** eller **204 No Content** innen 10 sekunder
- returnere ingen eller minimal body (DPS bryr seg kun om statuskode)
- ved 4xx/5xx eller timeout vil DPS prøve igjen med eksponentiell backoff

---

## Felles JSON-struktur

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

---

## Hendelser

DPS støtter foreløpig følgende hendelser.

---

### `submission.preserved`

Webhook sendt når en SIP-innlevering er bevart og lagret permanent.

**Eksempel**
```json
{
  "type": "submission.preserved",
  "timestamp": "2025-09-10T00:08:11.407000+02:00",
  "data": {
    "contractId": "ef23",
    "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
    "archiveId": "68b803fb25d74833747835f7"
  }
}
```

| Felt           | Type   | Beskrivelse                                                             |
|----------------|--------|-------------------------------------------------------------------------|
| `contractId`   | string | Identifikator for kontrakt eller avtale som innsendelsen er knyttet til |
| `submissionId` | string | Unik identifikator for SIP-innleveringen                                |
| `archiveId`    | string | Unik identifikator for arkivobjekt i DPS                                |

---

### `submission.rejected`

Webhook sendt når en SIP-innlevering er avvist under validering eller behandling.

**Eksempel**
```json
{
  "type": "submission.rejected",
  "timestamp": "2025-09-10T00:08:11.407000+02:00",
  "data": {
    "contractId": "ef23",
    "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
    "archiveId": "68b803fb25d74833747835f7",
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
| `archiveId`    | string | Unik identifikator for arkivobjekt i DPS                                                                                                       |
| `reasons`      | array  | Liste med årsaker til avvisning. Minst én oppføring.                                                                                           |
| → `code`       | string | Maskinlesbar feilkode som identifiserer typen feil. Stabil over tid                                                                            |
| → `message`    | string | Menneskelesbar beskrivelse av feilen                                                                                                           |
| → `filePath`   | string | Relativ sti til filen feilen gjelder, dersom feilen kan knyttes til en bestemt fil. Om dette feltet mangler, gjelder feilen pakken som helhet. |

---

### `dissemination.delivered`

Webhook sendt når et leveransesett (DIP) er gjort tilgjengelig for nedlasting.

**Eksempel**
```json
{
  "type": "dissemination.delivered",
  "timestamp": "2025-10-02T09:18:01.160+02:00",
  "data": {
    "archiveId": "68d3a838a0be2b1d75eeef75",
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

| Felt                  | Type      | Beskrivelse                                                                |
|-----------------------|-----------|----------------------------------------------------------------------------|
| `archiveId`           | string    | Unik identifikator for arkivobjekt i DPS                                   |
| `disseminationId`     | string    | Unik identifikator for leveransepakke                                      |
| `objectId`            | string    | Objekt identifikator fra avvleverer                                        |
| `clientId`            | string    | Mottaker                                                                   |
| `contractId`          | string    | Identifikator for kontrakt eller avtale som leveransepakken er knyttet til |
| `sumSizeInBytes`      | integer   | Total størrelse i bytes                                                    |
| `files`               | array     | Liste over filer i pakken                                                  |
| → `downloadURL`       | uri       | Presignert nedlastings-URL                                                 |
| → `filename`          | string    | Filnavn                                                                    |
| → `filesize`          | integer   | Filstørrelse i bytes                                                       |
| → `expirationDate`    | date-time | Utløpsdato for URL                                                         |
| → `checksum`          | string    | Sjekksum                                                                   |
| → `checksumAlgorithm` | enum      | Algoritme brukt for sjekksum                                               |

---

## Signaturverifisering

Webhookene signeres for å sikre autentisitet og integritet.  
Mottakeren må validere signaturen før meldingen behandles.

**Pseudokode:**

```text
raw = les_rå_body()
id = header["webhook-id"]
ts = header["webhook-timestamp"]
sig_header = header["webhook-signature"]   # kan inneholde flere (v1,<b64>)

base = id + "." + ts + "." + raw
calc = base64(hmac_sha256(secret, base))

# Godta dersom én v1-signatur i header matcher calc (konstant-tids-sammenligning)
# Avvis dersom |nå - ts| > toleransevindu (replay-beskyttelse)
# Parse JSON etter vellykket verifisering
```

---

## Feilsøking

### Vanlige problemer

1. **Timeout:** Sørg for at endepunktet svarer innen tidsfristen
2. **Sertifikatfeil:** TLS-sertifikatet må være gyldig og riktig konfigurert
3. **Signaturfeil:** Sjekk at HMAC-verifiseringen implementeres korrekt
4. **Duplikater:** Implementer deduplisering basert på `webhook-id`

---

## Konfigurasjon og støtte

I denne fasen håndteres registrering av webhook-URL og delt hemmelig nøkkel **manuelt av Nasjonalbiblioteket**.  
Vi koordinerer oppsett og test før produksjonsbruk.

For spørsmål om webhook-oppsett eller om du opplever problemer, kontakt teamet for digital bevaring ved Nasjonalbiblioteket.

Vi kan hjelpe med:

- Testing av webhook-endepunkt
- Oppgi faste IP-adresser for allowlisting
- Feilsøking av leveringsproblemer

---

## Oppsummering

| Egenskap      | Verdi                                                 |
|---------------|-------------------------------------------------------|
| Transport     | HTTPS                                                 |
| Metode        | POST                                                  |
| Innholdstype  | `application/json`                                    |
| Standard      | [Standard Webhooks](https://www.standardwebhooks.com) |
| Autentisering | HMAC-signatur (`webhook-signature`)                   |
| Respons       | `200 OK` eller `204 No Content` innen 10 sek          |
| Retries       | Ja (eksponentiell backoff. opptil 5 døgn totalt)      |
| Konfigurasjon | Håndteres manuelt av NB                               |


[^1]: Standard Webhooks: [https://www.standardwebhooks.com](https://www.standardwebhooks.com)