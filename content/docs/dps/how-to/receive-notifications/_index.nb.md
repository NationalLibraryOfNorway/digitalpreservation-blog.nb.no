---
title: Motta varsler
weight: 4
aliases:
  - /docs/dps/api/webhooks/
---

DPS kan sende varsler direkte til dine systemer via webhooks når innleveringer eller utleveringer endrer status, slik at du ikke trenger å spørre API-et kontinuerlig. Denne veiledningen viser hvordan du setter opp et endepunkt som tar imot og verifiserer disse meldingene. Headere, meldingsstruktur og feltene i hver melding er listet i [API-referansen](/nb/docs/dps/reference/api/#webhooks).

Når en hendelse oppstår i DPS:

1. DPS sender en **HTTP POST**-forespørsel til URL-en du har oppgitt
2. Meldingen inneholder informasjon om hendelsen i **JSON-format**, i henhold til *Standard Webhooks*[^1]
3. Ditt system mottar meldingen, validerer at den kommer fra DPS, og svarer med **HTTP 200 OK**

## Før du starter

- **Et HTTPS-endepunkt** som DPS kan nå, med gyldig TLS-sertifikat (TLS 1.2 eller høyere).
- **Kontakt med teamet for digital bevaring.** Nasjonalbiblioteket registrerer foreløpig alle webhook-endepunkter manuelt i samarbeid med hver partner.

## Steg

{{% steps %}}

### Sett opp et endepunkt

Du må eksponere en offentlig tilgjengelig URL som tar imot HTTPS POST-forespørsler med JSON-data, for eksempel:

```http
https://partner.example.com/api/dps/webhook
```

**Anbefalinger:**

- Bruk IP-allowlist (vi kan oppgi faste utgående IP-er ved behov)
- Sett opp overvåkning og varsling av at tjenesten din er operativ
- Valider signaturen for hver melding før behandling

### Registrer endepunktet hos Nasjonalbiblioteket

I denne fasen håndteres registrering av webhook-URL og delt hemmelig nøkkel **manuelt av Nasjonalbiblioteket**. Vi koordinerer oppsett og test før produksjonsbruk. Kontakt teamet for digital bevaring for å registrere endepunktet ditt.

### Verifiser signaturen

Webhookene signeres for å sikre autentisitet og integritet. Mottakeren må validere signaturen før meldingen behandles. Signaturen beregnes ut fra headerne `webhook-id` og `webhook-timestamp` og rå request-body.

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

>  **Tips:** verifiser alltid signaturen mot rå **request-body**, ikke en reserialisert JSON-struktur.

### Svar på meldingen

Webhook-mottakeren må:

- svare med HTTP **200 OK** eller **204 No Content** innen 10 sekunder
- returnere ingen eller minimal body (DPS bryr seg kun om statuskode)
- ved 4xx/5xx eller timeout vil DPS prøve igjen med eksponentiell backoff

Fordi DPS prøver på nytt, kan samme melding komme flere ganger. Bruk `webhook-id` som dedup-nøkkel.

### Behandle meldingen

Bruk feltet `type` til å avgjøre hva du skal gjøre:

- **`submission.preserved`:** materialet er bevart. Ta vare på `archiveId`; du trenger den for å bestille materialet senere. Du kan nå slette kildematerialet.
- **`submission.rejected`:** innleveringen ble avvist. Listen `reasons` forteller hva som gikk galt, og `filePath` peker på filen når en feil gjelder en enkelt fil.
- **`dissemination.delivered`:** bestilt materiale er klart. Last ned filene før lenkene utløper. Se [Bestille utlevering av bevart materiale](/nb/docs/dps/how-to/retrieve-content/).

Feltene i hver melding er listet under [Webhook-hendelser](/nb/docs/dps/reference/api/#webhook-hendelser).

{{% /steps %}}

## Feilsøking

1. **Timeout:** Sørg for at endepunktet svarer innen tidsfristen
2. **Sertifikatfeil:** TLS-sertifikatet må være gyldig og riktig konfigurert
3. **Signaturfeil:** Sjekk at HMAC-verifiseringen implementeres korrekt
4. **Duplikater:** Implementer deduplisering basert på `webhook-id`

## Støtte

For spørsmål om webhook-oppsett eller om du opplever problemer, kontakt teamet for digital bevaring ved Nasjonalbiblioteket.

Vi kan hjelpe med:

- Testing av webhook-endepunkt
- Oppgi faste IP-adresser for allowlisting
- Feilsøking av leveringsproblemer

[^1]: Standard Webhooks: [https://www.standardwebhooks.com](https://www.standardwebhooks.com)
