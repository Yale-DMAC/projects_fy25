import connections.SQL as sql
import connections.API as api
import csv, time, json, re

QUERY = """
SELECT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', e.archival_object_id) 
FROM extent e
JOIN archival_object ao ON ao.id = e.archival_object_id 
WHERE e.container_summary like '(%'
AND e.archival_object_id is not null
UNION ALL
SELECT CONCAT('/repositories/', a.repo_id, '/accessions/', e.accession_id)
FROM extent e
JOIN accession a ON a.id = e.accession_id 
WHERE e.container_summary like '(%'
AND e.accession_id is not null
UNION ALL
SELECT CONCAT('/repositories/', r.repo_id, '/resources/', e.resource_id)
FROM extent e
JOIN resource r ON r.id = e.resource_id 
WHERE e.container_summary like '(%'
AND e.resource_id is not null
UNION ALL
SELECT CONCAT('/repositories/', do.repo_id, '/digital_objects/', e.digital_object_id)
FROM extent e
JOIN digital_object do ON do.id = e.digital_object_id 
WHERE e.container_summary like '(%'
AND e.digital_object_id is not null
"""
path = 'files/cp_parentheses/'
date_str = time.strftime("%y%m%d")

updatefile = open(f'{path}{date_str}_updates.csv', 'a', encoding='utf8', newline='')
writer = csv.DictWriter(updatefile, fieldnames=['uri'] + ['original'] + ['update'] + ['info'])
writer.writeheader()

def sql_get(query):
    if sql.conn():
        cursor = sql.connection.cursor()
        cursor.execute(query)
        sql_data = cursor.fetchall()
    return sql_data

def backup(uri, data):
	with open(f"{path}backups/{uri.replace('/','_')}.json", 'w', encoding='utf8') as outfile:
	    json.dump(data, outfile, sort_keys=True, indent=4)

def unsuppress(uri, status):
	if status == True:
		api.client.post(f'{uri}/suppressed', params={"suppressed": False})
		return True
	else:
		api.client.post(f'{uri}/suppressed', params={"suppressed": True})
		return False

def cleanup(data):
	originals = []
	updates = []
	info = ''
	try:
		for x in data['extents'] :
			if 'container_summary' in x:
				if x['container_summary'].startswith("("):
					originals.append(x['container_summary'])
					x['container_summary'] = re.sub(r'^\((.*)\)',r'\1', x['container_summary'])
					updates.append(x['container_summary'])
	except Exception as gen_err:
		info = gen_err
	return originals, updates, data, info

def to_csv(uri, originals, updates, info):
	row_dict['uri'] = uri
	row_dict['original'] = originals
	row_dict['update'] = updates
	row_dict['info'] = info
	writer.writerow(row_dict)

row_dict = {}
sql_data = sql_get(QUERY)
if api.conn():
	for row in sql_data:
		uri = row[0]
		api_data = api.client.get(uri).json()
		backup(uri, api_data)
		if api_data['suppressed'] == True:
			suppress = unsuppress(uri, True)
			api_data = api.client.get(uri).json()
		else:
			suppress = False
		originals, updates, cs_update, info = cleanup(api_data)
		if not originals:
			info = 'No originals'
		else:
			data_update = api.client.post(uri, json=cs_update)
			if data_update.status_code == 200:
				info = data_update.status_code
			else:
				info = f'Code: {data_update.status_code}. Text: {json.loads(data_update.text)}'
		if suppress == True:
			suppress = unsuppress(uri, False)
		to_csv(uri, originals, updates, info)