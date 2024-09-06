SELECT CONCAT('/agents/people/', ari.agent_person_id) as uri
	, ari.record_identifier
FROM agent_record_identifier ari
JOIN enumeration_value ev on ev.id = ari.source_id
WHERE ari.agent_person_id is not null
AND ev.value = 'naf'
AND ari.record_identifier not like 'http%'
UNION ALL
SELECT CONCAT('/agents/families/', ari.agent_family_id) as uri
	, ari.record_identifier 
FROM agent_record_identifier ari
JOIN enumeration_value ev on ev.id = ari.source_id
WHERE ari.agent_family_id is not null
AND ev.value = 'naf'
AND ari.record_identifier not like 'http%'
UNION ALL
SELECT CONCAT('/agents/corporate_entities/', ari.agent_corporate_entity_id) as uri
	, ari.record_identifier
FROM agent_record_identifier ari
JOIN enumeration_value ev on ev.id = ari.source_id
WHERE ari.agent_corporate_entity_id is not null
AND ev.value = 'naf'
AND ari.record_identifier not like 'http%'