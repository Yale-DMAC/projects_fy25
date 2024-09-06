# SC Assessment Backlog Project
Last updated on 08/23/2024 by Kylene Hutchinson.

| Start Date | End Date   | Contributors      | Informed Stakeholders       |
| ---------- | ---------- | ----------------- | --------------------------- |
| 08/14/2024 | 08/23/2024 | Kylene Hutchinson | Alicia Deletich, Ellen Doon |

# Overview
## Problem Statement
Ellen Doon (Assistant Director of Access Services and Operations at Beinecke) has requested a report of Records containing an assessment note of "SPECIAL COLLECTIONS BACKLOG SURVEY 2023" in ArchivesSpace. She wishes to use this report to determine how much of specific collections were surveyed.
## Goals
User would like a report summarizing: 
- extents
- number of collections that have certain format boxes checked
- the number of assessments per a repository
- number of assessments with particular formats or conservation issues
- number of assessments with research value rating 7 or higher but access rating 3 or lower, etc.

User would like three reports of assessments:
- Area Studies & Humanities assessment data on its own
- Manuscripts and Archives assessment data on its own
- All Assessment data
OR one report in which Area Studies & Humanities and MSSA numbers are isolated.
# Background
The special collections libraries have been doing a backlog survey. In ArchivesSpace, records that were surveyed had an Assessment Note added on labeled 'SPECIAL COLLECTIONS BACKLOG SURVEY 2023'. A Summary Report was created in August 2023, but The Area Studies & Humanities Department (previously known as DASHRS - Department of Area Studies and Humanities Research Studies) had not completed their assessments in time for that last report.
All Purpose of Assessment notes should have the Backlog Survey label mentioned above, but it is notable that likely all the assessments in the Area of Studies repository should be related to this project so it should be easy to grab any mislabeled assessments. University Archives assessments have been kept track of, so Ellen Doon can gather a list if necessary.

Alicia Detelich (Head of Special Collections Metadata Services) has included a [SharePoint folder](https://tinyurl.com/ycyep2up) containing information about the August 2023 report, including the SQL code used, summary report created, and spreadsheet of data.

# Process
See [SC_Assessment_Backlog_Report.py](SC_Assessment_Backlog_Report.py), [SC_Assessment_Backlog_SQL.py](SC_Assessment_Backlog_SQL.py), and [SC_Assessment_Backlog_Other_SQL.py](SC_Assessment_Backlog_Other_SQL.py) for code used to update records.
- Queries the ArchivesSpace Database using SQL to pull two DataFrames, one for all repositories and the other for just Area_Studies and MSSA.
- Summarizes the data into counts based off formats, extents, conservation issues, etc. as a whole and per a repository
- Saves all the summaries and the raw data into an Excel File with individual Sheets.

# Notes

| Date       | Highlight               | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 08/14/2024 | Introduction to Project | Alicia Detelich introduced and assigned this project during a SCMS unit meeting. Project was assigned as due by the end of the month (2 weeks).                                                                                                                                                                                                                                                                                          |
| 08/15/2024 | Review                  | Reviewed the SQL code that Alicia provided and the summary files. Ran some test queries and noticed that Area Studies repository was not showing up on the list. Querying for any assessment in the Area Studies repository only returned one result. Awaiting Alicia to give me access to unpublished repositories so I can look into this in ASpace.                                                                                   |
| 08/16/2024 | Notes                   | repository.name to isolate by repository, assessment.purpose to isolate by backlog tag                                                                                                                                                                                                                                                                                                                                                   |
| 08/19/2024 | Code Test               | Using Alicia's provided SQL code, I wrote a python script that queries the SQL database and returns two excel files, one reviewing all repositories and the other just the MSSA and Area_Studies repositories. The first worksheet is the results of the SQL query, but the subsequent sheets are summaries of the data. (For example, sheet two is a count of records by Repository name, and sheet 3 is a count of format types, etc.) |
| 08/20/2024 | Review and Update       | Tested my code for creating summary reports and came back equal to Alicia's during tests. Only I realized some cells had multi values so I had to backtrack and spilt cells before doing value counts. Added in code to replace null values with 'None' in the summarize code so the summaries would keep track of number of records with no input in a column.                                                                          |
| 08/22/2024 | Meeting                 | Met with SCMS unit, and briefly presented my work. Had a few lingering questions answered by Alicia and got the go ahead to email results to Ellen Doon.                                                                                                                                                                                                                                                                                 |
| 08/23/2024 | Finalize and Submit     | Made a few minor changes - such as changing the where statement from repo names to repo id, and added in existing description checkbox counts to the summary tabs. Then emailed the results to Ellen Doon cc'ing Alicia.                                                                                                                                                                                                                 |

# Review

## Data Details
- Area_Studies repository has 0 assessments. Does not show up in the SQL tables or on the website.
- MSSA has 16.
- Total 452.
- Previous Report Total: 346
## Communication
| Name            | Position                                                         | Notes                                                                                                                                                                         |
| --------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ellen Doon      | Assistant Director of Access Services and Operations at Beinecke | - Submitted emails requesting reports.<br>- I sent the excel sheets of the reports she requested<br>- She is reaching out to the Area Studies folks to find out what happened |
| Alicia Detelich | Head of Special Collections Metadata Services at Beinecke        | Provided background and files to review.                                                                                                                                      |
## Results
Submitted two excel files to Ellen Doon consisting of 12 sheets each. The first sheet was the results of the SQL query, and the other 11 sheets were the requested summaries:
- Repository Counts
- Conservation Issue Counts
- Conservation Issue Counts by Repository
- Format Counts
- Format Counts by Repository
- Extent Value Counts
- Extent Value Counts by Repository
- Existing Description Counts
- Existing Description Counts by Repository
- Number of Assessments with a Research Value 7 or higher but Intellectual Access rating of 3 or lower
- Number of Assessments with a Research Value of 7 or higher but Physical Access rating of 3 or lower

The first file was for all the repositories in ArchivesSpace.
The second file was for just 'Manuscripts and Archives' and 'Area Studies'. However, 'Area Studies' currently has no assessments in ArchivesSpace so the file currently only reports on Manuscripts and Archives. Code should work to create a file for both should it be rerun after Area Studies has some assessments added in.

# References

- [Github Issue - Special Collections Backlog Reporting](https://github.com/orgs/Yale-DMAC/projects/1/views/1?pane=issue&itemId=74105188)
- [SharePoint - Special Collections August 2023 Backlog Reporting](https://tinyurl.com/ycyep2up)
