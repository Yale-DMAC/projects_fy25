-- get_location_id_by_code.sql
-- Created by: Will Nyarko
-- Date: 2025-04-24
-- Purpose: Retrieve location ID by location code

SELECT LOCATION_ID
FROM LOCATION
WHERE LOCATION_CODE = 'lsfmssr';

-- Output: LOCATION_ID