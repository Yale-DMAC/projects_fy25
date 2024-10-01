# TITLE
Last updated on [10/1/2024] by [Tyler Wade].

| Start Date | End Date | Contributors | Informed Stakeholders |
| ---------- | -------- | ------------ | --------------------- |
| 09/05/2024 |09/27/2024|  Tyler Wade  |   Alicia Deletich     |                       |

# Overview
## Problem Statement
-Agent records imported from LCNAF do not include the full HTTP address, only the record identifier. Example: https://archivesspace.library.yale.edu/agents/agent_person/6660

## Goals
-Identify all agent records which do not include full HTTP address (http://id.loc.gov/authorities/names/[record_id])

-Update agent records to include address
(there may be some other invalid record identifiers other than those which do not include the HTTP address (e.g. names in the identifier field). These should be fixed as well.)


# Background
N/A


# Process
-needed to identify all agent records imported from LCNAF that do not include the full HTTP addresses

-used sql query to get all agent records that did not have LCNAF HTTP addresses where then transferred into an CSV spreadsheet(https://yaleedu-my.sharepoint.com/:x:/g/personal/tyler_wade_yale_edu/EbnXUzlWBpVMiC5dtgGEjgIBC-D8bXN4vq46IpqSSiiY7Q?e=YEE3CK)

-Created a script to replace all agent records with LCNAF Http addresses and set them as the primary agent record identifier (import_http_addresses.py)


# Notes
(Keep track of meetings and formal communication of the project. Also include any highlights in the project's progress such as roadblocks or changes in approach.)

| Date | Highlight | Notes |
| ---- | --------- | ----- |
|      |           |       |

# Review

## Data Details
Include details about the amount of records, shared traits, collection information, etc.
## Communication
 ||Alicia Detelich | Head of Special Collections Metadata Services in Beinecke |Alicia Detelich gave advice and direction on how to complete project/task|
## Results
Https address replacement/updates ran smoothly with no issues

# References

- List of relevant links
