---
title: Pakkestruktur
weight: 1
---


| **ID** | **Beskrivelse** | **Krav** | **Kardinalitet** |
|:---|:-------|:---|:---|
| **CSIPSTR1** | Enhver Informasjonspakke **MÅ** være inkludert i én enkelt fysisk rotmappe (heretter kjent som “rotmappa”). Pakker som er pakket i et arkivformat (f.eks. ZIP, TAR), **MÅ** pakkes ut til én enkelt rotmappe, se CSIPSTR3 og NBSIPSTR3. | **MÅ** | **1..1** |
| **NBSIPSTR1** | En SIP MÅ beskrive nøyaktig én intellektuell entitet/ressurs. Se Omfang på informasjonspakker for mer informasjon. | **MÅ** |  |
| **NBSIPSTR2** | Navnet på SIP-ens rotmappe **MÅ** være det samme som @OBJID-attributten som oppgis på `METS.xml`-fila i rotmappa. Navnet **MÅ** kun bruke tillatte tegn, som er: `ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0123456789-_ `. Navnet på rotmappa **BØR** være en unik ID (f.eks. URN).  Dette kravet er en strengere, SIP-spesifikk variant av CSIPSTR2. | **MÅ** |  |
| **NBSIPSTR3** | En SIP **KAN** være pakket i et arkivformat eller komprimert format for overføring. Hvis SIP-en er pakket i et format **MÅ** kun TAR- eller ZIP-format brukes. Hvis en pakket SIP overføres i flere delfiler, **MÅ** enkeltdelene ikke være større enn 5GB. Se også CSIPSTR1.  Dette kravet er en strengere, SIP-spesifikk variant av CSIPSTR3. | **KAN** |  |
| **NBSIPSTR4** | `rotmappe/METS.xml`  En SIPs rotmappe **MÅ** inneholde en fil som heter `METS.xml`. Fila **MÅ** inneholde metadata som identifiserer pakka, gir en overordnet beskrivelse av pakka, dens struktur, samt inneholder henvisninger til pakkas representasjoner. `METS.xml` **MÅ** innfri kravene spesifisert i Krav for bruk av METS.xml.   Dette er en strengere, SIP-spesifikk variant av CSIPSTR4. | **MÅ** | **1..1** |
| **NBSIPSTR5** | `rotmappe/metadata`  En SIPs rotmappe **MÅ** inneholde nøyaktig én mappe som heter `metadata`. Her legges metadata som omhandler hele informasjonspakka.  Dette er en strengere, SIP-spesifikk variant av CSIPSTR5. | **MÅ** | **1..1** |
| **NBSIPSTR6** | `rotmappe/metadata/preservation`  Hvis bevaringsmetadata er tilgjengelig **MÅ** disse legges i en undermappe kalt `preservation`. E-ARK-spesifikasjonene anbefaler å formatere bevaringsmetadata i PREMIS (se E-ARK CSIP \| Common Specification for Information Packages og CS PREMIS).  Med bevaringsmetadata menes hendelser og håndteringshistorikk av den digitale ressursen. For eksempel dokumenteres flytting av filer til nytt lagringssystem, endring av filformat og validering/kontroll av filer.  Dette er en strengere, SIP-spesifikk variant av CSIPSTR6. Se også krav for bruk av METS.xml for metadata i CSIP31-57. | **MÅ** | **0..1** |
| **NBSIPSTR7** | `rotmappe/metadata/descriptive`  Mappa `metadata` på rot **MÅ** inneholde nøyaktig én undermappe som heter `descriptive`. Deskriptive metadata skal kun legges i denne undermappa og ikke på de enkelte representasjonene.  Med deskriptive metadata menes informasjon som beskriver det intellektuelle innholdet til et digitalt objekt, for eksempel identifikator, tittel, forfatter og publiseringsdato.  Dette er en strengere, SIP-spesifikk variant av CSIPSTR7. Se også NBSIP8-10 i METS.xml (SIP). | **MÅ** | **1..1** |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |