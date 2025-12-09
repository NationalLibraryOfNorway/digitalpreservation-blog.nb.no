---
title: Preferred file formats
description: "List of preferred file formats for digital preservation at the National Library of Norway"
weight: 6
date: 2024-05-07
draft: false
tags: [Policy, File formats]
authors: 
  - name: Digital Preservation Team
    image: /images/NB-svart.png
aliases: ["/docs/formats/2024-05-07-formats-in-use-en", "/docs/formats/preferred-formats-en"]
---

This list outlines the preferred file formats for preservation at the National Library of Norway. The recommendations have been developed by the respective media departments, while the list itself is maintained by the digital preservation team.

It includes both files produced by the National Library and those acquired from external sources. *Preferred formats* are those considered most suitable for preservation, while *acceptable formats* also can be used without the need for conversion/normalization. Any other file formats should be discussed with the relevant media departments prior to acceptance.

The list is inspired by [Open Preservation Foundation's (OPF)](https://openpreservation.org) list 
["International Comparison of Recommended File Formats"](https://docs.google.com/spreadsheets/d/1XjEjFBCGF3N1spNZc1y0DG8_Uyw18uG2j8V2bsQdYjk/edit#gid=1719869262) 
and the Library of Congress's overviews ["Sustainability of Digital Formats: Planning for Library of Congress Collections"](https://www.loc.gov/preservation/digital/formats/fdd/descriptions.shtml) 
and ["Recommended Formats Statement"](https://www.loc.gov/preservation/resources/rfs/index.html).

---

## Images

|  <div style="width:255px">Purpose</div> | Preferred formats                                     | Acceptable formats                              |
| --------------------------------------- | ----------------------------------------------------- | ----------------------------------------------- |
| Digitized images                        | <ul><li>TIFF (Tagged Image File Format), revision 6 [^1]  |                                                 |
| Posters                                 | <ul><li>PDF/A Family, PDF for Long-term Preservation [^2] | <ul><li>PDF (Portable Document Format) Family [^28] |
| Access copies                           | <ul><li>JPEG 2000 Part 2 (Extensions) jpf (jpx) [^3]      |                                                 |


## Moving images
| <div style="width:255px">Purpose</div>                    | Preferred formats                                                                                                                                                                                                                                                                                                              | Acceptable formats                                                                                                                  |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| Film masters and digitization                             | <ul><li>Matroska/FFV1/PCM (Matroska File Format with FFV1 video encoding) [^8]<li>DPX (Digital Moving-Picture Exchange), Version 2.0 [^9] <li> TIFF sequence [^1]<li>MPEG-4, Advanced Video Coding (Part 10) (H.264)/PCM (lossless, uncompressed mezzanine) [^15] <li> OpenEXR [^11] <li> Apple Prores4444/mov [^12]<li> DNxHR444  | <ul><li>Apple ProRes 422 High Quality/mov [^13]<li> DNxHR HQX/HQ                                                                        |
| TV (master), VOD, home video and access                   | <ul><li>Interoperable Master Format (IMF) [^14]<li>MXF/XDCAM<li>MXF OP1a [^32]                                                                                                                                                                                                                                                     | <ul><li>MPEG-4, Advanced Video Coding (Part 10) (H.264) [^15]<li> MPEG-2 Video Encoding (H.262) [^16] (50Mbit/s, Inter-frame encoded)|
| Film distribution (cinema)                                | <ul><li>DCP, Version 1.0 (Digital Cinema Initiative Distribution Package) [^17] (unencrypted)<li> IMF (Interoperable Master Format) [^14]  (unencrypted)                                                                                                                                                                               |                                                                                                                                     |
| Digitized video                                           | <ul><li>Matroska/FFV1/PCM [^8]                                                                                                                                                                                                                                                                                                     |                                                                                                                                     |
| Film sound (final mix/audio master)                       | <ul><li>BWF (Broadcast WAVE Audio File Format), Version 2 [^4]<li>WAVE Audio File Format with LPCM audio [^5]<li>FLAC (Free Lossless Audio Codec), Version 1.1.2 [^6]                                                                                                                                                              |                                                                                                                                     |
| Subtitles                                                 | <ul><li>SRT (SubRip Subtitle format) [^25]<li> PAC (Presentation Audio/Video Coding)<li> XML                                                                                                                                                                                                                                       |                                                                                                                                     |


## Sound
| <div style="width:255px">Purpose</div>                                                                                                   | Preferred formats                                                                                                                                               | Acceptable formats                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Masters and sound digitization<br><ul><li>Minimum bit depth: 16 bit <li>Recommended bit depth: 24 bit <li>Minimum sample rate: 44100 Hz | <ul><li>BWF (Broadcast WAVE Audio File Format), Version 2 [^4]<li>WAVE Audio File Format with LPCM audio [^5]<li>MBWF/RF64 (Multichannel BWF) [EBU TECH 3306] [^35] | <ul><li>FLAC (Free Lossless Audio Codec), Version 1.1.2 [^6] <li>AIFF LPCM (Audio Interchange File Format with LPCM Audio) [^36] |



## Web archive
| <div style="width:255px">Purpose</div> | Preferred formats                                                                       | Acceptable formats  |
| ---------------------------------------| --------------------------------------------------------------------------------------- | ------------------- |
| Web harvesting                         | <ul><li>WACZ (Web Archive Collection Zipped) [^26]<li>WARC (Web ARChive file format) [^27]  |                     |


## Text
| <div style="width:255px">Purpose</div> | Preferred formats                                                                                                 | Acceptable formats                              |
| ---------------------------------------| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------|
| Scanned text                           | <ul><li>JPEG 2000 Part 1 (Core) jp2 File [^29]                                                                        |                                                 |
| OCR                                    | <ul><li>ALTO XML [^30]                                                                                                |                                                 |
| Digital text                           | <ul><li>PDF/A Family, PDF for Long-term Preservation [^2] <li> EPUB (Electronic Publication) File Format Family [^31] | <ul><li>PDF (Portable Document Format) Family [^28] |
| Access copies                          | <ul><li>JPEG 2000 Part 2 (Extensions) jpf (jpx) [^3]                                                                  |                                                 |
| Cover page images                      | <ul><li>JPEG Image Encoding Family [^33] <li> PNG (Portable Network Graphics) [^34]                                   |                                                 |


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