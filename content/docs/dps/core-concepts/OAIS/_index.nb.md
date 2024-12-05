---
title: Open Archival Information System (OAIS)
weight: 1
aliases: ["/nb/oais/"]
---

Open Archival Information System (OAIS) er en referansemodell for langsiktig bevaring av digitale informasjonsressurser.
Et OAIS er et arkiv, bestående av en organisasjon, som kan være en del av en større organisasjon, av mennesker og systemer som har påtatt seg ansvaret for å bevare informasjon og gjøre den tilgjengelig for et “angitt fellesskap” (designated community). 
Referansemodellen er også en ISO standard: 14721:2012.

{{< figure src="OAIS_Functional_Model_(en).svg" alt="OAIS-modellen" caption="" attr="Mathieualexhache (original work); Mess (SVG conversion & English translation), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0), via Wikimedia Commons" >}}

## Funksjonelle komponenter

OAIS-modellen består av seks funksjonelle komponenter:

- **Ingest:** håndterer mottak og validering av informasjon som skal bevares. Ingest oppretter en AIP fra SIP, og overfører den nyopprettede AIP til arkivlageret.
- **Archival Storage:** er ansvarlig for å lagre informasjonen på en sikker måte.
- **Data Management:** håndterer beskrivende metadata, organisering og gjenfinning av informasjonen. Håndterer også oppslag mot databasen, og genererer rapporter.
- **Administration:** håndterer administrative oppgaver som styring av tilgang og autorisasjon.
- **Preservation Planning:** sikrer at informasjonen bevares i tråd med best practice og retningslinjer. Støtter alle oppgaver for å holde arkivmaterialet tilgjengelig og forståelig over lang tid selv om det opprinnelige datasystemet blir utdatert, f.eks. utvikling av detaljerte bevaring/migreringsplaner, teknologiovervåking, evaluering og risikoanalyse av innhold og anbefaling av oppdatering og migrering.
- **Access:** muliggjør tilgang til informasjonen for autoriserte brukere.
- Denne funksjonen inkluderer brukergrensesnittet som lar brukere hente informasjon fra arkivet.
- Den genererer en DIP fra den aktuelle AIP og leverer den til kunden som har bedt om informasjonen.

OAIS-modellen legger også vekt på bruk av metadata for å beskrive informasjonen som lagres, slik at det er mulig å forstå og bruke informasjonen på lang sikt.

OAIS-modellen har blitt mye brukt innenfor vitenskapelige og kulturelle institusjoner som arkiver, biblioteker og museer for å bevare digitale informasjonsressurser.

## Bevaringsobjekter

Hvert bevaringsobjekt skal i henhold til OAIS lagres som en autonom og selvdokumenterende arkivpakke, permanent forbundet med alle tilhørende logiske og tekniske metadata.

Bevaringsobjektet i en OAIS-arkivpakke kan være *et enkelt dokument* eller *et sammensatt objekt* bestående av flere filer.

## Ulike varianter av informasjonspakker

Det er tre typer informasjonspakker i OAIS-referansemodellen:

- **SIP (Submission Information Package):** Innleveringspakken som sendes fra produsenten til arkivet
- **AIP (Archival Information Package):** Arkivpakken som er tilrettelagt for langtidsbevaring i arkivet.
- **DIP (Dissemination Information Package):** Utleveringspakken som sendes til en bruker på forespørsel

Disse tre informasjonspakkene kan være identiske med hverandre, men trenger ikke å være det.

<!--
Arkivverket: Når en ny AIP genereres av et OAIS, krever OAIS-standarden at den mottatte SIP-versjonen innlemmes i tillegg. 
For å gjøre det mulig å spore operasjoner skal en opprinnelig SIP bevares *uendret* og *integritetssikret* – for alltid. 
Dette gjelder uavhengig av om en opprinnelig SIP fortsatt er tolkbar.

## Informasjonsmodellen

I OAIS-modellen defineres en informasjonspakke som en samling av data som skal bevares og som er underlagt samme bevaringsstrategi og metadata. En informasjonspakke kan bestå av flere komponenter, som alle er nødvendige for å bevare og gjenopprette informasjonen på en pålitelig måte.

Medlemmer av det “angitte fellesskapet” (designated community) for et arkiv bør kunne tolke og forstå informasjonen i et dataobjekt enten på grunn av deres etablerte kunnskapsbase eller ved hjelp av supplerende «representasjonsinformasjon»/tekniske metadata som er inkludert i dataobjektet.

Det er fire typer metadata som er nødvendige for å beskrive innholdet i en informasjonspakke i OAIS-modellen: Content Information, Preservation Description Information, Descriptive Information og Packaging Information.

**Archival Information Package**

![](media/image2.png)

**Content Information (innholdsinformasjon)**

Innholdsdataobjektet og dets tilhørende representasjonsinformasjon (eller nettverk) er samlet kjent som *innholdsinformasjon*. Det er innholdsinformasjonen - informasjonen som er i fokus for bevaring, sammen med tilstrekkelige metadata for å sikre at den forblir gjengivbart og forståelig for det utpekte samfunnet - at OAIS må forevige over tid.

> **Content Data Object (innholdsdataobjektet, filer)**
>
> Dette er informasjonen som er i fokus for bevaring. Innholdsdataobjektet kan ha form av hvilken som helst type av materiale: tekst, bilder, video, databaser, dataprogrammer - til og med fysisk materiale som jordprøver eller fossiler. Innholdsdataobjektet kan bestå av et enkelt, selvstendig objekt - for eksempel et dokument i PDF-format; Det kan også omfatte flere objekter, for eksempel et nettsted som består av tekst (HTML filer) og statiske bilder (GIF eller JPEG filer). Hovedpoenget er at OAIS er ansvarlig for å bevare innholdsdataobjektet på lang sikt, samt for å gjøre det tilgjengelig i en form som er uavhengig forståelig av fagmiljøet (designated community).
>
> **Representation Information (representasjonsinformasjon)**
>
> For å oppfylle det andre ansvaret - for å gjøre innholdsdataobjekt tilgjengelig i en form som er uavhengig forståelig av fagmiljøet (designated community) - må innholdsdataobjektet være ledsaget av en passende mengde representasjonsinformasjon: informasjon som er nødvendig for å gjengi og forstå biten Sekvenser som utgjør innholdsdataobjektet. Representasjonsinformasjon kan inneholde en beskrivelse av maskinvare- og programvaremiljøet som er nødvendig for å vise innholdsdataobjekt og/eller få tilgang til innholdet; Det kan også oppsummere passende tolkning av innholdsdataobjektet. For eksempel, hvis innholdsdataobjektet er en ASCII-fil med tall, kan representasjonsinformasjon indikere at tallene tilsvarer gjennomsnittlig daglige lufttemperaturavlesninger for London, målt i grader Celsius, for perioden 1972-2000.
>
> Representasjonsinformasjon kan deles inn i to typer: strukturinformasjon og semantisk informasjon.
>
> **Strukturinformasjon** forstås lettest i sammenheng med digitale objekter, og refererer til kartlegginger mellom digitale biter og forskjellige konsepter og datastrukturer som gjør bitene til forståelig informasjon - dvs. et bilde, tekst, et interaktivt program. Generelt sett beskriver strukturinformasjon formatet til det digitale objektet.
>
> **Semantisk informasjon** er derimot informasjon som tydeliggjør betydningen eller passende tolkning av innholdsdataobjektet. En ordliste, en dataordbok og en programvares brukerdokumentasjon er alle eksempler på semantisk informasjon som kan være samlet med innholdsdataobjektet som en del av dets representasjonsinformasjon. Referansemodellen definerer også en “catch-all” kategori kalt *annen representasjonsinformasjon* ( Other Representation Information), som inkluderer all representasjonsinformasjon som ikke lett er definert som verken struktur eller semantisk. For eksempel bemerker referansemodellen at informasjon om hvordan strukturen og semantisk informasjon forholder seg til hverandre, vil falle i denne kategorien.
>
> I praksis kan strukturen for representasjonsinformasjon være ekstremt kompleks. Et bestemt sett med representasjonsinformasjon kan kreve ytterligere representasjonsinformasjon for å bli gjengitt, tolket og/eller forstått av det utpekte samfunnet. Det andre settet med representasjonsinformasjon kan i seg selv kreve enda et sett med representasjonsinformasjon. Denne regressive prosessen kan fortsette for et vilkårlig antall trinn. Tenk for eksempel på et digitalt objekt i form av et METS (metadata koding og overføring standard) dokument. For å sikre forståeligheten av et METS-dokument, kan et arkiv av OAIS-type trenge å sikre en kopi av METS-skjemaet som en del av objektets representasjonsinformasjon. METS -skjemaet uttrykkes imidlertid i XML (utvidbart markeringsspråk); For å forstå METS -skjemaet (og derfor indirekte, for å forstå det originale METS -dokumentet), kan brukerne trenge tilgang til XML -spesifikasjonen. XML er i seg selv en profil av SGML (standard generalisert markeringsspråk) ISO Standard 8879: 1986; For å forstå XML fullt ut, kan en kopi av SGML -standarden også være nødvendig som en del av det opprinnelige objektets representasjonsinformasjon.
>
> Alle disse materialene - METS-skjemaet, XML-spesifikasjonen, SGML-standarden - danner et representasjonsnettverk tilknyttet innholdsdataobjektet (METS-dokumentet). Representasjonsnettverk er nestede informasjonskjeder som danner tilstrekkelig kontekst for det utpekte samfunnet til å forstå et innholdsdataobjekt, så vel som dets tilhørende representasjonsinformasjon. I teorien kan representasjonsnettverk danne en uendelig regresjon som fører til absurde resultater: Fortsetter vårt METS-eksempel, kan man si at SGML -standarden er tilgjengelig som ASCII-tekst, så en kopi av ASCII-spesifikasjonen er nødvendig for å forstå den; ASCII-spesifikasjonen er publisert på engelsk, så det er behov for en engelsk språkordbok og grammatikkregler for å forstå ASCII-spesifikasjonen, og så videre. I praksis vil selvfølgelig OAIS-arkivet avkalle representasjonsnettverket på et passende punkt basert på rimelige forutsetninger om den tidligere eller antatte kunnskapen som det utpekte samfunnet har besatt - for eksempel en antakelse om at det utpekte samfunnet forstår det engelske språket. OAIS-referansemodellen refererer til denne antatte kunnskapen som fagmiljøets (designated community) kunnskapsgrunnlag.
>
> Det ble nevnt tidligere at omfanget av fagmiljøet (designated community) påvirker mengden metadata som kreves for å støtte bevaringsprosessen. Det er med hensyn til representasjonsinformasjon at dette er slik. Generelt, jo bredere omfang av fagmiljøet (designated community), desto mindre spesialiserte kunnskapen som er knyttet til det samfunnet - det vil si, desto mindre informasjon som er relevant for å tolke og forstå den arkiverte informasjonen, kan OAIS anta at det utpekte samfunnet har. Jo mindre spesialiserte kunnskapsgrunnlaget, jo mer representasjonsinformasjon er det nødvendig for å sikre at den bevarte informasjonen forblir gjøres og forståelig for det utpekte samfunnet på lang sikt. I denne forstand er representasjonsinformasjon en betydelig kilde til risiko for et arkiv av OAIS-type: Når fagmiljøet (designated community) utvikler seg og muligens utvides over tid, må arkivet sørge for at representasjonsinformasjonen det fanger og vedlikeholder utvikler seg deretter. Dette kan være en utfordrende oppgave, fordi kravene til informasjonsinformasjon utvides over tid, kan arkivet bli bedt om å gjentroaktivt supplere representasjonsinformasjon for innholdsdataobjekter som har vært i arkivretensjon i en betydelig periode. Enkel som slik representasjonsinformasjon kan fås, eller faktisk om den fremdeles er tilgjengelig i det hele tatt, er et åpent spørsmål.

