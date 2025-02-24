import requests, csv, time, conn
from pprint import pprint
import xml.etree.ElementTree as ET
from tqdm import tqdm


M_QUERY = """
SELECT bt.bib_id, i.item_id, bt.title, l.location_code, mm.display_call_no, ic.item_stat_code_desc
FROM BIB_TEXT bt
INNER JOIN BIB_MFHD bm ON bm.bib_id = bt.bib_id
INNER JOIN MFHD_MASTER mm ON mm.mfhd_id = bm.mfhd_id
INNER JOIN location l ON mm.location_id = l.location_id
WHERE l.location_code IN ('lsfmapr', 'lsfmssr', 'lsfsslr', 'smlmss', 'smlyal', 'smlyalt', 'smlyalc', 'lsfr', 'lsfkslr', 'lsffesr', 'lsfnumr', 'lsfgdcr', 'lsfsemr', 'lsfbeir', 'beineliz', 'beingen', 'beinosb', 'beinsref', 'beinycal', 'beinycgl', 'beinref', 'beinwa', 'beints', 'beintso', 'beintsw', 'beintsa', 'beintsg', 'lsfbeiar', 'lsfbeior', 'lsfbeigr', 'lsfbeiwr')
AND GetBibTag(bt.bib_id, '506') not like '%curator%'
GROUP BY bt.bib_id
HAVING count(GetBibTag(bt.bib_id, '506')) > 1
"""

F_QUERY = """
SELECT bt.bib_id, i.item_id, bt.title, l.location_code, mm.display_call_no, ic.item_stat_code_desc, GetBibTag(bt.bib_id, '506')
FROM bib_text bt
INNER JOIN BIB_MFHD bm ON bm.bib_id = bt.bib_id
INNER JOIN MFHD_MASTER mm ON mm.mfhd_id = bm.mfhd_id
INNER JOIN location l ON mm.location_id = l.location_id
INNER JOIN item_vw iv ON iv.mfhd_id = mm.mfhd_id
INNER JOIN item_stats i ON i.item_id = iv.item_id
INNER JOIN item_stat_code ic ON ic.item_stat_id = i.item_stat_id
WHERE l.location_code IN ('lsfmapr', 'lsfmssr', 'lsfsslr', 'smlmss', 'smlyal', 'smlyalt', 'smlyalc', 'lsfr', 'lsfkslr', 'lsffesr', 'lsfnumr', 'lsfgdcr', 'lsfsemr', 'lsfbeir', 'beineliz', 'beingen', 'beinosb', 'beinsref', 'beinycal', 'beinycgl', 'beinref', 'beinwa', 'beints', 'beintso', 'beintsw', 'beintsa', 'beintsg', 'lsfbeiar', 'lsfbeior', 'lsfbeigr', 'lsfbeiwr')
AND (i.item_stat_id = 31 OR i.item_stat_id = 28 OR i.item_stat_id = 27 OR GetBibTag(bt.bib_id, '506') like '%curator%') 
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

def bibid_list(data):
    biblist = []
    for row in data:
        biblist.append(row[0])
    return biblist

def csv_config(file, data, fulldata = False):
    date_str = time.strftime("%y%m%d")
    updatefile = open(f'files/{date_str}_{file}.csv', 'a', encoding='utf8', newline='')
    if fulldata:
        processreport = csv.DictWriter(updatefile, fieldnames=['bib_id'] + ['item_id'] + ['title'] + ['location_code'] + ['call_number'] + ['506_note'] +  ['restrictions'])
        processreport.writeheader()
        for row in data:
                processreport.writerow({'bib_id': row[0], 'item_id':row[1], 'title':row[2], 'location_code':row[3], 'call_number':row[4], '506_field': row[6], ['restrictions']:row[5]})
    else:
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
        combined_values = []
        response = requests.get(f'https://libapp.library.yale.edu/VoySearch/GetBibMarc?bibid={id}')
        xml_data = response.text
        root = ET.fromstring(xml_data)
        namespaces = {'marc': 'http://www.loc.gov/MARC21/slim'}
        datafields_506 = root.findall('.//marc:datafield[@tag="506"]', namespaces=namespaces)
        for datafield in datafields_506:
            subfields = datafield.findall('marc:subfield', namespaces=namespaces)
            subfield_values = [subfield.text for subfield in subfields if subfield.text]
            combined_values.extend(subfield_values)
        if 'curator' in combined_values:
            curators[id] = "; ".join(combined_values)
    return curators


def main():
    print("Start Time: ", time.strftime("%H:%M:%S"))
    sql_data = sql_query(M_QUERY)
    curators = voysearch(bibid_list(sql_data))
    filtered_sql_data = []
    for row in sql_data:
        if row[0] in curators:
            row_with_field = row + (curators[row[0]],)
            filtered_sql_data.append(row_with_field)
    csv_config('curator_report', sql_query(F_QUERY), True)
    csv_config('curator_report', filtered_sql_data, True)
    print("End Time: ", time.strftime("%H:%M:%S"))

if __name__ == "__main__":
    main()