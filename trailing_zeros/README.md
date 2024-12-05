# Trailing Zeros
Last updated on 12/05/2024 by Kylene Hutchinson.

| Start Date | End Date   | Contributors      | Informed Stakeholders |
| ---------- | ---------- | ----------------- | --------------------- |
| 12/02/2024 | 12/05/2024 | Kylene Hutchinson | Alicia Detelich       |
# Overview
## Problem Statement
Some number fields in extent records for boxes end with .0 - e.g. 1.0 linear feet or 1.0 boxes. The trailing zero is unnecessary and should be removed.
## Goals
- Identify all records with a trailing .0 in the extent number field
- Remove this trailing .0
# Background
General clean up of unnecessary data that may cause future complications by being inconsistent. 

# Process
See [extents_trailing_zeros.py](extents_trailing_zeros.py), [extents_trailing_zeros.sql](extents_trailing_zeros.sql), [241203_updates.csv](241205_updates.csv)
- Write SQL code that returns URIs of records whose extent number ends in .0
- Create backups of these URIs
- Use the API to update record extent numbers
- Save details of errors and updates in a csv file.
# Notes

| Date       | Highlight          | Notes                                                                                                                                                                                                                                                                        |
| ---------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 12/02/2024 | Coding and Testing | Reviewed project and began coding. Tested code in the Test Environment in the afternoon, everything updated cleanly. Got permission from Alicia to run in production.                                                                                                        |
| 12/03/2024 | Delayed            | ArchivesSpace's Production database has been moved and has new login information, took until the end of the day for Lyrasis to provide the new database password.                                                                                                            |
| 12/04/2024 | Delayed            | ArchivesSpace has been having issues with production partly because of a migration over break, and partly due to bots hammering the site. Production API was not working at all and Production SQL was working intermittently so nothing can be done until this is resolved. |
| 12/05/2024 | Completed          | Ran in Production successfully.                                                                                                                                                                                                                                              |

# Review

## Data Details
- 396 records in Test Environment
	- 37 Resources
	- 280 Accessions
	- 61 archival objects
## Communication
| Name            | Position                                                                                           | Notes                               |
| --------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------- |
| Alicia Detelich | Assistant Director of Special Collection Metadata Services, Special Collections Technical Services | Approved running code in production |
## Results
398 records including resources, accessions, and archival objects were updated in production to remove the .0 from extent numbers that end with .0

# References

- [Github Issue - Check for trailing zeros in extent records](https://github.com/orgs/Yale-DMAC/projects/1/views/1?pane=issue&itemId=21043590)