import connections.API as api
import connections.SQL as sql
import csv
import json
import time

QUERY = ("""
SELECT DISTINCT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', ao.id) as uri
         FROM archival_object ao
         JOIN instance i ON i.archival_object_id = ao.id
         JOIN instance_do_link_rlshp idlr ON i.id = idlr.instance_id
         JOIN note on ao.id = note.archival_object_id
         JOIN file_version fv ON fv.digital_object_id = idlr.digital_object_id 
         Where note.notes like '%A copy of this material is available in digital form from Manuscripts and Archives%'
         AND idlr.digital_object_id is not NULL 
         AND (fv.file_uri like '%aviaryplatform.com%' OR fv.file_uri like 'https://collections.library.yale.edu%')
""")

if sql.conn():
    print("Connected to SQL.")
    cursor = sql.connection.cursor()
    cursor.execute(QUERY)
    sql_data = cursor.fetchall()
    with open('files/preservica_notes/uris.csv', 'w', encoding='utf8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['uri'])
        writer.writeheader()
        for row in sql_data:
            writer.writerow({'uri': row[0]})
    if api.conn():
        print("Connected to API.")
        with open('files/preservica_notes/uris.csv', 'r', encoding='utf8') as infile:
            reader = csv.DictReader(infile)
            outfile = open('files/preservica_notes/uris_status.csv', 'a', encoding='utf8', newline='')
            errfile = open('files/preservica_notes/uris_errors.csv', 'a', encoding='utf8', newline='') 
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames + ['info'])
            err_writer = csv.DictWriter(errfile, fieldnames=reader.fieldnames + ['info'])
            err_writer.writeheader()
            writer.writeheader()
            for row in reader:
                try:
                    uri = row['uri']
                    data = api.client.get(uri).json()
                    with open(f"files/preservica_notes/backups/{uri.replace('/','_')}.json", 'w', encoding='utf8') as outfile:
                        json.dump(data, outfile, sort_keys=True, indent=4)
                    notes = data['notes']
                    notes = [note for note in notes if note['type'] != 'altformavail']
                    data['notes'] = notes
                    update = api.client.post(uri, json=data)
                    row['info'] = update.status_code
                    writer.writerow(row)
                    time.sleep(0.3) 
                except(api.ArchivesSpaceError) as err:
                    api.logging.error(err)
                    row['info'] = err
                    err_writer.writerow(row)
                except Exception as gen_ex:
                    row['info'] = gen_ex
                    err_writer.writerow(row)
    else:
        print("API Connection Failed. Are you connected to the VPN?")  
else:
    print("SQL Connection Failed. Are you connected to the VPN?")