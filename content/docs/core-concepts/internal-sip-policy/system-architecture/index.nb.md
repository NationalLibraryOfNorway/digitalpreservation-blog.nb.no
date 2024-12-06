---
title: Systemdomener og -arkitektur
summary: This post discusses high-level metadata and data handling at the National Library of Norway
date: 2024-09-30
tags: [System architecture]
authors: 
  - name: Torbjørn Bakken Pedersen
    image: https://avatars.githubusercontent.com/u/113333557?v=4
images: 
  - arkitektur.png
weight: 1
aliases: ["/nb/systemarkitektur"]
---

Nasjonalbiblioteket baserer sitt arbeid med digital bevaring på OAIS-modellen[^3]. 
Når det er sagt, så kan man ikke uten videre kan ta utgangspunkt i OAIS modellen for å forstå hvordan løsningene i Nasjonalbiblioteket er satt sammen.
Dette skyldes at systemarkitekturen vår har blitt utvikler over flere år, samtidig som mange involverte systemer øker kompleksiteten.

{{% details title="OAIS-terminologi" closed="true" %}}

OAIS (Open Archive Information System) er en referansemodell for arkivering av digital informasjon.
<!-- Du kan lese mer om OAIS referansemodellen [her](lenke-til-lengre-OAIS-skriv). -->

{{< figure src="OAIS_Functional_Model_(en).svg" alt="OAIS-modellen" caption="" attr="Mathieualexhache (original work); Mess (SVG conversion & English translation), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0), via Wikimedia Commons" >}}

Sentrale begreper i OAIS modellen er de forskjellige informasjonspakkene (pakker med data og metadata): SIP, AIP og DIP. 
Disse begrepene benyttes også i Nasjonalbiblioteket for å skille mellom forsjellige typer informasjonspakker i forbindelse med digital bevaring.

- **SIP** (Submission information Package) – Informasjonspakke som leveres til digital bevaring. 
Datapakken inneholder filer med digitale innholdsdata pluss filer med dokumentasjon og metadata som er nødvendig for å lette langsiktig bevaring av dataene og for å gi tilgang til gjenbruk. 
- **AIP** (Archival Information Package) – Informasjonspakke slik den blir lagret i bit-repository i digital bevaring. 
Denne kan være identisk med den innleverte SIP-en, men kan også inneholde ytterligere informasjon om datapakken som skal bevares.
- **DIP** (Dissemination Information Package) – Informasjonspakke som utleveres fra digital bevaring. Denne kan bestå av hele eller deler av AIP-en.

Når vi snakker om informasjonspakker i de følgende dokumentene snakker vi om SIP-er, med mindre noe annet er spesifisert.

{{% /details %}}

Team digital bevaring utvikler og administrerer programvaren Digital Preservation Services (DPS), men dette er kun ett aspekt ved data- og metadatahåndtering i Nasjonalbiblioteket. 
Når vi fortsetter å utvikle DPS og standardisere informasjonspakker, er kunnskap om de forskjellige systemdomenenes ansvar, og hvordan disse samhandler, avgjørende.
 
## Systemdomener
Ansvaret for digitale objekter[^1] i Nasjonalbiblioteket er delt mellom en trio av forskjellige systemdomener, som forvalter forskjellige aspekter ved objektene.
Summen av informasjon i de tre systemdomenene gir det fulle bildet av objektene:

- **Metadatasystemer**
	-	Forvalter deskriptive metadata
	-	Forvalter den unike identifikatoren (UID) for digitale objekter
- **Digital Preservation Services (DPS)**
	-	Forvalter bevaringsdata
	-	Har en kopi av deskriptive metadata (fra metadatasystemene)
- **Offentlige tilgangstjenester**
	-	Forvalter tilgangsdata (utledet fra data for bevaring).
	-	Forvalter deskriptive metadata for tilgang (utledet fra metadatasystemene)

Limet som holder alt dette sammen er en UID (typisk en URN) brukt på tvers av systemene, men som forvaltes i metadatasystemene. 
Identifikatoren må være unik på tvers av de ulike systemene og bør ikke gjenbrukes.
 
### Metadatasystemer
Metadatasystemene er "master" og hovedkilde for deskriptive metadata i Nasjonalbiblioteket. 
Med metadatasystemer refererer vi til biblioteksystemer, kataloger, registre, forvaltningssystemer og andre fagsystemer som forvalter metadata.
Eksempler på noen slike systemer som er i bruk i Nasjonalbiblioteket i dag er Alma, Mavis og Hanske.
Enkelt forklart er dette ulike systemer som forvalter deskriptive metadata for ulike digitale og ikke-digitale objekter i Nasjonalbiblioteket.

Metadatasystemene er systemene som brukes i organisasjonen til å gjenfinne og få oversikt over objektene i Nasjonalbibliotekets samling[^2].
Disse systemene forvalter UID-en som brukes som muliggjør gjenfinning av data for tilgang og bevaring i de to andre systemdomenene.
 
