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


## Støtte

Trenger du hjelp eller har spørsmål, kontakt teamet for digital bevaring ved Nasjonalbiblioteket.

## API-referanse

For fullstendig informasjon om endepunkter, parametere, skjema og statuser, se [Swagger-dokumentasjonen](https://digitalpreservation.no/swagger/).
