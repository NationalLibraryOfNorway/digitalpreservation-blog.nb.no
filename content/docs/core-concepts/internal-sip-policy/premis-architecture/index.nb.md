---
title: Forvaltningsarkitektur
summary: This post discusses high-level metadata and data handling at the National Library of Norway
date: 2024-10-04
tags: [System architecture, PREMIS, Intellectual entities, representations]
authors: 
  - name: Torbjørn Bakken Pedersen
    image: https://avatars.githubusercontent.com/u/113333557?v=4
images: 
  - premis.png
weight: 2
aliases: ["/nb/forvaltningsarkitektur"]
---

I vårt pågående arbeid med innføring av [eArchiving-standardene for pakkestruktur](https://dilcis.eu "Website with standards and specifications for E-ARK"), er det viktig å definere hva som er et fornuftig pakkeomfang og regler for bruk av "representasjoner". 
Noen av disse begrepene kommer fra PREMIS[^1], som igjen er et rammeverk som hovedsakelig brukes internasjonalt i forbindelse med digital bevaring. 
  
{{% details title="PREMIS-terminologi" closed="true" %}}

### Intellektuelle entiteter (IE)
Fra PREMIS data dictionary:
> An **Intellectual Entity** is a distinct intellectual or artistic creation that is considered relevant to a designated community in the context of digital preservation: for example, a particular book, map, photograph, database, or hardware or software. An intellectual Entity can include other Intellectual Entities[...]

Intellektuelle entiteter brukes gjerne til å beskrive *intellektuelt innhold*.
Vi har mange forskjellige typer intellektuelle entiteter i metadatasystemene i Nasjonalbiblioteket, og disse er gjerne organisert i hierarkiske relasjoner med hverandre.
I vår foreslåtte bruk av informasjonspakker er det et én-til-én-forhold mellom informasjonspakker og en spesifikk type intellektuell entitetet i metadatasystemene. 

Det er kun de intellektuelle entitetene som beskriver digitale objekter, som er interessante for digital bevaring.
Disse holder UID-ene som holder våre tre systemdomener sammen.
Vanligvis er dette de *minste* og mest *håndfaste* beskrevne enhetene i våre metadatasystemer. 
I praksis, betyr det som regel en intellektuell entitet som holder en URN.
Dette utdypes i den følgende teksten om [omfang av informasjonspakker](/intellectual-sip-scope). 

Metadataene på rota av en informasjonspakke, beskriver den intellektuelle entiteten informasjonspakka inneholder representasjoner av.
Representasjonene er ulike datagjengivelser av en intellektuell entitet, og har dermed ikke egne beskrivende metadata. 
Informasjonspakker har derfor metadata om, og representasjoner av, intellektuelt innhold. 

### Representasjoner
I E-ARK-standardene er informasjonspakker spesifisert som pakker som inneholder *metadata* og *representasjoner*. 
Representasjonene består igjen av *data* og *metadata*. Representasjonsbegrepet er definert i PREMIS: 

> A **Representation** is the set of all file objects needed to render an Intellectual Entity.
> For example, a journal article may be complete in one PDF file; this single file constitutes the Representation.
> Another journal article may consist of one SGML file and two image files; these three files constitute the Representation.
> A third article may be represented by one TIFF image for each of 12 pages plus an XML file of structural metadata showing the order of the pages; these 13 files constitute the Representation.

En pakke kan bestå av flere representasjoner. 
Metadataene som sitter på rota av informasjonspakka, er metadata som beskriver *hele* pakken og alle representasjonene likt.

### Filer
Data og metadata kommer i form av filer:
> A **File** is a named and ordered sequence of bytes that is known to an operating system. 
> A File can be zero or more bytes and has a File format, access permissions, and File system characteristics such as size and last modification date.

{{% /details %}}

## Forvaltningsdomener
- **Metadatasystemer**
	- Forvalter intellektuelle entiteter 
	- Definerer representasjoner (gjennom representasjonens én-til-én-forhold til IE) 
- **Digital Preservation Services (DPS)**
	- Forvalter representasjoner og filer 
- **Offentlige tilgangstjenester**
	- Forvalter og formidler en høstet undergruppe av intellektuelle entiteter, tilgangsrepresentasjoner og filer. 

### Metadatasystemer
Metadatasystemene forvalter intellektuelle entiteter.
Representasjonsnivået er vanligvis *ikke* beskrevet i våre metadatasystemer.
Hvis en bruker skal finne en intellektuell entitet eller dens relaterte digitale objekter, bør metadatasystemene benyttes.

Metadatasystemene forvalter en rekke forskjellige intellektuelle entiteter, men det er kun en delmengde av disse som beskriver digitale objekter.
Disse systemene forvalter UID-ene som knytter en intellektuell entitet til en informasjonspakke (AIP) forvaltet av DPS. 

### Digital Preservation Services (DPS)
DPS forvalter for øyeblikket kun filer[^2].
Disse filene er *organisert* i intellektuelle entiteter og representasjoner. 

Filer lastes inn i DPS gjennom levering av informasjonspakker.
Disse informasjonspakkene gjenspeiler intellektuelle entiteter som beskriver digitale objekter i metadatasystemene.
For de aller fleste informasjonspakkene som håndteres i Nasjonalbiblioteket, er det én enkelt representasjon per pakke.
Som nevnt i dokumentet om [systemarkitektur](/nb/systemarkitektur), bevares vanligvis ikke tilgangsfiler som er automatisk utledet fra bevarte data i DPS. 

Vi har ikke som mål å gjenskape metadatasystemenes deskriptive metadatastrukturer og funksjonalitet i DPS. 
Brukere bør allerede ha identifisert de intellektuelle entitetene de vil ha tilgang til, før de bruker grensesnitt mot DPS.
Derimot, hvis du trenger data basert utelukkende på tekniske egenskaper på filnivå, kan du bruke DPS direkte til oppslag.   

### Offentlige tilgangstjenester
Tilgangstjenestene forvalter og gir tilgang til komprimerte *tilgangsrepresentasjoner* og -*filer*, i tillegg til høstede deskriptive metadata fra relevante intellektuelle entiteter.
De intellektuelle entititene og digitale objektene som er tilgjengelig gjennom disse systemene, er en delmengde av de intellektuelle entitetene som forvaltes av metadatasystemene og av DPS. 

De offentlige tilgangstjenestene konverterer de høstede metadataene til en enklere og flatere struktur av intellektuelle entiteter enn det man finner i metadatasystemene.
De offentlige tilgangstjenestene opererer for eksempel ikke med komplekse IE-til-IE-relasjoner, og opererer kun med én enkelt representasjon av hver entitet. 
De intellektuelle entitetene som finnes på nettet, speiler derfor ikke nødvendigvis enkelte intellektuell entiteteter fra metadatasystemene. 

## Arkitektur
Vi kan synliggjøre ulikhetene i hva som forvaltes i de forskjellige systemdomenene, ved å tegne opp et diagram over systemer og PREMIS-entiteter man finner der:

{{< figure src="premis.svg" alt="Diagram som viser de forskjellige systemenes ansvar for PREMIS entiteter" caption="PREMIS entiteter i forskjellige systemer" >}}

Diagrammet synliggjør det noe utfordrende delte ansvaret for representasjonen. 
Det er et én-til-én-forhold mellom den intellektuelle entiteten som brukes til å definere pakkeomfanget og dens primære representasjon i metadatasystemene. 

Dette betyr at selv om metadatasystemene ikke opererer med et eget representasjonsnivå, så *er* den primære representasjonen ofte beskrevet i tekniske termer i metadatasystemene.
En intellektuell entitet som beskriver et digitalt objekt (for eksempel en katalogpost med en URN), vil ha tekniske metadata for det digitale objektet.

Eventuelle *ytterligere* representasjoner av samme intellektuelle entitet, vil imidlertid *ikke* være beskrevet i metadatasystemene. 
De er kun beskrevet i DPS. 

Denne kompleksiteten stammer fra valget av type intellektuell entitet som brukes til å definere omfanget av informasjonspakkene. 
Det er avgjørende at våre tre systemdomener forblir synkroniserte, og opererer med lignende konsepter og enheter. 
Vi ønsker ikke å havne i en situasjon hvor vi har parallell, og muligens *motstridende*, informasjon i ulike systemer.
Det er viktig å være tydelig på hvilke systemer som er "master" og hovedkilde for hvilken type data og metadata.

Den neste teksten går mer i dybden på hva dette har å si i praksis.

[^1]: *PREMIS Data Dictionary (full document)*, Version 3.0, Nov. 2015, [https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf](https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf)
[^2]: Bitstream-nivået fra PREMIS er per i dag ikke beskrevet i DPS, men det kan bli det i fremtiden.