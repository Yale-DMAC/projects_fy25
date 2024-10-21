# Preservica Notes for Records with DCS Images
Last updated on 10/21/2024 by Kylene Hutchinson.

| Start Date | End Date   | Contributors      | Informed Stakeholders |
| ---------- | ---------- | ----------------- | --------------------- |
| 09/25/2024 | 10/21/2024 | Kylene Hutchinson | Alicia Detelich       |
# Overview
## Problem Statement
Certain ArchivesSpace records are made public with Preservica Digital Objects. These are not directly accessible to patrons so a note was added to each Archival Object explaining how patrons could request access to the Preservica Object.
As materials have been ingested into DCS, these notes are no longer needed, as patrons can directly access and download the material from Archives at Yale or DCS. Thus we should delete these notes from any MSSA archival object record which has a DCS or Aviary digital object.
## Goals
- Identify all MSSA archival objects which have both a 'Digital Copy Request' exloc note AND a linked Aviary or DCS digital object
- Delete the Digital Copy Request notes
# Background
In 2020 MSSA created many Existence and Location of Copies notes, linked to archival object records, which were intended to facilitate patron requests of materials which had already been digitized and ingested into Preservica, but which were not yet available in a digital access system.

The structure of the notes is generally as follows:
"A copy of this material is available in digital form from Manuscripts and Archives. Contact Manuscripts and Archives at [beinecke.library@yale.edu](mailto:beinecke.library@yale.edu) to request access to the digital copy." The text after the 'Preservica' part of the note varies depending on the name of the record in Preservica.

# Process
See [[preservica_notes.py]] 
- Pull a list of URIs from the SQL database for Archival Objects with the  'A copy of this material is available in digital form from Manuscripts and Archives' note, who have a digital object attached with a DCS or Aviary url.
- Put the URIs in a csv file
- Save backups of each object into a folder using the API
- Iterate over the Notes dictionary, copying all objects except for the object containing the key type = altformavail
- Use the API to overwrite the record with the updated record without the 'Existence and Location of Copies' note
- Save details about errors and updates into csv files.

# Notes

| Date       | Highlight               | Notes                                                                                                                                                                                                                                                           |
| ---------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 09/25/2024 | Introduction to Project | Alicia Detelich introduced and assigned this project.                                                                                                                                                                                                           |
| 09/25/2024 | Review and Coding       | Reviewed the code and asked Alicia a couple questions. Was able to adapt the [[Divinity Library Preferred Citation]] code to do this. Tested on a single record in Test and it went smoothly.                                                                   |
| 09/26/2024 | Testing                 | Tested in Test Environment                                                                                                                                                                                                                                      |
| 09/27/2024 | Testing Error           | Tested again in Test Environment but this time multiple notes were deleted. Sometimes all notes were deleted. Investigating why.                                                                                                                                |
| 10/01/2024 | Restoring Test Files    | Restoring Notes to Test Environment records using backups.                                                                                                                                                                                                      |
| 10/01/2024 | Testing                 | Tested again over Test Environment Records after updating code to skip adding 'altformavail' notes rather than delete it. Discovered that the SQL query results are not matching live?                                                                          |
| 10/01/2024 | On Hold                 | Spoke with Alicia, Test SQL database is not reflecting API results. Code wasn't deleting notes, SQL was just grabbing records with no notes in Test and reporting they had notes thanks to the bad database. She reached out to Trip and they contacted Lyrasis |
| 10/15/2024 | New Database            | Lyrasis got back to us with a new Test SQL database to use with new login credentials. We can resume testing now.                                                                                                                                               |
| 10/16/2024 | Testing                 | Test on 8k records in Test Environment, spot checking and seems to have worked as expected.                                                                                                                                                                     |
| 10/21/2024 | Updated Production      | Got permission from Alicia to run in Production. Ran the code and update 14,377k records.                                                                                                                                                                       |

# Review

## Data Details
- 14,559 archival objects have this note but also either an aviary or dcs digital object attached.
## Communication
| Name             | Position                                                                                           | Notes                                                              |
| ---------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Alicia Detelich  | Assistant Director of Special Collection Metadata Services, Special Collections Technical Services | - Assigned Project<br>- Investigated SQL issues and contacted Trip |
| Trip Kirkpatrick | Technical Lead of Digital Scholarship, Library IT                                                  | - Contacted Lyrasis about Test SQL DB                              |
## Results
Removed the Preservica note from 14,337k records that had a DCS or Aviary Digital Object attached.

# References

- [Github Issue - Delete Preservica notes for records with DCS images](https://github.com/orgs/Yale-DMAC/projects/1/views/1?pane=issue&itemId=23753477)
