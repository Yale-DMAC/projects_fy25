import connections.API as api
import pandas as pd
import time

#uses a function in a separate file containing passwords to establish a connection to the API. If connection is unsuccessful it returns an error.
if api.conn():
    print("Connected to API successfully.")

    #Asks the user for the path to the Excel file then parses it into a dataframe.
    filename = input('Enter Excel file path: \n')
    xl = pd.ExcelFile(filename)
    sheet_name = xl.sheet_names[0]
    df=xl.parse(sheet_name)

    #Creates a file path for the error log
    date_str = time.strftime("%y%m%d")
    error_file = open(f"files/{date_str}_enum_migrate_errorlog.txt", 'a')

    #For each row in the dataframe, it searches for the 'from', 'to', and 'enumid' columns. Enumid is used to determine which Controlled Value list to update, From values are merged into To values.
    for index, row in df.iterrows():
        fromvar = str(row['from'])
        tovar = str(row['to'])
        enumid = row['enumid']
        x = api.client.post("/config/enumerations/migration", 
                        json={
                            'enum_uri': f'/config/enumerations/{enumid}',
                            'from': fromvar,
                            'to': tovar,
                            'jsonmodel_type': 'enumeration_migration'
                            })
        #Checks if the migration was successful, otherwise returns the status code for the row and updates the error log.
        if x.status_code == 200:
            pass
        else:
            error_file.write(f'{fromvar} encountered Error: {x.status_code} - {x.reason}. \n')
            print(f'{fromvar} encountered Error: {x.status_code} - {x.reason}.')
else:
    print("Connection failed. Are you connected to the VPN?")
