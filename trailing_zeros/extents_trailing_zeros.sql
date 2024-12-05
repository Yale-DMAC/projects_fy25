SELECT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', extent.archival_object_id) 
FROM extent 
JOIN archival_object ao ON ao.id = extent.archival_object_id 
WHERE number like '%.0'
AND extent.archival_object_id is not null
UNION ALL
SELECT CONCAT('/repositories/', a.repo_id, '/accessions/', extent.accession_id)
FROM extent 
JOIN accession a ON a.id = extent.accession_id 
WHERE number like '%.0'
AND extent.accession_id is not null
UNION ALL
SELECT CONCAT('/repositories/', r.repo_id, '/resources/', extent.resource_id)
FROM extent 
JOIN resource r ON r.id = extent.resource_id 
WHERE number like '%.0'
AND extent.resource_id is not null
UNION ALL
SELECT CONCAT('/repositories/', do.repo_id, '/digital_objects/', extent.digital_object_id)
FROM extent 
JOIN digital_object do ON do.id = extent.digital_object_id 
WHERE number like '%.0'
AND extent.digital_object_id is not null