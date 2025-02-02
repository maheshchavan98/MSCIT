import sys 
import os 
import pandas as pd 
import sqlite3 as sq 
from pandas.io import sql 
import uuid 

sDatabaseName1 = 'C:/DS/Vermeulen.db' 
sDatabaseName2 = 'C:/DS/datavault.db' 

conn1 = sq.connect(sDatabaseName1) 
conn2 = sq.connect(sDatabaseName2) 

t = 0 
tMax = 360 * 180 

LocationFrame = pd.DataFrame()

for Longitude in range(-180, 180, 10): 
    for Latitude in range(-90, 90, 10): 
        t += 1 
        IDNumber = str(uuid.uuid4()) 
        LocationName = 'L' + format(round(Longitude, 3) * 1000, '+07.0f') + '' + format(round(Latitude, 3) * 1000, '+07.0f')

        print('Create:', t, 'of', tMax, ':', LocationName)

        LocationLine = {
            'ObjectBaseKey': ['GPS'],
            'IDNumber': [IDNumber],
            'LocationNumber': [str(t)],
            'LocationName': [LocationName],
            'Longitude': [Longitude],
            'Latitude': [Latitude]
        }
        
        LocationRow = pd.DataFrame(LocationLine)

        if t == 1: 
            LocationFrame = LocationRow 
        else: 
            LocationFrame = pd.concat([LocationFrame, LocationRow], ignore_index=True)

LocationHubIndex = LocationFrame.set_index(['IDNumber'], inplace=False) 

sTable1 = 'Process-Location' 
print('Storing:', sDatabaseName1, 'Table:', sTable1) 
LocationHubIndex.to_sql(sTable1, conn1, if_exists="replace") 

sTable2 = 'HubLocation' 
print('Storing:', sDatabaseName2, 'Table:', sTable2) 
LocationHubIndex.to_sql(sTable2, conn2, if_exists="replace") 

print('################') 
print('vacuum Databases') 
sSQL = "VACUUM"  # Replace 'TableName' with your actual table name
sql.execute(sSQL, conn1) 
sql.execute(sSQL, conn2) 
print('################') 

print('### Done!! ############################################')
##Process Superstep Location.py
#Open db in sqlite and show table hublocation
