---
title: "Better Late Than Never: Adding Checksums to 16 Million Legacy Files"
date: 2024-11-06T12:45:00+01:00 
description: "Case study on verifying 2.5 Petabytes of legacy data during migration at the National Library of Norway. Details how checksums validated 16 million files across multiple storage copies, finding zero corruptions after 20 years."
tags: ["Digital Preservation", "Checksums", "Data Migration", "Data Integrity", "Digital Storage", "File Verification", "Legacy Systems", "Digital Archives", "SAM-FS", "Long-term Storage"]  
authors: 
  - name: Digital Preservation Team
    image: /apple-touch-icon.png
images: 
  - cover.jpg
aliases: /checksum-generation
---

The National Library of Norway has used SAM-FS[^1] as a system for long-term storage and archiving of large amounts of data since 2007.
SAM-FS contains 14 Petabytes of data and will soon reach "end of life" status as a product.

In 2022, the National Library decided to replace SAM-FS with a more modern preservation solution for digital material.
This new solution is based on in-house developed software called DPS (Digital Preservation Services) and uses IBM-HPSS as the underlying system for data storage.

Over the last 10 years, the National Library has used checksums[^2] as a verification technique for preserved data.
In this context, a checksum is a calculated hash string used to verify that a data file has not been subject to any changes.
Common checksum calculation algorithms include MD5, SHA-1, SHA-256, or SHA-512.
The National Library uses MD5[^3].

## Lack of checksums
Many of the oldest files in SAM-FS **lacked** checksums when they were stored. 
As all files in SAM-FS are stored in three copies, you could say that without an accompanying checksum the three copies exist independently of each other.
If a discrepancy were to arise between the three copies, we would have no original checksum to use for verification.

{{< figure src="checksum1.svg" alt="Diagram showing the data flow in and out of SAM-FS" caption="Data stored in SAM-FS in 3 instances" >}}

As part of the process of migrating data from SAM-FS to the new DPS, it was decided that checksums should be calculated and stored for all files that did not already have one.

## Challenge
How could we ensure that files being transferred from SAM-FS to DPS were the same as those originally archived when there were no checksums to verify this?
The oldest files were over 20 years old and had been subjected to up to five hardware/platform migrations over time (see Figure 4).

Which of the three file instances stored in SAM-FS should we choose as the starting point for migration?
How could we know that this was the "correct file" without having to read and compare all three instances?
Reading and comparing all three instances was considered to be difficult, as this involved reading and processing many Petabytes[^4] of data on the same infrastructure that was also used for daily operations.

## Solution
The fact that we had the files preserved in multiple instances helped us, as we were about to generate checksums for "old" files for the first time.
One copy is stored on disk (disk copy), and two copies are on tape (tape copy 1 and tape copy 2).

{{< figure src="checksum2.svg" alt="Diagram showing data flow in checksum generation" caption="Checksum calculation" >}}

First (Step 2), we created a program (script) that extracted all files in SAM-FS without checksums from one of the tape copies.
A checksum was then calculated for each individual file, which was stored in a database.

This process took just over 2 calendar months to complete for a dataset of 2.5 Petabytes.

{{< figure src="checksum3.svg" alt="Diagram showing data flow in checksum verification and data transfer to the DPS" caption="Checksum verification and transfer to DPS" >}}

The actual task of transferring files from SAM-FS to DPS began after all the files on tape had been read, and checksums had been calculated and stored in a database.

The migration then started by retrieving a file from the disk instance in SAM-FS (step 3).
A checksum for this file was then calculated and compared with the checksum stored for the corresponding tape copy file.
If these matched, it meant that at least two of the three file copies were identical.

The file was then considered to be OK and was transferred to DPS with the accompanying new checksum (step 4).
If the checksum did not match, it meant that either the disk or tape copy of the file was incorrect.
This was then reported as an error and had to be followed up manually by checking the third copy to see if it matched one of the two that had already been checked.

## Outcome and lessons learned
None of the 16 million files in the dataset of 2.5 Petabytes had checksum discrepancies.
This method of ensuring that the files in DPS are authentic after migration was both time- and resource-consuming, but it proved to work well for us.

Another experience we had was that one can trust technical storage systems when it comes to avoiding changes in the bit pattern over time.
We have checksum-verified 16 million files that have undergone up to five technological shifts over 20 years, without finding any trace of changes in the bit pattern of any of the files.

### Platform/Technology generations in SAM-FS
Overview of technology shifts in the National Library's SAM-FS long-term storage system. 
The *TB* value here is native storage capacity per storage unit, disk/tape:

| **Time period** | **Disk copy** | **Tape copy 1** | **Tape copy 2** |
|----|----|----|----|
| 2007-2009 | SUN 6140 (1TB) | SUN SL8500 – T10kA (500GB) | SUN SL8500 – T10kA (500GB) |
| 2009-2011 | SUN 6180 (2TB) | SUN SL8500 – T10kB (1TB) | SUN SL8500 – T10kB (1TB) |
| 2012-2016 | Nexsan (3TB) | SUN SL8500 – T10kC (5TB) | SUN SL8500 – T10kC (5TB) |
| 2016-2019 | Nexsan (8TB) | *as above* | *as above* |
| 2020-2022 | Fujitsu (16TB) | SUN SL8500 – LTO8 (12TB) | SUN SL8500 – LTO8 (12TB) |

[^1]: Hierarchical storage Management System, SAM-FS is also known as Oracle HSM

[^2]: https://www.dpconline.org/handbook/technical-solutions-and-tools/fixity-and-checksums

[^3]: https://en.wikipedia.org/wiki/MD5

[^4]: 1 Petabyte = 1.000 Terabyte
