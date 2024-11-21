# MUL Languages
Last updated on 11/21/2024 by Kylene Hutchinson.

| Start Date | End Date | Contributors | Informed Stakeholders |
| ---------- | -------- | ------------ | --------------------- |
|     11/14/2024       | 11/21/2024         | Kylene Hutchinson           | Alicia Detelich                      |

# Overview
## Problem Statement
With the upgrade to ArchivesSpace 2.7.x a few years ago, it is now possible to associate multiple languages with a record (e.g. the language and script subrecord is now repeatable where previously it was not). Prior to this upgrade, when a record was associated with multiple languages, processing archivists would select 'mul' (multiple) from the language controlled value list, and then specify which languages were used in the free-text field. It is desirable to identify all 'mul' records and update them with the multiple languages with which they are associated.
## Goals
- Identify all records with 'mul' as a value in the language and script subrecord
- Identify all associated languages in the free text language field
- Create new subrecords for each language, using the controlled value for the language
- Delete the existing 'mul' language subrecord (or replace it with one of the new languages)
# Background
With the upgrade to ArchivesSpace and the ability to have multiple languages associated with the record, the standard was changed from using 'mul' language code with a note field explaining which languages were associated to attaching each individual language code to the record.


# Process
See [mullanguages.py](mullanguages.py) and [241121_mulnotes_updates.csv](241121_mulnotes_updates.csv)
- Write a SQL query to grab the uris of records with the MUL language code.
- Use the API to search the uris for language notes. If the record has a language note, create a backup file.
- Create a language code dictionary, and check for the language in the note field.
- If the language code already has a subrecord, skip. Otherwise first replace the MUL language code with one of the new language codes, and append new subrecords for any other language.
- Save errors and status information to csvs.

# Notes

| Date       | Highlight | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 11/14/2024 | Started   | Picked up this project from the ready to start list. Was able to find the list of languages on a record and the controlled vocab list for it, but cannot find the notes in the sql table. Didn't appear in the notes table or the language tables. Asked Alicia but she wasn't sure either. I only found a little over 300 records with the mul code and half of them didn't appear to have notes so it wont be taxing on the system to check the notes via API. |
| 11/18/2024 | Coding    | Wrote code to check the notes field via the API and then add in language fields as needed. Used ArchivesSpace's controlled values lists to create a language code dictionary. Some of the listed languages do not appear in the controlled value list so I will check if we should ignore these or add them into the controlled value list.                                                                                                                      |
| 11/19/2024 | Testing   | Ran in Test environment on the 356 records and updated 181 records who had language notes. 9 of these records returned 400 codes, not sure why they are rejecting the update as I cannot see any errors. Maybe these are locked or have something special about them? Need to investigate further.                                                                                                                                                               |
| 11/20/2024 | Testing   | Investigated the 9 records but could not find any difference between them and the other 172 records. Determined that it is specifically adding extra language subrecords that these 9 records are rejecting, any other editing seems fine. Sent some examples for Alicia to look at when she has time.                                                                                                                                                           |
| 11/21/2024 | Completed | Discovered the error was from a typo in the language dictionary where the Japanese language code was entered incorrectly and ArchivesSpace was rejecting language codes it did not recognize. Fixing the typo fixed the issue. With Alicia's approval I ran this in production with no issue. |

# Review

## Data Details
- 356 records have 'mul' as their language material id
	- 169 archival objects
	- 187 resources
- 181 of the 356 records have a language note
## Communication
| Name | Position | Notes |
| ---- | -------- | ----- |
| Alicia Detelich  | Assistant Director of Special Collection Metadata Services, Special Collections Technical Services | - Helped diagnosis the error in testing <br> - Got approval for running in production |
## Results
Completed successfully with no errors. Ran on 356 records and updated the 181 records with language notes.

# References

- [Github Issue - Update 'mul' languages ](https://github.com/orgs/Yale-DMAC/projects/1?pane=issue&itemId=20786181)
