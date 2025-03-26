---
title: Representasjonstyper
summary: This post discusses high-level metadata and data handling at the National Library of Norway
date: 2024-09-30
tags: [System architecture, PREMIS, Intellectual entities, representations]
authors: 
  - name: Torbjørn Bakken Pedersen
    image: https://avatars.githubusercontent.com/u/113333557?v=4
images: 
  - avsip.png
weight: 4
aliases: ["/nb/representasjonstyper"]
---

De fleste av våre internt produserte informasjonspakker inneholder kun én enkelt representasjon. 

Det produseres også andre representasjoner i Nasjonalbiblioteket, for eksempel til visning i nettbiblioteket, men kun et fåtall av disse lagres i DPS.  

Vi opererer med to typer representasjoner for digital bevaring hos oss:
 
## Primærrepresentasjon
Innholdet i denne mappa er det digitale objektet som pakken skal beskrive. Den første og primære representasjonen er den som inneholder det digitale objektet som er beskrevet ved hjelp av en IE i det relevante metadatasystemet[^1].
[^1]: Ikke beskrevet i våre MARC-baserte systemer. Se [forrige dokument](/nb/sip-omfang).
 
## Derivater av primærrepresentasjonen
Opprettelse av flere representasjoner i en informasjonspakke er kun relevant hvis det er spesielt ønskelig å bevare både primærrepresentasjonen og noe som er utledet fra den, i samme informasjonspakke. Dette kan være en tilgangskopi, prosessert, normalisert, formatmigrert eller reparert variant av primærrepresentasjonen. Typisk for disse er at de ikke er representert som en egen IE i metadatasystemet.

Et eksempel kan være der det primære digitale objektet er normalisert eller konvertert til et annet format for bevaring. Vi kan da bevare både det primære digitale objektet og en antatt mer bestandig bevaringsrepresentasjon. 

Formålet med et derivat, hvordan det er fremstilt, og hvilken relasjon det har til primærrepresentasjonen bør dokumenteres i bevaringsmetadata i pakken. Vi fraråder å bevare derivater som lett og maskinelt kan gjenskapes fra primærrepresentasjonen. Tilgangsrepresentasjoner vil for eksempel kun være aktuelle for forvaltning i DPS, hvis de er et resultat av betydelig arbeid og/eller ikke kan utledes maskinelt fra den primære representasjonen.  

## Eksempler:

### Eksempel som viser en typisk informasjonspakke med én representasjon

{{< figure src="1repsip.svg" alt="Informasjonspakke for filmdigitalisering med én representasjon" >}}

### Eksempel med to representasjoner
Intern digitalisering av fotonegativer produserer per i dag, én stor TIFF-fil for bevaring og en invertert og tungt etterbehandlet JP2-fil for tilgang.
Kun TIFF-fila er beskrevet ved hjelp av en *bærer* i metadatasystemet, men begge digitale objekter bevares i DPS.
JP2-fila er resultatet av omfattende manuelt arbeid og kan ikke automatisk eller enkelt reproduseres fra den primære TIFF-fila.

TIFF-fila ligger i den primære representasjonen i informasjonspakka, mens JP2-fila ligger i en tilgangsrepresentasjon.

{{< figure src="tiffjp2.svg" alt="Informasjonspakke som inneholder digitalisering av fotonegative med to representasjoner" >}}

### Eksempel som viser tre representasjonstypene
Et eksempel som viser en videomaster, med en tilgangsrepresentasjon og en bevaringsrepresentasjon som inneholder et digitalt objekt (som et resultat av en hypotetisk formatmigrering/normalisering av primærrepresentasjonen).

{{< figure src="avsip.svg" alt="Informasjonspakke for video master med tre representasjoner" >}}

---