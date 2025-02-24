# Curator Report
Last updated on 02/24/2025 by Kylene Hutchinson.

| Start Date | End Date | Contributors | Informed Stakeholders |
| ---------- | -------- | ------------ | --------------------- |
| 01//2025 | 02/07/2025 | Kylene Hutchinson | Jasmine Jones |

# Overview
## Problem Statement
"SCLT is working on reviewing access restriction issues. We would like a report from ArchivesSpace and Voyager from the following fields and with the following parameters. Please only provide reporting for Beinecke and MSSA materials."

## Goals
Create reports for ArchivesSpace and Voyager records from the Beinecke and MSSA.

***Voyager***
- 506 in the bib record there is an occurence of the word, "curator"
- OR the statistical category/ies in the item record are:
    - RestrictedCurApprSpecColl
    - RestrictedSpecColl
    - RestrictedFragileSpecColl

***ArchivesSpace***
Collections or specific children records where:
- Conditions governing access there is an occurence of the word, "curator"
- OR Local access restriction database values are:
    - RestrictedCurApprSpecColl
    - InProcessSpecColl
    - ColdStorageBrbl

# Background


# Process
See [archivesspace_access_report.sql](archivesspace_access_report.sql), [voyager_access_report.py](voyager_access_report.py), [250206_Voyager_Access_report.csv](250206_Voyager_Access_report.csv) and [250205_aspace_access_report.csv](250205_aspace_access_report.csv)
- Create a SQL report for Voyager
- Create a SQL report for ArchivesSpace


# Notes
(Keep track of meetings and formal communication of the project. Also include any highlights in the project's progress such as roadblocks or changes in approach.)

| Date | Highlight | Notes |
| ---- | --------- | ----- |
| 01/29/2025 | Requested | Request for Reports was submitted to Service Now |
| 01/30/2025 | Communication | Clarified some details about the parameters with Jasmine. |
| 02/04/2025 | Submitted for Review | Sent files to Jasmine for review. |
| 02/05/2025 | Communication | Jasmine requested some additional columns be added to the final report. Alicia introduced me to Voysearch to help get the data for the requested columns. |
| 02/06/2025 | Completed | Submitted the updated reports to Jasmine. |
| 02/18/2025 | Closed | Ticket was closed. Jasmine requested the files be resent since she couldn't find the ticket once closed. |

# Review

## Data Details
Include details about the amount of records, shared traits, collection information, etc.
## Communication
| Name | Position | Notes |
| ---- | -------- | ----- |
| Alicia Detelich  | Assistant Director of Special Collection Metadata Services, Special Collections Technical Services | - Provided Voysearch documentation |
| Jasmine Jones | Director of Special Collections Technical Services | - Requested Report<br>- Added clarifications |

## Results
5,850 ArchivesSpace records and 8,601 Voyager records were provided as two separate reports.

# References

- [Service Now Ticket: Report on access restrictions in Voyager and ASpace](https://yale.service-now.com/nav_to.do?uri=sc_req_item.do?sys_id=c7db0517939fde105ddef5bd1dba10c1)
