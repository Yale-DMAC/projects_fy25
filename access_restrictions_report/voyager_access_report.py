import requests, csv, time, conn
from tqdm import tqdm
from pprint import pprint
import xml.etree.ElementTree as ET

C_QUERY = """
SELECT bt.bib_id, GetBibTag(bt.bib_id, '506')
FROM bib_text bt
INNER JOIN BIB_MFHD bm ON bm.bib_id = bt.bib_id
INNER JOIN MFHD_MASTER mm ON mm.mfhd_id = bm.mfhd_id
INNER JOIN location l ON mm.location_id = l.location_id
WHERE l.location_code in ('lsfmapr', 'lsfmssr', 'lsfsslr', 'smlmss', 'smlyal', 'smlyalt', 'smlyalc', 'lsfr', 'lsfkslr', 'lsffesr', 'lsfnumr', 'lsfgdcr', 'lsfsemr', 'lsfbeir', 'beineliz', 'beingen', 'beinosb', 'beinsref', 'beinycal', 'beinycgl', 'beinref', 'beinwa', 'beints', 'beintso', 'beintsw', 'beintsa', 'beintsg', 'lsfbeiar', 'lsfbeior', 'lsfbeigr', 'lsfbeiwr')
AND GetBibTag(bt.bib_id, '506') like '%curator%'
GROUP BY bt.bib_id
"""

M_QUERY = """
SELECT bt.bib_id, count(GetBibTag(bt.bib_id, '506'))
FROM BIB_TEXT bt
INNER JOIN BIB_MFHD bm ON bm.bib_id = bt.bib_id
INNER JOIN MFHD_MASTER mm ON mm.mfhd_id = bm.mfhd_id
INNER JOIN location l ON mm.location_id = l.location_id
WHERE l.location_code IN ('lsfmapr', 'lsfmssr', 'lsfsslr', 'smlmss', 'smlyal', 'smlyalt', 'smlyalc', 'lsfr', 'lsfkslr', 'lsffesr', 'lsfnumr', 'lsfgdcr', 'lsfsemr', 'lsfbeir', 'beineliz', 'beingen', 'beinosb', 'beinsref', 'beinycal', 'beinycgl', 'beinref', 'beinwa', 'beints', 'beintso', 'beintsw', 'beintsa', 'beintsg', 'lsfbeiar', 'lsfbeior', 'lsfbeigr', 'lsfbeiwr')
AND GetBibTag(bt.bib_id, '506') not like '%curator%'
GROUP BY bt.bib_id
HAVING count(GetBibTag(bt.bib_id, '506')) > 1
"""

def sql_query(query):
    if conn.conn():
        print("Connected Succesfully!")
        cursor = conn.connection.cursor()
        print("Executing Query...")
        cursor.execute(query)
        sql_data = cursor.fetchall()
        return sql_data
    else:
        print("Connection Failed. Are you connected to the VPN?")

def csv_config(file, data):
    date_str = time.strftime("%y%m%d")
    updatefile = open(f'files/{date_str}_{file}.csv', 'a', encoding='utf8', newline='')
    processreport = csv.DictWriter(updatefile, fieldnames=['bib_id'] + ['506_field'])
    processreport.writeheader()
    if isinstance(data, dict):
        for bib_id, field in data.items():
            processreport.writerow({'bib_id': bib_id, '506_field': field})
    elif isinstance(data, list):
        for row in data:
            processreport.writerow({'bib_id': row[0], '506_field': row[1]})

def voysearch(bib_ids):
    curators = {}
    for id in tqdm(bib_ids, desc="Processing Bib IDs", unit="Bib ID"):
        time.sleep(2)
        response = requests.get(f'https://libapp.library.yale.edu/VoySearch/GetBibMarc?bibid={id}')
        xml_data = response.text
        root = ET.fromstring(xml_data)
        namespaces = {'marc': 'http://www.loc.gov/MARC21/slim'}
        datafields_506 = root.findall('.//marc:datafield[@tag="506"]', namespaces=namespaces)
        for datafield in datafields_506:
            subfields = datafield.findall('marc:subfield', namespaces=namespaces)
            for subfield in subfields:
                if 'curator' in subfield.text:
                    curators[id] = subfield.text
    return curators


def main():
    print("Start Time: ", time.strftime("%H:%M:%S"))
    csv_config('506_curators', sql_query(C_QUERY))
    sql_data = sql_query(M_QUERY)
    bib_ids = []
    for row in sql_data:
        bib_ids.append(row[0])
    curators = voysearch(bib_ids)
    csv_config('506_multis', curators)
    print("End Time: ", time.strftime("%H:%M:%S"))

if __name__ == "__main__":
    main()