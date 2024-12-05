import connections.SQL as sql
import connections.API as api
import csv, time, json, re

QUERY = """
SELECT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', extent.archival_object_id) 
FROM extent 
JOIN archival_object ao ON ao.id = extent.archival_object_id 
WHERE number like '%.0'
AND extent.archival_object_id is not null
UNION ALL
SELECT CONCAT('/repositories/', a.repo_id, '/accessions/', extent.accession_id)
FROM extent 
JOIN accession a ON a.id = extent.accession_id 
WHERE number like '%.0'
AND extent.accession_id is not null
UNION ALL
SELECT CONCAT('/repositories/', r.repo_id, '/resources/', extent.resource_id)
FROM extent 
JOIN resource r ON r.id = extent.resource_id 
WHERE number like '%.0'
AND extent.resource_id is not null
UNION ALL
SELECT CONCAT('/repositories/', do.repo_id, '/digital_objects/', extent.digital_object_id)
FROM extent 
JOIN digital_object do ON do.id = extent.digital_object_id 
WHERE number like '%.0'
AND extent.digital_object_id is not null
"""

path = 'files/trailing_zeros/'
date_str = time.strftime("%y%m%d")

updatefile = open(f'{path}{date_str}_updates.csv', 'a', encoding='utf8', newline='')
writer = csv.DictWriter(updatefile, fieldnames=['uri'] + ['status'] + ['info'])
writer.writeheader()

if sql.conn():
    print('Connected to SQL.')
    cursor = sql.connection.cursor()
    cursor.execute(QUERY)
    sql_data = cursor.fetchall()
    row_dict = {}
    if api.conn():
        print('Connected to API.')
        for row in sql_data:
            try:
                uri = row[0]
                api_data = api.client.get(f'{uri}').json()
                data = api_data['extents'][0]['number']
                if data.endswith('.0'):
                    with open(f"{path}backups/{uri.replace('/','_')}.json", 'w', encoding='utf8') as outfile:
                        json.dump(api_data, outfile, sort_keys=True, indent=4)
                    data_update = re.sub(r'\.0','',data)
                    api_data['extents'][0]['number'] = data_update
                    update = api.client.post(uri, json=api_data)
                    row_dict['uri'] = uri
                    row_dict['status'] = update.status_code
                    if update.status_code != 200:
                        row_dict['info'] = json.loads(update.text)
                    else:
                        row_dict['info'] = ''
                    writer.writerow(row_dict)
            except Exception as gen_ex:
                row_dict['uri'] = row[0]
                row_dict['info'] = gen_ex
                row_dict['status'] = 'error'
                writer.writerow(row_dict) 
    else:
        print("Error connecting to the API. Are you connected to the VPN?")
else:
    print("Error connecting to the SQL. Are you connected to the VPN?")

