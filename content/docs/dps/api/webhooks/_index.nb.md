---
title: Webhooks
weight: 3
---

## Oversikt

Nasjonalbiblioteket kan sende statusoppdateringer direkte til dine systemer via webhooks. Dette lar deg motta automatiske varsler om statusendringer i innleveringer og utleveringer uten å måtte spørre vårt API kontinuerlig.

Denne dokumentasjonen beskriver hvordan du som samarbeidspartner kan sette opp HTTP-endepunkter (webhooks) som vi vil kalle for å levere statusmeldinger.

**Formål:**

- Varsle om statusendringer i innleveringer
- Varsle om fullførte utleveringer
- Sikre trygg og forutsigbar levering med tydelige kontrakter

## Tekniske krav

### Transport og format

- **Protokoll:** HTTPS (TLS 1.2+)
- **Metode:** POST
- **Format:** JSON (`Content-Type: application/json; charset=utf-8`)
- **Autentisering:** Bearer-token (OAuth2 Client Credentials eller statisk), eller Basic auth over HTTPS
- **Responstid:** Må svare innen 5 sekunder ved normal drift
- **Sertifikat:** Må ha gyldig TLS-sertifikat

### Endepunkt-oppsett

Du må eksponere en offentlig tilgjengelig URL, for eksempel:

```http
POST https://partner.example.com/webhooks/status
```

**Anbefalinger:**

- Bruk IP-allowlist (vi kan oppgi faste utgående IP-er ved behov)
- Implementer logging for debugging
- Sett opp monitoring og alerting

## Meldingsformat

### Headere

Hver webhook-forespørsel inkluderer spesielle headere:

```http
webhook-id: 74ea5da5-df40-47e9-9d44-4040b0c292fc
webhook-timestamp: 1757458468973
```

**Feltbeskrivelser:**

- `webhook-id`: Unik meldingsID som ikke endres ved retry
- `webhook-timestamp`: Unix timestamp i millisekunder for når meldingen ble sendt

### Meldingsstruktur

Alle meldinger følger samme grunnstruktur:

```json
{
  "type": "submission.preserved",
  "timestamp": "2025-08-26T14:39:53.344522+02:00",
  "data": {
    "contractId": "ef23",
    "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
    "archiveId": "68b803fb25d74833747835f7"
  }
}
```

**Feltbeskrivelser:**

