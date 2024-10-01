SELECT CONCAT('/repositories/', repo_id, '/resources/', id) as uri, CONCAT('/repositories/3') as target_repo
FROM resource
WHERE repo_id = 2