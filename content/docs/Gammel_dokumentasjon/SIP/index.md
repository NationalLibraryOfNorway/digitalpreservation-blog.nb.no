---
title: Description of SIP format
draft: true
weight: 1
---
This structure is a "best practice" for structuring SIP. Initially, it's the product teams delivering SIP who should relate to this structure and for whom it should make sense.
DPS does not wish to impose guidelines for the file structure in SIP in the long term, but until we finish the new version of DPS, the checksum files are required. In cases where we don't have packed files (tar packages), we can disregard checksum.md5 after agreement with the Digital Preservation Team.

## Suggested naming for folder structure:
- / (root folder)
    - checksum.md5 (required checksum file if the files being delivered are packed)
    - checksum_transferred.md5 (required checksum file created after packing files)
- access (viewing copies)
    - images (jp2 lossy)
    - sound (mp3/mp4)
    - video (mp4)
- preservation (converted originals for preservation)
    - images (tiff/jp2 lossless)
    - sound (wav files)
    - video/film/moving images (mp4)
    - PDF
- original (original files, legally deposited files)
    - images (jpg)
    - sound (flac)
    - video (mov)
- logs (output from various programs run against the preservation objects. (JHOVE, Mediainfo, VeraPDF, JPlyzer, Transfer file from film scanner?)
    - access
    - meta
    - original
    - preservation
- meta
    - Mets files at page level
    - Metadata file from catalog (-marc.xml)
    - meta (ddex file)
    - ocr (alto files)
    - alto files
    - mets files with structure info from Docworks
- reference (reference material)
    - images
- processed (processed variants of originals, typically for viewing purposes)
    - images (tif)
    - sound (wav)

## Example of file structure
```
no-nb_dagensnaeringsliv_null_null_20230607_134_128_1
├── checksum.md5              <--- In principle required, but exceptions can be made       
├── checksum_transferred.md5  <--- Always required
├── meta
│   └── dagensnaeringsliv_null_null_20230607_134_128_1_meta_xml.tar
├── ocr
│   └── dagensnaeringsliv_null_null_20230607_134_128_1_ocr_xml.tar
├── pdf
│   └── dagensnaeringsliv_null_null_20230607_134_128_1_pdf.tar
└── view
    └── dagensnaeringsliv_null_null_20230607_134_128_1_view_jp2.tar
```

## Checksum files
The checksum file must contain checksums of all files to be delivered. The file paths must be relative to the root level.

See separate wiki page describing how the checksum files can be generated.

## Content of checksum.md5
```
3fb1e6c8d4380ebacdc18cd5bfaa85e6 *pdf/dagensnaeringsliv_null_null_20230607_134_128_1-1_001_hovedavis.pdf
69f0fd05e00aca528ebacd35f7a4c6aa *pdf/dagensnaeringsliv_null_null_20230607_134_128_1-1_002_hovedavis.pdf
2dedca9dc33a0ce8958d393e30d37a8e *pdf/dagensnaeringsliv_null_null_20230607_134_128_1-1_003_hovedavis.pdf
a3f52040a22968915d0be3bcbe015472 *pdf/dagensnaeringsliv_null_null_20230607_134_128_1-1_004_hovedavis.pdf
711f47072f852ad2a99d71720741fb55 *pdf/dagensnaeringsliv_null_null_20230607_134_128_1-1_005_hovedavis.pdf
8fd80ed5197871c07896d46bbd159632 *pdf/dagensnaeringsliv_null_null_20230607_134_128_1-1_006_hovedavis.pdf
6a4afc71965c29bb6ad57319915560bf *pdf/dagensnaeringsliv_null_null_20230607_134_128_1-1_007_hovedavis.pdf
939f0d17a9e537a82eeebcdf7330a891 *pdf/dagensnaeringsliv_null_null_20230607_134_128_1-1_008_hovedavis.pdf
6a94209252d4e293813f71710db9e068 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_001_hovedavis.jp2.xml
316df33033899d189445db203218a462 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_001_hovedavis.pdf.xml
64f0af8bb96efa3e369cf863d2060c5f *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_001_hovedavis.tif.xml
428384f9c0ee3cd7992cc46d513dac5a *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_001_hovedavis.xml.xml
36667dc4e887c4dc67ba6865373c48ea *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_002_hovedavis.jp2.xml
ae7452f373a70f88c748f1feb1d75604 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_002_hovedavis.pdf.xml
a690a9ab8d8538c38c33f1ea28fbbe9b *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_002_hovedavis.tif.xml
a8d7b33d2f59538d983f6943986e32c7 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_002_hovedavis.xml.xml
8de12113b6d59317b0e5e01f0342fc9f *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_003_hovedavis.jp2.xml
25d3967be1f8b5da073f0c206673d219 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_003_hovedavis.pdf.xml
e143ef8329a33e6d2217ac205551ca5a *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_003_hovedavis.tif.xml
7d143ce4063de870da0401cd2ead83c8 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_003_hovedavis.xml.xml
c235e53c7303aaefebb9a25bb420d92a *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_004_hovedavis.jp2.xml
d89a6d495d3fafff5f4542d1aba7415f *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_004_hovedavis.pdf.xml
3327005afb39890baae8d4223c2d2a42 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_004_hovedavis.tif.xml
cd2d2399d67593a1c33f22274faca9b6 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_004_hovedavis.xml.xml
1ca0a3cb61d1ef8979bb528b543d04bc *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_005_hovedavis.jp2.xml
c18732d90d13ff956a04199e9a2e6dd7 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_005_hovedavis.pdf.xml
f6ec1f47094e4569c7d8bbfa06e3cac8 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_005_hovedavis.tif.xml
abda8acdab35242c3d43768806e6fb63 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_005_hovedavis.xml.xml
6cc58f7353fc9758942d0894586d615f *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_006_hovedavis.jp2.xml
8a007826f13673dddc6d409326d4d765 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_006_hovedavis.pdf.xml
f1e700e19cc065ef75e06098f59e2746 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_006_hovedavis.tif.xml
0c50ee47e398a653e62f08725cfd0709 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_006_hovedavis.xml.xml
30cd48a1ad580b1c4a9609cb20c7251b *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_007_hovedavis.jp2.xml
119f686f83d4eff63a0be7930aedbf29 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_007_hovedavis.pdf.xml
17577e1926c3d431eff267a0455706d2 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_007_hovedavis.tif.xml
e3bb011f89ca7f2b0e4d7998add9031b *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_007_hovedavis.xml.xml
8feb8b1e4bf919d63ebe856ab43e1dfc *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_008_hovedavis.jp2.xml
e63d5c8329fb6ca7f727cab6a69e5484 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_008_hovedavis.pdf.xml
9f9b1bb2bd9204798e4e589ec74fe8f0 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_008_hovedavis.tif.xml
31411827c0b9455403e88a19ae783a84 *meta/JHOVE_dagensnaeringsliv_null_null_20230607_134_128_1-1_008_hovedavis.xml.xml
831f7bc4de22f406e33276c6ba5ef3c3 *meta/MAVIS_dagensnaeringsliv_null_null_20230607_134_128_1.xml
aafa01f48c701aa0a48c5b815a0e7ef7 *meta/MAVIS_yearTitle_dagensnaeringsliv_null_null_20230607_134_128_1.xml
7b4d09574f1cdbda1028d8831462a0e3 *meta/METS_dagensnaeringsliv_null_null_20230607_134_128_1-1_001_hovedavis.xml
583813010f2975c76e2b1db992f815c9 *meta/METS_dagensnaeringsliv_null_null_20230607_134_128_1-1_002_hovedavis.xml
901031db6f040fdba5bbf30b9b870367 *meta/METS_dagensnaeringsliv_null_null_20230607_134_128_1-1_003_hovedavis.xml
9a02d3660c722d1411fa29f47b17a33b *meta/METS_dagensnaeringsliv_null_null_20230607_134_128_1-1_004_hovedavis.xml
26148822bdf562ccfb9803edf6f48909 *meta/METS_dagensnaeringsliv_null_null_20230607_134_128_1-1_005_hovedavis.xml
b5891a4e66a935813307786c14387126 *meta/METS_dagensnaeringsliv_null_null_20230607_134_128_1-1_006_hovedavis.xml
443f5f07fe347d958f844b2249d835bf *meta/METS_dagensnaeringsliv_null_null_20230607_134_128_1-1_007_hovedavis.xml
6dac7b0fb7e8be98f2a49be862e294cd *meta/METS_dagensnaeringsliv_null_null_20230607_134_128_1-1_008_hovedavis.xml
74371855eea47b81144cf41841662407 *ocr/dagensnaeringsliv_null_null_20230607_134_128_1-1_001_hovedavis.xml
f30b8e0ef83b54cc34106d64f691f482 *ocr/dagensnaeringsliv_null_null_20230607_134_128_1-1_002_hovedavis.xml
4dbeb8c94736ba8329494d95298cee12 *ocr/dagensnaeringsliv_null_null_20230607_134_128_1-1_003_hovedavis.xml
93122df56e8e7440ce9c259099684a0f *ocr/dagensnaeringsliv_null_null_20230607_134_128_1-1_004_hovedavis.xml
30abf7793493b7186463448fee76bfce *ocr/dagensnaeringsliv_null_null_20230607_134_128_1-1_005_hovedavis.xml
7bb77e1c060b5c26db40cfcdf2f90858 *ocr/dagensnaeringsliv_null_null_20230607_134_128_1-1_006_hovedavis.xml
44c2f38dad1239d1da75fd686ec96712 *ocr/dagensnaeringsliv_null_null_20230607_134_128_1-1_007_hovedavis.xml
aebe64b779cd9ff4aeebccec775480b4 *ocr/dagensnaeringsliv_null_null_20230607_134_128_1-1_008_hovedavis.xml
```



## Content of checksum_transferred.md5
NOTE: Note that we want to include checksum.md5 here
```
ffff5ab4c72e87589ed7cd10a5e6a6a5 *meta/dagensnaeringsliv_null_null_20230607_134_128_1_meta_xml.tar
0c1af21bf8ec7883f1347f72b95fc4d7 *ocr/dagensnaeringsliv_null_null_20230607_134_128_1_ocr_xml.tar
ae4ab3e5ba01d84c44cd3c91ed4b6962 *pdf/dagensnaeringsliv_null_null_20230607_134_128_1_pdf.tar
a593473d499d3f62d646b10230a1438e *view/dagensnaeringsliv_null_null_20230607_134_128_1_view_jp2.tar
e31bfe7c4aaa5019ae11353d606885b9 *checksum.md5
``

