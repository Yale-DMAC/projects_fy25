# Access Restrictions Report
Last updated on 02/04/2025 by Kylene Hutchinson.

| Start Date | End Date | Contributors | Informed Stakeholders |
| ---------- | -------- | ------------ | --------------------- |
| 01/30/2025 | 02/04/2025 | Kylene Hutchinson | Alicia Detelich, Jasmine Jones |

# Overview
## Problem Statement
SCLT needs a report on access restrictions in ArchivesSpace and Voyager for Beinecke and MSSA materials.

## Goals
Voyager
- 506 in the bib record there is an occurence of the word, "curator"
- Or the statistical category/ies in the item record are:
    - RestrictedCurApprSpecColl
    - RestrictedSpecColl
    - RestrictedFragileSpecColl

ArchivesSpace
Collections or specific children records where the: 
- Conditions governing access there is an occurence of the word, "curator"
- Or Local access restriction database values are:
    - RestrictedCurApprSpecColl 
    - InProcessSpecColl 
    - ColdStorageBrbl 

# Background
SCLT is working on reviewing access restriction issues and needs a report to review.


# Process
See [aspace_access_report.sql](aspace_access_report.sql), [voyager_access_report.sql](voyager_access_report.sql), [voyager_access_report.py](voyager_access_report.py), [aspace_access_report.csv](aspace_access_report.csv), [voyager_access_report.csv](voyager_access_report.csv)
- Query ArchivesSpace SQL database.
- Save to a csv.

- Query Voyager SQL database.
- Create a list of bib_ids with more than one 506 in the bib record.
- Use VoySearch to search the list of bib_ids for the word 'curator' in the 506s.
- Save to a csv.

# Notes
| Date | Highlight | Notes |
| ---- | --------- | ----- |
| 01/30/2025 | Report started | Jasmine submitted request for a report. Completed ArchivesSpace report. |
| 01/31/2025 | Voyager Report | Running reports to gather bib ids with multiple 506s. Repeat fields function returning a value error, and get tag function only searches first tag in the record. |
| 02/03/2025 | Update Report | Spoke with Alicia about Voyager locations and ideas for searching multiple 506s. Came up with the idea to use Voysearch. |
| 02/04/2025 | Update Report | Rerunning reports with updated list of voyager locations. |

# Review

## Data Details
 Voyager:
 - 7,612 total items, 2,034 total bibs
 - 7,436 items have one of the three statistical categories
 - 1,374 bibs have a 506 with 'curator' mentioned.
 - 11 MSSA and 7,600 Beinecke

 ArchivesSpace:
 - 5,849 total records
 - 1,099 records mentioned a 'curator' in the access restriction note but did not have one of the three database values
 - 4,704 records do no mention 'curator
 - 46 have both curator and a database value
 - 4,622 MSSA and 1,227 BRBL

## Communication
| Name | Position | Notes |
| ---- | -------- | ----- |
| Jasmine Jones | Director of Special Collections Techincal Services in Beinecke | Checked in with Jasmine to ask if there was an 'or' missing from one of the parameters and she confirmed there was. |
| Alicia Detelich | Head of Special Collections Metadata Services in Beinecke | Checked in about Voyager locations and she introduced me to VoySearch. |

## Results
Created two reports, one from Voyager (7,612) the other from ArchivesSpace (5,849). Contains IDs, title, locations, call numbers, database/statistical category, etc. The 506 was not included in the Voyager columns due to the difficulty of grabbing the correct field via SQL, but the report still includes bibs that have the appropriate 506.

# References

- [ServiceNow: Report on access restrictions in Voyager and ASpace](https://yale.service-now.com/nav_to.do?uri=sc_task.do?sys_id=89ebc9df3b135250a84bf547f4e45a22)
