---
title: "Piloten har landet - Oppdrag utført!"
date: 2025-12-17
description: "Team digital bevaring, Kulturdirektoratet og KulturIT har fullført pilotprosjetet for langtidsbevaring av museenes digitale materiale."
tags: ["Digital bevaring, Nasjonalbiblioteket, Digital Preservation, National library of Norway, kulturarv"]
draft: false
authors: 
  - name: Trond Teigen
    image: /apple-touch-icon.png 
---

![Skisse for bevaring av museenes digitale kulturarv](/pilot.png)


Nasjonalbiblioteket, Kulturdirektoratet og KulturIT fikk i oppdrag fra Kultur- og likestillingsdepartementet å gjennomføre en pilot for langtidsbevaring av museenes digitale materiale i NBs løsning for langtidsbevaring (DPS).  Oppdraget ble gitt i desember 2024. 

Nasjonalbiblioteket og KulturIT har det siste året samarbeidet om å utvikle og teste en løsning for inn- og utlevering av digitale museumsobjekter i form av bilder. For oss i Team Digital Bevaring innebar det at vi har måttet etablere flere nye funksjoner i vårt DPS.  

Vi har utviklet et API-grensesnitt som gjør det mulig for ulike datasystemer å kommunisere med vårt DPS. API’et håndterer autentisering og autorisering, og all kommunikasjon vil være regulert av avtaler mellom Nasjonalbiblioteket og de institusjoner som ønsker å benytte løsningen. Du kan lese mer om vårt nye API [her](https://digitalpreservation.no/nb/docs/dps/api/). 

For inn- og utlevering av data ble det testet ut en datautvekslingsplattform basert på Amazon S3-protokollen. Denne løsningen gjør at brukerne ikke trenger å forholde seg til hvordan data faktisk lagres internt på datautvekslingsplattformen. 

Det er klargjort for at data som skal leveres til Nasjonalbiblioteket må følge [E-ARK](https://dilcis.eu/specifications/sip) standarden for struktur og innhold i informasjonspakker. Du kan lese mer om våre krav til informasjonspakker [her](https://digitalpreservation.no/nb/docs/dps/sip/1.0/). 

I tillegg er det utarbeidet krav til metadata som skal leveres sammen med informasjonspakken. Dette er metadata som anses som nødvendige for forvaltning av materialet i bevaringsomgivelsene. Disse dataene leveres via API’et. Du kan lese mer om våre krav til metadata [her](https://digitalpreservation.no/nb/docs/dps/api/submission/metadata/). 

[KulturIT](https://kulturit.org/) har på sin side utviklet funksjonalitet for utvelgelse av museumsobjekter som skal bevares. Samt løsning for å levere inn- og hente ut bevarte museumsobjekter i Nasjonalbibliotekets løsning for langtidsbevaring (DPS). 

Løsningen er testet av tre av KulturITs eiermuseer og pilotoppdraget anses som vellykket. 

Det er Skrevet en rapport som er overlevert Kultur- og likestillingsdepartementet. Rapporten beskriver hvordan oppdraget er utført og gir en anbefaling om at det etableres en fast tjeneste for digital langtidsbevaring av bilder for museene. Denne skal bygge videre på resultater fra piloten, med en innledende fase for fem museer. 

På sikt kan denne tjenesten også utvides til andre museer, og benyttes for andre medietyper som tekst, lyd og levende bilder. 

Nasjonalbiblioteket, Kulturdirektoratet og KulturIT har samarbeidet godt om piloten og støtter rapportens anbefalinger for videre arbeid. 
