---
title: Programmeringsgrensesnitt (API)
weight: 1
---

## Oversikt

Nasjonalbibliotekets tjenester for digital bevaring tilbyr REST-baserte API-er for å håndtere innlevering (submission) og utlevering (dissemination) av digitale objekter. Dette lar klienter integrere sine systemer med våre bevaringsløp.

Denne dokumentasjonen gir en overordnet oversikt over tilgjengelige API-er. For komplette tekniske detaljer, se vår [Swagger UI](https://digitalpreservation.no/swagger/).

Følgende tjenester er tilgjengelige:
- [**Submission Service API**](submission/): For innlevering av digitale objekter for bevaring.
- [**Dissemination Service API**](dissemination/): For bestilling av bevarte digitale objekter.

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

* Kontraktsspesifikke roller (`{contractId}_R`, `{contractId}_W`) gir lese- og skrivetilgang til ressurser under en spesifikk kontrakt
* Rollen `DPS_SUBMISSION_HANDLER` kreves for interne statusoperasjoner

Klientapplikasjonen må hente access token, og den utstedte JWT-en vil inneholde tildelte roller.


## Feilhåndtering

API-et bruker vanlige HTTP-statuskoder:

* `200 OK` – Vellykket
* `201 Created` – Ressurs opprettet
* `400 Bad Request` – Feil i forespørselen
* `401 Unauthorized` – Manglende eller ugyldig token
* `403 Forbidden` – Token gyldig, men mangler rettigheter
* `404 Not Found` – Ressurs ikke funnet
* `409 Conflict` – Duplikat forespørsel
* `422 Unprocessable Entity` – Ressurs finnes men er ikke bevart / ikke klar
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


## Støtte

Trenger du hjelp eller har spørsmål, kontakt teamet for digital bevaring ved Nasjonalbiblioteket.

## API-referanse

For fullstendig informasjon om endepunkter, parametere, skjema og statuser, se [Swagger-dokumentasjonen](https://digitalpreservation.no/swagger/).
