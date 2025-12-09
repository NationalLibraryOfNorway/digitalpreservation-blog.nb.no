---
title: Pakkeomfang og representasjoner
weight: 1
---

DPS er et system utviklet for å motta, sikkert bevare og tilgjengeliggjøre bevarte **digitale objekter.**
I vår terminologi brukes uttrykket "digitalt objekt" synonymt med en digital **representasjon** av en **intellektuell entitet**.

DPS organiserer mottak, forvaltning og utlevering av slike representasjoner gjennom utveksling av informasjonspakker.
Envher informasjonspakke kan inneholde én eller flere representasjoner.
For å kunne lage og levere en pakke til DPS må man ha en foremening om hva om som skal ligge i én pakke.
Enhver pakke har et **intellektuelt omfang**, som igjen styrer hvor stort **data-omfanget** er i en pakke.

## Representasjoner

Representasjonsbegrepet er definert i PREMIS:

> A **Representation** is the set of all file objects needed to render an Intellectual Entity.
> For example, a journal article may be complete in one PDF file; this single file constitutes the Representation.
> Another journal article may consist of one SGML file and two image files; these three files constitute the Representation.
> A third article may be represented by one TIFF image for each of 12 pages plus an XML file of structural metadata showing the order of the pages; these 13 files constitute the Representation. 

Representasjoner kan dermed være enten **enkle objekter** som består av enkeltstående filer, eller **sammensatte objekter** som består av grupper av filer som er ment brukt sammen.

Et eksempel på et enkelt digitalt objekt kan være ett enkelt bilde i TIFF-format, mens et eksempel på et sammensatt digitalt objekt kan være det nevnte eksemplet over med artikkelen representert av 12 TIFF-bilder og en XML-fil, eller en DCP (som er en mappe som inneholder bilde- og lydstrømmer i MXF-containere sammen med XML-filer).

## Intellektuelle entiteter og innhold

Følgende definisjon stammer fra PREMIS data dictionary:
> An **Intellectual Entity** is a distinct intellectual or artistic creation that is considered relevant to a designated community in the context of digital preservation: for example, a particular book, map, photograph, database, or hardware or software.

Intellektuelle entiteter beskriver gjerne **intellektuelt innhold**.
For å holde kompleksiteten nede, anbefaler vi at enkle, håndfaste intellektuelle entiteter brukes til å definere pakkeomfanget (for eksempel **items** eller **eksemplarer**), snarere enn overordnede, abstrakte intellektuelle entiteter (for eksempel **verk**).

{{< callout >}}
Vi **anbefaler sterkt** å begrense det intellektuelle omfanget i en pakke til ett bestemt digitalt eksemplar.
{{< /callout >}}

Dette innebærer at den intellektuelle entiteten som definerer pakkeomfanget, og dens primære representasjon, er svært tett sammenknyttet.
De deskriptive metadataene på rotnivået av pakka beskriver det intellektuelle innholdet i akkurat dette eksemplaret.
De fleste pakker vil bestå av én enkelt representasjon.

Noen eksempler på pakkeomfang for digitalt født materiale:
- Et bestemt digitalt bilde
- Et bestemt digitalt eksemplar av en bok
- En bestemt digital masterfil for et lydspor
- En bestemt digital masterfil for en spillefilm

Noen eksempler på pakkeomfang for digitisert materiale:
- En bestemt skanning av et fotografisk bilde
- En bestemt digitisering av en bok
- En bestemt digitisering av et videobånd
- En bestemt skanning av en filmrull

Med andre ord vil en pakke inneholde ett bestemt digitalt eksemplar av en bok, ikke alle digitaliserte versjoner og digitale utgaver av det samme litterære verket.
Disse andre eksemplarene er intellektuelle entiteter og pakker i sin egen rett.
På tilsvarende måte håndteres en ny digitsering av et fysisk kildeobjekt, som tidligere er digitalisert, som en ny intellektuell entitet og pakke.

## Ny pakke eller ny representasjon?

Når den intellektuelle entiteten og dens primære representasjon er så tett definert, blir spørsmålet når man skal opprette en ny pakke, og når man skal opprette en ny representasjon.

Helt enkelt forklart, er en ny representasjon i vårt regelsett en **teknisk formatvariant** av den primære representasjonen.
Hvis det intellektuelle omfanget i en pakke er ett eksemplar, er representasjonene forskjellige varianter av **dette spesifikke** eksemplaret.

