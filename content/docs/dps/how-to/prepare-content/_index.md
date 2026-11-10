---
title: Prepare content for submission
weight: 1
---

This guide shows how to package content as a Submission Information Package (SIP) that DPS accepts. Each step links to the requirements it covers; the requirement pages are normative, and this guide does not repeat them. What a package contains, and why, is explained in [Information packages](/docs/dps/understanding/information-packages/).

## Before you start

- **The content files**, preferably in one of the [preferred file formats](/docs/policies/formats/).
- **Descriptive metadata** for the content, for example an export of a catalogue record.
- **An identifier for the package.** It is used as the name of the package's root folder.
- **The media type** of the content: images, audio, moving images, text, web archive, or datasets. Each has its own [METS.xml requirements](/docs/dps/reference/sip/mets/).

## Steps

{{% steps %}}

### Decide the scope of the package

A package describes exactly one intellectual entity ([NBSIPSTR1](/docs/dps/reference/sip/structure-requirements/#:~:text=NBSIPSTR1)). We recommend limiting a package to one particular digital exemplar, such as one scan of a photograph or one digitization of a book. A technical variant of the same exemplar, such as a derived access format, is a new representation in the same package, not a new package. See [New package or new representation?](/docs/dps/understanding/information-packages/#new-package-or-new-representation)

### Create the folder structure

Create a root folder named after the package identifier, using only the letters `A–Z`, `a–z`, digits, `-` and `_`. The same identifier is used as `@OBJID` in the root `METS.xml` ([NBSIPSTR2](/docs/dps/reference/sip/structure-requirements/#:~:text=NBSIPSTR2)). Give it this structure:

```text
<package identifier>/
├── METS.xml
├── metadata/
│   └── descriptive/
├── representations/
│   └── primary_YYYYMMDD/
│       ├── METS.xml
│       ├── data/
│       └── metadata/
└── schemas/
```

The package may only contain folders that the requirements permit ([NBSIPSTR20](/docs/dps/reference/sip/structure-requirements/#:~:text=NBSIPSTR20)). The [anatomy of a package](/docs/dps/understanding/information-packages/#what-a-package-contains) explains what each folder is for.

### Add the content files

Put the content files in `representations/primary_YYYYMMDD/data/` ([NBSIPSTR11](/docs/dps/reference/sip/structure-requirements/#:~:text=NBSIPSTR11), [NBSIPSTR13](/docs/dps/reference/sip/structure-requirements/#:~:text=NBSIPSTR13)), where `YYYYMMDD` is the date the folder was created. If the package has more than one representation, give each additional representation its own folder, named with a meaningful name and the date, for example `processed_20251214` ([NBSIPSTR12](/docs/dps/reference/sip/structure-requirements/#:~:text=NBSIPSTR12)).

### Add the metadata files

Put at least one file with descriptive metadata in `metadata/descriptive/` ([NBSIPSTR9](/docs/dps/reference/sip/structure-requirements/#:~:text=NBSIPSTR9)). Add source, technical, and preservation metadata to the representation they belong to. [Metadata placement at a glance](/docs/dps/reference/sip/structure-requirements/#metadata-placement-at-a-glance) shows where each kind goes.

Preservation events, such as digitization or validation, are better submitted through the API than as files. See [Add preservation events](/docs/dps/how-to/add-preservation-events/).

### Add schemas and documentation

Put all XML schemas for the structured metadata in the package in `schemas/` ([NBSIPSTR18](/docs/dps/reference/sip/structure-requirements/#:~:text=NBSIPSTR18)). If additional documentation is needed to make use of the content, add it in `documentation/` ([NBSIPSTR19](/docs/dps/reference/sip/structure-requirements/#:~:text=NBSIPSTR19)).

### Write the METS files

Write a `METS.xml` in the root folder ([NBSIPSTR4](/docs/dps/reference/sip/structure-requirements/#:~:text=NBSIPSTR4)) and one in each representation folder ([NBSIPSTR14](/docs/dps/reference/sip/structure-requirements/#:~:text=NBSIPSTR14)). They must meet the [METS.xml requirements](/docs/dps/reference/sip/mets/) and the additional requirements for your media type, which include the content category and the profile to declare.

The National Library's [DPS E-ARK SIP Generator](https://github.com/NationalLibraryOfNorway/dps-eark-generator) can generate the METS files and add the XML schemas from a folder structure like the one above. It is built on [commons-ip](https://github.com/keeps/commons-ip), an open-source library and command-line tool for creating and validating E-ARK information packages. Check that the result meets the media type requirements, such as the declared profile.

### Calculate checksums

Calculate an MD5 checksum for every file in the package. You register each file with its checksum when you submit, and DPS verifies the checksums on ingest. Verify the checksums again just before you submit, to make sure the files have not changed.

### Check the package

Check the package against the requirements before you submit it. [commons-ip](https://github.com/keeps/commons-ip) and the `validate` action in the [DPS E-ARK SIP Generator](https://github.com/NationalLibraryOfNorway/dps-eark-generator) check the package against the E-ARK specifications, but not against the National Library's additional requirements. DPS validates the package against both the E-ARK and the National Library's requirements after it has been transferred; if it does not meet them, the submission is rejected with a list of reasons.

{{% /steps %}}

## Next steps

- [Submit content for preservation](/docs/dps/how-to/submit-content/) through the API.
- See the [examples](/docs/dps/reference/sip/examples/) of complete packages for different media types.
