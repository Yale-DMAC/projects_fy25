SELECT * FROM
(SELECT aspace_uri
	, COUNT(*) as dob_count
	, GROUP_CONCAT(dob_title SEPARATOR '; ') as dob_titles
FROM (SELECT CONCAT('https://archives.yale.edu/repositories/', ao.repo_id, '/archival_objects/', ao.id) as aay_url
	, JSON_UNQUOTE(JSON_EXTRACT(resource.identifier, '$[0]')) as call_number
	, resource.title as resource_title	
	, ao.display_string as ao_title
	, dob.title as dob_title
	, CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as aspace_uri 
	, dob.digital_object_id
FROM archival_object ao
JOIN instance on instance.archival_object_id = ao.id
JOIN instance_do_link_rlshp idlr on idlr.instance_id = instance.id
JOIN digital_object dob on dob.id = idlr.digital_object_id
JOIN resource on resource.id = ao.root_record_id
WHERE dob.digital_object_id REGEXP "^[a-zA-Z0-9]{8}[-][a-zA-Z0-9]{4}[-][a-zA-Z0-9]{4}[-][a-zA-Z0-9]{4}[-][a-zA-Z0-9]{12}$") preservica_objects
GROUP BY aspace_uri) counts
WHERE dob_count > 1
ORDER BY aspace_uri