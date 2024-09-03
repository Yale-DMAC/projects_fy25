# 655$5 Report
Last updated on 08/28/2024 by Kylene Hutchinson.

| Start Date | End Date | Contributors | Informed Stakeholders |
| ---------- | -------- | ------------ | --------------------- |
| 08/27/2024 | 08/28/2024 | Kylene Hutchinson | Zoe Dobbs |

# Overview
## Problem Statement
Zoe Dobbs (Cataloging/Metadata Librarian, Beinecke Special Collections Technical Services) requested a report of Voyager MARC records for her use.
## Goals
Create a spreasheet report of the following fields for any record containing a 655$5:
- 655$a
- 655$5
- Bib number
- Location
- Call number

this was later updated to:
- 655$a
- 655$5
- Bib number
- MFHD ID

# Background
Not much background, just a simple request for the current state of the data from someone who doesn't have access to the SQL databases.

# Process
See [Report_655_5.py](Report_655_5.py) for details.
- Create a SQL query that will grab the requested data
- Save the data into an Excel file

# Notes
| Date | Highlight | Notes |
| ---- | --------- | ----- |
| 08/27/2024 | Report Requested | Zoe sent the email at the end of the day. |
| 08/28/2024 | Assigned and Coded | I offered to fulfill the request and was given approval from Alicia. I wrote a quick SQL query, but it does require python use to use the getsubfield function so I passed it through python and saved to an excel sheet |
| 08/28/2024 | Update | Zoe asked for a change made to the data so instead of Location Code and Call number it pulled the MFHD id |

# Review
## Communication
| Name | Position | Notes |
| ---- | -------- | ----- |
| Zoe Dobbs | Cataloging/Metadata Librarian, Beinecke Special Collections Technical Services | Requested the report and requested an update to the report |
| Alicia Detelich | Head of SCMS, Beinecke Special Collections Technical Services | Approved assignment |
## Results
Submitted the [initial report](240828_655_5.xlsx) file to Zoe containing all requested fields for records containing a 655$5.  
Submitted the [updated report](240828_655_5_mfhd.xlsx) file to Zoe with the requested changes.