I Nasjonalbiblioteket opprettes det typisk en ny pakke, når et nytt digitalt eksemplar opprettes som en entitet i metadatasystemene og tildeles en URN.
URN-en identifiserer den **intellektuelle entiteten** som definerer pakken, og dens primære representasjon.
Ytterligere representasjoner, utover den primære, er formatvarianter som er utledet fra den primære representasjonen, men som ikke anses tilstrekkelig forskjellige til å beskrives som egne entiteter i metadatasystemene.
Alle representasjonene i pakken identifiseres av den samme URN-en.

Internt er regelsettet:

- Én URN = én enkelt pakke
- Flere URN-er = flere pakker

Hvis du bare har én URN for å beskrive materialet du har, men likevel ønsker å bevare ytterligere representasjoner i DPS, oppretter du en ny representasjon i samme pakke som den primære digitale representasjonen.

<!-- {{< callout >}}
En idé å si noe om føringer i DPS?

- ID-er tildeles på pakkenivå
- Tilgangskontroll styres på pakkenivå
- Versjonering er ikke tillatt
- Pakker utleveres typisk som en helhet
{{< /callout >}}
 -->
## Eksempler på representasjoner
De fleste av våre internt produserte informasjonspakker inneholder kun én enkelt representasjon. 

Det produseres også andre representasjoner i Nasjonalbiblioteket, for eksempel til visning i nettbiblioteket, men kun et fåtall av disse lagres i DPS.  

Vi opererer med to typer representasjoner:
 
### Primærrepresentasjon
Den første og primære representasjonen er den som inneholder det digitale objektet som er beskrevet som en intellektuell entitet i det relevante metadatasystemet.
 
### Derivater av primærrepresentasjonen
Opprettelse av flere representasjoner i en pakke er kun relevant hvis det er spesielt ønskelig å bevare både primærrepresentasjonen og noe som er utledet fra den, i samme informasjonspakke. 
Dette kan være en tilgangskopi, prosessert, normalisert, formatmigrert eller reparert variant av primærrepresentasjonen. 
Typisk for disse er at de ikke er representert som en egen IE i metadatasystemet.

Et eksempel kan være der det primære digitale objektet er normalisert eller konvertert til et annet format for bevaring. Vi kan da bevare både det primære digitale objektet og en antatt mer bestandig bevaringsrepresentasjon. 

Formålet med et derivat, hvordan det er fremstilt, og hvilken relasjon det har til primærrepresentasjonen bør dokumenteres i bevaringsmetadata i pakken. Vi fraråder å bevare derivater som lett og maskinelt kan gjenskapes fra primærrepresentasjonen. Tilgangsrepresentasjoner vil for eksempel kun være aktuelle for forvaltning i DPS, hvis de er et resultat av betydelig arbeid og/eller ikke kan utledes maskinelt fra den primære representasjonen.  

### Eksempler:

#### Eksempel som viser en typisk pakke med én representasjon

{{< figure src="1repsip.svg" alt="Pakke for filmdigitalisering med én representasjon" >}}

#### Eksempel med to representasjoner
Intern digitalisering av fotonegativer produserer per i dag, én stor TIFF-fil for bevaring og en invertert og tungt etterbehandlet JP2-fil for tilgang.
Kun TIFF-fila er beskrevet ved hjelp av en *bærer* i metadatasystemet, men begge digitale objekter bevares i DPS.
JP2-fila er resultatet av omfattende manuelt arbeid og kan ikke automatisk eller enkelt reproduseres fra den primære TIFF-fila.

TIFF-fila ligger i den primære representasjonen i pakka, mens JP2-fila ligger i en tilgangsrepresentasjon.

{{< figure src="tiffjp2.svg" alt="Pakke som inneholder digitalisering av fotonegative med to representasjoner" >}}

#### Eksempel som viser tre representasjonstyper
Et eksempel som viser en videomaster, med en tilgangsrepresentasjon og en bevaringsrepresentasjon som inneholder et digitalt objekt (som et resultat av en hypotetisk formatmigrering/normalisering av primærrepresentasjonen).

{{< figure src="avsip.svg" alt="Ppakke for video master med tre representasjoner" >}}