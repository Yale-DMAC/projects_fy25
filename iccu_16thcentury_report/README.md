# ICCU 16th Century Report
Last updated on 12/20/2024 by Kylene Hutchinson.

| Start Date | End Date | Contributors | Informed Stakeholders |
| ---------- | -------- | ------------ | --------------------- |
| 12/06/2024 | 12/19/2024 | Kylene Hutchinson | Alicia Detelich, Todd Fell, Marianna Morrealle |

# Overview
## Problem Statement
The Istituto centrale per il catalogo unico delle Biblioteche italiane e per le informazioni (ICCU) has reached out to Yale requesting a list of titles from Beinecke's collection published in the 16th century either in Italy or from any country but in the Italian language.
## Goals
Create an excel file for the following criteria:
- Published between 1501-1600
- Either published in Italy, or published elsewhere in the Italian language
- Part of Beinecke collections
- Not electronic
- Include any CNCE numbers  
  
Additions:
- Include 300 and 260 fields to report.
# Background
Todd Fell forwarded an email from the ICCU to Yale asking for this report. I originally included the title, author, edition, published language, published country code, published date, CNCE, and network_number (OCLC and such numbers). ICCU requested we add in a 260 and 300 field.


# Process
See [ita_report.py](ita_report.py).
- Write a SQL query that searches for title, author, edition, published language, published country code, published date, CNCE number, network number, 260 field, 300 field, and location code.
    - Add substrings to pull publisher information out of the 008 field
    - Use utl_i18n string conversions to ensure UTF8 encoding is preservered
    - Use List Agg in a seperate table to contain any multiple CNCE numbers in a single cell
- Published date may contain characters such as 156u, these need to be filtered in the python code rather than the SQL query to avoid complications.
- Use try and int on the published date before using an if statment to filter out dates between 1501 and 1600
- Use except to check if the published date is 4 characters long and starts with '15' to catch any relevant dates containing 'u'.
- Save to csv

# Review

## Communication
| Name | Position | Notes |
| Alicia Detelich | Assistant Director of Special Collection Metadata Services, Special Collections Technical Services | Supervising project |
| Todd Fell | Associate Director, Bibliographic Description | Requested and reviewed project |
| Marianna Morrealle | Library Officer, Istituto Centrale per il Catalogo Unico delle Biblioteche italiane e per le informazioni bibliografiche  (ICCU) | Received report from Yale and clarified parameters of the request. |
| Elena Ravelli |  Istituto centrale per il catalogo unico delle Biblioteche italiane e per le informazioni (ICCU) | Requested Report |

## Results
Sent report to Todd Fell for review, then submitted it to Marianna Morrealle who requested two additional fields be added (300 and 260). Final report was submitted on 12/18/2024.

