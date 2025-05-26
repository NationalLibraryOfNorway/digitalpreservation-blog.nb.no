---
title: Pakkestruktur
weight: 1
---


| **ID** | **Beskrivelse** | **Krav** | **Kardinalitet** |
|---|---|---|---|
| **CSIPSTR1** | Enhver Informasjonspakke MÅ være inkludert i én enkelt fysisk rotmappe (heretter kjent som “rotmappa”). Pakker som er pakket i et arkivformat (f.eks. ZIP, TAR), MÅ pakkes ut til én enkelt rotmappe, se CSIPSTR3 og NBSIPSTR3. | **MÅ** | **1..1** |
| **NBSIPSTR1** | En SIP MÅ beskrive nøyaktig én intellektuell entitet/ressurs. Se Omfang på informasjonspakker for mer informasjon. | **MÅ** |  |
| **NBSIPSTR2** | Navnet på SIP-ens rotmappe MÅ være det samme som @OBJID-attributten som oppgis på METS.xml-fila i rotmappa. Navnet MÅ kun bruke tillatte tegn, som er: ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0123456789-_ . Navnet på rotmappa BØR være en unik ID (f.eks. URN).  Dette kravet er en strengere, SIP-spesifikk variant av CSIPSTR2. | **MÅ** |  |
|  |  |  |  |
|  |  |  |  |