**Preservation Description Information (beavaringsmetadata)**

Langsiktig bevaring av innholdsinformasjonen krever ytterligere metadata for å støtte og dokumentere OAISs bevaringsprosesser. Disse metadataene kalles *Preservation Description Information* (bevaringsmetadata), eller PDI. I henhold til referansemodellen er PDI spesielt fokusert på å beskrive fortids- og nåværende tilstander for innholdsinformasjonen, og sikre at den er unikt identifiserbar, og sikre at den ikke har blitt ubevisst endret.

PDI består av fem komponenter:

- **Reference Information** (referanseinformasjon) identifiserer innholdsinformasjonen unikt innen OAISs interne systemer, så vel som for enheter og systemer utenfor OAIS. Eksempler inkluderer en systemgenerert intern identifikator, og en ISBN.

- **Context Information** (kontekstinformasjon) beskriver innholdsinformasjonens forhold til andre innholdsinformasjonsobjekter: for eksempel de som er relatert til den tematisk (f.eks. Som en del av en emnebasert samling), eller de som representerer versjoner av det samme innholdet i alternative formater.

- **Provenance Information** (Proveniensinformasjon) dokumenterer historien til innholdsinformasjonen, inkludert opprettelsen, eventuelle endringer i innholdet eller formatet over tid, dens varetektskjede, eventuelle tiltak som er iverksatt for å bevare innholdsinformasjonen (for eksempel normalisering eller formatmigrasjon), og resultatet av utfallet av disse handlingene.

