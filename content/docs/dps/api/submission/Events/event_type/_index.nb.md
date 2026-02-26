---
title: Event-typer
weight: 2
draft: false
---


Nasjonalbiblioteket har tatt utgangspunkt i [Library of Congress](https://www.loc.gov/) sin liste over [EventTypes](https://id.loc.gov/vocabulary/preservation/eventType.html). Lista har blitt innskrenket, og bruken av de ulike typene er spesifisert til å passe våre behov og bevaringsomgivelser. Andre typer enn det som er spesifisert i lista nedenfor blir ikke godkjent i API.


## EventTypes


### Capture

| Navn 	| **capture** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen der en agent (organisasjon, team, rolle, system, tjeneste, automatisert prosess) aktivt tilegner seg et objekt gjennom andre mekanismer enn overføring fra skaper eller giver. 	|
| Omfang 	| IE, Fil 	|


**Retningslinjer for bruk:**
- Brukes når det høstes nettsteder ved hjelp av crawling.


**Eksempler:**

 


### Creation 


 | Navn 	| **creation** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen der et nytt objekt opprettes. 	|
| Omfang 	| Fil 	|


**Retningslinjer for bruk:**
- Brukes for å dokumentere det digitale objektet i en informasjonspakke. 
-	Brukes til å dokumentere opprinnelsen til filen eller den Intellektuelle Entiteten (IE), og beskriver metoden og prosessen for å opprette filen/IE. Se også eventType "imaging". 
  

**Eksempler:**



### Filename change 


 | Navn 	| **filename change** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen der et filnavn endres.  	|
| Omfang 	| Fil 	|


**Retningslinjer for bruk:**
-	Relevant ved endring av navn på en født digital fil, eller når for eksempel en fil må gis nytt navn for å oppfylle kravene til lagringssystemet. 
-	Enten fjerning av forbudte tegn eller delvis/hel erstatning av det opprinnelige filnavnet. Dette kan brukes for å dokumentere endringer som fjerning av tegn, eller der et system fjerner filnavnet helt og erstatter det med et systemgenerert navn.



**Eksempler:**
 


 ### Fixity check 


 | Navn 	| **fixity check** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen med å verifisere at et objekt ikke har blitt endret i en gitt periode.	|
| Omfang 	| IE, Fil 	|


**Retningslinjer for bruk:**
-	Eventen bør knyttes til IE når det er mulig. Knyttes kun til fil dersom det er behov for å dokumentere avvik.
-	Vil mest sannsynlig inneholde resultatene fra eventen «message digest calculation».
- Spesielt viktig når sjekksummer mottas fra eksterne. 


**Eksempler:**
 


 ### Imaging 


 | Navn 	| **imaging** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen med å hente ut et diskbilde fra et fysisk informasjonsmedium.	|
| Omfang 	| IE 	|


**Retningslinjer for bruk:**
-	Brukes for å dokumentere prosessen med å lage en eksakt digital kopi (diskbilde) av et lagringsmedium, inkludert alle filer, metadata, filsystemstruktur og noen ganger også ledig plass og slettede data.
-	Der det er relevant, skal denne eventen brukes i stedet for, ikke i tillegg til, «creation»-eventen. 


**Eksempler:**



### Message digest calculation 


 | Navn 	| **message digest calculation** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen der en sjekksum (checksum) opprettes.	|
| Omfang 	| IE, Fil	|


**Retningslinjer for bruk:**
-	Eventen bør knyttes til IE når det er mulig. Knyttes kun til fil dersom det er behov for å dokumentere avvik.
-	Eventen «fixity check» kontrollerer Sjekksummen.
- Brukes ved opprettelse av nye sjekksummer. Hvis sjekksummer opprettes lokalt, er det ikke behov for å bruke eventen "fixity check" i tillegg til event "message digest calculation". Se også EventType "fixity check". 




**Eksempler:**




### Metadata extraction 


 | Navn 	| **metadata extraction** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen med å hente ut metadata fra et objekt. Dette inkluderer tekniske, administrative og beskrivende metadata.	|
| Omfang 	| Fil	|


**Retningslinjer for bruk:**
- Brukes når metadata hentes ut av en fil og resulterer i en eller flere metadatafiler. 
- Filen(e) som utledes må referere til opprinnelsesfila. 


**Eksempler:**




### Migration


 | Navn 	| **migration** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen der et objekt konverteres fra ett filformat til ett eller flere andre filformater.	|
| Omfang 	| IE, Fil	|


**Retningslinjer for bruk:**
-	Eventen bør knyttes til IE når det er mulig, for eksempel dersom filene er konvertert på samme måte til samme format.
-	Brukes ved endring av filformat, ikke til å dokumentere komprimering som del av lagringsoptimalisering. Se også eventType «compression».
-	Migration-events skal alltid resultere i en ny pakke eller fil. 
- Filen(e) som migreres må referere til opprinnelsesfila. 


**Eksempler:**




### Transfer 


 | Navn 	| **transfer** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen med å overføre metadata og/eller digitale objekter mellom systemer. 	|
| Omfang 	| IE	|


**Retningslinjer for bruk:**
-	Brukes ved overføring av objekter inn eller ut av bevaringsområdet eller midlertidige arbeidsområder. Dette inkluderer for eksempel flytting mellom bit-lagre, fra bit-lager til arbeidsområde for bearbeiding, eller fra arbeidsområde til bit-lager.


**Eksempler:**




### Validation 


 | Navn 	| **validation** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen med å sammenligne et objekt med en standard og registrere samsvar eller avvik. 	|
| Omfang 	| IE, Fil	|


**Retningslinjer for bruk:**
-	Objektet som valideres kan være en fil eller en Intellektuell enhet. Eventen bør knyttes til IE når det er mulig. For eksempel hvis filene er validert på samme måte med samme verktøy, eller strukturen er validert for hele pakken. 
-	Det kan være hensiktsmessig å lage én event for hele valideringen der man heller beskriver hvilke verktøy som er brukt i de ulike stegene, i stedet for å lage flere eventer for flere valideringer. 
 


**Eksempler:**





### Virus check 


 | Navn 	| **virus check** 	|
|:---	|:---	|
| Beskrivelse 	| Prosessen der en fil skannes for virus eller skadelig programvare. 	|
| Omfang 	| IE, Fil	|


**Retningslinjer for bruk:**
-	Eventen bør knyttes til IE når det er mulig. Knyttes kun til fil dersom det er behov for å dokumentere avvik.

 

**Eksempler:**