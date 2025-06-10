# Roadmaps Multiple Languages
Last updated on 06/10/2025 by Kylene Hutchinson.

| Start Date | End Date | Contributors | Informed Stakeholders |
| ---------- | -------- | ------------ | --------------------- |
| 04/23/2025 | 06/05/2025 | Kylene Hutchinson | Mary Caldera, Alicia Detelich |

# Overview
## Problem Statement
A collection of road maps in ArchiveSpace need additional languages added to their records.
## Goals
- Extract Languages from Comments
- Identify records
- Add additional languages to archival objects.
# Background
A spreadsheet containing a list of road maps was supplied. This spreadsheet had the additional comments tucked away in comments instead of in a column, which provided a challenge to extract as these are designed to not be machine readable. Further, no archival object ids were provided and many rows in the spreadsheet contained identical information due to the fact that multiple records in this series have identical identifying information despite being from different records. This spreadsheet was originally used to create the finding aid for the resource.


# Process
See [roadmaps_lang.py](roadmaps_lang.py), [250605_report.csv](250605_report.csv), [Excel_Commment_Extraction.md](Excel_Comment_Extraction.md), Original Spreadsheet: [Road_Maps_Boxes_1_240_COMPLETE_FILE.xlsb](Road_Maps_Boxes_1_240_COMPLETE_FILE.xlsb), Updated Spreadsheet: [Road_Maps_Boxes.csv](Road_Maps_Boxes.csv)
- Extract Additional Languages from Excel Spreadsheet comments and move them into a usable column.
- Manually clean up language fields and use ArchivesSpace appropriate language codes.
- Manually identify archival object ids for each row.
- Using API get the archival object JSON
    - Make a copy of the record and save it to file as a backup.
    - Add json for each additional language to the archival object
    - Using API post the update archival object.
    - Create a report on each record updated.

# Notes
| Date | Highlight | Notes |
| ---- | --------- | ----- |
| 04/23/2025 | Submission | Mary Caldera submitted the email to SCMS requesting this project be completed. This originally slipped under the radar as we had recently transitioned to using Service Now and had not yet set up procedures in moving these requests into Service Now |
| 05/13/2025 | Assigned | Alicia Detelich and Kylene Hutchinson discussed this project and Kylene began work on it. |
| 05/15/2025 | Comment Extraction | We were able to extract the comments into a column in the spreadsheet and clean them up to be machine readable. |
| 05/16/2025 | Contact | Reached out to Mary Caldera about record identification but never received a response. |
| 05/27/2025 | Identifying Records | Began working on identifying records the best we could with the limited information. |
| 05/30/2025 | Identification Completed | Finished matching ids with records. This was a manual process using a list filtered down with SQL. |
| 06/02/2025 | Python | Began writing python code to update these records. |
| 06/03/2025 - 06/05/2025 | Testing | Performed careful tests and made adjustments as needed. |
| 06/05/2025 | Updated | Updated all records. |

# Review

## Data Details
 - 360 records need updating in production
## Communication
| Name | Title | Notes |
| ---- | ----- | ----- |
| Alicia Detelich  | Associate Director of Special Collections Metadata Services in Special Collections Technical Services | Assigned project, assisted with extracting comments. |
| Mary Caldera | Associate Director of Archival Description Unit in Special Collections Technical Services | Submitted project. We reached out about record identification but did not get a response. |
## Results
360 records were updated without incident.