- **Fixity Information** (sjekksuminformasjon) sikrer at innholdsinformasjonen ikke er endret på en udokumentert måte, gjennom autentisitet eller integritetsvalideringsmekanismer som sjekk summer, digitale signaturer eller digitale vannmerker.

- **Access Rights Information** (informasjon om tilgangsrettigheter) dokumenterer alle betingelser eller begrensninger knyttet til innholdsinformasjonen som gjelder både bevaring og tilgang. Det kan også omfatte beskrivelser av rettighetshåndhevelsesmekanismer. Eksempler inkluderer lisensvilkår, identifisering av de med autoriserte tilgangstillatelser (f.eks. Et spesifisert IP -adresseområde) og bevaringsbetingelser og betingelser som er forhandlet mellom OAIS -arkivet og produsenten av innholdsinformasjonen.

Sammenlagt representerer *innholdsinformasjon* og *bevaringsmetadata* det arkiverte digitale innholdet, metadataene som er nødvendige for å gjengi og forstå det, og metadataene som er nødvendige for å støtte dens bevaring, autentisitet og formidling.

**Packaging Information (pakkeinformasjon)**

Pakkeinformasjon brukes til å binde *innholdsinformasjon* (informasjon om innholdsdata og representasjonsinformasjon) og *bevaringsmetadata* (referanse, kontekst, proveniens, sjekksum og tilgangsrettighetsinformasjon) til en enkelt logisk pakke. Mer spesifikt tjener pakkeinformasjon til å kombinere (logisk) alle disse informasjonskomponentene til en AIP, slik at de kan identifiseres og lokaliseres som en enkelt logisk enhet i arkivsystemet. Pakkeinformasjon kan ha form av grunnleggende informasjon som katalogstier og filnavn, eller et mer detaljert pakkeskjema som METS.

**Descriptive Information (beskrivende metadata)**

Beskrivende metadata støtter oppdagelse og gjenfinning av innholdsinformasjon fra en OAISs forbrukere, via dens søkemuligheter. For eksempel kan beskrivende informasjon ha form av en Dublin Core Metadata -post, avledet fra innholdsinformasjonen og den tilhørende bevaringsmetadat, og vedlikeholdes av OAIS for å lette oppdagelsen fra arkivets brukere.

