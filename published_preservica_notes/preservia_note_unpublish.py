import connections.SQL as sql
import connections.API as api
import csv
import json
import time

QUERY = """
SELECT DISTINCT CONCAT('/repositories/', r.repo_id, '/resources/', r.id) as uri, note.notes
FROM note
LEFT JOIN resource r ON note.resource_id = r.id
Where note.notes like '%as matching Preservica null%' AND note.resource_id is not null and note.notes like '%"type":"odd"%' AND note.notes like '%publish":true%'
UNION
SELECT DISTINCT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as uri, note.notes
FROM note
LEFT JOIN archival_object ao ON note.archival_object_id = ao.id
Where note.notes like '%as matching Preservica null%' AND note.archival_object_id is not null and note.notes like '%"type":"odd"%' AND note.notes like '%publish":true%'
UNION
SELECT DISTINCT CONCAT('/repositories/', r.repo_id, '/resources/', r.id) as uri, note.notes
FROM note
LEFT JOIN resource r ON note.resource_id = r.id
Where note.notes like '%https://preservica.library.yale.edu%' AND note.resource_id is not null AND note.notes like '%otherfindaid%' AND note.notes like '%publish":true%'
UNION
SELECT DISTINCT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as uri, note.notes
FROM note
LEFT JOIN archival_object ao ON note.archival_object_id = ao.id
Where note.notes like '%https://preservica.library.yale.edu%' AND note.archival_object_id is not null AND note.notes like '%otherfindaid%' AND note.notes like '%publish":true%'
"""

if sql.conn():
    print("Connected to SQL.")
    cursor = sql.connection.cursor()
    cursor.execute(QUERY)
    sql_data = cursor.fetchall()
    date_str = time.strftime("%y%m%d")
    with open(f'files/preservica_pub/{date_str}_preservicapub_uris.csv', 'w', encoding='utf8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['uri'])
        writer.writeheader()
        for row in sql_data:
            writer.writerow({'uri': row[0]})
    if api.conn():
        print("Connected to API.")
        with open(f'files/preservica_pub/{date_str}_preservicapub_uris.csv', 'r', encoding='utf8') as infile:
            reader = csv.DictReader(infile)
            updatefile = open(f'files/preservica_pub/{date_str}_preservicapub_uris_update.csv', 'a', encoding='utf8', newline='')
            errfile = open(f'files/preservica_pub/{date_str}_preservicapub_errors.csv', 'a', encoding='utf8', newline='')
            writer = csv.DictWriter(updatefile, fieldnames=reader.fieldnames + ['info'] + ['status'])
            writer.writeheader()
            err_writer = csv.DictWriter(errfile, fieldnames=reader.fieldnames + ['status'])
            err_writer.writeheader()
            for row in reader:
                try:
                    uri = row['uri']
                    api_data = api.client.get(uri).json()
                    with open(f"files/preservica_pub/backups/{uri.replace('/','_')}.json", 'w', encoding='utf8') as outfile:
                        json.dump(api_data, outfile, sort_keys=True, indent=4)
                    notes = api_data['notes']
                    preservica_url= 'https://preservica.library.yale.edu'
                    delete_note = 'was deleted from catalogue on'
                    for x in notes:
                        check_subnotes = x.get('subnotes')
                        if check_subnotes:
                            subnotes = x['subnotes'][0]
                            if 'content' in subnotes and (preservica_url in subnotes['content'] or delete_note in subnotes['content']):
                                if x['publish'] == True:
                                    x['publish'] = False
                                    row['info'] = "Unpublished"
                                    if subnotes['publish'] == True:
                                        subnotes['publish'] = False
                                elif subnotes['publish'] == True:
                                    subnotes['publish'] = False
                                    row['info'] = "Unpublished"
                                else:
                                    row['info'] = "Already Unpublished"
                    update = api.client.post(uri, json=api_data)
                    row['status'] = update.status_code
                    writer.writerow(row)
                except Exception as gen_ex:
                    row['status'] = gen_ex
                    err_writer.writerow(row)
    else:
        print("API Connection Failed. Are you connected to the VPN?")  
else:
    print("SQL Connection Failed. Are you connected to the VPN?")