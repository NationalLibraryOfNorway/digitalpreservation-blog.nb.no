---
title: Metadata Requirements
weight: 1
---



In addition to requiring a metadata file within the Submission Information Packages (SIPs), the National Library of Norway also requires a set of metadata submitted via the submission API. 
This ensures that a minimum level of metadata associated with the submitted representations is indexed and made searchable.

The metadata requirements are based on [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/), an international ISO standard widely used in archives, libraries, and digital collections. 
Dublin Core was chosen because it is relatively easy to understand, simple to implement, and both flexible and extensible. 
To make the metadata more structured, the standard are supplemented with attributes.

Most metadata elements are optional, but it is strongly recommended to provide as complete metadata as possible. This enhances searchability and improves the long-term understanding and usability of the resources.

## General Guidelines for the Use of Standards
- Punctuation and character encoding for field input should follow [UTF-8](https://snl.no/UTF-8).
- [ISO 639-3](https://www.iso.org/obp/ui/#iso:std:iso:639:-3:ed-1:v1:en) is used as the standard for specifying language when the lang attribute is applied.
- [ISO 8601-2](https://www.iso.org/obp/ui/en/#iso:std:iso:8601:-2:ed-1:v1:en) is used as the standard format for specifying dates and times.
- [ISO 3166-2](https://www.iso.org/obp/ui/en/#iso:std:iso:3166:-1:ed-4:v1:en) is used to specify country codes.

## Metadataelements

### Type


| Name        | **Type**                                                                                                         |
|:------------|:-----------------------------------------------------------------------------------------------------------------|
| Description | Form/genre of the resource. The National Library uses its own Norwegian controlled vocabulary for allowed types. |
| Requirement | MUST                                                                                                             |
| Cardinality | 1..1                                                                                                             | 

**Guidelines for Use:**

Allowed types for describing the resource per media type: 

- **Text:** `Bok`, `Avis`, `Tidsskrift`, `Artikkel`, `Småtrykk`, `Brev`, `Epost`, `Manuskript`, `Musikkmanuskript`, `Noter`, `Programrapport`, `Programstatistikk`. 
- **Images:** `Bilde`, `Kart`, `Plakat`, `Postkort`, `Referansemateriale`. 
- **Audio:** ``Lydbok``, ``Musikk``, ``Radio``.
- **Moving images:** `Film`, `Fjernsyn`.

The vocabulary is limited to Norwegian values.

In the requirements for [METS.xml](/nb/docs/dps/sip/1.0/mets/) there is a mandatory attribute named Content category `@TYPE`. Content category specifies the media type on a higher level than this attribute.

> [!TIP]
> We would like input and suggestions for any missing terms in this vocabulary. It is possible to request the addition of new types if needed.

**Example:**
```json
{
  "type": "Bilde"
}
``` 

### Identifier

| Name        | **Identifier**                                                                                                              |
|:------------|:----------------------------------------------------------------------------------------------------------------------------|
| Description | Identifiers (identifier type + ID/value).<br> The `type` and `value` attributes MUST be used to define the identifier type. |
| Requirement | MUST                                                                                                                        |
| Cardinality | 1..n                                                                                                                        |

**Guidelines for Use:**

The identifier type MUST be defined. 
The use of the type attribute should be meaningful to the submitter, reflect the metadata catalog or system, and be applied consistently (using a standardized format).

Examples of identifier types may include URN, PID, URI to a record in a catalog or metadata system, document ID, issue ID, copy number, ISBN, ISSN, ISMN, ISNI, DOI, record label, etc.

**Examples:**
```json
{
  "identifier": [
    {
      "type": "URN",
      "value": "URN:NBN:no-nb_digifoto_20220311_00191_NB_PE_VM_M_05_09_01_036"
    },
    {
      "type": "image-id",
      "value": "NB_PE_VM_M_05_09_01_036"
    },
    {
      "type": "call-number",
      "value": "POEL00003975"
    }
  ]
}
```

### Title

| Name        | **Title**                                                                                                                                                                                                  |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | Name given to the resource. If a title is missing, the recommended practice is to assign the resource a “meaningful” title. <br> The `lang` attribute SHOULD be used to specify the language of the title. |
| Requirement | MUST                                                                                                                                                                                                       |
| Cardinality | 1..1                                                                                                                                                                                                       |

**Guidelines for Use:**

Every package MUST have a title.

Some resources already have predefined titles, such as books, journals, articles, painted works, artistic photographs, etc. 
When a title is missing, the recommended practice is to devise a “meaningful” title for the resource. 
By meaningful, we mean a title that facilitates recognition and identification of the resource, essentially, a name that makes sense to the submitter.

The language of the title should be specified according to the [ISO 639-3](https://www.iso.org/obp/ui/#iso:std:iso:639:-3:ed-1:v1:en) standard, using the `lang` attribute is applied.
 
**Examples:**
```json
{
  "title": {
    "value": "Ola and Kari on a fishing trip in Rondane",
    "lang": "eng"
  }
}
```
```json
{
  "title": {
    "value": "Photographic negative from June 1972 [image 394]",
    "lang": "eng"
  }
}
```
```json
{
  "title": {
    "value": "20131007.jpg"
  }
}
```

### Alternative

| Name        | **Alternative**                                                                                                                                                                               |
|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | Alternative Title (original title, subtitle, etc.) <br>The `type` attribute MUST be used to specify the type of title. <br> The `lang` attribute SHOULD be used to specify the language code. |
| Requirement | SHOULD                                                                                                                                                                                        |
| Cardinality | 0..n                                                                                                                                                                                          |

**Guidelines for Use:**

This attribute allows the resource to be given multiple titles. For example titles on different languages, working titles, etc.

To improve searchability by title, it is recommended to add an alternative title when the original title contains numbers and/or special characters, or when numbers are originally written out as words. 

The alternative titles MUST have a type, to describe what kind of title is submitted.
The use of the type attribute should be meaningful to the submitter, reflect the metadata catalog or system, and be applied consistently (using a standardized format).

The language of the title should be specified according to the [ISO 639-3](https://www.iso.org/obp/ui/#iso:std:iso:639:-3:ed-1:v1:en) standard, using the `lang` attribute is applied.

**Example:**
```json
{
  "alternative": [
    {
      "type": "original title",
      "value": "Ola and Kari on fishing trip in Rondane",
      "lang": "eng"
    }
  ]
}
```

### Creator

| Name        | **Creator**                                                                                                                                                                                                                                                                                                                                                                                                      |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | Name or entity appearing in a central role (e.g. author, composer, film director, photographer, etc.). <br>The`role` attribute SHOULD be used to define the specific role. <br>The `type` attribute SHOULD be used to indicate the type of entity. Allowed types include: `person`, `korporasjon`, `konferanse`, `standardtittel`. <br>The `authority` attribute SHOULD be used to specify the authority source. |
| Requirement | SHOULD                                                                                                                                                                                                                                                                                                                                                                                                           |
| Cardinality | 0..n                                                                                                                                                                                                                                                                                                                                                                                                             |

**Guidelines for use:**

The use of an authority register is recommended whenever one is available, both for personal names and corporate entities. 
The specific authority register used must be identified. 
An example of such a register is the  [Shared Authority Register for Persons and Corporate Bodies](https://bibliotekutvikling.no/kunnskapsorganisering/vokabularer-utkast/felles-autoritetsregister-for-personer-og-korporasjoner/).

The creator should also be identified using their full name (first name, last name/corporation). 
Birth and death years may be included in parentheses after the name. 
Examples: 
*Nesbø, Jo (1960– )*, *Shakespeare, William (1564–1616)*. 

It should be specified whether the name refers to a person or a corporation. 
This is handled in different ways across various metadata catalogs and authority registers. 
The vocabulary is Norwegian. 
Currently, the following values are allowed to define the type of name or entity though additional types may be added if needed: 

- `person`
- `korporasjon` (organization)
- `konferanse` (conferance)
- `standardtittel` (uniform title. e.g., treaty, contract)

The role of the person or organization should be specified. 
Examples of roles include: 
author, composer, film director, photographer, creator, etc. 

The use of the role attribute should be meaningful for the data provider, reflect the metadata catalog or system being used, and follow consistent (standardized) formatting.

Explanation of *authority* information:
- `source`: The name of the authority file from which the value is taken, provided as a plain text string.
- `code`: A unique identifier for the authority entry within the register, typically a numeric or alphanumeric code.
- `URI`: A persistent link (URI) that points directly to the authority record from which the value is derived.


**Examples:**
```json
{
  "creator": [
    {
      "name": "Marek, Václav (1908-1994)",
      "type": "Person",
      "role": "Photographer",
      "authority": {
        "source": "Felles autoritetsregister (BARE)",
        "code": "90169632",
        "uri": "https://bibsys-almaprimo.hosted.exlibrisgroup.com/permalink/f/nelpa2/AUTREG90169632"
      }
    }
  ]
}
```
```json
{
  "creator": [
    {
      "name": "Shakespeare, William (1564-1616)",
      "type": "Person",
      "role": "author",
      "authority": {
        "source": "Felles autoritetsregister (BARE)",
        "code": "9016555",
        "uri": "https://bibsys-almaprimo.hosted.exlibrisgroup.com/permalink/f/nelpa2/AUTREG9016555"
      }
    }
  ]
}
```

### Contributor

| Name        | **Contributor**                                                                                                                                                                                                                                                                                                                                                                                                  |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | Names appearing in a central role (e.g., illustrator, photographer, co-author). <br>The `role` attribute SHOULD be used to specify the person's or organization's role. <br>The `type` attribute SHOULD be used to indicate the type of authority. Allowed types include: `person`, `korporasjon`, `konferanse`, `standardtittel`. <br>The `authority` attribute SHOULD be used to specify the authority source. |
| Requirement | SHOULD                                                                                                                                                                                                                                                                                                                                                                                                           |
| Cardinality | 0..n                                                                                                                                                                                                                                                                                                                                                                                                             |

**Guidelines for Use:**
  
The use of an authority register is recommended whenever one is available, both for personal names and corporate entities. 
The specific authority register used must be identified. 
An example of such a register is the  [Shared Authority Register for Persons and Corporate Bodies](https://bibliotekutvikling.no/kunnskapsorganisering/vokabularer-utkast/felles-autoritetsregister-for-personer-og-korporasjoner/).

The contributor should also be identified using their full name (first name, last name/corporation). 
Birth and death years may be included in parentheses after the name. 
Examples: 
*Nesbø, Jo (1960– )*, *Shakespeare, William (1564–1616)*. 

It should be specified whether the name refers to a person or a corporation. 
This is handled in different ways across various metadata catalogs and authority registers. 
The vocabulary is Norwegian. 
Currently, the following values are allowed to define the type of name or entity though additional types may be added if needed: 

- `person`
- `korporasjon` (organization)
- `konferanse` (conferance)
- `standardtittel` (uniform title. e.g., treaty, contract)

The role of the person or organization should be specified. 
Examples of roles include: 
contributor, depicted person, illustrator, model, editor, designer, etc.

The use of the role attribute should be meaningful for the data provider, reflect the metadata catalog or system being used, and follow consistent (standardized) formatting.

Explanation of *authority* information:
- `source`: The name of the authority file from which the value is taken, provided as a plain text string.
- `code`: A unique identifier for the authority entry within the register, typically a numeric or alphanumeric code.
- `URI`: A persistent link (URI) that points directly to the authority record from which the value is derived.


**Examples:**
```json
{
  "contributor": [
    {
      "role": "depicted",
      "type": "Person",
      "name": "Nordmann, Ola"
    },
    {
      "role": "depicted",
      "name": "Nordmann, Kari"
    }
  ]
}
```

```json
{
  "contributor": [
    {
      "role": "illustrator",
      "type": "Person",
      "name": "Solberg, Erna",
      "authority": {
        "source": "Kulturnav",
        "code": "e762d909-5cce-4d2b-892b-258272514fde",
        "uri": "https://kulturnav.org/e762d909-5cce-4d2b-892b-258272514fde"
      }
    }
  ]
}
```

### Publisher

| Name        | **Publisher**                                                                                                                                                                                                                                                                                                           |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | Names appearing in a central role (the entity that has published the resource). <br> The `type` attribute SHOULD be used to define the type of authority. Allowed types include: `person`, `korporasjon`, `konferanse`, `standardtittel`. <br>The `authority` attribute SHOULD be used to specify the authority source. |
| Requirement | SHOULD                                                                                                                                                                                                                                                                                                                  |
| Cardinality | 0..n                                                                                                                                                                                                                                                                                                                    |

**Guidelines for use:**

It is recommended to use an authority register whenever one is available. 
The specific authority register used, as well as the type of authority, MUST be indicated. 
Allowed types include: 

- `Person`
- `Korporasjon` (Organization)
- `Konferanse` (conference)
- `Standardtittel`  (uniform title  e.g., treaty, contract).

When using an authority register, the publisher’s full name should also be provided. 
The place and/or year of publication can be added in parentheses after the name. 
Example: 
National Library (Oslo, 1984).

Explanation of *authority* information:
- `source`: The name of the authority file from which the value is taken, provided as a plain text string.
- `code`: A unique identifier for the authority entry within the register, typically a numeric or alphanumeric code.
- `URI`: A persistent link (URI) that points directly to the authority record from which the value is derived.

**Example:**
```json
{
  "publisher": [
    {
      "name": "National library of Norway (Oslo, 1984)",
      "type": "Korporasjon",
      "authority": {
        "source": "Felles autoritetsregister (BARE)",
        "code": "90362181",
        "uri": "https://bibsys-almaprimo.hosted.exlibrisgroup.com/permalink/f/nelpa2/AUTREG90362181"
      }
    }
  ]
}
```

### Spatial

| Name        | **Spatial**                                                                                                                                                                                                                                                                                                                                        |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | Names of relevant geographic locations (place names). These may refer to geographic locations such as countries, regions or cities that are significant to the resource. <br> The `type` attribute SHOULD be used to specify what type of place is being referred to.<br>The `authority` attribute SHOULD be used to specify the authority source. |
| Requirement | SHOULD                                                                                                                                                                                                                                                                                                                                             |
| Cardinality | 0..n                                                                                                                                                                                                                                                                                                                                               |

**Guidelines for use:**

- Use [ISO 3166-2](https://www.iso.org/obp/ui/en/#iso:std:iso:3166:-1:ed-4:v1:en) for specifying countries. Country codes should be placed in parentheses after the country name (e.g., Norway (NO)). 

It is recommended to use official place name services or registries for specifying Norwegian place names. 
One example is the  [Central Place Name Register (SSR)](https://www.kartverket.no/api-og-data/stedsnavndata) provided by the Norwegian Mapping Authority (Kartverket). 
The source registry MUST be specified. 

When using authority registries to specify spatial information, the full form of the place name should also be included. 
If no registry is used, the location should preferably be written in the following format: 
country; region/county; municipality; place; street.
 
Coordinates may be provided using latitude and longitude. 
The format should be as follows: 
`latitude`=61.85401 `longitude`=9.80856.

Examples of `type` might include place of publication, recording location, setting, place of printing, place of birth, etc. 
The use of the `type` attribute should be meaningful for the data provider, reflect the metadata catalog or system, and follow a consistent and standardized format.

Explanation of *authority* information:
- `source`: The name of the authority file from which the value is taken, provided as a plain text string.
- `code`: A unique identifier for the authority entry within the register, typically a numeric or alphanumeric code.
- `URI`: A persistent link (URI) that points directly to the authority record from which the value is derived.

**Examples:**
```json
{
  "spatial": [
    {
      "name": "Norway (NO);Innlandet;Stor-Elvdal;Rondane gjestegård",
      "type": "Depicted location",
      "authority": {
        "source": "Kulturnav",
        "code": "1031636c-0717-4d12-8895-fb88a7d4e952",
        "uri": "http://kulturnav.org/1031636c-0717-4d12-8895-fb88a7d4e952"
      },
      "coordinateReferenceSystem": "EPSG:4326",
      "latitude": 61.788453,
      "longitude": 10.224725
    },
    {
      "name": "Norge (NO);Innlandet;Lillehammer;Lillehammer"
    }
  ]
}
```

### Date

| Name        | **Date**                                                                                                                                                                                                                 |
|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | Relevant dates for the resource (such as publication, copyright, creation, digitization date, etc., including the type of date.). <br> The `type` attribute MUST be used to specify what kind of date it is reffered to. |
| Requirement | SHOULD                                                                                                                                                                                                                   |
| Cardinality | 0..n                                                                                                                                                                                                                     |

**Guidelines for Use:**

The type of date and the corresponding year or value must be specified. 
[ISO 8601-2](https://www.iso.org/obp/ui/en/#iso:std:iso:8601:-2:ed-1:v1:en) is the standard to be used.  

The use of the type attribute should be meaningful for the data provider, reflect the metadata catalog or system, and be applied consistently with a standardized format.

**Examples:**
```json
{
  "date": [
    {
      "type": "Content date",
      "value": "1938"
    },
    {
      "type": "Digitized",
      "value": "2022-03-05T14:28:12+02:00"
    },
    {
      "type": "Published",
      "value": "2022-03-12"
    }
  ]
}
```

### Language

| Name        | **Language**                                                                                                                                                                                                                                                                        |
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | Languages used in the resource. The value should confirm to a [ISO 639-3](https://www.iso.org/obp/ui/#iso:std:iso:639:-3:ed-1:v1:en) code.<br> The `type` attribute MUST be used to define what the language represents (e.g., subtitles, spoken language, written language, etc.). |
| Requirement | SHOULD                                                                                                                                                                                                                                                                              |
| Cardinality | 0..n                                                                                                                                                                                                                                                                                |

**Guidelines for Use:**

The value should be in the form of a [ISO 639-3](https://www.iso.org/obp/ui/#iso:std:iso:639:-3:ed-1:v1:en) code.

The type of language representation must be indicated. 
Examples of language types include subtitles, spoken language, written language, etc. 

The use of the `type` attribute should be meaningful for the data provider, reflect the metadata catalog or system, and be applied consistently using a standardized format.
  
**Examples:**
```json
{
  "language": [
    {
      "type": "subtitle",
      "value": "eng"
    }
  ]
}
```
```json
{
  "language": [
    {
      "type": "written language",
      "value": "fre"
    }
  ]
}
```

### Relation

| Name        | **Relation**                                                                                                                                                                                                                                                                                                                                                                |
|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | A related resource in which the described resource is physically or logically included (e.g., title of the parent or related work, collection, series, or part).<br>Attributes for `title` + `type` OR `id` + `type` MUST be used. <br> The`URI` attribute SHOULD be used.<br> The `lang` attribute SHOULD be used to specify the language of the related resource's title. |
| Requirement | SHOULD                                                                                                                                                                                                                                                                                                                                                                      |
| Cardinality | 0..n                                                                                                                                                                                                                                                                                                                                                                        |

**Guidelines for use:**

The use of attributes may vary, but the `type` attribute AND `title` attribute or `id` attribute are always required.

The `title` attribute specifies the title of the related resource. Language of the title should be specified using the `lang` attribute and a code from the [ISO 639-3](https://www.iso.org/obp/ui/#iso:std:iso:639:-3:ed-1:v1:en) standard.

The `type` attribute indicates the nature of the relationship between resources. 
It is recommended to use terms from Dublin Core (`conformsTo`, `hasFormat`, `hasPart`, `hasVersion`, `isFormatOf`, `isPartOf`, `isReferencedBy`, `isReplacedBy`, `isRequiredBy`, `isVersionOf`, `references`, `replaces`, `requires`).
If other terms are used for the type attribute, they should be meaningful to the data provider, reflect the metadata catalog or system, and be applied consistently with a standardized format.

An example of using the `id` attribute is to reference a series record, work record, or other resources within the same series or work.

The `URI` attribute is used to provide a link to the related resource (such as a catalog record or webpage). 

**Examples:**
```json
{
  "relation": [
    {
      "title": "Norway from end to end with Ola and Kari",
      "lang": "eng",
      "id": "987654321",
      "type": "IsPartOf",
      "URI": "https://www.nb.no/items/eb57e3c314894b0120cf631104065e74?page"
    }
  ]
}
```
```json
{
  "relation": [
    {
      "title": "Chronicles of Narnia",
      "lang": "eng",
      "type": "IsPartOf"
    }
  ]
}
```
```json
{
  "relation": [
    {
      "title": "20161203.jpg",
      "type": "hasPart",
      "URI": "https://www.nb.no/items/83af9a36b005c5737aa33d1fb64f429d?page"
    }
  ]
}
```

### Provenance

| Name        | **Provenance**                                                                                                                                                                                                                     |
|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | Information about any changes that may affect the authenticity, integrity, or interpretation of the resource (e.g., ownership, management, etc.). <br> The `lang` attribute MUST be used to spesify the language of the attribute. |
| Requirement | SHOULD                                                                                                                                                                                                                             |
| Cardinality | 0..n                                                                                                                                                                                                                               |

**Guidelines for use:**

The language of the provenance value must be provided using the `lang` attribute according to the [ISO 639-3](https://www.iso.org/obp/ui/#iso:std:iso:639:-3:ed-1:v1:en) standard. 

**Example:**
```json
{
  "provenance": [
    {
      "value": "The image is part of a digital collection that was donated to the National Library of Norway by Ola Nordmann on 2025-01-01.",
      "lang": "eng"
    }
  ]
}
```
```json
{
  "provenance": [
    {
      "value": "This digital object was previously part of the collection of Museum X between 1999 and 2002, before being transferred to Museum Y. Museum Y deposited the object with the National Library of Norway in 2025.",
      "lang": "eng"
    }
  ]
}
```
```json
{
  "provenance": [
    {
      "value": "Digitization was carried out internally at the National Library of Norway between 2022 and 2024. The project was initiated and completed after it was discovered that the film was a lost German feature film, with no other known copies internationally. As part of the digital work, the original projection print (ID-12345) was scanned in 2022. The aim of the project was to digitally safeguard the film with its original colour characteristics.",
      "lang": "eng"
    }
  ]
}
```

### Subject

| Name        | **Subject**                                                                                                         |
|:------------|:--------------------------------------------------------------------------------------------------------------------|
| Description | Subject terms related to the resource.<br>The `authority` attribute SHOULD be used to specify the authority source. |
| Requirement | MAY                                                                                                                 |
| Cardinality | 0..n                                                                                                                |

**Guidelines for use:**

This field is used to describe the content or subject matter of the resource. 
Examples include words or expressions that indicate the subject, theme, events, landmarks, buildings, or time periods relevant to the resource.

Dewey Decimal Classification (DDC) values are valid.

References to authority registers may be used where applicable. 
When using authority registers, subject terms must also be written out in full.

Explanation of *authority* information:
- `source`: The name of the authority file from which the value is taken, provided as a plain text string.
- `code`: A unique identifier for the authority entry within the register, typically a numeric or alphanumeric code.
- `URI`: A persistent link (URI) that points directly to the authority record from which the value is derived.

**Examples:**
```json
{
  "subject": [
    {
      "value": "rondane"
    },
    {
      "value": "fishingtrip"
    },
    {
      "value": "nature"
    }
  ]
}
```

```json
{
  "subject": [
    {
      "value": "nature",
      "authority": {
        "source": "Kulturnav",
        "code": "1031536c-0717-4d12-8895-fb88a7d4e952",
        "uri": "http://kulturnav.org/1031636c-0717-4d32-8895-fb88a7d4e952"
      }
    }
  ]
}
```

### Description

| Name        | **Description**                                                                                                                                                                                                                              |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | Description of the resource. The description may include a summary, a table of contents, a graphical representation or any free-text information about the resource.  <br> The `lang` attribute SHOULD be used to specify the language code. |
| Requirement | MAY                                                                                                                                                                                                                                          |
| Cardinality | 0..n                                                                                                                                                                                                                                         |

**Guidelines for use:** 

Language code must be specified. 
[ISO 639-3](https://www.iso.org/obp/ui/#iso:std:iso:639:-3:ed-1:v1:en) is used as the standard for indicating language when the `lang` attribute is applied.

**Example:**
```json
{
  "description": [
    {
      "value": "The image is part of the collection of Václav Marek, who followed Ola and Kari Nordmann on their journey across Norway. Václav Marek was an Englishman with a strong interest in Norway and its natural environment.",
      "lang": "eng"
    }
  ]
}
```

## Example containing all the metadata elements

```json
{
  "objectId": "av_6e8bc430-9c3a11d9",
  "priority": 50,
  "metadata": {
    "type": "Bilde",
    "identifier": [
      {
        "type": "URN",
        "value": "URN:NBN:no-nb_digifoto_20220311_00191_NB_PE_VM_M_05_09_01_036"
      },
      {
        "type": "image-id",
        "value": "NB_PE_VM_M_05_09_01_036"
      },
      {
        "type": "call-number",
        "value": "POEL00003975"
      }
    ],
    "title": {
      "value": "Ola and Kari on a fishingtrip in Rondane",
      "lang": "eng"
    },
    "alternative": [
      {
        "type": "original title",
        "value": "Ola og Kari på fisketur i Rondane",
        "lang": "nor"
      }
    ],
    "creator": [
      {
        "name": "Marek, Václav",
        "type": "Person",
        "role": "Photographer",
        "authority": {
          "source": "Felles autoritetsregister (BARE)",
          "code": "90362181",
          "uri": "https://bibsys-almaprimo.hosted.exlibrisgroup.com/permalink/f/nelpa2/AUTREG90362181"
        }
      }
    ],
    "contributor": [
      {
        "role": "depicted",
        "type": "Person",
        "name": "Nordmann, Ola"
      },
      {
        "role": "illustrator",
        "type": "Person",
        "name": "Solberg, Erna",
        "authority": {
          "source": "Kulturnav",
          "code": "e762d909-5cce-4d2b-892b-258272514fde",
          "uri": "https://kulturnav.org/e762d909-5cce-4d2b-892b-258272514fde"
        }
      }
    ],
    "publisher": [
      {
        "name": "National library of Norway",
        "type": "Korporasjon",
        "authority": {
          "source": "Felles autoritetsregister (BARE)",
          "code": "90362181",
          "uri": "https://bibsys-almaprimo.hosted.exlibrisgroup.com/permalink/f/nelpa2/AUTREG90362181"
        }
      }
    ],
    "spatial": [
      {
        "name": "Norge (NO);Innlandet;Stor-Elvdal;Rondane gjestegård",
        "type": "Depicted location",
        "authority": {
          "source": "Kulturnav",
          "code": "1031636c-0717-4d12-8895-fb88a7d4e952",
          "uri": "http://kulturnav.org/1031636c-0717-4d12-8895-fb88a7d4e952"
        },
        "coordinateReferenceSystem": "EPSG:4326",
        "latitude": 61.788453,
        "longitude": 10.224725
      },
      {
        "name": "Norge (NO);Innlandet;Lillehammer;Lillehammer"
      }
    ],
    "date": [
      {
        "type": "Content date",
        "value": "1938"
      },
      {
        "type": "digitized",
        "value": "2022-03-05T14:28:12+02:00"
      },
      {
        "type": "published",
        "value": "2022-03-12"
      }
    ],
    "language": [
      {
        "type": "subtext",
        "value": "eng"
      }
    ],
    "relation": [
      {
        "title": "Norway from end to end with Ola and Kari",
        "lang": "eng",
        "type": "IsPartOf",
        "id": "987654321",
        "URI": "https://www.nb.no/items/eb57e3c314894b0120cf631104065e74?page"
      }
    ],
    "provenance": [
      {
        "value": "The collection was donated to the National Library by Václav Marek on May 12, 1979.",
        "lang": "eng"
      }
    ],
    "subject": [
      {
        "value": "rondane"
      },
      {
        "value": "fishingtrip"
      },
      {
        "value": "nature",
        "authority": {
          "source": "Kulturnav",
          "code": "1031536c-0717-4d12-8895-fb88a7d4e952",
          "uri": "http://kulturnav.org/1031636c-0717-4d32-8895-fb88a7d4e952"
        }
      }
    ],
    "description": [
      {
        "value": "The image is part of the collection of Václav Marek, who followed Ola and Kari Nordmann on their journey across Norway. Václav Marek was an Englishman with a strong interest in Norway and its natural environment.",
        "lang": "eng"
      }
    ]
  }
}
```



