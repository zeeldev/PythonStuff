"""
data.json is the default file name of Self-Serve > DB Info > Environments: All > JSON

Usage: 
python json_reader.py <org_name>
Ex. 
python json_reader.py lmc 
lmc
dbName:  us_lmc_multi
dbServer:  pccsql-use2-prod-w23-cli0003.4ccb146400ac.database.windows.net
dbSize(GB):  1497
==============================================================================================
Date            Author                Comment                  
18-Oct-2021     Lem Elesterio         initial make.  I find the Self-Serve front-end very slow
"""


import json, sys;

orgname = sys.argv[1]

print(orgname)

f = open('data.json',) 

org_data = json.load(f)

for x in range(len(org_data)):
    if org_data[x]['org_code'].lower() == orgname.lower():
        if org_data[x]['deleted'].lower() == 'n' and \
            org_data[x]['archived'].lower() == 'n':
            print("dbName: ",org_data[x]['database_name'])
            print("dbServer: ", org_data[x]['server_name'])
            print("dbSize(GB): ",org_data[x]['db_size'])
            print("environment: ",org_data[x]['environment'])
            print("country: ",org_data[x]['country'])
            print("dbVersion: ",org_data[x]['db_version'])
            break;
