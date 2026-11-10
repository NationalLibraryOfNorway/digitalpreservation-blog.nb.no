---
title: Preservation events
weight: 1
---

Preservation events are a type of preservation metadata. An event documents an action or occurrence that has affected a digital object, such as its creation, migration, validation, or transfer. Together, the events form a record of what has been done to an object throughout its lifecycle, by whom, and with what result. [Metadata management](/docs/dps/understanding/metadata-management/) describes how events enter DPS, both from the Producer and from DPS itself. This page explains how events are modelled, why we recommend submitting them through the API, and how much to document.

## How events are modelled

DPS bases its events on the [PREMIS data model](https://www.loc.gov/standards/premis/) for preservation metadata. Each event connects three things:

- **The object** the event concerns: either the whole information package (the Intellectual Entity) or a single file within it.
- **The event** itself: what kind of action it was, when it happened, what was done, and what the outcome was.
- **The agent** that performed it: software, hardware, an organization, or a person.

PREMIS is a flexible framework rather than a fixed recipe, and there is little guidance on how to apply it in practice. The National Library has chosen a deliberately simple model to start with, and expects to extend it over time. The background to these choices is described in the blog post [PREMIS without a single right answer](/blog/2026-03-24-premis-without-a-single-right-answer-our-approach-to-preservation-metadata-and-events/).

Event types come from a controlled vocabulary. The National Library bases it on the Library of Congress list of [event types](https://id.loc.gov/vocabulary/preservation/eventType.html), narrowed down and specified to suit our material and preservation environment.

## Events in the API and in the SIP

Events are stored in the preservation metadata database rather than written as files inside the information package. This makes it possible to add new events throughout the lifetime of an object without changing the preserved package. Events submitted by the Producer are preserved in the same way as the events DPS records itself, so the complete history of an object is available in one place when it is retrieved.

Preservation metadata can also be included as files in the Submission Information Package (SIP). Such files are preserved as part of the package, but they are not available as events through the API. This is why we recommend submitting events through the API. If practical or technical constraints prevent this, it is still better to include the information in the SIP than to leave it out. Information about provenance can also be given in the *Provenance* element of the [descriptive metadata](/docs/dps/reference/descriptive-metadata/).

## Documenting deliberately

More events do not necessarily mean better documentation. Many events that convey the same information make the history harder to read, and add to the metadata that must be managed over time. As a general rule, events are linked to the information package as a whole, and to individual files only when a file-level action or deviation needs to be documented. The most important consideration is to be deliberate about what is documented, why, and at which level.

Events should be written with future management and use in mind, so that the information remains clear and verifiable over time.

## Read more

- [Add preservation events](/docs/dps/how-to/add-preservation-events/): which events to record for your workflow, and how to submit them.
- [Preservation events reference](/docs/dps/reference/preservation-events/): event elements, event types, and examples.
