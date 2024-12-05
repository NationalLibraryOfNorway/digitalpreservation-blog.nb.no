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

De fleste av våre interne informasjonspakker vil kun inneholde én enkelt representasjon.
Ytterligere representasjoner produseres i organisasjonen, men det finnes kun noen få reelle eksempler hvor disse er lagret i DPS.

Vi opererer med tre typer representasjoner:
 
## Primærrepresentasjoner
Den første pg primære representasjonen er representasjonen som inneholder det digitale objektet som er beskrevet ved hjelp av en IE i det relevante metadatasystemet[^1].
[^1]: Ikke beskrevet i våre MARC-baserte systemer. Se [forrige dokument](/nb/sip-omfang).
 
## Tilgangsrepresentasjoner
Tilgangsrepresentasjoner brukes for digitale objekter utledet fra det digitale objektet i primærrepresentasjonen, for å gi enklere tilgang.
De brukes som proxy, eller stedfortreder, for den primære representasjonen.
Disse representasjosnene inneholder vanligvis mye mindre, komprimerte (eller mer komprimerte) filer.
 
Enhver representasjon kan i teorien ha en tilgangsrepresentasjon, men disse administreres og forvaltes primært av de offentlige tilgangstjenestene. 
Tilgangsrepresentasjoner forvaltes kun i DPS, hvis de er et resultat av betydelig arbeid og/eller ikke kan utledes maskinelt fra den primære representasjonen. 
De offentlige tilgangsjenestene støtter på sin side kun én enkelt (tilgangs)representasjon per UID.
 
## Bevaringsrepresentasjoner
I tilfeller hvor det primære digitale objektet er normalisert eller konvertert til et annet format for bevaring, kan du bruke dette formatet som representasjonstype. 
Dette gjør oss i stand til å bevare både det primære digitale objektet og en antatt mer bestandig bevaringsrepresentasjon. 
Foreløpig er dette et hovedsaklig hypotetisk brukstilfelle, enn noe som skjer regelmessig i organisasjonen.

## Eksempler:

### Eksempel som viser en typisk informasjonspakke med én representasjon

{{< figure src="1repsip.svg" alt="Informasjonspakke for filmdigitalisering med én representasjon" >}}

### Eksempel med to representasjoner
Intern digitalisering av fotonegativer produserer per i dag, én stor TIFF-fil for bevaring og en invertert og tungt etterbehandlet JP2-fil for tilgang.
Kun TIFF-fila er beskrevet ved hjelp av en *bærer* i metadatasystemet, men begge digitale objekter bevares i DPS.
JP2-fila er resultatet av omfattende manuelt arbeid og kan ikke automatisk eller enkelt reproduseres fra den primære TIFF-fila.

TIFF-fila ligger i den primære representasjonen i informasjonspakka, mens JP2-fila er ligger i en tilgangsrepresentasjon.

{{< figure src="tiffjp2.svg" alt="Informasjonspakke som inneholder digitalisering av fotonegative med to representasjoner" >}}

### Eksempel som viser alle tre representasjonstypene
Et eksempel som viser en videomaster, med en tilgangsrepresentasjon og en bevaringsrepresentasjon som inneholder et digitalt objekt (som et resultat av en hypotetisk formatmigrering/normalisering av primærrepresentasjonen).

{{< figure src="avsip.svg" alt="Informasjonspakke for video master med tre representasjoner" >}}

---