# Controlled Values Cleanup
Last updated on 09/03/2024 by Kylene Hutchinson.

| Start Date | End Date   | Contributors      | Informed Stakeholders |
| ---------- | ---------- | ----------------- | --------------------- |
| 08/26/2024 | 09/04/2024 | Kylene Hutchinson | Alicia Deletich       |
# Overview
## Problem Statement
The controlled values describing the record contents contains duplicate values that need to be merged and updated (i.e. 'photo' and 'photograph', 'Box' and 'box')
## Goals
- Generate report of controlled values for enums 14, 16
- Review and ID duplicates, errors, etc. and determine appropriate value
	- Consult with creators as needed or run reports to determine usage
- Prep data - needs enum URI value to be merged (e.g. enumerations?id=16, photo, photograph)
- Use migrate_enumerations.py to update
# Background
Originally, all users could add new values to Controlled Values. However, this lead to duplicate and inappropriate values being added to the list. This happened most frequently because a column in the spreadsheet would be deleted by mistake and the importer would pull the Child type from the Child Indicator instead.
ArchivesSpace has been updated to reject records with incorrect controlled values rather than add them to the list, but the duplicate values need to be cleaned up.

## Process
See [controlled_value_cleanup_report.py](controlled_value_cleanup_report.py), [controlled_value_cleanup_migrate.py](controlled_value_cleanup_migrate.py), and [240903_enum_migration.xlsx](240903_enum_migration.xlsx) for files relevant to this project.
- Create SQL query that counts the number of records using each extent or container_type
- Created a SQL query that pulled the container_types with no discernable merge instance, and included the name of the user that created it as well as the URI of the records.
	- Contacted the Users in the report and confirmed it was appropriate to merge these into folder
- Created an Excel sheet that had the Value I was merging from, the Value I was merging into, and the table id
- Created python code that migrated the values in the excel sheet using the API.

# Notes

