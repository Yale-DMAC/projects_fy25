import connections.SQL as sql
import connections.API as api
import json, csv, time

path = 'files/mullanguages/'

QUERY = """
SELECT CONCAT('/repositories/', ao.repo_id, '/archival_objects/', lm.archival_object_id) as uri
FROM lang_material lm 
LEFT JOIN language_and_script las on las.lang_material_id = lm.id
LEFT JOIN archival_object ao on ao.id = lm.archival_object_id 
WHERE las.language_id = 685 AND lm.archival_object_id is not null
UNION 
SELECT CONCAT('/repositories/', r.repo_id, '/resources/', lm.resource_id) as uri
FROM lang_material lm 
LEFT JOIN language_and_script las on las.lang_material_id = lm.id
LEFT JOIN resource r on r.id = lm.resource_id 
WHERE las.language_id = 685 AND lm.resource_id is not null
"""
date_str = time.strftime("%y%m%d")
updatefile = open(f'{path}{date_str}_mulnotes_updates.csv', 'a', encoding='utf8', newline='')
errfile = open(f'{path}{date_str}_errors.csv', 'a', encoding='utf8', newline='')
writer = csv.DictWriter(updatefile, fieldnames=['uri'] + ['status'] + ['info'])
writer.writeheader()
err_writer = csv.DictWriter(errfile, fieldnames=['uri'] + ['info'])
err_writer.writeheader()

lang_dict = {
    'Afrikaans': 'afr',
    'Algonquian': 'alg',
    'Amharic': 'amh',
    'Arabic': 'ara',
    'Aramaic': 'arc',
    'Bosnian': 'bos',
    'Catalan': 'cat',
    'Chinese': 'chi',
    'Coptic': 'cop',
    'Croatian': 'hrv',
    'Czech': 'cze',
    'Dutch': 'dut',
    'Egyptian': 'egy',
    'English': 'eng',
    'Finnish': 'fin',
    'French Creole': 'cpf',
    'French': 'fre',
    'German': 'ger',
    'Greek': 'gre',
    'Gujarati': 'guj',
    'Hausa': 'hau',
    'Hebrew': 'heb',
    'Hungarian': 'hun',
    'Igbo': 'ibo',
    'Ilocano': 'ilo',
    'Indonesian': 'ind',
    'Italian': 'ita',
    'Japanese': 'jpn',
    'Judeo-Arabic': 'jrb',
    'Ladino': 'lad',
    'Latin': 'lat',
    'Malagasy': 'mlg',
    'Malay': 'may',
    'Marathi': 'mar',
    'Middle English': 'enm',
    'Pahlavi': 'pal',
    'Persian': 'per',
    'Polish': 'pol',
    'Portuguese': 'por',
    'Romanian': 'rum',
    'Rundi': 'run',
    'Russian': 'rus',
    'Serbian': 'srp',
    'Serbo-Croatian': 'hrv',
    'Slavic': 'sla',
    'Slovak': 'slo',
    'Somali': 'som',
    'Sotho': 'sot',
    'Spanish': 'spa',
    'Susu': 'sus',
    'Swahili': 'swa',
    'Syriac': 'syr',
    'Tagalog': 'tgl',
    'Tigrina': 'tir',
    'Turkish': 'tur',
    'Urdu': 'urd',
    'Vietnamese': 'vie',
    'Welsh': 'wel',
    'Wolof': 'wol',
    'Yiddish': 'yid',
    'Yoruba': 'yor'
}

if sql.conn():
    print("Connected to SQL.")
    cursor = sql.connection.cursor()
    cursor.execute(QUERY)
    data = cursor.fetchall()
    if api.conn():
        print("Connected to API.")
        row_dict = {}
        for row in data:
            try:
                uri = row[0]
                api_data = api.client.get(f'{uri}').json()
                if len(api_data['lang_materials']) > 1 and len(api_data['lang_materials'][1]['notes']) > 0:
                    with open(f"{path}backups/{uri.replace('/','_')}.json", 'w', encoding='utf8') as outfile:
                            json.dump(api_data, outfile, sort_keys=True, indent=4)
                    lang_note = api_data['lang_materials'][1]['notes'][0]['content'][0]
                    languages_in_note = []
                    for lang in lang_dict.keys():
                        if lang in lang_note:
                            languages_in_note.append(lang_dict[lang])
                    i = 0
                    for x in languages_in_note:
                        lang_exist = False
                        for n in api_data['lang_materials']:
                            if 'language_and_script' in n and n['language_and_script']['language'] == x:
                                lang_exist = True
                            else:
                                pass
                        if lang_exist == True:
                            pass
                        elif i == 0 and api_data['lang_materials'][0]['language_and_script']['language'] == 'mul':
                            api_data['lang_materials'][0]['language_and_script']['language'] = x
                            i += 1
                        else:
                            api_data['lang_materials'].append({'jsonmodel_type': 'lang_material', 'language_and_script': {'jsonmodel_type': 'language_and_script', 'language': x}} )
                    if api_data['lang_materials'][0]['language_and_script']['language'] == 'mul':
                        del api_data['lang_materials'][0]
                    update = api.client.post(uri, json=api_data)
                    row_dict['info'] = json.loads(update.text)
                    row_dict['uri'] = uri
                    row_dict['status'] = update.status_code
                    writer.writerow(row_dict)
                else:
                    pass
            except Exception as gen_ex:
                row_dict['uri'] = row[0]
                row_dict['info'] = gen_ex
                err_writer.writerow(row_dict)
    else:
        print("Error connecting to the API. Are you connected to the VPN?")         
else:
    print("Error connecting to the SQL. Are you connected to the VPN?")