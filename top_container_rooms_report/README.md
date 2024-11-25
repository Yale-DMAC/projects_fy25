# Top Containers Rooms Custom Report
Last updated on 11/25/2024 by Kylene Hutchinson.

| Start Date | End Date | Contributors | Informed Stakeholders |
| ---------- | -------- | ------------ | --------------------- |
| 10/01/2024 | 10/22/2024 | Kylene Hutchinson | Alicia Detelich |

# Overview
## Problem Statement
ArchivesSpace requires a custom report on all top containers in a given room(s).

## Goals
- Create a custom report in the yale-archivesspace-reports plugin
- Return details similar to those of other custom Top Container Reports (barcode, creation times, title, uri, etc.)
- Add in columns for room and building information
- Add parameters that allow users to limit to specific rooms or buildings
- Limit to current repository

# Background
A custom report for top containers in a specific location has been needed for awhile. The report needs to be limited to current repository to ensure no one is able to see information that they should not have access to.  
Requires testing in a Docker Environment before submitting via pull request on github.


# Process
See [top_containers_room.rb](top_containers_room.rb), [_building.html.erb](_building.html.erb), [_roomname.html.erb](_roomname.html.erb), and [en.yml](en.yml)  
- Create a local ArchivesSpace enivironment using Docker.
- Install yale-archivesspace-reports to the plugins folder.
- Create a .rb in the backend/model folder containg a SQL query and ruby.
- Update the en.yml file in frontend/locales add to the list a title, description, and identifier-prefix for your report. Add any new parameters to the parameter list.
- Add parameter files to frontend/views/jobs/report_partials as _parameter.html.erb

# Notes
| Date | Highlight | Notes |
| ---- | --------- | ----- |
| 10/01/2024 | Assigned | Alicia assigned this project at my request to work on ArchivesSpace plugins |
| 10/03/2024 | Setting up Docker | Set up an ArchivesSpace environment with Docker using a Windows Subsystem for Linux |
| 10/08/2024 | Wrote Custom Report | Wrote a custom report for Top Containers and tested using Docker Environment. Everything ran as expected.|
| 10/10/2024 | Updating Docker | Trying to set up a custom Yale ArchivesSpace environment to ensure everything works as expected with our data. |
| 10/18/2024 | Yale Enviroment Failed | Failed to set up a custom Yale ArchivesSpace environment in a timely manner. Current device is struggling to index our records due to a lack of RAM and I am unable to set up an ArchivesSpace 3.1 environment, likely due to a gems update that no longer works with older versions of ArchivesSpace. Yale is currently running on 3.1 but I have to run a 3.5 environment. Likely not to cause any issues with custom reports but may cause issues with plugin creations until Yale updates to 3.5 |
| 10/22/2024 | Sent Pull Request | Sent pull request to yale-archivesspace-reports |
| 11/25/2024 | Update | Forgot to add the parameters files to the project folder. |

# Review

## Data Details
N/A
## Communication
N/A
## Results
Managed to create a custom report for Top Containers by room, however I was unable to test it in a 3.1 environment. Despite this, we anticipate no issues with the report. Report was sent as a pull request to YaleArchiveSpace/yale-archivesspace-reports.

# References

- [Github Issue - Add report on all top containers in a given room(s) to reports plugin](https://github.com/orgs/Yale-DMAC/projects/1/views/1?pane=issue&itemId=44064929)
