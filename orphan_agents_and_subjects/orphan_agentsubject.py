import connections.SQL as sql
import connections.API as api
import csv, json, time

QUERY = """
SELECT CONCAT('agents/people/', np.agent_person_id) as uri
FROM name_person np
LEFT JOIN linked_agents_rlshp lar on np.agent_person_id = lar.agent_person_id
LEFT JOIN `user` ur on ur.agent_record_id = np.agent_person_id
LEFT JOIN payment_authorizer_rlshp par on par.agent_person_id = np.agent_person_id
WHERE np.is_display_name is not null
AND lar.id is null
AND ur.id is null
AND par.id is null
UNION ALL
SELECT CONCAT('agents/families/', nf.agent_family_id) as uri
FROM name_family nf
LEFT JOIN linked_agents_rlshp lar on nf.agent_family_id = lar.agent_family_id
WHERE nf.is_display_name is not null
AND lar.id is null
UNION ALL
SELECT CONCAT('agents/corporate_entities/', nce.agent_corporate_entity_id) as uri
FROM name_corporate_entity nce
LEFT JOIN linked_agents_rlshp lar on nce.agent_corporate_entity_id = lar.agent_corporate_entity_id
LEFT JOIN repository r ON r.agent_representation_id = nce.agent_corporate_entity_id 
WHERE nce.is_display_name is not null
AND lar.id is null
AND r.id IS NULL
UNION ALL
SELECT CONCAT('agents/software/', ns.agent_software_id) as uri
FROM name_software ns
LEFT JOIN linked_agents_rlshp lar on ns.agent_software_id = lar.agent_software_id 
WHERE ns.is_display_name is not null
AND lar.id is null
AND ns.agent_software_id not like '1'
UNION ALL
SELECT CONCAT('subjects/', s.id) as uri
FROM subject s
LEFT JOIN subject_rlshp sr ON sr.subject_id = s.id
WHERE s.title is not NULL 
AND sr.id is NULL
"""

if sql.conn():
    print("Connected to SQL.")
    cursor = sql.connection.cursor()
    cursor.execute(QUERY)
    sql_data = cursor.fetchall()
    date_str = time.strftime("%y%m%d")
    with open(f'files/orphan_agentsubject/{date_str}_uris.csv', 'w', encoding='utf8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['uri'])
        writer.writeheader()
        for row in sql_data:
            writer.writerow({'uri': row[0]})
    if api.conn():
        print("Connected to API.")
        with open(f'files/orphan_agentsubject/{date_str}_uris.csv', 'r', encoding='utf8') as infile:
            reader = csv.DictReader(infile)
            updatefile = open(f'files/orphan_agentsubject/{date_str}_update.csv', 'a', encoding='utf8', newline='')
            errfile = open(f'files/orphan_agentsubject/{date_str}_errors.csv', 'a', encoding='utf8', newline='')
            writer = csv.DictWriter(updatefile, fieldnames=reader.fieldnames + ['info'] + ['status'])
            writer.writeheader()
            err_writer = csv.DictWriter(errfile, fieldnames=reader.fieldnames + ['info'])
            err_writer.writeheader()
            for row in reader:
                try:
                    uri = row['uri']
                    api_data = api.client.get(uri).json()
                    with open(f"files/orphan_agentsubject/backups/{uri.replace('/','_')}.json", 'w', encoding='utf8') as outfile:
                        json.dump(api_data, outfile, sort_keys=True, indent=4)
                    if api_data['is_linked_to_published_record'] == False:
                        deleted = api.client.delete(uri)
                        row['info'] = "Deleted"
                        row['status'] = deleted.status_code
                        writer.writerow(row)
                    else:
                        row['info'] = "Linked Record"
                        row['status'] = ""
                        writer.writerow(row)
                except Exception as gen_ex:
                    row['info'] = gen_ex
                    err_writer.writerow(row)
    else:
        print("Connection Failed. Are you connected to the VPN?")
else:
    print("Connection Failed. Are you connected to the VPN?")