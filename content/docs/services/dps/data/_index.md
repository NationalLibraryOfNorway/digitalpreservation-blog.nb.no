---
title: Data management
weight: 1
---

## What is data?

The DPS is a set of services created to preseve data. In the context of the DPS we talk about *data* and *metadata*. Data is the content being preserved: the digital files you submit to the DPS. DPS metadata exists to enable preservation and provide access to those data. Without data, nothing else follows. The DPS does not accept metadata without data.

To submit data, you must give it to us in the shape of a SIP, structured according to our [SIP specifications](/docs/dps/sip/1.0/). Within the SIP, data lives in the `data/` directory inside each representation. The METS.xml files, metadata folders, schemas, and documentation outside the data directories are the packaging that makes the content machine-readable and verifiable. The [E-ARK specifications](https://dilcis.eu/specifications) define what kind of files belong in which folders, so a future user retrieving the data knows where to look for what.

If you want to preserve metadata (such as library catalogue exports), you will treat them as *data* in the context of the DPS and put them in the `data/` directory of the SIP. In turn the DPS will also require metadata that describes those data.

The purpose of digital preservation is to ensure that digital materials remain unchanged and accessible. The DPS currently manages petabytes of preserved data. Once data enters the DPS, the obligation to preserve it follows the content for as long as it has been deemed worthy of preservation by the client and the submission agreement. Unless otherwise stated, this means indefinitely. The DPS is not intended to be temporary storage for files.

## Choosing what to preserve

The DPS and the digital preservation team **do not** decide what is worthy of preservation. Selection happens at two levels:

- **Agreement level**: the National Library and the submitting client organization agree on a contract allowing use of the DPS. A single contract may result in multiple submission agreements, each controlling which clients can submit and access the content under it.
- **Object level**: the selection criteria lie entirely with the client. You determine which individual objects enter the DPS and which stays out.

At the agreement level, the submission agreement defines the scope of what may be submitted and under what terms. We cannot currently validate automatically at the object level against what is stated in the submission agreement, and rely on you as the client to follow your obligations.

At the object level, the choice is yours. After the submission agreement has been signed, our role is not to judge what merits preservation; it is to ensure that what you entrust to us remains unchanged and accessible, regardless of the files you choose to preserve.

We strongly encourage clients to make informed decisions at the object level, in line with the [Principles for Digital Preservation](/docs/principles/). In particular, we recommend:

- **Use well-documented and open file formats**: this increases the likelihood that files will remain usable over time (principle 2). See [Preferred file formats](/docs/formats) for our recommendations.
- **Avoid unnecessarily large files**: every bit stored in the DPS carries a perpetual cost of storage and management (principle 1). Bloated files carry unnecessary cost without providing additional value. Submitting the smallest reasonable version of each digital object helps keep the system sustainable.
- **Avoid unnecessary duplication of data**: files that can be automatically generated from preserved master files (such as access copies or lower-resolution derivatives) should not be submitted (principle 1). The DPS focuses on preserving the source from which other versions can be produced.
- **Analyze the file**: generate checksums early, confirm file formats, and validate that the content is what it claims to be (principle 4). The DPS requires checksums to be delivered with each file in the SIP.

## How data enters the DPS

Data enters the DPS through Submission Information Packages submitted through the submission service. You authenticate with the API, which verifies that you are authorized to submit against your submission agreement (see [role-based access control](/docs/services/dps/access-control/)).

The submission workflow: create a submission → register the files that make up the SIP → upload the file content → finalize to trigger ingest.

Files are preserved if they validate against the [SIP structure requirements](/docs/dps/sip/1.0/structure-requirements/), the [METS.xml requirements](/docs/dps/sip/1.0/mets/), and the [API requirements](/docs/dps/api/submission/). Submissions that do not comply will be rejected.

## How data is preserved in the DPS

Once data enters the DPS, the commitment is simple: what you submit is what you get back, unchanged. Preservation happens at two levels:

### Passive preservation

Passive preservation ensures the bits themselves survive. It requires no understanding of the content, only that the files remain unchanged.

- **Bit-level preservation**: the original file is preserved. Data is stored as a faithful copy of what was received, with no transformation, compression, or alteration that would change the bits of the original files. The DPS requires files to be delivered with a checksum in the SIP. Those checksums are stored, verified at ingest, and re-checked whenever content is disseminated. If a discrepancy is found, it is documented and the other two copies are checked to identify the correct version. In practice, this works at scale: over 16 million files have been checksum-verified through five technological shifts over 20 years, with zero bit-level changes found.
- **Redundant storage**: data is protected by the 3-2-1 policy: three copies, on two different storage technologies, with one copy stored off-site. If a single copy is lost or corrupted, the other copies ensure the data survives. Multiple copies also make the integrity verification meaningful: when a discrepancy is found, the uncorrupted copies provide the reference for determining the correct version.

All data is stored in the bit repository. Every file's physical location is tracked, linked to the digital object it belongs to. The DPS may repackage files behind the scenes for storage efficiency, but this is transparent: dissemination returns your content in its original form.

### Active preservation

Active preservation goes beyond storing bits: it gathers knowledge about the content so that the DPS can act on it over time.

As part of ingest, the DPS performs format identification and technical metadata extraction on every file. This builds an overview of what files exist in the repository, their formats, and their technical properties. It also detects potential issues: if the DPS finds something that may be wrong with a file, even after the file has passed SIP structure validation, the issue is documented, but the file is still preserved. A future user who discovers a fault can see that the DPS already recorded it at the point of ingestion, and that the file's integrity has remained unchanged since.

This knowledge feeds into preservation planning. Understanding what file formats are present and in what volumes allows the DPS to monitor at-risk formats and assess when intervention may be needed. Periodic integrity checks verify that files have not changed. Every operation is documented, forming an audit trail that records what happened to each file and when.

The digital preservation team maintains expertise on different formats, their strengths and weaknesses, and the implications of migrating from one to another. This allows us to help clients make informed decisions about what actions to take, if and when a format becomes at risk. For a detailed walkthrough of how all this metadata is managed, see [Metadata](/docs/services/dps/metadata/).

## How data is accessed

Data in the DPS is cold storage: access is not immediate. The DPS operates on an asynchronous architecture, and dissemination requests are processed as background jobs with inherent delays. This is a conscious trade-off: the bit repository is optimized for long-term safety and cost efficiency over fast retrieval.

Data is retrieved through dissemination. Access to retrieve data requires a consumer role tied to your submission agreement (see [role-based access control](/docs/services/dps/access-control/)):

- You create a dissemination request through the API, specifying the DPS-ID of the content you want to retrieve (see [Dissemination API](/docs/dps/api/dissemination/)).
- A fixity check is performed as part of the dissemination process, verifying that the content has not been altered since it was stored.
- Once ready, the content is made available through a presigned URL, delivered via a webhook.
- You can also poll the status of the request through the API while the DPS prepares the content.

When content is disseminated, files are returned in their original form. The repackaging applied during storage is transparent to retrieval.

## How data changes over time

Today, data in the DPS is immutable. Once preserved, the original files cannot be altered. If you need to update or replace content, you submit a new version through a new submission. The original is kept alongside the updated version. Preservation actions such as format migrations or fixity checks are documented and may produce derivative copies, but they do not modify the preserved originals.

The DPS is a work in progress. We are actively discussing ways of enabling versioning and additions of new data to existing packages. This is not yet implemented, but reflects an ongoing commitment to making the system more flexible over time.
