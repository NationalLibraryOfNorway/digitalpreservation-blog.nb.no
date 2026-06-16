---
title: Images
weight: 1
Draft: false
---

## Example SIP for images
{{< filetree/container >}}
  {{< filetree/folder name="URN_bilde_1" >}}
    {{< filetree/folder name="metadata" state="closed" >}}
		{{< filetree/folder name="descriptive" state="open">}}
  			{{< filetree/file name="MODS.xml" >}}
		{{< /filetree/folder >}}
	{{< /filetree/folder >}}
	{{< filetree/folder name="representations" state="open" >}}
		{{< filetree/folder name="primary_20250325" state="open" >}}
			{{< filetree/file name="METS.xml" >}}
			{{< filetree/folder name="data" state="open" >}}
				{{< filetree/file name="bilde_1.tiff" >}}
			{{< /filetree/folder >}}
			{{< filetree/folder name="metadata" state="closed" >}}
				{{< filetree/folder name="preservation" state="open" >}}
					{{< filetree/file name="events.xml" >}}
				{{< /filetree/folder >}}
				{{< filetree/folder name="technical" state="open" >}}
					{{< filetree/folder name="JHOVE" state="open" >}}
						{{< filetree/file name="JHOVE_bilde_1.tiff.xml" >}}
					{{< /filetree/folder >}}
				{{< /filetree/folder >}}
				{{< filetree/folder name="source" state="open" >}}
					{{< filetree/file name="primus_analog_bærer.xml" >}}
				{{< /filetree/folder >}}
			{{< /filetree/folder >}}
		{{< /filetree/folder >}}
	{{< /filetree/folder >}}
	{{< filetree/folder name="schemas" state="closed" >}}
		{{< filetree/file name="xlink.xsd" >}}
		{{< filetree/file name="mets1_12.xsd" >}}
		{{< filetree/file name="DILCISExtensionSIPMETS.xsd" >}}
		{{< filetree/file name="DILCISExtensionMETS.xsd" >}}
		{{< filetree/file name="MODS.xsd" >}}
	{{< /filetree/folder >}}
	{{< filetree/folder name="documentation" state="closed" >}}
		{{< filetree/file name="manual.txt" >}}
	{{< /filetree/folder >}}
	{{< filetree/file name="METS.xml" >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

## Example SIP for images

{{< figure src="imagesip.nb.svg" caption="Red frames indicate MUST-requirements in the package structure" alt="Red frames indicate MUST-requirements in the package structure" >}}
