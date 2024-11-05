WITH url_pub as (
SELECT DISTINCT CONCAT('/repositories/', r.repo_id, '/resources/', r.id) as uri, note.notes
FROM note
LEFT JOIN resource r ON note.resource_id = r.id
Where note.notes like '%https://preservica.library.yale.edu%' AND note.notes like '%publish":true%' AND note.resource_id is not null AND note.notes like '%otherfindaid%'
UNION
SELECT DISTINCT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as uri, note.notes
FROM note
LEFT JOIN archival_object ao ON note.archival_object_id = ao.id
Where note.notes like '%https://preservica.library.yale.edu%' AND note.notes like '%publish":true%' And note.archival_object_id is not null AND note.notes like '%otherfindaid%'
),
total_url as (
SELECT DISTINCT CONCAT('/repositories/', r.repo_id, '/resources/', r.id) as uri, note.notes
FROM note
LEFT JOIN resource r ON note.resource_id = r.id
Where note.notes like '%https://preservica.library.yale.edu%' AND note.resource_id is not null AND note.notes like '%otherfindaid%'
UNION
SELECT DISTINCT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as uri, note.notes
FROM note
LEFT JOIN archival_object ao ON note.archival_object_id = ao.id
Where note.notes like '%https://preservica.library.yale.edu%' AND note.archival_object_id is not null AND note.notes like '%otherfindaid%'
),
delete_pub as(
SELECT DISTINCT CONCAT('/repositories/', r.repo_id, '/resources/', r.id) as uri, note.notes
FROM note
LEFT JOIN resource r ON note.resource_id = r.id
Where note.notes like '%as matching Preservica null%' and note.notes like '%publish":true%' AND note.resource_id is not null and note.notes like '%"type":"odd"%'
UNION
SELECT DISTINCT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as uri, note.notes
FROM note
LEFT JOIN archival_object ao ON note.archival_object_id = ao.id
Where note.notes like '%as matching Preservica null%' and note.notes like '%publish":true%' AND note.archival_object_id is not null and note.notes like '%"type":"odd"%'
),
total_delete as (
SELECT DISTINCT CONCAT('/repositories/', r.repo_id, '/resources/', r.id) as uri, note.notes
FROM note
LEFT JOIN resource r ON note.resource_id = r.id
Where note.notes like '%as matching Preservica null%' and note.resource_id is not null and note.notes like '%"type":"odd"%'
UNION
SELECT DISTINCT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as uri, note.notes
FROM note
LEFT JOIN archival_object ao ON note.archival_object_id = ao.id
Where note.notes like '%as matching Preservica null%' and note.archival_object_id is not null and note.notes like '%"type":"odd"%'
)
SELECT 'Preservica Notes' as note_type, count(DISTINCT url_pub.uri) as published_count, count(DISTINCT total_url.uri) as total_count
FROM total_url
LEFT JOIN url_pub ON url_pub.uri = total_url.uri
UNION
SELECT 'Delete Notes' as note_type, count(DISTINCT delete_pub.uri) as published_count, count(DISTINCT total_delete.uri) as total_count
FROM total_delete
LEFT JOIN delete_pub ON delete_pub.uri = total_delete.uri