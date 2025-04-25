-- get_blank_call_num_mssa_holdings.sql
-- Created by: Will Nyarko
-- Date: 2025-04-24
-- Purpose: Retrieve holdings records with blank call numbers for MSSA dissertation holdings

SELECT m.mfhd_id,
       b.bib_id,
       bt.title,
       bt.author,
       bt.begin_pub_date,
       bt.end_pub_date,
       bt.publisher,
       bt.pub_place,
       m.display_call_no
FROM   mfhd_master m
JOIN   bib_mfhd b ON m.mfhd_id = b.mfhd_id
JOIN   bib_text bt ON b.bib_id = bt.bib_id
WHERE  m.location_id = 248
  AND (m.display_call_no IS NULL OR TRIM(m.display_call_no) = '')
ORDER BY bt.title;