- `type` (string): Hendelsestype (se [Hendelsestyper](#hendelsestyper))
- `timestamp` (string): ISO 8601-tidsstempel med tidssone for statusendring
- `data` (object): Hendelsespesifikke data

**Fremtidig kompatibilitet:**
Vi kan legge til nye, ikke-påkrevde felter. Ditt endepunkt bør ignorere ukjente felter for å forbli kompatibel med fremtidige versjoner.

## Hendelsestyper

### Submission-hendelser

Følgende hendelsestyper sendes for innleveringer:

- `submission.validating` - Innlevering valideres
- `submission.queued` - Innlevering i kø for prosessering  
- `submission.processing` - Arkivobjekt behandles av DPS
- `submission.archiving` - Arkivobjekt sendes til lagring
- `submission.preserved` - Arkivobjekt kontrollert og bevart
- `submission.rejected` - Feil under validering, arkivobjekt avvises

**Eksempel submission-melding:**

```json
{
  "type": "submission.preserved",
  "timestamp": "2025-08-26T14:39:53.344522+02:00",
  "data": {
    "contractId": "ef23",
    "submissionId": "8Z7x1T9rN0Xc2B5Yq4L3zP",
    "archiveId": "68b803fb25d74833747835f7"
  }
}
```

### Dissemination-hendelser

For utleveringer sendes følgende hendelsestype:

- `dissemination.delivered` - Utlevering er klar for nedlasting

**Eksempel dissemination-melding:**

```json
{
  "type": "dissemination.delivered",
  "timestamp": "2025-10-15T12:18:42.315+02:00",
  "data": {
    "archiveId": "68ee1917e2768fd730076661",
    "disseminationId": "0pS8bYb6KmJoRvBtZ3Qxd1",
    "objectId": "5280df44-d34e-4195-ac6f-ee96fe0e01d4",
    "clientId": "client-id",
    "contractId": "ef23",
    "sumSizeInBytes": 215040,
    "files": [
      {
        "downloadURL": "https://s3.nb.no/bucket/0pS8bYb6KmJoRvBtZ3Qxd1/68ee1917e2768fd730076661/metadata.tar",
        "filename": "metadata.tar",
        "filesize": 163840,
        "expirationDate": "2025-10-16T12:18:41.919934218+02:00",
        "checksum": "43943b08cbfc1748abe7b30e2ffc9963",
        "checksumAlgorithm": "MD5"
      },
      {
        "downloadURL": "https://s3.nb.no/bucket/0pS8bYb6KmJoRvBtZ3Qxd1/68ee1917e2768fd730076661/primary_20251014.tar",
        "filename": "primary_20251014.tar",
        "filesize": 51200,
        "expirationDate": "2025-10-16T12:18:41.934462292+02:00",
        "checksum": "ae393a24d6e5c0f4e0bc6d544be56570",
        "checksumAlgorithm": "MD5"
      }
    ]
  }
}
```

Vi kan avtale hvilke hendelsestyper som skal sendes varsling på basert på dine behov.

## Autentisering

### Bearer Token (anbefalt)

Vi støtter to typer Bearer token-autentisering:

#### OAuth2 Client Credentials

1. Vi sender POST-forespørsel til ditt token-endepunkt med `grant_type=client_credentials`
2. Vi mottar et `access_token` (JWT eller opaque)  
3. Ved hvert webhook-kall sender vi headeren:

   ```http
   Authorization: Bearer <access_token>
   ```

4. Vi fornyer token automatisk ved utløp. Ved 401 Unauthorized henter vi nytt token og forsøker på nytt.

#### Statisk API-token

Du kan utstede en lang, tilfeldig API-token som vi sender i headeren:

```http
Authorization: Bearer <API_token>
```

### Basic Authentication

Alternativt kan du kreve HTTP Basic over HTTPS:

```http
Authorization: Basic <base64(username:password)>
```

**Viktig:** Basic auth brukes kun over sikker TLS-forbindelse.

### Tilleggstiltak

- **IP-allowlist:** Du kan begrense trafikk til våre utgående IP-adresser
- **Rate limiting:** Implementer beskyttelse mot for mange forespørsler

## Responskrav

Ditt endepunkt må respondere med passende HTTP-statuskoder:

### Suksess

- `200 OK` eller `204 No Content` – Melding mottatt og lagret/prosessering startet

### Klientfeil (4xx)

- `401 Unauthorized` – Ugyldig autentisering
- `403 Forbidden` – Manglende tilgang
- `404 Not Found` – Endepunkt ikke funnet  
- `422 Unprocessable Entity` – Ugyldig meldingsformat

### Serverfeil (5xx)

- `500 Internal Server Error` – Midlertidig feil på din side
- `502 Bad Gateway` – Gateway-feil
- `503 Service Unavailable` – Tjeneste ikke tilgjengelig

**Viktig:** Ved 4xx-feil anser vi meldingen som permanent mislykket og prøver ikke på nytt. Ved 5xx-feil implementerer vi retry-logikk.

Responsbody er valgfri og ignoreres.

## Idempotens og re-levering

### Duplikathåndtering

- Vi kan sende samme melding flere ganger ved nettverksfeil eller andre problemer
- Bruk `webhook-id` fra headeren som dedup-nøkkel
- Implementer idempotent behandling (ingen bivirkninger ved gjentatt prosessering)

### Retry-strategi

Ved ikke-suksess (ikke 2xx-status) forsøker vi igjen med eksponentiell backoff:

**Backoff-sekvens:**
30s → 1m → 2m → 4m → 8m → 16m → 32m → 1t → 2t → 4t → 8t → 16t → deretter hvert døgn

**Maksimal varighet:** 5 dager total retry-periode

Etter maksimal tidsvindu markeres hendelsen som ikke-levert. Vi kan eventuelt sende en manuell rapport om mislykkede leveringer.

## Implementeringseksempel

Her er et enkelt eksempel på hvordan du kan implementere et webhook-endepunkt:

```python
from flask import Flask, request, jsonify
import hashlib
import hmac

app = Flask(__name__)

# Lagring for duplikatsjekk (bruk database i produksjon)
processed_webhooks = set()

@app.route('/webhooks/status', methods=['POST'])
def handle_webhook():
    # Hent webhook-ID for duplikatsjekk
    webhook_id = request.headers.get('webhook-id')
    
    if webhook_id in processed_webhooks:
        # Allerede behandlet - returner suksess uten handling
        return '', 204
    
    # Validér autentisering
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return {'error': 'Missing or invalid authorization'}, 401
    
    try:
        # Parse JSON-innhold
        data = request.get_json()
        
        # Behandle melding basert på type
        if data['type'] == 'submission.preserved':
            handle_submission_preserved(data)
        elif data['type'] == 'dissemination.delivered':
            handle_dissemination_delivered(data)
        else:
            # Ukjent type - ignorer for fremtidig kompatibilitet
            print(f"Unknown webhook type: {data['type']}")
        
        # Merk som behandlet
        processed_webhooks.add(webhook_id)
        
        return '', 200
        
    except Exception as e:
        # Log feil
        print(f"Error processing webhook: {e}")
        return {'error': 'Internal server error'}, 500

def handle_submission_preserved(data):
    # Din logikk for submission-hendelser
    submission_id = data['data']['submissionId']
    print(f"Submission {submission_id} is now preserved!")

def handle_dissemination_delivered(data):
    # Din logikk for dissemination-hendelser  
    dissemination_id = data['data']['disseminationId']
    print(f"Dissemination {dissemination_id} is ready for download!")
```

## Feilsøking

### Vanlige problemer

1. **Timeout-feil:** Sørg for at endepunktet svarer innen 5 sekunder
2. **Sertifikatfeil:** Verifiser at TLS-sertifikatet er gyldig og riktig konfigurert
3. **Autentiseringsfeil:** Sjekk at Bearer token eller Basic auth er riktig implementert
4. **Duplikater:** Implementer deduplisering basert på `webhook-id`

## Støtte

For spørsmål om webhook-oppsett eller problemer med leveringer, kontakt teamet for digital bevaring ved Nasjonalbiblioteket.

Vi kan også hjelpe med:

- Testing av webhook-endepunktet ditt
- Oppgi faste IP-adresser for allowlisting
- Feilsøking av leveringsproblemer