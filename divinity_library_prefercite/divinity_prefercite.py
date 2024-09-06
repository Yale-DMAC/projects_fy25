import connections.SQL as sql
import connections.API as api
import pandas as pd
import re
import time

#SQL query that creates a URI from records in the Divinity Library repository that have 'prefercite' and 'Divinity School Library' in the notes field.
QUERY =  ('''
        SELECT DISTINCT CONCAT('/repositories/', resource.repo_id, '/resources/', resource.id) as uri,
         note.notes
         FROM resource
         LEFT JOIN note on resource.id = note.resource_id
         Where note.notes like '%prefercite%Divinity School Library%' and resource.repo_id = "4"
         ''')

#Checks that the connection to the SQL database was successful before continuning otherwise returns an error message. sql.conn function is in a separate file and is essentially just the host, password, username, and ssh tunnel information.
if sql.conn():
    #Opens a connection and exectutes the above query before storing the information in a DataFrame.
    print("Connected to SQL.")
    cursor = sql.connection.cursor()
    cursor.execute(QUERY)
    data = cursor.fetchall()
    df = pd.DataFrame(data=data, columns=["uri", "note"])
    #Adds a blank column to store API data in
    df['original_data'] = pd.Series()

    #Checks that the connection to the API was successful before continuning, otherwise returns an error message. api.conn function is in a separate file and is essentially just the url, username, and password information.
    if api.conn():
        print("Connected to API.")

        #Pulls the URI from the DataFrame and pulls the API json data before storing it in the correct cell in the DataFrame under the 'original_data' column. Acts as a backup of original data before any updates are made.
        row = 0
        for x in df.uri:
            data = api.client.get(x).json()
            df.at[row, 'original_data'] = data
            row += 1
            time.sleep(0.3)

        #Saves the DataFrame to an excel file, uses today's date in the file name if the form of yymmdd.
        date_str = time.strftime("%y%m%d")
        df.to_excel(f"files/{date_str}_Div_prefercite_originaldata.xlsx",engine='xlsxwriter', index=False)

        #Pulls the URI and the api data from the DataFrame. Saves the Notes object from the api data to the notes variable.
        row=0
        for x in df.uri:
            uri = x
            data = df.loc[row, 'original_data']
            row += 1
            notes = data['notes']
                
            #Searches each unlabeled object in the Notes object for a type of 'prefercite'. If the object is a prefercite type, then it will use regex to update 'Yale Divinity School Library' to 'Yale Divinity Library' then post the updated object to ArchivesSpace using the API.
            for i in range(len(notes)):
                if notes[i]['type'] == 'prefercite':
                    cite = notes[i]['subnotes'][0]['content']
                    update = re.sub("Yale Divinity School Library", "Yale Divinity Library", cite)
                    notes[i]['subnotes'][0]['content'] = update
                    api.client.post(x, json=data)
            time.sleep(0.3)   
    else:
        print("API Connection Failed. Are you connected to the VPN?")  
else:
    print("SQL Connection Failed. Are you connected to the VPN?")
