---
title: Foretrukne filformater
description: "Liste over foretrukne filformater for digital bevaring ved Nasjonalbiblioteket"
weight: 6
date: 2024-05-07
draft: false
tags: [Policy, File formats]
authors: 
  - name: Digital Preservation Team
    image: /images/NB-svart.png
aliases: ["/docs/formats/2024-05-07-formats-in-use-no", "/docs/formats/preferred-formats-no/"]
---

Dette er en liste over filformatene som er foretrukket av Nasjonalbiblioteket for digital bevaring. 
Anbefalingene er utarbeidet av de respektive fagseksjonene, mens lista forvaltes av teamet for digital bevaring.

Lista omfatter både formater Nasjonalbiblioteket produserer selv og formater Nasjonalbiblioteket mottar fra andre. 
Formatene på lista er de som er anbefalt for bevaring av fagressurser i Nasjonalbiblioteket.
De foretrukne formatene er det vi helst vil ha, mens de akseptable også vil bli godtatt uten konvertering/normalisering. 
Alle andre formater bør diskuteres med relevante fagseksjoner, før de eventuelt blir akseptert går inn i forvaltningen. 

Lista er inspirert av [Open Preservation Foundations (OPF)](https://openpreservation.org) liste ["International Comparison of Recommended File Formats"](https://docs.google.com/spreadsheets/d/1XjEjFBCGF3N1spNZc1y0DG8_Uyw18uG2j8V2bsQdYjk/edit#gid=1719869262) og Library of Congress sine oversikter ["Sustainability of Digital Formats: Planning for Library of Congress Collections"](https://www.loc.gov/preservation/digital/formats/fdd/descriptions.shtml) og ["Recommended Formats Statement"](https://www.loc.gov/preservation/resources/rfs/index.html).


---

## Bilder

|  <div style="width:255px">Formål</div> | Foretrukne formater                                   | Akseptable formater                             |
| -------------------------------------- | ----------------------------------------------------- | ----------------------------------------------- |
| Bevaring av digitaliserte bilder       | <li>TIFF (Tagged Image File Format), revision 6 [^1]  |                                                 |
| Bevaring av plakater                   | <li>PDF/A Family, PDF for Long-term Preservation [^2] | <li>PDF (Portable Document Format) Family [^28] |
| Tilgangskopier                         | <li>JPEG 2000 Part 2 (Extensions) jpf (jpx) [^3]      |                                                 |


## Levende bilder
| <div style="width:255px">Formål</div>                     | Foretrukne formater                                                                                                                                                                                                                                                                        | Akseptable formater                                                                                                                 |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| Filmmastere og filmdigitalisering                         | <li>Matroska/FFV1/PCM (Matroska File Format with FFV1 video encoding) [^8]<li>DPX (Digital Moving-Picture Exchange), Version 2.0 [^9] <li> TIFF sequence [^1]<li>MPEG-4, Advanced Video Coding (Part 10) (H.264)/PCM (lossless, ukomprimert mezzanin) [^15] <li> OpenEXR [^11] <li> Apple Prores4444/mov [^12]<li> DNxHR444  | <li>Apple ProRes 422 High Quality/mov [^13]<li> DNxHR HQX/HQ                                    |
| Fjernsyn (master/sendemaster), VOD,hjemmevideo og tilgang | <li>Interoperable Master Format (IMF) [^14]<li>MXF/XDCAM<li>MXF OP1a [^32]                                                                                                                                                                                                                 | <li>MPEG-4, Advanced Video Coding (Part 10) (H.264) [^15]<li> MPEG-2 Video Encoding (H.262) [^16] (50Mbit/s, bare Inter-frame-kodet)|
| Filmdistribusjon (kino)                                   | <li>DCP, Version 1.0 (Digital Cinema Initiative Distribution Package) [^17] (ukryptert)<li> IMF (Interoperable Master Format) [^14]  (ukryptert)                                                                                                                                           |                                                                                                                                     |
| Digitalisert video                                        | <li>Matroska/FFV1/PCM [^8]                                                                                                                                                                                                                                                                 |                                                                                                                                     |
| Filmlyd (sluttmix/audiomaster)                            | <li>BWF (Broadcast WAVE Audio File Format), Version 2 [^4]<li>WAVE Audio File Format with LPCM audio [^5]<li>FLAC (Free Lossless Audio Codec), Version 1.1.2 [^6]                                                                                                                          |                                                                                                                                     |
| Undertekster                                              | <li>SRT (SubRip Subtitle format) [^25]<li> PAC (Presentation Audio/Video Coding)<li> XML                                                                                                                                                                                                   |                                                                                                                                     |


## Lyd
| <div style="width:255px">Formål</div>                                                                                                    | Foretrukne formater                                                                                                                             | Akseptable formater                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Mastere og lyddigitalisering<br><li>Minimum bitdybde: 16 bit <li>Anbefalt bitdybde: 24 bit <li>Minimum samplingsfrekvens: 44100 Hz       | <li>BWF (Broadcast WAVE Audio File Format), Version 2 [^4]<li>WAVE Audio File Format with LPCM audio [^5]<li>MBWF/RF64 (Multichannel BWF) [EBU TECH 3306] [^35] | <li>FLAC (Free Lossless Audio Codec), Version 1.1.2 [^6] <li>AIFF LPCM (Audio Interchange File Format with LPCM Audio) [^36] |

## Nettarkiv
| <div style="width:255px">Formål</div> | Foretrukne formater                                                                    | Akseptable formater |
| ------------------------------------- | -------------------------------------------------------------------------------------- | ------------------- |
| Netthøsting                           | <li>WACZ (Web Archive Collection Zipped) [^26]<li>WARC (Web ARChive file format) [^27] |                     |


## Tekst
| <div style="width:255px">Formål</div> | Foretrukne formater                                                                                               | Akseptable formater                             |
| --------------------------------------| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------|
| Skannet tekst                         | <li>JPEG 2000 Part 1 (Core) jp2 File [^29]                                                                        |                                                 |
| OCR                                   | <li>ALTO XML [^30]                                                                                                |                                                 |
| Digital tekst                         | <li>PDF/A Family, PDF for Long-term Preservation [^2] <li> EPUB (Electronic Publication) File Format Family [^31] | <li>PDF (Portable Document Format) Family [^28] |
| Tilgangskopier                        | <li>JPEG 2000 Part 2 (Extensions) jpf (jpx) [^3]                                                                  |                                                 |
| Forsidebilder                         | <li>JPEG Image Encoding Family [^33] <li> PNG (Portable Network Graphics) [^34]                                   |                                                 |


[^1]: Sustainability of digital formats: Planning for Library of Congress Collections. TIFF, Revision 6.0. (2023, June 21). https://www.loc.gov/preservation/digital/formats/fdd/fdd000022.shtml 

[^2]: Sustainability of digital formats: Planning for Library of Congress Collections. PDF/A Family, PDF for Long-term Preservation. (2020, December 31). https://www.loc.gov/preservation/digital/formats/fdd/fdd000318.shtml 

[^3]: Sustainability of digital formats: Planning for Library of Congress Collections. JPEG 2000 Part 2 (Extensions) jpf (jpx) File Format. (2022, November 22). https://www.loc.gov/preservation/digital/formats/fdd/fdd000154.shtml 

[^4]: Sustainability of digital formats: Planning for Library of Congress Collections. Broadcast WAVE Audio File Format, Version 2. (2024, April 23). https://www.loc.gov/preservation/digital/formats/fdd/fdd000357.shtml 

[^5]: Sustainability of digital formats: Planning for Library of Congress Collections. WAVE Audio File Format with LPCM audio. (2024, April 23). https://www.loc.gov/preservation/digital/formats/fdd/fdd000002.shtml 

[^6]: Sustainability of digital formats: Planning for Library of Congress Collections. FLAC (Free Lossless Audio Codec), Version 1.1.2. (2015, December 21). https://www.loc.gov/preservation/digital/formats/fdd/fdd000198.shtml 

[^7]: Sustainability of digital formats: Planning for Library of Congress Collections. Advanced Audio Coding (MPEG-4). (2022, April 28). https://www.loc.gov/preservation/digital/formats/fdd/fdd000114.shtml 

[^8]: Sustainability of digital formats: Planning for Library of Congress Collections. Matroska File Format with FFV1 video encoding. (2022, April 4). https://www.loc.gov/preservation/digital/formats/fdd/fdd000343.shtml 

[^9]: Sustainability of digital formats: Planning for Library of Congress Collections. Digital Moving-Picture Exchange (DPX), Version 2.0. (2016, December 13). https://www.loc.gov/preservation/digital/formats/fdd/fdd000178.shtml 

[^11]: Sustainability of digital formats: Planning for Library of Congress Collections. OpenEXR. (2023, May 12). https://www.loc.gov/preservation/digital/formats/fdd/fdd000583.shtml 

[^12]: Sustainability of digital formats: Planning for Library of Congress Collections. Apple ProRes 4444 Codec Family. (2020, December 11). https://www.loc.gov/preservation/digital/formats/fdd/fdd000527.shtml 

[^13]: Sustainability of digital formats: Planning for Library of Congress Collections. Apple ProRes 422 High Quality. (2020, November 17). https://www.loc.gov/preservation/digital/formats/fdd/fdd000403.shtml 

[^14]: Sustainability of digital formats: Planning for Library of Congress Collections. Interoperable Master Format (IMF). (2024, January 2). https://www.loc.gov/preservation/digital/formats/fdd/fdd000535.shtml 

[^15]: Sustainability of digital formats: Planning for Library of Congress Collections. MPEG-4, Advanced Video Coding (Part 10) (H.264). (2011, December 5). https://www.loc.gov/preservation/digital/formats/fdd/fdd000081.shtml 

[^16]: Sustainability of digital formats: Planning for Library of Congress Collections. MPEG-2 Video Encoding (H.262). (2011, December 1). https://www.loc.gov/preservation/digital/formats/fdd/fdd000028.shtml 

[^17]: Sustainability of digital formats: Planning for Library of Congress Collections. Digital Cinema Initiative Distribution Package (DCP), Version 1.0. (2022, April 11). https://www.loc.gov/preservation/digital/formats/fdd/fdd000200.shtml 

[^25]: Sustainability of digital formats: Planning for Library of Congress Collections. SubRip Subtitle format (SRT). (2023, March 28). https://www.loc.gov/preservation/digital/formats/fdd/fdd000569.shtml 

[^26]: Sustainability of digital formats: Planning for Library of Congress Collections. Web Archive Collection Zipped. (2023, May 19). https://www.loc.gov/preservation/digital/formats/fdd/fdd000586.shtml 

[^27]: Sustainability of digital formats: Planning for Library of Congress Collections. WARC, Web ARChive file format. (2024, April 29). https://www.loc.gov/preservation/digital/formats/fdd/fdd000236.shtml 

[^28]: Sustainability of digital formats: Planning for Library of Congress Collections. PDF (Portable Document Format) Family. (2023, August 29). https://www.loc.gov/preservation/digital/formats/fdd/fdd000030.shtml

[^29]: Sustainability of digital formats: Planning for Library of Congress Collections. JPEG 2000 Part 1, Core Coding System. (2022, November 22). https://www.loc.gov/preservation/digital/formats/fdd/fdd000138.shtml  

[^30]: Alto: Technical metadata for layout and text objects (standards, Library of Congress). (n.d.). https://www.loc.gov/standards/alto/ 

[^31]: Sustainability of digital formats: Planning for Library of Congress Collections. EPUB (Electronic Publication) File Format Family. (2020, May 12). https://www.loc.gov/preservation/digital/formats/fdd/fdd000310.shtml 

[^32]: Sustainability of digital formats: Planning for Library of Congress Collections. MXF Operational Pattern 1a (OP1a). (2015, December 3). https://www.loc.gov/preservation/digital/formats/fdd/fdd000266.shtml 

[^33]: Sustainability of digital formats: Planning for Library of Congress Collections. JPEG Image Encoding Family. (2022, April 26). https://www.loc.gov/preservation/digital/formats/fdd/fdd000017.shtml 

[^34]: Sustainability of digital formats: Planning for Library of Congress Collections. PNG, Portable Network Graphics. (2022, April 15). https://www.loc.gov/preservation/digital/formats/fdd/fdd000153.shtml 

[^35]: MBWF / RF64: An extended file format for audio (EBU TECH 3306). (n.d.). https://tech.ebu.ch/docs/tech/tech3306v1_1.pdf

[^36]: Sustainability of digital formats: Planning for Library of Congress Collections. AIFF File Format with LPCM Audio. (2010, June 28). https://www.loc.gov/preservation/digital/formats/fdd/fdd000116.shtml 