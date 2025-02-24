SELECT ao.id, ao.display_string as title, re.name as repository, r.identifier
    , JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.subnotes[0].content')) AS access_note
    , JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.rights_restriction.local_access_restriction_type')) AS restrictions
    , CONCAT('/repositories/', ao.repo_id, '/archival_objects/', n.archival_object_id) as uri
    FROM note n 
    LEFT JOIN archival_object ao on ao.id = n.archival_object_id 
    LEFT JOIN repository re on re.id = ao.repo_id 
    LEFT JOIN resource r on r.id = ao.root_record_id 
    WHERE JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.type')) like '%accessrestrict%'
    AND n.archival_object_id is not NULL
    AND (ao.repo_id = '11' OR ao.repo_id = '12')
    AND (JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.rights_restriction.local_access_restriction_type')) like '%RestrictedCurApprSpecColl%'
    OR JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.rights_restriction.local_access_restriction_type')) like '%InProcessSpecColl%'
    OR JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.rights_restriction.local_access_restriction_type')) like '%ColdStorageBrbl%'
    OR JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.subnotes[0].content')) like '%curator%')
UNION ALL
SELECT r.id, r.title, re.name as repository, r.identifier
    , JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.subnotes[0].content')) AS access_note
    , JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.rights_restriction.local_access_restriction_type')) AS restrictions
    , CONCAT('/repositories/', r.repo_id, '/resources/', n.resource_id) as uri
    FROM note n 
    LEFT JOIN resource r on r.id = n.resource_id 
    LEFT JOIN repository re on re.id = r.repo_id
    WHERE JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.type')) like '%accessrestrict%'
    AND n.resource_id is not NULL
    AND (r.repo_id = '11' OR r.repo_id = '12')
    AND (JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.rights_restriction.local_access_restriction_type')) like '%RestrictedCurApprSpecColl%'
    OR JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.rights_restriction.local_access_restriction_type')) like '%InProcessSpecColl%'
    OR JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.rights_restriction.local_access_restriction_type')) like '%ColdStorageBrbl%'
    OR JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.subnotes[0].content')) like '%curator%')