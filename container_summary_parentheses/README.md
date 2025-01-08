# Container Summaries Parentheses
Last updated on 01/08/2025 by Kylene Hutchinson.

| Start Date | End Date | Contributors | Informed Stakeholders |
| ---------- | -------- | ------------ | --------------------- |
| 01/06/2025 | 01/08/2025 | Kylene Hutchinson | Alicia Detelich |

# Overview
## Problem Statement
Some values in the container summary field of extent subrecords have parentheses which are not needed. They previously were added for display purposes, but served no other purpose and so should be removed.

## Goals
- Identify all container summaries with parentheses
- Remove parentheses from container summaries

# Background
The container summary extent used to display beside the title in public discovery so parentheses were added to make the display less confusing. This is no longer the case, and container summaries are not filled out with parentheses anymore. For consistency's sake, we are cleaning up these older extent subrecords by removing these extraneous parentheses.


# Process
See [cs_parentheses.py](cs_parentheses.py), [250106_updates.csv](250108_updates.csv)
- Create a SQL Query that identifies records with extent summaries containing parentheses at the beginning of the summary.
- Use API and regexp to update container summaries to remove the parentheses.
    - If a record is suppressed, unsuppresses the record before updating then resuppresses.
    - Checks that container summary starts with a '(' before editing.
- Save data about the updates to a csv, and create backup files of records before editing.

# Notes

| Date | Highlight | Notes |
| ---- | --------- | ----- |
| 01/06/2025 | Wrote and Tested code | Wrote code to update theses and tested it in the Test Environment. |
| 01/07/2025 | Updated Code | Updated the code to account for suppressed records. |
| 01/07/2025 | Approved | Spoke with Alicia and got approval to run in production. |
| 01/08/2025 | Complete | Ran code in production and completed project. |

# Review

## Data Details
- 7,874 archival objects with parentheses
- 2,115 accession records with parentheses
- 4,338 resource records with parentheses
- 0 digital objects with parentheses

## Communication
| Name | Position | Notes |
| ---- | -------- | ----- |
| Alicia Detelich | Head of Special Collections Metadata Services in Beinecke | Assigned project, provided background, gave approval. |

## Results
Updated 14,327 records to remove parentheses for display purposes based on the fact the parenthesis is at the beginning of the container summary (So '(1 box)' and not '1 Optical Disc (DVD)').
12 records have errors that needed to be manually resolved; 10 due to missing language materials information, 1 due to a schema error, and 1 due to an extent note date error.

# References
- [Github Issue - Remove parentheses in container summaries in extent records](https://github.com/orgs/Yale-DMAC/projects/1/views/1?pane=issue&itemId=21043742)
