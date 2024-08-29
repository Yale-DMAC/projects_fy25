SELECT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as uri
	, ao.title
FROM archival_object ao
WHERE ao.title like '%emph%'
AND ao.repo_id = 2