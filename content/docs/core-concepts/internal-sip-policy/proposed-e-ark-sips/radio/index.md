---
title: Legal deposit radio (timespan)
weight: 1
draft: true
---

## Normal use-case
```
no-nb_nrk_RAK202303190100
├── metadata
│   ├── preservation 
│   │   └── events.jsonl
│   └── descriptive
│       └── MODS.xml
├── METS.xml
├── representations
│   └── primary-001
│       ├── data
│       │   └── nrk_RAK202303190100_BWFWAV_48s24.wav
│       ├── metadata
│       │   ├── other
│       │   │   └── Mediainfo
│       │   │       ├── MEDIAINFO_nrk_RAK202303190100_BWFWAV_48s24.wav.json
│       │   │       └── MEDIAINFO_nrk_RAK202303190100_BWFWAV_48s24.wav.xml
│       │   └── preservation
│       │       └── events.jsonl
│       └── METS.xml
└── schemas
    ├── DILCISExtensionMETS.xsd
    ├── DILCISExtensionSIPMETS.xsd
    ├── mediainfo_2_0.xsd
    ├── mets1_12.xsd
    ├── mods-v3-8.xsd
    └── xlink.xsd
```

### Option: access representation stored alongside primary representation
```
no-nb_nrk_RAK202303190100
├── metadata
│   ├── preservation 
│   │   └── events.jsonl
│   └── descriptive
│       └── MODS.xml
├── METS.xml
├── representations
│   ├── primary-001
│   │   ├── data
│   │   │   └── nrk_RAK202303190100_BWFWAV_48s24.wav
│   │   ├── metadata
│   │   │   ├── other
│   │   │   │   └── Mediainfo
│   │   │   │       ├── MEDIAINFO_nrk_RAK202303190100_BWFWAV_48s24.wav.json
│   │   │   │       └── MEDIAINFO_nrk_RAK202303190100_BWFWAV_48s24.wav.xml
│   │   │   └── preservation
│   │   │       └── events.jsonl
│   │   └── METS.xml
│   └── access-001
│       ├── data
│       │   └── nrk_RAK202303190100__MPEG2L3_40_16m16.mp3
│       ├── metadata
│       │   ├── preservation 
│       │   │   └── events.jsonl
│       │   ├── other
│       │   │   └── Mediainfo
│       │   │       ├── MEDIAINFO_nrk_RAK202303190100_MPEG2L3_40_16m16.mp3.json
│       │   │       └── MEDIAINFO_nrk_RAK202303190100_MPEG2L3_40_16m16.mp3.xml
│       └── METS.xml
└── schemas
    ├── DILCISExtensionMETS.xsd
    ├── DILCISExtensionSIPMETS.xsd
    ├── mediainfo_2_0.xsd
    ├── mets1_12.xsd
    ├── mods-v3-8.xsd
    └── xlink.xsd
```