### Digital Preservation Services (DPS)
DPS-programvaren forvalter alle data i Nasjonalbibliotekets bit repository. 
Systemet tar i mot bevaringsdata, sikrer dataintegritet og styrer tilgangen til bevarte data.
Det er i dette domenet vi opererer med de forskjellige OAIS-konseptene,[^4] som SIP, AIP. DIP, etc. 
Sammen med de bevarte dataene lagrer vi en *kopi* av utvalgte deskriptive metadata fra de relevante metadatasystemene. 
Dette gjøres for å sikre at de digitale objektene er gjenfinnbare, kontekstualiserte og anvendelige i et langsiktig perspektiv, uavhengig av omgivelsene utenfor DPS.

Informasjonspakker som mottas for bevaring i DPS, representerer en entitet som er beskrevet i metadatasystemene. 
DPS er "master" og hovedkilde for tekniske metadata på filnivå i Nasjonalbiblioteket.
 
DPS kan også brukes til å identifisere og gjenfinne *filer* (gjennom tekniske metadata), men dette har til nå vært lite brukt i organisasjonen. 
 
### Offentlige tilgangstjenester
De offentlige tilgangstjenestene[^5] til Nasjonalbiblioteket lar eksterne brukere få tilgang til et utvalg av deskriptive metadata *høstet* fra metadatasystemene våre, samt *filer* ment for tilgang.
Hovedtjenestene våre for slik offentlig tilgang er: [Nettbiblioteket](https://www.nb.no/search "lenke til nettbiblioteket på nb.no"), som lar deg *søke* i og *få tilgang* til et utvalg av digitale objekter fra våre digitale samlinger; og, [Oria](http://nb.oria.no/ "lenke til søketjenesten Oria"), som lar deg *søke* i våre trykte samlinger.

Metadataene i offentlige tilgangstjenestene er høstet fra de interne metadatasystemene.
På samme måte er tilgangsdataene proxy-kopier utledet fra bevarte høykvalitetsfiler i DPS. 
Disse filene er typisk mindre og komprimerte varianter av digitale objekter i DPS. 

## Arkitektur
Dette er et forenklet diagram over systemarkitekturen i Nasjonalbiblioteket. 
Diagrammet er idealisert og dekker ikke alle mulige scenarier, men er likevel nyttig for å forstå hva slags systeminteraksjoner vi opererer med. 
Selv om vi bruker OAIS-modellen som et rammeverk for å diskutere arkitekturen vår, kan det være vanskelig å kjenne igjen komponentene i vår kontekst.[^6]

{{< figure src="arkitektur.svg" alt="architecture diagram" caption="Data- og metadataflyt mellom systemer" >}}

Informasjonspakken som går til DPS i dette diagrammet (SIP), inneholder data til bevaring, samt en kopi av metadata fra det relevante metadatasystemet i et standardisert format (for eksempel MODS).
DPS-systemet er per i dag ikke eksponert offentlig. 
All offentlig tilgang til *bevarte* data går derfor gjennom andre interne tjenester bygd på toppen av DPS.

Det er en målsetning at DPS ikke skal bevare *tilgangsdata*, som kan utledes automatisk fra *bevaringsdata*. 
Et eksempel er et JP2-bilde for tilgang, som kan automatisk utledes fra et bevart TIFF-bilde. 
Slike tilgangsdata forvaltes kun av tjenestene for offentlig tilgang.



[^1]: "Digitale objekter" her peker til både *enkle digitale objekter* (individuelle enkeltfiler), og *komplekse digitale objekter* (grupper av filer som sammen utgjør en helhet). Eksempler på enkle digitale objekter kan være enkeltbilder i TIFF-format, mens eksempler på komplekse digitale objekter kan være en DCP, som er en mappe bestående av mange forskjellige filer (mxf, xml, etc). (Higgins, Sarah. “The DCC Curation Lifecycle Model.” *International Journal of Digital Curation*, vol. 3, no. 1, Dec. 2008, pp. 134–40. DOI.org (Crossref), [https://doi.org/10.2218/ijdc.v3i1.48](https://doi.org/10.2218/ijdc.v3i1.48)).
[^2]: Noen av disse systemene er også eksponert for søk til brukere utenfor Nasjonalbiblioteket.
[^3]: [Open Archival Information System-modellen](https://no.wikipedia.org/wiki/OAIS-modellen "Wikipediasida for OAIS-modellen")
[^4]: Vi har dokumentert kjernekonsepter i OAIS [her](/nb/oais/).
[^5]: Mer informasjon finnes [her](https://www.nb.no/veiledning-og-bibliotektjenester/soke/).
[^6]: Selv om dette ikke gjøres i dag, kunne vi i teorien bruke DIP-konseptet til å beskrive formidlingen av data og metadata i offentlige tilgangstjenestene. Tradisjonelt er OAIS-terminologien kun brukt når man snakker om digital bevaring i Nasjonalbiblioteket.

