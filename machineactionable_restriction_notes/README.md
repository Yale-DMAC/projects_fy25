# Machine-Actionable Restriction Notes
Last updated on 11/14/2024 by Kylene Hutchinson.

| Start Date | End Date | Contributors      | Informed Stakeholders |
| ---------- | -------- | ----------------- | --------------------- |
| 11/12/2024 | 11/14/2024 | Kylene Hutchinson | Alicia Detelich       |
# Overview
## Problem Statement
Some access restriction notes in ArchivesSpace contain dates in the free-text part of the note, but nothing in the structured date part of the note. In order to facilitate management of this data in ArchivesSpace and Aeon, we need to convert all free-text dates to structured dates.
## Goals
 - [ ] Identify all access restriction notes which have a date in the free-text field and no date in the structured field
- [ ]  Add the date to the structured field
# Background
Occasionally individuals forget to enter the structured data in the Access Restriction notes. This can cause issues with other systems, so we decided to identify and repair notes missing this structured data.

# Process
See [machineactionable_restriction_notes.py](machineactionable_restriction_notes.py) and [241114_update.csv](241114_update.csv)
- Write a SQL query that grabs resources and archival objects with access restriction notes containing dates in the free text but no structured end date. Filter out notes that contain multiple dates as these need manual review.
- Save URIs from the SQL query in a csv
- Save backups of the URIs in a folder
- Check to ensure you are grabbing the correct note from the URI
- Use regexp to find a date pattern in the free text then convert it into a number format yyyy-mm-dd
- Add the end key to the rights_restriction dictionary using the converted date as the value.
- Save info about updates and errors to csv files.
# Notes

| Date       | Highlight       | Notes                                                                                                                                                                                                                                                                                                  |
| ---------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 11/12/2024 | Started Project | Began investigating data and spoke to Alicia about potential complications with multiple dates in the free text                                                                                                                                                                                        |
| 11/13/2024 | Explored data   | Records the total notes with this issues and details about them. Looked for any other complications besides multiple dates. Found abbreviated dates.                                                                                                                                                   |
| 11/14/2024 | Testing         | Tested code in the Test Environment. Originally had complications with abbreviated dates and 'rights_restriction' dictionaries missing. Made some changes to the code and these updated smoothly. Only one came back with a 409, due to the fact it is locked from editing due to to being suppressed . |
| 11/14/2024 | Complete | Ran the code in Production with permission from Alicia. The 28 notes with 2 dates are a seperate project as these are likely dates that need to be transferred from parent to children. |

# Review

## Data Details
- 509 total
	- 405 in repo 12
	- 90 in repo 11
	- 2 in repo 5
	- 5 in repo 4
	- 7 in repo 7
- 28 have more than 1 end date
	- 19 from repo 12
	- 4 from repo 7
	- 5 in repo 11
- 481 records that have only 1 date in every repo
	- 95 records not in repo 12
	- 386 in repo 12
		- 54 resources
		- 332 archival objects
	- 85 in repo 11
		- 30 resources
		- 55 archival objects
	- 2 in repo 5 (1 of each)
	- 5 in repo 4
		- 1 resource
		- 4 archival objects
	- 3 archival objects in repo 7
## Communication
| Name            | Position                                                   | Notes                                                      |
| --------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| Alicia Detelich | Assistant Director of Special Collection Metadata Services | - Assigned Project<br>-Approved Running Code in Production |
## Results
Ran in production without any issue. Free-Text dates were copied into Structured Data dates on Conditions Governing Access notes. Ran on 481 records throughout 5 repositories in ArchivesSpace. One record returned a 409, but that is because it is suppressed and cannot be edited. 

# References

- [Github Issue: Add machine-actionable restrictions for RUs with free-text-only notes](https://github.com/orgs/Yale-DMAC/projects/1/views/1?pane=issue&itemId=23638969)
