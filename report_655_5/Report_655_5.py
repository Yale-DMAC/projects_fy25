import conn as sql
import pandas as pd
import time

#Queries Voyager's SQL for the 655$a, 655$5, Bibnumber, and MFHD ID for records that have a 655$5
QUERY = """
SELECT getbibsubfield(bt.bib_id, '655', 'a'), getbibsubfield(bt.bib_id, '655', '5') , bt.BIB_ID as Bib_number, BM.MFHD_ID as MFHD_ID
FROM BIB_TEXT BT
JOIN BIB_MFHD BM ON BT.BIB_ID = BM.BIB_ID
JOIN MFHD_MASTER MM ON MM.MFHD_ID = BM.MFHD_ID
JOIN LOCATION LOC ON LOC.LOCATION_ID = MM.LOCATION_ID
WHERE getbibsubfield(bt.bib_id, '655', '5') IS NOT NULL
"""

#Uses a function in a separate file containing passwords and usernames to connect with the SQL database. If successful it continues, otherwise it returns an error.
if sql.conn():
    print("Connected Succesfully!")
  #Saves the results from the execute SQL query into the data variable.
    cursor = sql.connection.cursor()
    print("Executing Query...")
    cursor.execute(QUERY)
    data = cursor.fetchall()
  #Some records were returning encoding errors when putting it in a DataFrame so this line updates it to ISO if UTF-8 fails.
    decoded_data = [[str(cell, 'latin1') if isinstance(cell, bytes) else cell for cell in row] for row in data]
  #Saves the updated data in a DataFrame then saves it to an excel file with today's date.
    df = pd.DataFrame(data=decoded_data, columns=["655_a", "655_5", "Bib number", "MFHD number"])
    date_str = time.strftime("%y%m%d")
    df.to_excel(f"files/{date_str}_655_5_mfhd.xlsx",engine='xlsxwriter', index=False)
    print("Query Completed.")
else:
    print("Connection Failed. Are you connected to the VPN?")
