# Divinity Library Preferred Citation
Last updated on 08/26/2024 by Kylene Hutchinson.

| Start Date | End Date   | Contributors      | Informed Stakeholders         |
| ---------- | ---------- | ----------------- | ----------------------------- |
| 08/14/2024 | 08/26/2024 | Kylene Hutchinson | Alicia Detelich, Scott Libson |
# Overview
## Problem Statement
Divinity Library has been using the wrong title in ArchiveSpace's preferred citation field. They have been entering 'Yale Divinity School Library' instead of 'Yale Divinity Library'.
## Goals
Replace all instances of Yale Divinity School Library with Yale Divinity Library in ArchivesSpace's preferred citation field.
- Identify Divinity Library preferred citation notes with incorrect name
- Create/Update spreadsheet with correct name
- Update notes
# Background
The Divinity Library was originally called the 'Yale Divinity School Library' but sometime during 2011-2019 the name was changed to 'Yale Divinity Library', dropping the school from the name. Unfortunately, Divinity Librarians continued to use the Divinity School version of the name until Scott Libson (Divinity Special Collections Librarian) spotted the error and contacted SCMS about correcting the records.

# Process
See [divinty_prefercite.py](divinity_prefercite.py) for code used to update records.
- File queries the ArchivesSpace database for URIs of resources with Notes containing Preferred Citation and 'Divinity School Library' in the Divinity Library Repository.
- Then creates an excel file containing the URI, note field, and backup api data of the entire record.
- Finally it uses regex to update the Preferred Citation Note contents from 'Divinity School Library' to 'Divinity Library' and posts to update via the API.


# Notes

| Date       | Highlight               | Notes                                                                                                                                                                                                                                                        |
| ---------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 08/14/2024 | Introduction to Project | Alicia Detelich introduced and assigned this project during a SCMS unit meeting. Project was assigned as due by the end of the month (2 weeks).                                                                                                              |
| 08/15/2024 | Testing                 | Created a query that would pull Preferred Citation Notes, and wrote code that would update the citations. Next step is to explore the data to make sure I'm grabbing everything and not mistakenly updating anything that shouldn't be updated.              |
| 08/16/2024 | API/Atools              | Some confusion over the baseurl for the API. Teams didn't include /api as part of the url so I was using an incomplete url when trying to get tools to work. Fixed it and can now connect.                                                                   |
| 08/19/2024 | API code                | Wrote code to call a specific URI and update the preferred citation note contents from 'Yale Divinity School Library' to 'Yale Divinity Library'.  Can use the SQL code to pull a list of URIs, then use those URIs to call the API records and update them. |
| 08/20/2024 | Reviewing Data and Code | Spending time reviewing the pulled data and updating the code to remove or add records as needed.                                                                                                                                                            |
| 08/21/2024 | Testing                 | Tested the code with a few Test Server URIs. Everything updated as expected. Tried to add a step where the old data is added to the spreadsheet as backup but kept running into the problem where it would only add the updated data.                        |
| 08/22/2024 | Meeting                 | Met with SCMS unit and presented my work. Got go ahead from Alicia to update production cite notes after doing a final test in the Test server.                                                                                                              |
| 08/23/2024 | Finalize                | Make any last edits to the code and performed the final test in the Test Server. Will wait until Monday to perform in Production.                                                                                                                            |
| 08/26/2024 | Run job                 | Updated 356 Records in production.                                                                                                                                                                                                                           |

# Review

## Data Details
| Data                                    | Notes                                                                                                                                                                                        |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 360 records found                       | these included MSSA records.                                                                                                                                                                 |
| 3 MSSA records found by mistake         | structured as 'Divinity School, Yale University, ... Manuscripts and Archives, Yale University Library.'                                                                                     |
| 356 records found                       | Updated SQL to restrict to just Divinity Repository (actually grabs 357 but one is a repeat because it has 2 preferred cite fields)                                                          |
| 1 record has 2 preferred Citation notes | Preferred Citation notes says the same exact thing (repositories/4/resources/5561)                                                                                                           |
| 362 Resources                           | Searching for "Yale Divinity" under notes in the web client returned 548 results, 362 being Resources                                                                                        |
| 361 Resources                           | Searching for "Yale Divinity School" under notes in the web client returned 524 results, 361 being Resources                                                                                 |
| 6 records not found in SQL              | Found 6 records via the web client that contain "Yale Divinity" in notes that were not found by SQL query. 2 had the correct preferred citation, the other 4 had no preferred citation note. |
| 1 of the above 6                        | Is a collection called 'Yale Divinity School Library Records' (/repositories/4/resources/13485) and has many notes and fields using Divinity School Library.                                 |
| 1 of the above 6                        | Has a Processing Information Note that contains the same text as preferred citations with 'Yale Divinity School Library' (/repositories/4/resources/231)                                     |

## Communication
| Name            | Position                                                  | Notes                                   |
| --------------- | --------------------------------------------------------- | --------------------------------------- |
| Scott Libson    | Divinity Special Collections Librarian                    | Submitted emails requesting correction. |
| Alicia Detelich | Head of Special Collections Metadata Services in Beinecke | Provided background and tools.          |

## Results
Created a backup of the original API data for each ArchivesSpace record that was updated. Prefer Citation Note was updated from 'Yale Divinity School Library' to 'Yale Divinity Library' in 356 records.

# References

- [Github Issue - Divinity preferred citation note updates](https://github.com/orgs/Yale-DMAC/projects/1/views/1?pane=issue&itemId=74792677)
- [Github Repo - Divinity preferred citation Python File](divinity_prefercite.py)
