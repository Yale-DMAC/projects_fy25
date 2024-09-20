Last updated on 09/16/2024 by Kylene Hutchinson.
**Tags:**

| Start Date | End Date   | Contributors      | Informed Stakeholders                            |
| ---------- | ---------- | ----------------- | ------------------------------------------------ |
| 09/05/2024 | 09/20/2024 | Kylene Hutchinson | Alicia Detelich, Jess Quagliaroli, Francis Lapka |
# Overview
## Problem Statement
YCBA has 2 repos Rare Books and Manuscripts (RBM) and Institutional Archives (IA) and wants them merged. Alicia performed the merge in test before going on leave with no problems, but the process failed in production. We need to determine why it failed and fix the issue so it can be successfully merged.
Alicia thinks Test probably didn't have Preservica objects, but there are some in production. One repo has a bunch of Preservica objects, so we might want to merge into that one so uris don't change.
## Goals
- Identify which repository (IA or RBM) has the most Preservica digital objects: set this as the target repository
- Identify and resolve merging errors
- Re-run merge script in production
# Background
Process was originally performed in January 2024 but failed in Production.

-Why do they need to merge?-
# Process
See [transfer_resources_updated.py](transfer_resources_updated.py), [transfers_sql_query.sql](transfers_sql_query.sql), [transfers.csv](transfers.csv), and [transfers_success.csv](transfers_success.csv) for files used during the merge.  
See [original/transfer_resources.py](original/transfer_resources.py), [original/ycba_transfers_prod.csv](original/ycba_transfers_prod.csv), and [original/ycba_transfers_prod_errors.csv](original/ycba_transfers_prod_errors.csv) for the original attempt. 

- Pull a list of resources using a SQL query and save it to a csv with columns for the URI and the target_repo.
- Use API to create backups and transfer resources to the target repository.
- Create two files, one for successful transfers and the other for errors.
	- If transfer is successful, URI and target_repo data will be added to the success file, along with an Info column containing the transfer status.
	- If transfer is unsuccessful, the URI and target_repo will be added to the error file, along with an Info column containing the error message.
- Back ups of the json files will be saved to a backup folder.

# Notes

| Date       | Highlight            | Notes                                                                                                                                                                                                                                                                                     |
| ---------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 09/09/2024 | Reviewing Files      | Reviewed over the provided files and read up on transferring repos in archivesspace via api                                                                                                                                                                                               |
| 09/10/2024 | Tested Code          | Used Original code, edited down to work with my setup and tested in the test environment using area_studies since RBM had already been merged and a sync is happening tomorrow. All files transferred successfully. Transferred them back to Area_Studies afterwards.                     |
| 09/10/2024 | Identified the Error | The production test error was the result of an identifier duplication. The test resource had an identifier of 0000 and a resource in the new repository had the same identifier on a different resource. I updated the identifier to something else and the file successfully transferred. |
| 09/11/2024 | Gathering Info       | Spoke with Alicia about the previous errors. She said the first two records failed during her attempt at transferring Production records. One of which was the previously identified error, but couldn't recall what the second error was.                                                |
| 09/12/2024 | Transfer Test        | Tested Transferring 5 records in Production. No errors returned.                                                                                                                                                                                                                          |
| 09/13/2024 | API down             | API on the test instance went down after an update and sync. Tech Lead out until next week, so final testing is on hold.                                                                                                                                                                  |
| 09/20/2024 | API up!              | Test API available after being down for a week. Did a test merge of the repos, and everything merged smoothly. Got approval from Alicia to perform in Production. Production transfer ran smoothly, no errors.                                                                                                                         |

# Review

## Data Details
- RBM has 86 resource records, 10 digital objects, and 11,048 archival objects
	- 9 digital objects have Preservica links
- IA has 61 resource records, 3,351 digital objects, and 58,201 archival objects
	- 3350 digital objects have Preservica links
## Communication
| Name             | Position                                                   | Notes                                                                              |
| ---------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Alicia Detelich  | Assistant Director of Special Collection Metadata Services | - Assigned Project<br>- Confirmed details about previous errors<br>-Approved Merge |
| Jess Quagliaroli | Chief Archivist, Yale Center for British Art               | Informed of Successful Repo Merge                                                  |
| Francis Lapka    | Senior Catalogue Librarian, Yale Center for British Art    | Informed of Successful Repo Merge                                                  |
## Results
Original errors seem to be the result of an identifier being duplicated between the two merging repos (trying to move repo/2/0000 into repo 3 when repo/3/0000 already exists). After fixing the duplicated identifier, everything was able to smoothly transfer all 86 records from RBM to IA.

# References

- [Github Issue - YCBA repository merge ](https://github.com/orgs/Yale-DMAC/projects/1/views/1?pane=issue&itemId=44064279&sortedBy%5Bdirection%5D=asc&sortedBy%5BcolumnId%5D=Assignees)
