# Analysis of MSSA Dissertation Holdings with Blank Call Numbers
Last updated on 2025-04-25 by Will Nyarko.

| Start Date | End Date | Contributors | Informed Stakeholders |
| ---------- | -------- | ------------ | --------------------- |
| 2025-04-23 | 2025-04-25 | Will Nyarko | Alicia Detelich-Boersig, Todd Fell |

# Overview
## Problem Statement
Voyager holding records for MSSA Dissertations (`LOCATION_CODE` = `lsfmssr`) exist without associated call number information (e.g., missing `$h` or `$i` in MARC field 852). This results in retrieval issues for these materials in Aeon. The ServiceNow ticket included a screenshot ([Screenshot%202025-02-21%20111455.png](Screenshot%202025-02-21%20111455.png)) illustrating this exact scenario: an 852 field containing only a `$b` subfield for the location.

## Goals
### Primary Goal
- Quantify the number of MSSA dissertation holding records lacking a display call number.

### Supplementary Goals
- Extract associated bibliographic metadata (BIB_ID, TITLE, AUTHOR, PUB_DATE, PUBLISHER, PUB_PLACE) for these records.
- Analyze the characteristics of the extracted data, focusing on uniqueness, data quality (e.g., publication dates), and common values (e.g., publisher, place).
- Provide summary data and reports to document the findings.
- Organize the analysis scripts and outputs logically.

# Background
A request was made via ServiceNow ticket (RITM0394736) to get a count of MSSA dissertation holdings (`lsfmssr`) without call numbers due to Aeon retrieval problems. Initial exploration confirmed that a blank `display_call_no` in the `MFHD_MASTER` table for `LOCATION_ID` = 248 (corresponding to `LOCATION_CODE` = `lsfmssr`) reliably identifies the target records. Records lacking `$h` or `$i` subfields in the MARC 852 field, often only containing `$b lsfmssr`, exhibit this blank `display_call_no`.

A SQL query was developed to join `MFHD_MASTER`, `BIB_MFHD`, and `BIB_TEXT` tables to extract the relevant holding and bibliographic data for analysis.

# Process
- **Data Extraction:** A SQL query (located in `scripts/sql-processing/get_blank_call_num_mssa_holdings.sql`) was run against the Voyager database (`YALEDB` schema) to select the target records.
- **Data Export:** The results were exported to a CSV file (`data/mssa_diss_blank_mfhd__*.csv`) for offline analysis.
- **Data Analysis:** Python scripts (located in `scripts/python-postprocessing/`) were developed to analyze the exported data. While manual analysis in tools like Excel is possible, Python was chosen for its efficiency in handling the dataset size and generating detailed logs (`logs/`) and summary data files (`data/`).
- **Reporting:** A summary report (`report_mssa_dissertation_blank_holdings.md`) was created to document the findings.
- **Organization:** Project files were organized into dedicated directories: `data/` for data files, `logs/` for script logs, and `scripts/` (containing `python-postprocessing/` and `sql-processing/`) for analysis code.

# Notes
(Keep track of meetings and formal communication of the project. Also include any highlights in the project's progress such as roadblocks or changes in approach.)

| Date | Highlight | Notes |
| ---- | --------- | ----- |
| 2025-04-23 | Initial Query & Scripting | Developed SQL, exported data, started Python analysis. |
| 2025-04-25 | Refinement & Organization | Completed scripts, generated report, organized directories. Preparing documentation to highlight approaches used. Stay tuned! |

# Review

## Data Details
- The analysis focuses on **11,564** holding records from `MFHD_MASTER` where `LOCATION_ID` = 248 and `DISPLAY_CALL_NO` is NULL or blank.
- Associated data includes `MFHD_ID`, `BIB_ID`, `TITLE`, `AUTHOR`, `BEGIN_PUB_DATE`, `END_PUB_DATE`, `PUBLISHER`, `PUB_PLACE`.
- See `report_mssa_dissertation_blank_holdings.md` for detailed findings on data characteristics (duplicates, date ranges, common publishers/places).

## Communication
- Initial request via ServiceNow ticket.

## Results
- Successfully quantified the target holding records.
- Generated detailed logs (`logs/`) and summary data files (`data/`) analyzing key metadata fields.
- Produced a comprehensive report (`report_mssa_dissertation_blank_holdings.md`) summarizing the findings.
- Established a repeatable process for analyzing this dataset.

# Resources and References

- `report_mssa_dissertation_blank_holdings.md`: Summary report of the analysis results.
- [ServiceNow Ticket Screenshot](Screenshot%202025-02-21%20111455.png): Illustrates the missing call number data in Voyager.
- [MFHD Record Creation Guidelines (Yale)](https://web.library.yale.edu/cataloging/manuscript/mfhd-record)
- [MARC Format for Holdings Data (MFHD) - Beinecke Manual](https://msu-cataloging-manual.beinecke.library.yale.edu/marc-format-holdings-record-mfhd)
- [YUL Policy for E-Variant Record Links](https://web.library.yale.edu/cataloging/yul-policy-e-variant-record-links-marc-third-party-e-variant)
- [MARC 852 - Location (Library of Congress)](https://www.loc.gov/marc/holdings/hd852.html)
- [MARC 866 - Textual Holdings (Library of Congress)](https://www.loc.gov/marc/holdings/hd866.html)
- [MARC 014 - Linkage Number (Library of Congress)](https://www.loc.gov/marc/holdings/hd014.html)
