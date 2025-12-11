---
title: "Flytting av 4,3 millioner digitale aviser"
date: 2024-11-06T12:46:00+01:00
description: "Nasjonalbiblioteket har gjennomført et omfattende rearkiveringsprosjekt for å migrere 4,3 millioner digitale aviser (2,5 petabyte) fra gammelt til nytt bit-lager. Prosjektet inkluderte både opprydding i store datamengder, produksjon av sjekksummer og flere andre kvalitetsforbedringer."
tags: ["Digital Preservation", "Newspaper Archives", "Data Migration", "Digital Collections", "Mass Digitization", "Digital Storage", "Legacy Systems", "SAM-FS", "Cultural Heritage", "Digital Libraries", "OCR", "Digital Newspapers", "digital bevaring", "avissamling", "kulturarv"]
authors: 
  - name: Digital Preservation Team
    image: /apple-touch-icon.png
images: 
  - image2.png
---

Nasjonalbiblioteket er i ferd med å bytte ut sitt gamle bit-lager fra 2007 med en mer moderne bevaringsløsning for digitalt materiale. Den nye løsningen bygger på en egenutviklet  programvare kalt DPS (Digital Preservation Services), og bruker IBM-HPSS som underliggende system for datalagring.

## Overgangen til ny bevaringsløsning

I 2023 ble all ny tilvekst av bevaringsdata ved Nasjonalbiblioteket flyttet over til DPS. På dette tidspunktet inneholdt det gamle bit-lageret mer enn 14 petabyte[^1] med digitalisert og historisk avlevert materiale som måtte rearkiveres. En viktig del av arbeidet har vært å analysere og pakke om det historiske materialet slik at det tilfredsstiller kravene til den nye løsningen.

Det ble bestemt at den digitale avissamlingen var det første materialet som skulle rearkiveres. Arbeidet ble gjennomført som et samarbeid mellom team Tekst og team  Digital bevaring.   Tekst-teamet har ansvar for digitalisering av alt tekstbasert materiale, mens Digital bevaringsteamet har ansvar for langtidsbevaring av den digitale samlingen.


## Kort oversikt over Nasjonalbibliotekets digitale avissamling

- Samlingen består av både digitalt fødte og digitaliserte aviser fra 1763 og frem til i dag.
- Totalt finnes det rundt 4,6 millioner aviser fordelt på 1800 avistitler. Av disse skulle omtrent 4,3 millioner rearkiveres til DPS.
- Over 16 millioner pakkede filer måtte flyttes fra det gamle bit-lageret.
- Dette tilsvarer rundt 2,5 petabyte med data.
  
Nasjonalbibliotekets avissamling kommer fra tre hovedkilder:

1.  **Digital Pliktavlevering av PDF-aviser**  
    Dette er trykkegrunnlaget fra avisene, levert som PDF. Filene hentes daglig fra avisutgiverne, og blir deretter behandlet og klargjort for formidling og bevaring. I 2024 mottok Nasjonalbiblioteket trykkegrunnlag fra 220 aviser. Dette utgjør rundt 6 % av avissamlingen.

2.  **Aviser skannet fra mikrofilm**  
    Papiravisene ble først fotografert på mikrofilm, og deretter ble mikrofilmen digitalisert av kommersielle aktører. De fleste av disse avisene er publisert før år 2000. Dette utgjør omtrent 41 % av samlingen.

3.  **Skannede papiraviser**  
    Originale papiraviser som er skannet og behandlet internt ved Nasjonalbiblioteket. Dette utgjør rundt 53 % av samlingen.

Avisene kan variere mye i størrelse og antall sider, avhengig av tidsperiode og publiseringsformat.

![Foto av avisskanning](/avisdigitalisering.jpg)

I nesten 20 år har Nasjonalbiblioteket systematisk digitalisert og mottatt digitale aviser i stort omfang, og metodene har endret seg underveis. Det betyr at aviser som ble digitalisert for 20 år siden er pakket og arkivert med en helt annen struktur enn dagens aviser.

Slik behandles aviser som digitaliseres eller mottas digitalt i dag:

- Hver enkelt side OCR[^2]-behandles.
- Innholdet analyseres gjennom strukturgjenkjenning, der bilder, titler, utgiverinformasjon, utgivelsesdato m.m. identifiseres. Informasjonen lagres i egne OCR/ALTO[^3]-filer.
- Det lages egne JP2K (.jpx)-filer til formidling på nb.no, også for PDF-aviser.
- Det lages separate JP2K (.jp2)-filer til langtidsbevaring.
- Det opprettes en METS[^4]-struktur som knytter sammen innholdet i alle filer. Dette gjør det mulig å virtuelt bla i avisen, søke i fritekst og få uthevede søketreff. 
- Som et eksempel kan en 20-siders avis bestå av rundt 160 filer, inkludert metadatafiler og datafiler. Typiske filtyper er JP2K-HQ, JP2K-LQ, OCR, ALTO, METS, JHOVE m.m.
- •	Like filtyper pakkes i .tar-filer[^5], og én avis består av en mappe med flere slike tar-pakker.



Dette betyr at det eldste digitaliserte avismaterialet i samlingen ikke nødvendigvis er behandlet på samme måte som dagens avismateriale.

## Forbedringer/avgjørelser som påvirket rearkiveringen

Før rearkiveringen startet, ble innholdet i bit-lageret analysert. Dette førte til flere viktige avgjørelser:

- Alle filer som rearkiveres skal ha tilhørende sjekksummer[^6]. I det gamle systemet manglet de fleste dette.
- Det skulle gjennomføres intern opprydding i eksisterende arkivpakker. Midlertidige filer og filer som var irrelevante i bevaringssammenheng ble fjernet.
- Alle filer skulle identifiseres ved hjelp av verktøyet DROID[^7], basert på PRONOM-registeret[^8]. 
- Alle prosesser som ble utført på filene skulle logges i DPS som hendelser basert på PREMIS-standarden[^9].
- Data som var overført og bekreftet lagret i DPS skulle slettes fra det gamle bit-lageret.

