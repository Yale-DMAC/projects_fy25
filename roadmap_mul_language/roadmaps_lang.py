import connections.API as api
import csv, json, time, os
from tqdm import tqdm

use_test = False
file = "files/roadmaps/Road_Maps_Boxes.csv"
path = "files/roadmaps"

def post(uri, data):
    method_name = 'test_conn' if use_test else 'conn'
    if getattr(api, method_name)():
        response = api.client.post(uri, json=data)
        if response.status_code == 200:
            result = response.json()
            return result
        else:
            error = response.text
            error = json.loads(error)
            return error

def get(uri):
    method_name = 'test_conn' if use_test else 'conn'
    if getattr(api, method_name)():
        response = api.client.get(uri)
        result = response.json()
        return result

def lang(langs, apidata):
    existing_langs = {
        n['language_and_script']['language']
        for n in apidata.get('lang_materials', [])
        if 'language_and_script' in n and 'language' in n['language_and_script']
    }
    for x in langs:
        if x not in existing_langs:
            apidata.setdefault('lang_materials', []).append({
                'jsonmodel_type': 'lang_material',
                'language_and_script': {
                    'jsonmodel_type': 'language_and_script',
                    'language': x
                }
            })
    return apidata

def csv_config(path):
        date_str = date_str = time.strftime("%y%m%d")
        if not os.path.exists(path):
            os.makedirs(path)
        updatefile = open(f'{path}/{date_str}_report.csv', 'a', encoding='utf8', newline='')
        writer = csv.DictWriter(updatefile, fieldnames=['id', 'uri', 'results', 'record'])
        writer.writeheader()
        return writer

def to_csv(writer, uri, results, record, id):
        row_dict = {}
        row_dict['id'] = id
        row_dict['uri'] = uri
        row_dict['results'] = results
        row_dict['record'] = record
        writer.writerow(row_dict)

def backup(path, uri, data):
        if not os.path.exists(f'{path}/backups'):
            os.makedirs(f'{path}/backups')
        with open(f"{path}/backups/{uri.replace('/','_')}.json", 'w', encoding='utf8') as outfile:
	        json.dump(data, outfile, sort_keys=True, indent=4)	

def main():
    input = open(file, encoding='utf-8')
    reader = csv.reader(input)
    writer = csv_config(path)
    for row in tqdm(reader, desc="Processing URIs", unit="URI"):
        id = row[3]
        langs = row[6].lower().split()
        uri = 'repositories/11/archival_objects/' + id
        apidata = get(uri)
        backup(path, uri, apidata)
        apidata = lang(langs, apidata)
        result = post(uri, apidata)
        to_csv(writer, uri, result, apidata, id)

if __name__ == "__main__":
    main()