**Sette sammen brikkene**  
Informasjonskomponentene beskrevet ovenfor - innholdsinformasjon (innholdsdataobjekt og representasjonsinformasjon), bevaringsmetadata (referanse, kontekst, proveniens, fiksitet og tilgangsrettighetsinformasjon), pakkeinformasjon og beskrivende metadata - danner samlet informasjonsmodellen til en OAIS-arkiv. Mer spesifikt danner innholdsinformasjon og bevaringsmetadata en arkivpakke; pakkeinformasjon gjør at AIP kan identifiseres og lokaliseres som en enkelt logisk enhet; og beskrivende metadata støtter oppdagelse og formidling av AIP.

Akkurat som OAIS -referansemodellen ikke foreskriver noen spesiell tilnærming til å implementere den funksjonelle modellen beskrevet i avsnitt 5.3, på samme måte som den unngår enhver spesifikk anbefaling for å implementere de forskjellige komponentene i informasjonsmodellen. Målet er i stedet å gi en konseptuell modell av informasjonsobjektene som administreres av et arkiv av OAIS-type. Implementering av disse konseptene vil avhenge av de spesifikke arkitekturene, systemene og skjemaet som brukes i et bestemt arkivmiljø.

1.  **Content Information (innholdsinformasjon)**: dette inkluderer dataobjektet og dets representasjonsinformasjon.  
      
    ChatGPT: Beskriver selve innholdet som skal bevares, for eksempel en fil eller en samling av filer. Dette kan være tekst, bilder, lyd, video eller andre digitale formater. Content Information er den primære informasjonen som OAIS-arkivet vil bevare og beskytte. Innholdet vil normalt være lagret i et standardformat som er godt egnet for langsiktig bevaring.  
      
    Består igjen av:

    1.  **Content Data Object** (Innholdsdata (filer)

    2.  **Representation Information** (Tekniske metadata)

2.  **Preservation Description Information (bevaringsmetadata)**:  
    inneholder informasjon som er nødvendig for å bevare den tilknyttede innholdsinformasjonen (som informasjon om varens herkomst, unike identifikatorer, en sjekksum eller andre autentiseringsdata, etc.)  
      
    ChatGPT: beskriver hvordan innholdet i en informasjonspakke skal bevares på en pålitelig måte. Dette kan inkludere informasjon om formatet og kodingen av innholdet (tekniske metadata), eventuelle konverterings- eller migrasjonsprosesser som er utført, og informasjon om de tekniske egenskapene til lagringsmedier og -systemer som brukes til å bevare innholdet.

3.  **Descriptive Information (beskrivende metatada)**: metadata om objektet som gjør at objektet kan lokaliseres på et senere tidspunkt ved hjelp av arkivets søke- eller gjenfinningsfunksjoner.  
      
    ChatGPT: beskriver innholdet i en informasjonspakke på en måte som gjør det lettere å forstå og gjenfinne. Dette kan inkludere informasjon om innholdets opphav, eierskap, formål, kontekst og relevans. Descriptive Information gir informasjon om hva innholdet i en informasjonspakke handler om, og gjør det lettere å finne igjen og bruke innholdet i fremtiden.

4.  **Packaging Information:** holder komponentene i informasjonspakken sammen.  
      
    ChatGPT: beskriver hvordan informasjonen i en informasjonspakke skal pakkes eller struktureres for å oppfylle bestemte krav, og kan omfatte tekniske detaljer om hvordan dataene i en informasjonspakke skal organiseres og lagres på lagringsmedier.

Sammen beskriver disse fire typene metadata alle aspekter ved en informasjonspakke som er nødvendige for å bevare og gjenopprette innholdet på en pålitelig måte. Ved å bruke disse metadataene kan OAIS-arkiver sikre at informasjonspakkene kan bevares over tid, og at de kan gjenopprettes og brukes på en pålitelig måte når de er nødvendige.
 -->
### Relevante dokumenter

[OAIS Reference Model: Introductory Guide (2nd Edition)](https://www.dpconline.org/docs/technology-watch-reports/1359-dpctw14-02/file)

[OAIS modellen kan leses i sin helhet her.](https://public.ccsds.org/pubs/650x0m2.pdf)