## Tidslinje for rearkiveringen

{{% steps %}}

### Mars-April 2023
De to teamene startet med innledende undersøkelser og kartlegging av avismaterialet i det gamle bit-lageret våren 2023.

### Mai 2023 (migreringsstart)
Testmigrering avslørte behov for opprydding i kildematerialet. Det ble laget en egen arbeidsflyt for rearkivering av aviser til DPS. 

### Juni-Juli 2023
Arbeidet med å generere pålitelige sjekksummer startet. Dette arbeidet er beskrevet i en egen [bloggpost](/nb/blog/2024-11-04-checksums/).

### Oktober 2023
Storskala rearkivering av aviser fra mikrofilm og avleverte PDF-aviser. Rundt 1 PB ble flyttet før arbeidet ble stoppet på grunn av manglende lagringskapasitet.

### Januar 2024
Rearkivering av aviser som var skannet ved Nasjonalbiblioteket startet – ca. 1,5 PB.

### Juni 2024
Migrering fullført. 

<!-- Rearkivering fullført 1 juni 2024. -->

{{% /steps %}}

#### Tidslinje for behandlet datavolum

![](/image2.png "Høyeste datamengde prosessert på én dag: 42,15 TB")

#### Tidslinje for antall aviser behandlet

![](/image3.png "Høyeste antall aviser migrert på én dag: 97 528")

## Resultater og erfaringer

- Arkiveringshastigheten varierte mye, og nådde opptil 42 TB per dag for det enkleste materialet. Dette viste at det nye bit-lageret (HPSS) har høy kapasitet, og ga oss nyttige  tidsestimater for fremtidige migreringer. Komplekst materiale (som de som krever OCR-reprosessering) hadde betydelig lavere arkiveringshastighet på grunn av ekstra tid til prosessering på forhånd. 
- Manglende lagringskapasitet førte til en uplanlagt pause. Dette viste at teknisk forberedelse alene ikke var nok. Det var også behov for grundig administrativ planlegging, særlig i forbindelse med innkjøp og anbud.
- Gamle data kan være uoversiktlige, og migrering gir en verdifull mulighet til opprydding. 
    - Vi oppdaget og fjernet 4,5 millioner filer på 0 byte – rester etter midlertidig statusoppdateringer fra tidligere digitaliseringsprosesser. Denne oppryddingen fjernet unødvendig materiale og sørger for at bevaringspakkene våre er i tråd med [prinsippene](/nb/docs/principles/) våre.
    - Vi ryddet opp i materiale som var feilpakket eller inneholdt ufullstendig informasjon, og sørget for at avissamlingen nå er likt pakket og arkivert i DPS.
    - Dårlig OCR-kvalitet ble avdekket i to årganger fra 2010-2011, tilsammen 53 678 aviser/107 TB. Disse var fra de første to årene det ble utført OCR-behandling på materialet. Avisene ble behandlet på nytt med dagens arbeidsflyt for å produsere ny og forbedret OCR. 
    - Enkelte aviser som var skannet fra mikrofilm  hadde svært dårlig kvalitet og ble erstattet av nye skanninger fra papiroriginaler (totalt 2 051 aviser). Dette viser at originalmateriale ofte gir bedre resultat enn avledede kopier.

![Svein Erik Molberg og Mona Løkås fra team Tekst, Vigdis Sørensen fra team Digital bevarings.](/image1.png "Svein Erik Molberg og Mona Løkås fra team Tekst, Vigdis Sørensen fra team Digital Preservation.")

## Noen tall

### Oversikt over aviser som er arkivert på nytt i DPS

| Kilde                 | Avisutgaver | Avisutgaver i  % | Datavolum i TB | Datavolum i % |
| ---------------------- | ------------------ | ----------------------- | ----------------- | ---------------- |
| Født digitalt           | 247 385            | 6%                      | 75                | 3%               |
| Mikrofilm              | 1 779 043          | 41%                     | 784               | 32%              |
| Papiravis             | 2 250 038          | 53%                     | 1 580             | 65%              |
| **Rearkivert til DPS** | **4 276 466**      | **100%**                | **2 439**         | **100%**         |


### Oversikt over alle aviser i DPS (rearkiverte og ny tilvekst siden 2023)

| Kilde                 | Avisutgaver | Avisutgaver i  %  | Datavolum i TB | Datavolum i %  |
| ---------------------- | ------------------ | ----------------------- | ----------------- | ---------------- |
| Født digitalt           | 302 372            | 7%                      | 87                | 3%               |
| Mikrofilm               | 1 899 481          | 41%                     | 820               | 31%              |
|  Papiravis            | 2 397 660          | 52%                     | 1 703             | 66%              |
| **Totalt i DPS i dag** | **4 599 513**      | **100%**                | **2 610**         | **100%**         |


[^1]: 1 Petabyte = 1.000 Terrabyte

[^2]: https://no.wikipedia.org/wiki/Optisk_tegngjenkjenning

[^3]: https://www.loc.gov/standards/alto/techcenter/elementSet/index.html

[^4]: https://www.loc.gov/standards/mets/

[^5]: https://en.wikipedia.org/wiki/Tar\_(computing)

[^6]: https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums

[^7]: https://www.nationalarchives.gov.uk/information-management/manage-information/policy-process/digital-continuity/file-profiling-tool-droid

[^8]: https://www.nationalarchives.gov.uk/pronom/

[^9]: https://www.loc.gov/standards/premis/