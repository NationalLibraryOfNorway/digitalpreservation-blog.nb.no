---
title: Use of event elements
weight: 2
draft: false
---

For event formatting, see technical documentation here: [Swagger DPS Submission Service API](https://digitalpreservation.no/swagger/).


**The following elements are permitted:**

Agent:* 
- agentName*
- agentType*
- agentVersion
- agentNotes

Event:*
- eventDateTime*
- eventType*
- eventDetail
- outcome*
- outcomeDetail

Elements marked with * are required.
<br><br>

# How to use Event Elements:

## Agent:
The Agent describes the actor that performed the action. This may be software, an organization, or a person.


### AgentName
The name of the actor that performed the action. The name must be unique and used consistently.

**Examples:**
- "Apache NiFi"
- "Nasjonalbiblioteket – Team Digital Preservation"
- "Ola Nordmann"
- "JHOVE"


### AgentType
Specifies the type of actor that performed the action.

**Allowed values:**
- "software"
- "organization"
- "person"



### AgentVersion
The version number of the agent if it is software. AgentVersion is used to ensure traceability and reproducibility, as different versions of the same tool may produce different results.

**Examples:**
- "1.15.0"
- "3.2"
- "1.11.0; DROID_SignatureFile_V116.xml; container-signature-20231127.xml"



### AgentNotes
Additional information about the agent that performed the action. This element documents characteristics, context, or configuration of the agent itself — not what the agent did in a specific event.

**This may include:**
- What the agent is and what it does in general
- How the agent is configured or installed
- Operational context or responsibility
  
**Examples:**
- "Siegfried is a file format identification tool using PRONOM signatures. Installed with signature set v95 for PDF, TIFF, JPEG, and XML formats." 
- "Apache NiFi is a dataflow automation tool that enables the design and management of complex data pipelines." 
- "JHOVE custom installation with PDF, TIFF and JPEG modules enabled. Running under Java 17 runtime environment."
- "Institution with formal responsibility for digital preservation, ingest, and long-term management of archival materials."

> [!NOTE]
> AgentNotes should be used as consistently as possible for the same agent. Variations in the wording of AgentNotes will result in the creation of a new Agent entry in the registry.



## Event:
The Event describes the action performed on the object.


### EventDateTime
The date and time when the event occurred. Must be expressed according to the ISO 8601 standard, including time zone.

**Example:**
- "2026-02-23T10:45:00+01:00"



### EventType
Specifies the type of action performed. This element describes the kind of process the event represents.
The value must be a controlled and consistently used term — [list of allowed event types](/docs/dps/api/submission/events/eventType/).



### EventDetail
A precise description of what was done in the event. This element elaborates on EventType and describes the specific operation carried out.

**Examples:**
- "MD5 checksum generated" 
- "Migrated from TIFF to JPEG2000"
- "Validated against PDF/A-2b standard"


### Outcome
The overall result of the event. This element indicates whether the event was completed as expected, failed, or was completed with deviations.

**Allowed values:**
- "success"
- "failure"
- "warning"


### OutcomeDetail
A concrete and precise description of the result of the event.
This element documents what was actually achieved or which deviations were identified. The description should be concise and clear. Not all events require additional documentation beyond success/failure/warning — in such cases, the Outcome element alone is sufficient.

**Examples:**
- "Identified as fmt/353 (TIFF 6.0)."
- "Validated against profile E-ARK-SIP-v2-2-0, NB-SIP-STRUCTURE-1.0 and NB-SIP-MOVINGIMAGES-PROFILE-1.0."


















