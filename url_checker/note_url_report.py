import connections.SQL as sql
import csv, time

QUERY = """
SELECT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', n.archival_object_id) as uri, JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.subnotes[0].content')) AS content_note, 'archival object' as type, ao.title
FROM note n
JOIN archival_object ao ON ao.id = n.archival_object_id
WHERE n.notes like '%http%'
AND n.archival_object_id is not null
UNION
SELECT CONCAT('/repositories/', r.repo_id, '/resources/', n.resource_id) as uri, JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.subnotes[0].content')) AS content_note, 'resource' as type, r.title
FROM note n
JOIN resource r on r.id = n.resource_id 
WHERE n.notes like '%http%'
AND n.resource_id is not null
UNION
SELECT CONCAT('/repositories/', do.repo_id, '/digital_objects/', n.digital_object_id) as uri, JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.subnotes[0].content')) AS content_note, 'digital object' as type, do.title
FROM note n
JOIN digital_object do on do.id = n.digital_object_id
WHERE n.notes like '%http%'
AND n.digital_object_id is not null
UNION
SELECT CONCAT('/agents/people/', n.agent_person_id) as uri, JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.subnotes[0].content')) AS content_note, 'person agent' as type, np.sort_name
FROM note n
JOIN name_person np on np.agent_person_id = n.agent_person_id
WHERE n.notes like '%http%'
AND n.agent_person_id is not null
UNION
SELECT CONCAT('/agents/corporate_entities/', n.agent_corporate_entity_id) as uri, JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.subnotes[0].content')) AS content_note, 'corporate agent' as type, nc.sort_name
FROM note n
JOIN name_corporate_entity nc on nc.agent_corporate_entity_id = n.agent_corporate_entity_id
WHERE n.notes like '%http%'
AND n.agent_corporate_entity_id is not null
UNION
SELECT CONCAT('/agents/software/', n.agent_software_id) as uri, JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.subnotes[0].content')) AS content_note, 'software agent' as type, ns.sort_name
FROM note n
JOIN name_software ns on ns.agent_software_id = n.agent_software_id
WHERE n.notes like '%http%'
AND n.agent_software_id is not null
UNION
SELECT CONCAT('/agents/families/', n.agent_family_id) as uri, JSON_UNQUOTE(JSON_EXTRACT(CONVERT(n.notes USING utf8), '$.subnotes[0].content')) AS content_note, 'family agent' as type, nf.sort_name
FROM note n
JOIN name_family nf on nf.agent_family_id = n.agent_family_id
WHERE n.notes like '%http%'
AND n.agent_family_id is not null
"""

date_str = time.strftime("%y%m%d")
rows_per_file = 100
file_count = 1
rows_written = 0
output_file = open(f'files/broken_urls/{date_str}_urls_{file_count}.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.DictWriter(output_file, fieldnames=['uri'] + ['note'] + ['type'] + ['title'])
csv_writer.writeheader()

if sql.conn():
    cursor = sql.connection.cursor()
    cursor.execute(QUERY)
    sql_data = cursor.fetchall()
    for row in sql_data:
        if rows_written == rows_per_file:
            output_file.close()
            file_count += 1
            output_file = open(f'files/broken_urls/files/{date_str}_urls_{file_count}.csv', 'w', newline='', encoding='utf-8')
            csv_writer = csv.DictWriter(output_file, fieldnames=['uri'] + ['note'] + ['type'] + ['title'])
            csv_writer.writeheader()
            rows_written = 0 
        csv_writer.writerow({'uri': row[0], 'note': row[1], 'type': row[2], 'title': row[3]})
        rows_written += 1
else:
    print("Error. Are you connected to the VPN?")