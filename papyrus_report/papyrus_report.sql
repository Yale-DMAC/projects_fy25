WITH tempnote AS (SELECT n.archival_object_id, 
JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.subnotes[0].content')) AS content_note
FROM note n
WHERE n.notes like '%acqinfo%')
SELECT CONCAT('archives.yale.edu/repositories/', ao.repo_id, '/archival_objects/', ao.id) as uri, 
ao.component_id, 
ao.display_string, 
ev.value as iso_language_code, 
(CASE 
	WHEN ev.value = 'grc' THEN 'Greek, Ancient (to 1453)' 
	WHEN ev.value = 'egy' THEN 'Egyptian (Ancient)'
	WHEN ev.value = 'lat' THEN 'Latin'
	WHEN ev.value = 'ara' THEN 'Arabic'
	WHEN ev.value = 'cop' THEN 'Coptic'
	WHEN ev.value = 'syr' THEN 'Syriac'
	WHEN ev.value = 'pal' THEN 'Pahlavi'
	WHEN ev.value = 'heb' THEN 'Hebrew'
	WHEN ev.value = 'ira' THEN 'Iranian'
	WHEN ev.value = 'ita' THEN 'Italian'
	WHEN ev.value = 'arc' THEN 'Aramaic (700-300 BCE)'
END) AS language,
content_note as acquistions_note
FROM archival_object ao
LEFT JOIN tempnote tn on tn.archival_object_id = ao.id
LEFT JOIN lang_material lm on lm.archival_object_id = ao.id
LEFT JOIN language_and_script las on las.lang_material_id = lm.id
LEFT JOIN enumeration_value ev on ev.id = las.language_id
WHERE root_record_id = 5894
AND component_id is not null
GROUP BY ao.id, ao.component_id