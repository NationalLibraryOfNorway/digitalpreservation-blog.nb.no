---
title: Lyd
draft: false
weight: 3
aliases:
  - /docs/dps/sip/examples/audio/
  - /docs/dps/reference/sip/examples/audio/
---

## Eksempel på SIP for lyd


## Normal use-case
{{< filetree/container >}}
  {{< filetree/folder name="no-nb_nrk_RAK202303190100" >}}
    {{< filetree/folder name="metadata" state="closed" >}}
      {{< filetree/folder name="preservation" >}}
        {{< filetree/file name="events.jsonl" >}}
      {{< /filetree/folder >}}
      {{< filetree/folder name="descriptive" >}}
        {{< filetree/file name="MODS.xml" >}}
      {{< /filetree/folder >}}
    {{< /filetree/folder >}}
    {{< filetree/file name="METS.xml" >}}
    {{< filetree/folder name="representations" >}}
      {{< filetree/folder name="primary-001" >}}
        {{< filetree/folder name="data" >}}
          {{< filetree/file name="nrk_RAK202303190100_BWFWAV_48s24.wav" >}}
        {{< /filetree/folder >}}
        {{< filetree/folder name="metadata" state="closed" >}}
          {{< filetree/folder name="other" >}}
            {{< filetree/folder name="Mediainfo" >}}
              {{< filetree/file name="MEDIAINFO_nrk_RAK202303190100_BWFWAV_48s24.wav.json" >}}
              {{< filetree/file name="MEDIAINFO_nrk_RAK202303190100_BWFWAV_48s24.wav.xml" >}}
            {{< /filetree/folder >}}
          {{< /filetree/folder >}}
          {{< filetree/folder name="preservation" >}}
            {{< filetree/file name="events.jsonl" >}}
          {{< /filetree/folder >}}
        {{< /filetree/folder >}}
        {{< filetree/file name="METS.xml" >}}
      {{< /filetree/folder >}}
    {{< /filetree/folder >}}
    {{< filetree/folder name="schemas" state="closed" >}}
      {{< filetree/file name="DILCISExtensionMETS.xsd" >}}
      {{< filetree/file name="DILCISExtensionSIPMETS.xsd" >}}
      {{< filetree/file name="mediainfo_2_0.xsd" >}}
      {{< filetree/file name="mets1_12.xsd" >}}
      {{< filetree/file name="mods-v3-8.xsd" >}}
      {{< filetree/file name="xlink.xsd" >}}
    {{< /filetree/folder >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

### Option: access representation stored alongside primary representation
{{< filetree/container >}}
  {{< filetree/folder name="no-nb_nrk_RAK202303190100" >}}
    {{< filetree/folder name="metadata" state="closed" >}}
      {{< filetree/folder name="preservation" >}}
        {{< filetree/file name="events.jsonl" >}}
      {{< /filetree/folder >}}
      {{< filetree/folder name="descriptive" >}}
        {{< filetree/file name="MODS.xml" >}}
      {{< /filetree/folder >}}
    {{< /filetree/folder >}}
    {{< filetree/file name="METS.xml" >}}
    {{< filetree/folder name="representations" >}}
      {{< filetree/folder name="primary-001" >}}
        {{< filetree/folder name="data" >}}
          {{< filetree/file name="nrk_RAK202303190100_BWFWAV_48s24.wav" >}}
        {{< /filetree/folder >}}
        {{< filetree/folder name="metadata" state="closed" >}}
          {{< filetree/folder name="other" >}}
            {{< filetree/folder name="Mediainfo" >}}
              {{< filetree/file name="MEDIAINFO_nrk_RAK202303190100_BWFWAV_48s24.wav.json" >}}
              {{< filetree/file name="MEDIAINFO_nrk_RAK202303190100_BWFWAV_48s24.wav.xml" >}}
            {{< /filetree/folder >}}
          {{< /filetree/folder >}}
          {{< filetree/folder name="preservation" >}}
            {{< filetree/file name="events.jsonl" >}}
          {{< /filetree/folder >}}
        {{< /filetree/folder >}}
        {{< filetree/file name="METS.xml" >}}
      {{< /filetree/folder >}}
      {{< filetree/folder name="access-001" >}}
        {{< filetree/folder name="data" >}}
          {{< filetree/file name="nrk_RAK202303190100__MPEG2L3_40_16m16.mp3" >}}
        {{< /filetree/folder >}}
        {{< filetree/folder name="metadata" state="closed" >}}
          {{< filetree/folder name="preservation" >}}
            {{< filetree/file name="events.jsonl" >}}
          {{< /filetree/folder >}}
          {{< filetree/folder name="other" >}}
            {{< filetree/folder name="Mediainfo" >}}
              {{< filetree/file name="MEDIAINFO_nrk_RAK202303190100_MPEG2L3_40_16m16.mp3.json" >}}
              {{< filetree/file name="MEDIAINFO_nrk_RAK202303190100_MPEG2L3_40_16m16.mp3.xml" >}}
            {{< /filetree/folder >}}
          {{< /filetree/folder >}}
        {{< /filetree/folder >}}
        {{< filetree/file name="METS.xml" >}}
      {{< /filetree/folder >}}
    {{< /filetree/folder >}}
    {{< filetree/folder name="schemas" state="closed" >}}
      {{< filetree/file name="DILCISExtensionMETS.xsd" >}}
      {{< filetree/file name="DILCISExtensionSIPMETS.xsd" >}}
      {{< filetree/file name="mediainfo_2_0.xsd" >}}
      {{< filetree/file name="mets1_12.xsd" >}}
      {{< filetree/file name="mods-v3-8.xsd" >}}
      {{< filetree/file name="xlink.xsd" >}}
    {{< /filetree/folder >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}


### Eksempel på SIP for lyd: 

{{< filetree/container >}}
  {{< filetree/folder name="URN_lyd_01" >}}
    {{< filetree/file name="METS.xml" >}}
    {{< filetree/folder name="metadata" state="closed" >}}
      {{< filetree/folder name="descriptive" >}}
        {{< filetree/file name="digital_item_axiell_collections_2022113.xml" >}}
      {{< /filetree/folder >}}
    {{< /filetree/folder >}}
    {{< filetree/folder name="representations" >}}
      {{< filetree/folder name="primary_20260706" >}}
        {{< filetree/file name="mets.xml" >}}
        {{< filetree/folder name="data" >}}
          {{< filetree/file name="nb_digilyd_20220905110.waw" >}}
        {{< /filetree/folder >}}
        {{< filetree/folder name="metadata" state="closed" >}}
          {{< filetree/folder name="technical" >}}
            {{< filetree/folder name="audioinspector" >}}
              {{< filetree/file name="nb_digilyd_20220905.xml" >}}
            {{< /filetree/folder >}}
          {{< /filetree/folder >}}
          {{< filetree/folder name="source" >}}
            {{< filetree/file name="anlog_item_axiell_collections_2022114.xml" >}}
          {{< /filetree/folder >}}
        {{< /filetree/folder >}}
      {{< /filetree/folder >}}
    {{< /filetree/folder >}}
    {{< filetree/folder name="schemas" state="closed" >}}
      {{< filetree/file name="DILCISextensionMETS.xsd" >}}
      {{< filetree/file name="DILCISextensionSIPMETS.xsd" >}}
      {{< filetree/file name="mets1.xsd" >}}
      {{< filetree/file name="xlink.xsd" >}}
    {{< /filetree/folder >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

![Eksempel SIP lyd](eksempel_lydpakke.png)

**Forklaring av symboler:**
- **Blå ruter:** Mapper
- **Gule ruter:** Filer
- **Røde rammer:** Viser elementer som er omfattet av MÅ-krav i pakkestrukturen.