| Date       | Highlight               | Notes                                                                                                                                                                                                                                                                                                                                            |
| ---------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 08/14/2024 | Introduction to Project | Alicia Detelich introduced this project briefly as a future task.                                                                                                                                                                                                                                                                                |
| 08/22/2024 | Meeting                 | Alicia Detelich assigned this project during a SCMS meeting.                                                                                                                                                                                                                                                                                     |
| 08/26/2024 | Pulled Data             | Pulled lists of Instances and Extents Controlled Values and identified duplicates. Trying to get full related item counts to determine which term should be merged into which.                                                                                                                                                                   |
| 08/27/2024 | Reviewed SQL            | Spent time querying the SQL tables to find where the control_type info was being stored. Turned out they were split between top_containers.type_id and sub_container.type_2_id. Wrote SQL code to count totals and compare to the number I pulled manually from the webclient.                                                                   |
| 08/28/2024 | Wrote Code              | Wrote python and sql code to create reports. One report returns counts of related item by container_type, the other returns a report of URIs for specific container_types (stuff like #1, 9, etc. instead of file or box)                                                                                                                        |
| 08/29/2024 | Even more Code!!        | Updated python reporter and added in extent_type reports. Reviewed Extent_Type counts and made notes about merging                                                                                                                                                                                                                               |
| 08/30/2024 | Contacted Stakeholders  | Contacted Michael Lotstein about the archival objects Instance Child Types being updated to Folder and asked for him to let me know if anything should be changed. All of Abigail Aguilera's objects helpfully had 'folder' in the title, so I sent her an email warning her in case any of them should not be marked as folder for some reason. |
| 08/30/2024 | Tested Migration API    | Keep getting a 403 when trying to migrate enumeration data. Might be missing the 'update_enumeration_record' permission.<br>Created a script that allows the user to input an excel sheet with columns 'to', 'from', and 'enumid' which should migrate each row in the spreadsheet.                                                              |
| 09/03/2024 | Tested Migration API    | Alicia gave necessary permissions in test environment. Ran my code and everything came back as expected. Spot checked a few records and everything appeared to be the correct type.                                                                                                                   |
| 09/04/2024 | Migrated Enum Values | Ran the migration in production. Everything merged smoothly. |

# Review

## Data Details
### Container_Type
#### Counts

| Value        | Position | Sum     | Notes           |
| ------------ | -------- | ------- | --------------- |
| Box          | 0        | 260119  |                 |
| folder       | 1        | 2104972 |                 |
| item         | 2        | 4123    |                 |
| volume       | 3        | 677     |                 |
| page         | 4        | 1168    |                 |
| reel         | 5        | 15647   |                 |
| frame        | 6        | 5       |                 |
| item_barcode | 7        | 21821   |                 |
| File         | 8        | 18674   |                 |
| Volume       | 9        | 13      | merge into POS3 |
| 9            | 10       | 23      | merge into POS1 |
| Carton       | 11       | 0       |                 |
| Page         | 12       | 53      | merge into POS4 |
| box          | 13       | 10402   | merge into POS0 |
| Folder       | 14       | 6115    | merge into POS1 |
| #1           | 15       | 11      | merge into POS1 |
| 2            | 16       | 24      | merge into POS1 |
| 1            | 17       | 27      | merge into POS1 |
| oversize_box | 18       | 0       |                 |
| case         | 19       | 0       |                 |
| 58           | 20       | 1       | merge into POS1 |
| 3            | 21       | 24      | merge into POS1 |
| 4            | 22       | 23      | merge into POS1 |
| 5            | 23       | 23      | merge into POS1 |
| 6            | 24       | 23      | merge into POS1 |
| 7            | 25       | 23      | merge into POS1 |
| 8            | 26       | 23      | merge into POS1 |
| 10           | 27       | 21      | merge into POS1 |
| 11           | 28       | 21      | merge into POS1 |
| 12           | 29       | 20      | merge into POS1 |
| 13           | 30       | 19      | merge into POS1 |
| 14           | 31       | 19      | merge into POS1 |
| 15           | 32       | 18      | merge into POS1 |
| 16           | 33       | 18      | merge into POS1 |
| 17           | 34       | 18      | merge into POS1 |
| 18           | 35       | 17      | merge into POS1 |
| 19           | 36       | 16      | merge into POS1 |
| 20           | 37       | 14      | merge into POS1 |
| 21           | 38       | 11      | merge into POS1 |
| 22           | 39       | 10      | merge into POS1 |
| 23           | 40       | 9       | merge into POS1 |
| 24           | 41       | 9       | merge into POS1 |
| 25           | 42       | 7       | merge into POS1 |
| 26           | 43       | 6       | merge into POS1 |
| 27           | 44       | 4       | merge into POS1 |
| 28           | 45       | 3       | merge into POS1 |
| 29           | 46       | 2       | merge into POS1 |
| 30           | 47       | 1       | merge into POS1 |
| 31           | 48       | 1       | merge into POS1 |
| 49           | 49       | 1       | merge into POS1 |
#### Unknown Merges
| Parent ID | Creator          | Container_Type | Archival Object Count |
| --------- | ---------------- | -------------- | --------------------- |
| 3816608   | Abigail Aguilera | 1-9            | 9                     |
| 3816607   | Abigail Aguilera | 1              | 1                     |
| 3816607   | Michael Lotstein | 1-31           | 243                   |
| 3816608   | Michael Lotstein | 1-11           | 20                    |
| 3816609   | Michael Lotstein | 1-27           | 201                   |
| 3873505   | Michael Lotstein | 1-12           | 18                    |
### Extent Type
#### Counts

| Value                            | Position | Sum   | Notes             |
| -------------------------------- | -------- | ----- | ----------------- |
| videocassettes (VHS)             | 127      | 406   | Merge into POS89  |
| videocassettes (U-matic)         | 126      | 44    | Merge into POS88  |
| videocassettes (MiniDV)          | 128      | 412   | Merge into POS87  |
| videocassettes (BetacamSP)       | 132      | 7     | Merge into POS80  |
| videocassettes (VHS-C)           | 129      | 1     | Merge into POS78  |
| Linear Feet                      | 150      | 34    | Merge into POS47  |
| Folders                          | 146      | 1265  | Merge into POS43  |
| film reels                       | 133      | 3     | Merge into POS41  |
| computer storage media           | 138      | 2     | Merge into POS30  |
| computer files                   | 144      | 765   | Merge into POS29  |
| Audiotape Reels                  | 134      | 783   | Merge into POS4   |
| audiotape reels                  | 135      | 51    | Merge into POS4   |
| audio discs (CD)                 | 131      | 84    | Merge into POS1   |
| See container summary            | 148      | 1     | Merge into POS 64 |
| audio\_discs\_(CD)               | 1        | 597   | -                 |
| audiotape_reels                  | 4        | 6935  | -                 |
| computer_files                   | 29       | 1292  | -                 |
| computer_storage_media           | 30       | 63    | -                 |
| film_reels                       | 41       | 211   | -                 |
| folders                          | 43       | 25655 | -                 |
| linear_feet                      | 47       | 27071 | -                 |
| see_container_summary            | 64       | 2838  | -                 |
| videocassettes (vhs-c)           | 78       | 26    | -                 |
| videocassettes_(betacamsp)       | 80       | 6382  | -                 |
| videocassettes_(minidv)          | 87       | 1145  | -                 |
| videocassettes_(u-matic)         | 88       | 6858  | -                 |
| videocassettes_(vhs)             | 89       | 13970 | -                 |
| audio_cylinders                  | 0        | 17    |                   |
| audio_wire_reels                 | 2        | 36    |                   |
| audiocassettes                   | 3        | 20439 |                   |
| audiotapes                       | 5        | 95    |                   |
| binder                           | 6        | 19    |                   |
| boxes                            | 7        | 330   |                   |
| broadsides                       | 8        | 12    |                   |
| computer                         | 9        | 6     |                   |
| computer file (ai)               | 10       | 2     |                   |
| computer file (fla)              | 11       | 1     |                   |
| computer file (mov)              | 12       | 23    |                   |
| computer files (doc)             | 13       | 331   |                   |
| computer files (dvd-video)       | 14       | 66    |                   |
| computer files (dwg)             | 15       | 2     |                   |
| computer files (eml)             | 16       | 27    |                   |
| computer files (jpg)             | 17       | 238   |                   |
| computer files (mbx)             | 18       | 75    |                   |
| computer files (mp3)             | 19       | 67    |                   |
| computer files (mp4)             | 20       | 110   |                   |
| computer files (pcd)             | 21       | 3     |                   |
| computer files (pdf)             | 22       | 558   |                   |
| computer files (ppt)             | 23       | 5     |                   |
| computer files (psd)             | 24       | 3     |                   |
| computer files (rtf)             | 25       | 2     |                   |
| computer files (tiff)            | 26       | 572   |                   |
| computer files (wav)             | 27       | 275   |                   |
| computer files (zip)             | 28       | 1     |                   |
| copies                           | 31       | 2027  |                   |
| cubic_feet                       | 32       | 10179 |                   |
| disks                            | 33       | 4     |                   |
| ephemera\_items_(accessions)     | 34       | 1     |                   |
| files                            | 35       | 6     |                   |
| film reel (35mm)                 | 36       | 226   |                   |
| film reels (8mm)                 | 37       | 91    |                   |
| film_cassettes                   | 39       | 1     |                   |
| floppy disks                     | 42       | 18    |                   |
| gigabytes                        | 45       | 63    |                   |
| items                            | 46       | 6883  |                   |
| manuscript\_items_(accessions)   | 48       | 10170 |                   |
| megabytes                        | 49       | 342   |                   |
| microcassettes                   | 50       | 475   |                   |
| monograph\_titles_(accessions)   | 51       | 2     |                   |
| non-book\_formats_(accessions)   | 53       | 3578  |                   |
| optical disc (xdcam)             | 54       | 2     |                   |
| optical disks (dvd)              | 55       | 935   |                   |
| pages                            | 58       | 1728  |                   |
| phonograph_records               | 59       | 2036  |                   |
| photographic_prints              | 60       | 156   |                   |
| photographic_slides              | 61       | 66    |                   |
| photographs                      | 62       | 20019 |                   |
| reels                            | 63       | 564   |                   |
| serial\_volumes_(accessions)     | 66       | 1     |                   |
| sound_track_film_reels           | 68       | 33    |                   |
| super 8 film                     | 69       | 25    |                   |
| terabytes                        | 70       | 13    |                   |
| videocassettes                   | 72       | 3916  |                   |
| videocassettes (d-2)             | 74       | 2     |                   |
| videocassettes (dvcpro)          | 75       | 19    |                   |
| videocassettes (s-vhs)           | 76       | 3     |                   |
| videocassettes (vcr vc-30)       | 77       | 2     |                   |
| videocassettes_(betacam)         | 79       | 485   |                   |
| videocassettes_(betacamsp_l)     | 81       | 69    |                   |
| videocassettes_(betamax)         | 82       | 41    |                   |
| videocassettes_(digital_betacam) | 83       | 80    |                   |
| videocassettes_(dvcam)           | 84       | 712   |                   |
| videocassettes_(hi8)             | 86       | 632   |                   |
| videocassettes_(video_8)         | 90       | 29    |                   |
| videodiscs                       | 91       | 13    |                   |
| videoreels                       | 92       | 30    |                   |
| videotape (.5")                  | 93       | 98    |                   |
| videotape (2")                   | 94       | 8     |                   |
| videotape (v-30h)                | 95       | 3     |                   |
| videotapes (8 mm)                | 96       | 1     |                   |
| volumes                          | 97       | 112   |                   |
| audio discs                      | 98       | 84    |                   |
| audio belts                      | 100      | 5     |                   |
| film rolls                       | 102      | 2     |                   |
| JAZ_disks                        | 106      | 1     |                   |
| ZIP_disks                        | 107      | 232   |                   |
| DVD-Rs                           | 108      | 2392  |                   |
| external_hard_drives             | 109      | 84    |                   |
| internal_hard_drives             | 110      | 26    |                   |
| flash_drives                     | 111      | 57    |                   |
| laptop_computers                 | 112      | 5     |                   |
| CD-Rs                            | 114      | 6285  |                   |
| CD-RWs                           | 115      | 407   |                   |
| DVD-RWs                          | 116      | 371   |                   |
| 3.5_floppy_disks                 | 117      | 5990  |                   |
| 5.25_floppy_disks                | 118      | 2183  |                   |
| collection                       | 119      | 13    |                   |
| Videocassettes (3/4" U-Matic)    | 120      | 809   |                   |
| paintings                        | 124      | 1     |                   |
| film reels (16 mm)               | 125      | 3441  |                   |
| books                            | 130      | 30    |                   |
| computer files (xlsx)            | 136      | 1     |                   |
| duration_HH_MM_SS_mmm            | 137      | 24852 |                   |
| film reels (8 mm)                | 139      | 6     |                   |
| bytes                            | 140      | 3072  |                   |
| kilobytes                        | 141      | 11    |                   |
| optical_disks                    | 142      | 13    |                   |
| microfilm_reels                  | 143      | 4     |                   |
| slides                           | 145      | 3158  |                   |

## Communication
| Name             | Position                                                                | Notes                                                                      |
| ---------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Alicia Detelich  | Head of Special Collections Metadata Services in Beinecke               | Provided background                                                        |
| Abigail Aguilera | Archives Assistant 2 in Beinecke Special Collections Technical Services | Confirmed that all her archival objects should have a Child Type of Folder |
| Michael Lotstein | University Archivist, Beinecke Public Services and Operations           | Confirmed that all his archival objects should have a Child Type of Folder |
## Results
- Extent Values table had 16 values that needed to be merged into another value, only 1 of which was an error value ('1') the rest were duplicates.
- Container Type Values table had 38 values that needed to be merged into another value, 4 of which were duplicates and the rest were error values that were merged into folders.
  
Migration ran smoothly with no issues. All error values were approved by their creators to be merged into the folders value.

# References

- [Controlled Value Lists](https://archivesspace.library.yale.edu/enumerations)
