# Published Preservica Notes
Last updated on 11/05/2024 by Kylene Hutchinson.

| Start Date | End Date | Contributors | Informed Stakeholders |
| ---------- | -------- | ------------ | --------------------- |
| 10/22/2024 | 11/05/2024 | Kylene Hutchinson | Alicia Detelich |

# Overview
## Problem Statement
Some Preservica Notes are accidentally marked as published and need to be made unpublished. Both notes containing preservica links, and notes about deleted preservica digital objects need to be marked as unpublished.
## Goals
- Report on published Preservica notes
- Update to unpublished
# Background
We keep track of specific Preservica data in the notes of archival objects and resources, these are for internal use only and should be marked as unpublished. Occassionally these are mistakenly marked as published instead of unpublished during creation.


# Process
See [preservica_note_unpublish.sql](preservica_note_unpublish.sql), [preservica_note_unpublish.py](preservica_note_unpublish.py), [241025_preservicapub_uris_update.csv](241025_preservicapub_uris_update.csv), [241028_preservicapub_uris_update.csv](241028_preservicapub_uris_update.csv), [241030_preservicapub_uris_update.csv](241030_preservicapub_uris_update.csv), [241031_preservicapub_uris_update.csv](241031_preservicapub_uris_update.csv), [241105_preservicapub_uris_update.csv](241105_preservicapub_uris_update.csv), [full_preservicapub_uris_update.csv](full_preservicapub_uris_update.csv)
- Create a SQL query that reports on the number of preservica notes and how many are unpublished.
- Create a python file that queries the SQL database for published preservica notes
- Save backups of the records using api
- Update the notes publish status from 'true' to 'false'
- Save reports on any changes or errors that occurred.


# Notes
| Date | Highlight | Notes |
| ---- | --------- | ----- |
| 10/22/2024 | Started | Picked up this project from the 'Ready to Start' column in the project backlog |
| 10/22/2024 | Tested | Wrote code and tested it in the Test Environment |
| 10/23/2024 | Report | Wrote a report counting the total number of notes and how many are published in Production. |
| 10/24/2024 | Updated | Made a few minor changes to the python and sql to ensure only otherfindaid notes were being chosen. |
| 10/24/2024 | Meeting | Presented my work at the SCMS meeting, noted that 4 records had sql data that suggested the notes were published but the api and web client both reported they were unpublished. Gave data to Alicia to review and made adjustments to the code to ignore publish flag status as everything should be set to false and setting a false flag to false won't cause harm. | 
| 10/25/2024 | Testing | Ran updated code on Test Environment. Everything came back as expected, got permission to run in Production. |
| 10/25/2024 | Ran in Production | Ran code in Production which had way more notes than test. API was way too slow to handle the 108k records that had one of the two notes. |
| 11/01/2024 | Meeting | Spoke with Alicia about the issues I was experiencing and how long it took to run on every record. ArchivesSpace API just isn't capable of handling that many updates. Reviewing the SQL discrepency again revealed that the issue seemed to have been resolved on its own. We still aren't sure why some of these records had incorrect SQL data. |
| 11/05/2024 | Completed | Ran in production using the original code that restricted the records to those marked as published. 1.8k records were updated this time without issue. No discrepencies between SQL and API found. |


# Review

## Data Details
5,069 out of 108,834 Preservica notes are published in Production.  
70 resources have a published preservica note.  
4,999 archival objects have a published preservica note.  
292 records have a published Preservica delete note.  
  
After SQL updated, 7,652 out of 108,845 Preservica notes are published in Production.
## Communication
| Name             | Position                                                                                           | Notes                                                              |
| ---------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Alicia Detelich  | Assistant Director of Special Collection Metadata Services, Special Collections Technical Services | - Approved running code in production |
## Results
Ran the code in production in several passes.  
1,811 records unpublished on 11/05  
5,502 records unpublished on 10/31  
86 records unpublished on 10/30  
248 records unpublished on 10/28  
5 records unpublished on 10/25  
All notes are now set to unpublished without any issues.
# References

- [Github Issue - Update published Preservica notes](https://github.com/orgs/Yale-DMAC/projects/1/views/1?pane=issue&itemId=44064853)
- [Github Issue - Review and fix published "deleted from catalogue" Preservica notes](https://github.com/orgs/Yale-DMAC/projects/1/views/1?pane=issue&itemId=20963736)
- [Deleted from Catalogue Note Structure examples](https://github.com/YaleArchivesSpace/Archives-at-Yale-EAD3/search?q=%22+deleted+from+catalogue%22)