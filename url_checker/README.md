# URL Checker
Last updated on 02/21/2025 by Kylene Hutchinson.

| Start Date | End Date | Contributors | Informed Stakeholders |
| ---------- | -------- | ------------ | --------------------- |
| 12/03/2024 | 02/13/2025 | Kylene Hutchinson | Alicia Detelich  |

# Overview
## Problem Statement
Every so often it is good practice to look for broken links. Some of these notes containing URLs were written years ago and have not been inspected since.

## Goals
- Identify all notes with hyperlinks
- Attempt to resolve these links
- If links are broken, review and potentially delete the link and/or the note

# Background



# Process
See [note_url_report.py](note_url_report.py), [note_url_checker.py](note_url_checker.py), and [25_broken_urls.csv](25_broken_urls.csv)
- SQL query pulls a list of notes with urls in them.
- Report is split into files of 100 urls
- Checker runs a webscrape on 200 urls (2 files) then takes a 30 minute break.
- Keeps track of the last 5 base urls that were scraped and adds 1 second delay for each repeated base url, up to 5 seconds.
- Creates two reports, one that tracks the results of every url, and the other is just a report of urls that failed to return a 200 status code.
- We then manually review the failed list for broken links and either fix them, delete them, or alert someone of the issue.

# Notes
| Date | Highlight | Notes |
| ---- | --------- | ----- |
| 12/03/2024 | Break | Stepping away from this project for a bit to rethink my approach |
| 01/28/2025 | Ran Updated Code | Started the project over with fresh code that throttles the webscrapping based on how many times it has been previously requested up to 5 sec delay, splits the report into files of 100 urls, runs 2 reports then waits 30 minutes. |
| 01/31/2025 | Finished Checking | Completed checking URLs from ArchivesSpace notes. Compiled a list of broken links. 'http://hdl.handle.net/10079/digcoll/*' does not work, tons of records have this link with specific ids at the end (instead of *) but they all link back to the Digital Collections main page. |
| 02/13/2025 | Finished Cleanup | Finished fixing and deleting URLS. Around 10 URLs being sent to Alicia to see if she believes they should be deleted or someone contacted about another option. |

# Review

## Data Details
Aproximately 15,000 notes in ArchivesSpace have urls in them.
Roughly 165 of these notes have broken URLs that need to be addressed (That are not 'http://hdl.handle.net/10079/digcoll/*')

## Communication
| Name            | Position                                                   | Notes                                                      |
| --------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| Alicia Detelich | Assistant Director of Special Collection Metadata Services | - Assigned Project<br>- Helping with reviewing urls |
## Results
Reviewed 15,000 urls in ArchivesSpace and tested whether they were broken. 
Approximately 165 were a handle url for digital collections that linked back to the digital collections main page instead of the object they were trying to refer to. Cleanup for that will be addressed in a different project after discussing it with appropriate parties.
Approximately 65 other urls were broken and needed addressing. 21 of these urls were sent to Alicia for further review. 37 were fixed by correcting typos or finding where the url had moved to. 4 urls were removed because the linked materials no longer existed, or because it linked to a virus. 

# References

- [Github Issue: Review/update links in notes](https://github.com/orgs/Yale-DMAC/projects/1?pane=issue&itemId=20789709)
