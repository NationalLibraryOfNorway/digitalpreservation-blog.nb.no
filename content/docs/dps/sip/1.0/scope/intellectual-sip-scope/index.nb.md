---
title: Omfang på informasjonspakker
summary: This post discusses some key concepts related to information package scope and the eArchviving standards and specifications
date: 2024-10-04
tags: [Information packages, IP, E-ARK, eArchiving, asset management, cataloging]
authors: 
  - name: Torbjørn Bakken Pedersen
    image: https://avatars.githubusercontent.com/u/113333557?v=4
images: 
  - ie-sip.png
weight: 3
aliases: ["/nb/sip-omfang"]
---

I den foregående teksten var det lagt vekt på kompleksiteten i håndtering av representasjoner i Nasjonalbiblioteket. 
For å forstå denne kompleksiteten bedre, må vi først se på hvordan metadatasystemene våre er modellert.

## Intellektuelle entiteter i metadatasystemene
Intellektuelle entiteter (IE) er et begrep vi finner i de ulike forvaltning/katalogsystemene utenfor det digitale bevaringsmiljøet. 
I disse systemene opereres det ofte med mange forskjellige IE-er, vanligvis organisert i et slags hierarki. 
 
Ved bruk av PREMIS og E-ARK er det vanligvis entiteten på høyeste nivå fra disse hierarkiene, som refereres til som IE og brukes til å definere omfang av informasjonspakker.
Dette vil for eksempel være et *verk* eller *uttrykk*. 
Vi velger derimot å definere informasjonspakkeomfanget annerledes, ved å bruke en entitet som sitter på et lavere beskrivelsesnivå:

- Omfanget på informasjonspakker er definert av typen IE i metadatasystemet, som holder UID-en som knytter en IE til en informasjonspakke.

Dette er nødvendig for å holde alle komponenter i [systemarkitekturen](/nb/systemarkitektur) vår synkronisert. 
UID-en er kun brukt på spesifikke typer intellektuelle entiteter i våre metadatasystemer.

## Hierarkiske og flate strukturer
En endring i arkitekturen vår kunne åpnet for bruk av en annen UID, plassert på en annen IE i disse metadatahierarkiene.
Vi mener imidlertid at dette er upraktisk da det introduserer unødvendig kompleksitet, som igjen kan hindre skalerbarhet på tvers av systemene våre.

Intellektuelle entiteter høyt i disse metadatahierarkiene, beskriver gjerne abstrakte konsepter.
Nedover i hierarkiene beskriver entitetene mer og mer spesifikke og håndfaste konsepter.
Det nederste nivået er det mest spesifikke og beskriver som regel fysiske eller digitale objekter.
 
Informasjonspakker definert av intellektuelle entiteter, som beskriver abstrakte konsepter, introduserer en rekke utfordringer:
- Svært store pakkestørrelser (titalls terabyte)
- Et stort antall representasjoner per informasjonspakke
- Komplekse relasjoner mellom representasjoner i informasjonspakkene
- Endringer i deskriptive metadata kan føre til omstrukturering av bevarte data
- Bevaring av uidentifiserte digitale objekter uten relasjoner til en IE med nødvendig UID
- Økt kompleksitet i synkroniseringen av våre tre systemdomener

Noen av disse utfordingene stammer fra komplekse metadatastrukturer i metadatasystemene.
Vi ønsker ikke å speile eller forvalte komplette hierarkiske katalogstrukturer i bevaringsomgivelsene.
Dette er tross alt det metadatasystemene er ment for!

Vi foretrekker å holde strukturere informasjonspakker i en flat struktur.
Det vil si at det er et én-til-én-forhold mellom en informasjonspakke i DPS og en intellektuell entitet i metadatasystemene. 
Dette for å unngå å operere med unike metadataentiteter eller "størrelser" i bevaringsmiljøet, samt for å lette prosessene for inntak av metadata.

## Intellektuelt pakkeomfang
Regelsettet vi ender opp med er som følger:

- Et **digitalt objekt** er beskrevet som en **IE** i metadatasystemene
- Det **digitale objektet** pakkes som den **primære representasjonen** i en **informasjonspakke**
- **Informasjonspakka** og **IE-en** deler en **URN**, forvaltet i metadatasystemet
- Ethvert nytt digitalt objekt beskrives som en ny **IE**, som mottar en **ny URN**, og må derfor representeres som en primær representasjon i en **ny informasjonspakke**

På grunn av hvordan URN-er knytter alt sammen, ligger regelsettet som avgjør om du skal opprette en ny informasjonspakke eller en ny representasjon, i domenet til metadatasystemene.
- En enkelt URN = en enkelt informasjonspakke
- Flere URN-er = flere informasjonspakker

Hvis du bare har én URN men likevel ønsker å bevare et annet utledet digitalt objekt i DPS, vil du opprette en annen representasjon i samme informasjonspakke som det primære digitale objektet.

{{< figure src="ie-sip.svg" alt="Diagram som viser forholdet mellom IE i metadatasystem og informasjonspakke i DPS" caption="IE til informasjonspakke-forhold" >}}

## UID, IE og informasjonspakke
I metadatasystemene *sitter* eller *peker* den essensielle UID-en til det *laveste* hierarkiske beskrivelsesnivået.

Våre mer komplekse metadatasystemer (f.eks. Axiell Collections) er avanserte forvaltningssystemer, som beskriver det faktiske digitale objektet i teknisk detalj ved hjelp av en *bærer*[^1]-IE. 
URN-en identifiserer bærer-IE-en, og dermed også informasjonspakken som sendes til og deretter forvaltes av DPS.

Våre MARC-baserte metadatasystemer (f.eks. ALMA) bruker URN til å *peke til* informasjonspakken og dens primære representasjon.
Det digitale objektet blir derimot ikke beskrevet i disse metadatasystemene.
I disse systemene identifiserer URN-en kun informasjonspakka som sendes til og forvaltes av DPS, men *ikke* den intellektuelle posten som holder URN-en.
Informasjonspakka i DPS er dermed det eneste stedet man kan finne teknisk metadata for slike digitale objekter.

Å bruke den minst abstrakte IE-en for å definere omfang på informasjonspakker har flere positive effekter:

- Pakkestørrelsen holdes liten
- Representasjonsreglene holdes enkle
- Definisjonen av pakkeomfanget ligger hos produsentmiljøet
- Krav for innlasting til DPS senkes (vi trenger kun å beskrive den tekniske ressursen, ikke nødvendigvis dets intellektuelle innhold)
- Omstruktureringer av pakker på grunn av endringer i deskriptive metadata holdes til et minimum

[^1]: Bærerentiteten i våre metadatasystemer er den mest spesifikke beskrevne entiteten i disse systemene. Bæreren beskriver det faktiske, håndfaste *objektet* - *tingen*. Dette gjelder både for analoge og digitale objekter. Vi refererer til disse spesifikke, håndfaste IE-ene som "bærer", selv om det ikke nødvendigvis kalles "bærer" i alle disse systemene.