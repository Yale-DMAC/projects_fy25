import connections.API as api
import connections.SQL as sql
import time, json, csv, re
from datetime import datetime

path = 'files/machineactionable/'

QUERY = """
SELECT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', n.archival_object_id) as uri
FROM note n 
LEFT JOIN archival_object ao on ao.id = n.archival_object_id 
WHERE n.notes like '%type":"accessrestrict%'
AND n.notes not like '%end":%'
AND n.notes like '%, 20%'
AND n.notes not like '%, 20%, 20%'
AND n.archival_object_id is not NULL
UNION ALL
SELECT CONCAT('/repositories/', r.repo_id, '/resources/', n.resource_id) as uri
FROM note n 
LEFT JOIN resource r on r.id = n.resource_id 
WHERE n.notes like '%type":"accessrestrict%'
AND n.notes not like '%end":%'
AND n.notes like '%, 20%'
AND n.notes not like '%, 20%, 20%'
AND n.resource_id is not NULL 
"""

if sql.test_conn():
    print("Connected to SQL.")
    cursor = sql.connection.cursor()
    cursor.execute(QUERY)
    sql_data = cursor.fetchall()
    date_str = time.strftime("%y%m%d")
    with open(f'{path}{date_str}_uris.csv', 'w', encoding='utf8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['uri'])
        writer.writeheader()
        for row in sql_data:
            writer.writerow({'uri': row[0]})
    if api.test_conn():
        print("Connected to API.")
        with open(f'{path}{date_str}_uris.csv', 'r', encoding='utf8') as infile:
            reader = csv.DictReader(infile)
            updatefile = open(f'{path}{date_str}_update.csv', 'a', encoding='utf8', newline='')
            errfile = open(f'{path}{date_str}_errors.csv', 'a', encoding='utf8', newline='')
            writer = csv.DictWriter(updatefile, fieldnames=reader.fieldnames + ['status'])
            writer.writeheader()
            err_writer = csv.DictWriter(errfile, fieldnames=reader.fieldnames + ['info'])
            err_writer.writeheader()
            for row in reader:
                try:
                    uri = row['uri']
                    api_data = api.client.get(uri).json()
                    with open(f"{path}backups/{uri.replace('/','_')}.json", 'w', encoding='utf8') as outfile:
                        json.dump(api_data, outfile, sort_keys=True, indent=4)
                    notes = api_data['notes']
                    for x in notes:
                        if x['type'] == 'accessrestrict' and ('rights_restriction' not in x or 'end' not in x['rights_restriction']):
                            check_subnotes = x.get('subnotes')
                            if check_subnotes:
                                subnotes = x['subnotes'][0]
                                if 'content' in subnotes:
                                    date_pattern = r'\b([A-Z][a-z]+) (\d{1,2}), (\d{4})\b'
                                    contentnotes = subnotes['content']
                                    dates = re.findall(date_pattern, contentnotes)
                                    if dates:
                                        for date in dates:
                                            month, day, year = date
                                        try:
                                            month_num = datetime.strptime(month, "%B").month
                                        except ValueError:
                                            month_num = datetime.strptime(month, "%b").month
                                        if 'rights_restriction' not in x:
                                            x['rights_restriction'] = {}
                                        x['rights_restriction']['end'] = f"{year}-{month_num:02d}-{int(day):02d}"
                        else:
                            pass
                    update = api.client.post(uri, json=api_data)
                    row['status'] = update.status_code
                    writer.writerow(row)
                except Exception as gen_ex:
                    row['info'] = gen_ex
                    err_writer.writerow(row)
    else:
        print("Connection Failed. Are you connected to the VPN?")
else:
    print("Connection Failed. Are you connected to the VPN?")