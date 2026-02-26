---
title: Events/preservation metadata
weight: 2
draft: false
---

> ⚠️ **These pages is under construction** ⚠️


In digital preservation, an “event” documents an action or occurrence that has affected a digital object, such as creation, migration, validation, or transfer. Events are considered important preservation metadata, as they provide traceability and evidence of what has been done to the object throughout its entire lifecycle.

Submitting events is not mandatory, but we recommend doing so when such information is available. Events added through the API will be preserved in a dedicated event database, just like events that occur within the preservation environment (DPS). When disseminated, this provides a clearer overview of all events associated with an object. If you want do submit other types of preservation metadata, it is also possible to submit preservation metadata as part of the information package (SIP). See more information under [metadata primer](/docs/dps/sip/1.0/metadata/) and [requirements for SIP structure](/docs/dps/sip/1.0/structure-requirements/). Information relating directly to provenance may be included under [metadata requirements](/docs/dps/api/submission/metadata/).

Events can be associated with either the entire information package or with individual files. In general, events should be associated with the package level, the Intellectual Entity (IE), where possible. This is to avoid large numbers of events that essentially convey the same information. It is possible to associate events with individual files when there is a need to document file-level actions. The most important consideration is to be deliberate about what is documented, why it is documented, and at which level.

The technical documentation of submissions in API are to be found here: [Swagger DPS Submission Service API](https://digitalpreservation.no/swagger/)

Here you will find explanations of how the different elements in an event are used, as well as the various event types:


{{< cards >}}
  {{< card link="event_elements" title="Use of event elements " icon="document-text" >}} 
  {{< card link="eventType" title="Event-types" icon="document-text" >}}
{{< /cards >}}


