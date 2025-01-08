import conn, time, csv

QUERY = """
WITH cnce_table as(
SELECT LISTAGG(getbibsubfield(btc.bib_id, '510', 'c'), '; ') WITHIN GROUP (ORDER BY getbibsubfield(btc.bib_id, '510', 'c')) AS cnce_value, btc.bib_id
FROM BIB_TEXT btc
WHERE getbibsubfield(btc.bib_id, '510', 'c') like 'CNCE%'
GROUP BY btc.bib_id
)
SELECT utl_i18n.raw_to_nchar(rawtohex(bti.title), 'UTF8'), utl_i18n.raw_to_nchar(rawtohex(bti.author), 'UTF8'), utl_i18n.raw_to_nchar(rawtohex(bti.edition), 'UTF8'), bti.language, SUBSTR(bti.field_008, 16, 3) as pubcountry, SUBSTR(bti.field_008, 8, 4) as pubdate, li.location_code, bti.network_number, cti.cnce_value
, utl_i18n.raw_to_nchar(rawtohex(getallbibtag(bti.bib_id, '260', 1)), 'UTF8') AS bibtag260, utl_i18n.raw_to_nchar(rawtohex(getallbibtag(bti.bib_id, '300', 1)), 'UTF8') AS bibtag300
FROM BIB_TEXT bti
LEFT JOIN cnce_table cti ON cti.bib_id = bti.bib_id
LEFT JOIN BIB_LOCATION bli ON bli.bib_id = bti.bib_id
LEFT JOIN LOCATION li ON li.location_id = bli.location_id
WHERE SUBSTR(bti.field_008, 16, 2) = 'it'
AND bti.field_008 is not NULL
AND li.LOCATION_CODE LIKE 'bein%'
UNION ALL
SELECT utl_i18n.raw_to_nchar(rawtohex(bt.title), 'UTF8'), utl_i18n.raw_to_nchar(rawtohex(bt.author), 'UTF8'), utl_i18n.raw_to_nchar(rawtohex(bt.edition), 'UTF8'), bt.language, SUBSTR(bt.field_008, 16, 3) as pubcountry, SUBSTR(bt.field_008, 8, 4) as pubdate, l.location_code, bt.network_number, ct.cnce_value
, utl_i18n.raw_to_nchar(rawtohex(getallbibtag(bt.bib_id, '260', 1)), 'UTF8') AS bibtag260, utl_i18n.raw_to_nchar(rawtohex(getallbibtag(bt.bib_id, '300', 1)), 'UTF8') AS bibtag300
FROM BIB_TEXT bt
LEFT JOIN cnce_table ct ON ct.bib_id = bt.bib_id
LEFT JOIN BIB_LOCATION bl ON bl.bib_id = bt.bib_id
LEFT JOIN LOCATION l ON l.location_id = bl.location_id
WHERE SUBSTR(bt.field_008, 16, 2) != 'it'
AND bt.language = 'ita'
AND bt.field_008 is not NULL
AND l.LOCATION_CODE LIKE 'bein%'
"""
date_str = time.strftime("%y%m%d")

updatefile = open(f'files/{date_str}_ita_report_filter.csv', 'a', encoding='utf8', newline='')
processreport = csv.DictWriter(updatefile, fieldnames=['title', 'author', 'edition', 'language', 'pub_country', 'pub_date', '260_field', '300_field', 'location_code', 'network_num', 'CNCE'])
processreport.writeheader()

if conn.conn():
    print("Connected Succesfully!")
    cursor = conn.connection.cursor()
    print("Executing Query...")
    cursor.execute(QUERY)
    data = cursor.fetchall()
    for row in data:
        try:
            pub_date = int(row[5])
            if 1500 < pub_date < 1601:
                processreport.writerow({'title': row[0], 'author': row[1], 'edition': row[2], 'language': row[3], 'pub_country': row[4], 'pub_date': row[5], 'location_code': row[6], 'network_num': row[7], 'CNCE': row[8], '260_field': row[9], '300_field': row[10]})
        except ValueError:
            if len(str(row[5])) == 4 and str(row[5]).startswith('15'):
                processreport.writerow({'title': row[0], 'author': row[1], 'edition': row[2], 'language': row[3], 'pub_country': row[4], 'pub_date': row[5], 'location_code': row[6], 'network_num': row[7], 'CNCE': row[8], '260_field': row[9], '300_field': row[10]})
            else:
                pass
else:
    print("Connection Failed. Are you connected to the VPN?")