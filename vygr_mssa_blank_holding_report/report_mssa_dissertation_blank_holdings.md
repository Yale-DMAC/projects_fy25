# MSSA Dissertation Holdings Report - Blank Call Numbers

This report provides an analysis of MSSA dissertation holdings records located at `lsfmssr` that have a blank `display_call_no` in Voyager, based on data extracted on 2025-04-24. It begins by addressing the primary request from the associated ServiceNow ticket (counting these records) and then presents a supplementary analysis exploring the completeness, uniqueness, and content characteristics of key data fields within this specific dataset.

## Primary Finding: Total Holdings Count

**Directly addressing the ServiceNow ticket request:**

*   The total count of holdings records (`MFHD_ID`s) in Voyager located at `lsfmssr` (location_id 248) and having a blank `display_call_no` (i.e., missing the standard call number components) is **11,566**.

---

## Supplementary Data Analysis

This section details the analysis performed on the 11,566 records identified above, using the `mssa_diss_blank_mfhd__202504241239.csv` dataset. It examines several key fields for completeness (blank values) and data characteristics (uniqueness, common patterns, potential issues).

*   **Total Records Analyzed:** 11,566

### Blank Counts per Column:
*   **`MFHD_ID`:** 0 blanks
*   **`BIB_ID`:** 0 blanks
*   **`TITLE`:** 0 blanks
*   **`AUTHOR`:** 3 blanks (0.03%). MFHD_IDs: `['3505793', '8380818', '8896121']`
*   **`BEGIN_PUB_DATE`:** 1 blank (0.01%). MFHD_ID: `['13044140']`
*   **`END_PUB_DATE`:** 11,513 blanks (99.54%). _Note: Likely expected for single-year publications, but I'm just guessing._
*   **`PUBLISHER`:** 11,507 blanks (99.49%).
*   **`PUB_PLACE`:** 11,507 blanks (99.49%).
*   **`DISPLAY_CALL_NO`:** 11,566 blanks (100.00%). _Note: This confirms all records in the dataset meet the primary criteria from the ServiceNow ticket._

---

## Detailed Column Analysis

This section provides specific findings for each relevant column in the dataset (`mssa_diss_blank_mfhd__202504241239.csv`).

### `MFHD_ID` Findings (Holding Record ID)

*   **Role:** Primary unique identifier for holding records in Voyager.
*   **Total Count:** The dataset contains 11,566 unique `MFHD_ID` values, matching the total number of records analyzed.
*   **Completeness:** 100% complete (0 blank values).
*   **Uniqueness:** 100% unique. Each value identifies one specific holding record.

### `BIB_ID` Findings (Bibliographic Record ID)

*   **Role:** Links the holding record (`MFHD_ID`) to the parent bibliographic record describing the dissertation.
*   **Completeness:** 100% complete (0 blank values).
*   **Uniqueness:** Not unique across all holdings in this dataset.
    *   Total Entries: 11,566
    *   Distinct Values: 11,363
    *   Duplicate Values: 201 `BIB_ID` values are associated with more than one holding record in this dataset.
    *   Interpretation: This indicates instances where a single dissertation (bibliographic record) has multiple physical holdings associated with `lsfmssr` and lacks a call number. The maximum occurrence is 4 holdings linked to `BIB_ID` `4370533`.
*   **Reference:** See `data/duplicate_summary_by_value.csv` for the list of `BIB_ID`s associated with multiple `MFHD_ID`s.

### `TITLE` Findings

*   **Role:** Contains the title of the dissertation.
*   **Completeness:** 100% complete (0 blank values).
*   **Uniqueness:** Not unique across all holdings in this dataset.
    *   Total Entries: 11,566
    *   Distinct Values: 11,362
    *   Duplicate Values: 202 distinct titles are associated with more than one holding record in this dataset.
    *   Interpretation: This indicates instances where the same title is linked to multiple holding records. The most frequent is "Iroquoian morphology / by Floyd Glenn Lounsbury." (4 holdings).
*   **Reference:** See `data/duplicate_summary_by_value.csv` for the list of titles associated with multiple `MFHD_ID`s.

### `AUTHOR` Findings

*   **Role:** Contains the author of the dissertation.
*   **Completeness:** Not 100% complete.
    *   Total Records: 11,566
    *   Blank Values: 3 (0.03%). `MFHD_ID`s: `['3505793', '8380818', '8896121']`.
    *   Non-Blank Entries: 11,563
*   **Uniqueness (of non-blank values):** Not unique across all holdings in this dataset.
    *   Total Non-Blank Entries: 11,563
    *   Distinct Non-Blank Values: 11,347
    *   Duplicate Values: 213 distinct non-blank author names are associated with more than one holding record.
    *   Interpretation: Indicates authors linked to multiple dissertations/holdings in this dataset. The most frequent is "Lounsbury, Floyd Glenn." (4 holdings).
*   **Reference:** See `data/duplicate_summary_by_value.csv` for the list of authors associated with multiple `MFHD_ID`s.

### `BEGIN_PUB_DATE` Findings (Publication Start Year)

*   **Role:** Indicates the publication start year (or single year) of the dissertation.
*   **Completeness:** High (99.99%).
    *   Total Records: 11,566
    *   Blank Values: 1 (`MFHD_ID`: `['13044140']`).
    *   Non-Blank Entries: 11,565
*   **Data Validity (of non-blank entries):**
    *   Valid Years (YYYY format, 1500-2025 range): 11,551 entries.
    *   Invalid/Out-of-Range: 14 records associated with 5 unique patterns. **_(I'm just going by regular assumptions by current time vs. what I am seeing in the log knowing that there might be legitimate reasons why some of these may appear invalid)_**
        *   `'19uu'` (Format Error): 1 record (`MFHD_ID`: `['13927740']`)
        *   `'200u'` (Format Error): 6 records (`MFHD_ID`s: `['6756491', '6757444', '6742485', '12133702', '6731758', '12138364']`)
        *   `'9999'` (Out of Range): 5 records (`MFHD_ID`s: `['14505340', '14505338', '14505336', '14505334', '14505339']`)
        *   `'2080'` (Out of Range): 1 record (`MFHD_ID`: `['8881753']`)
        *   `'2041'` (Out of Range): 1 record (`MFHD_ID`: `['12619390']`)
*   **Date Range (based on valid years):**
    *   Earliest Year: 1878
    *   Latest Year: 2020
*   **Distribution by Decade (based on valid years):**
    *   The data spans from the 1870s to the 2020s.
    *   Concentration is heavily weighted towards recent decades:
        *   2010s: 3,829 records (approx. 33.1%)
        *   2000s: 3,180 records (approx. 27.5%)
        *   1990s: 2,968 records (approx. 25.7%)
    *   Older decades (1870s-1980s) account for the remaining ~13.7%.
*   **Reference:** Full details are in `logs/pub_date_analysis.log`.

### `PUBLISHER` Findings

*   **Role:** Identifies the publisher of the dissertation.
*   **Completeness:** Low (only 52.48% complete).
    *   Total Records: 11,566
    *   Blank Values: 5,496 (47.52%)
    *   Non-Blank Values: 6,070
*   **Data Content (of non-blank values):**
    *   Low Variation: Only 12 unique non-blank values exist.
    *   Dominant Value: `'Yale University,'` represents 97.22% (5,901) of non-blank entries.
    *   Variations of 'Yale University': The non-blank values include:
        *   `'Yale University,'` (5901)
        *   `'[Yale University],'` (9)
        *   `'Yale University , '` (6)
        *   `'Yale University Press,'` (2)
        *   `'Yale University],'` (1)
    *   Other Values:
        *   `'[publisher not identified],'` (137)
        *   `'s.n.],'` (9)
        *   4 other unique single-occurrence values (see log for details).
    *   No purely numeric values were identified.
*   **Reference:** Full list of all 12 unique values and counts are in `logs/publisher_place_analysis.log`.

### `PUB_PLACE` Findings (Place of Publication)

*   **Role:** Identifies the place of publication.
*   **Completeness:** Low (only 53.04% complete).
    *   Total Records: 11,566
    *   Blank Values: 5,431 (46.96%)
    *   Non-Blank Values: 6,135
*   **Data Content (of non-blank values):**
    *   Moderate Variation: 49 unique non-blank values exist.
    *   Dominant Values: `'[New Haven, Connecticut] :'` (5472, 89.19%) and `'New Haven, Connecticut :'` (441, 7.19%) together account for over 96% of non-blank entries.
    *   Year-like Entries: 32 unique patterns resemble years or date formats (e.g., '1998.', 'c2003.', '[2002]', '1899-'). These account for only 55 records in total.
    *   Other Notable Values:
        *   `'[Place of publication not identified] :'` (137, 2.23%) is the third most frequent.
        *   Various other formats like `'[New Haven, Conn. :'` (8), `'New Haven :'` (2) exist.
*   **Reference:** Full list of all 49 unique values and counts are in `logs/publisher_place_analysis.log`.

---

## Supplementary Analysis: Data Uniqueness

Analysis of key identifiers within the 11,566 records:

*   **`MFHD_ID` Uniqueness:**
    *   Result: All 11,566 `MFHD_ID` values are unique.
    *   _Interpretation:_ Each row represents a distinct holdings record, as expected.

*   **`BIB_ID` Uniqueness:**
    *   Result: Duplicate non-blank `BIB_ID` values found.
    *   Number of unique `BIB_ID` values that appear more than once: 201
    *   _Interpretation:_ 201 bibliographic records in this dataset have multiple associated holdings records at `lsfmssr` with blank call numbers. The most frequent is `BIB_ID` `4370533` (4 associated holdings).

*   **`TITLE` Uniqueness:**
    *   Result: Duplicate non-blank `TITLE` values found.
    *   Number of unique `TITLE` values that appear more than once: 202
    *   _Interpretation:_ 202 distinct titles are associated with multiple holdings records in this dataset.

*   **`AUTHOR` Uniqueness:**
    *   Result: Duplicate non-blank `AUTHOR` values found.
    *   Number of unique `AUTHOR` values that appear more than once: 213
    *   _Interpretation:_ 213 distinct authors are associated with multiple holdings records in this dataset.

*   **Detailed Duplicates List:**
    *   A detailed summary listing each non-unique `BIB_ID`, `TITLE`, and `AUTHOR`, along with their associated `MFHD_ID`s, is available in the file: `data/duplicate_summary_by_value.csv`.

---

# Resources and References

- [ServiceNow Ticket Screenshot](Screenshot%202025-02-21%20111455.png): Illustrates the missing call number data in Voyager.
