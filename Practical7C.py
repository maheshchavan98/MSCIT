import sys 
import os 
from datetime import datetime 
from pytz import timezone 
import pandas as pd 
import sqlite3 as sq 
import uuid 
pd.options.mode.chained_assignment = None 
################################################################ 

# Paths for CSV and SQLite database
csv_path = 'C:/DS/Dataset2.csv'
db_path = 'C:/DS/datavault.db'

# Create SQLite connections
conn1 = sq.connect(db_path)
conn2 = sq.connect(db_path)
################################################################ 
print('\n#################################') 
print('Time Dimension') 
BirthZone = 'Atlantic/Reykjavik' 
BirthDateUTC = datetime(1960, 12, 20, 10, 15, 0) 
BirthDateZoneUTC = BirthDateUTC.replace(tzinfo=timezone('UTC')) 
BirthDateZoneStr = BirthDateZoneUTC.strftime("%Y-%m-%d %H:%M:%S") 
BirthDateZoneUTCStr = BirthDateZoneUTC.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)") 
BirthDate = BirthDateZoneUTC.astimezone(timezone(BirthZone)) 
BirthDateStr = BirthDate.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)") 
BirthDateLocal = BirthDate.strftime("%Y-%m-%d %H:%M:%S") 
################################################################ 
IDTimeNumber = str(uuid.uuid4()) 
TimeLine = {
    'TimeID': [IDTimeNumber],
    'UTCDate': [BirthDateZoneStr],
    'LocalTime': [BirthDateLocal],
    'TimeZone': [BirthZone]
} 
TimeFrame = pd.DataFrame(TimeLine) 
############################################################### 
DimTime = TimeFrame 
DimTimeIndex = DimTime.set_index(['TimeID'], inplace=False) 
################################################################ 
sTable = 'Dim_Time' 
print('\n#################################') 
print('Storing :', db_path, '\n Table:', sTable) 
print('\n#################################') 
DimTimeIndex.to_sql(sTable, conn1, if_exists="replace") 
DimTimeIndex.to_sql(sTable, conn2, if_exists="replace") 
################################################################ 
print('\n#################################') 
print('Dimension Person') 
print('\n#################################') 
FirstName = 'Mahesh' 
LastName = 'More' 
############################################################### 
IDPersonNumber = str(uuid.uuid4()) 
PersonLine = {
    'PersonID': [IDPersonNumber],
    'FirstName': [FirstName],
    'LastName': [LastName],
    'Zone': ['UTC'],
    'DateTimeValue': [BirthDateZoneStr]
} 
PersonFrame = pd.DataFrame(PersonLine) 
################################################################ 
DimPerson = PersonFrame 
DimPersonIndex = DimPerson.set_index(['PersonID'], inplace=False) 
################################################################ 
sTable = 'Dim_Person' 
print('\n#################################') 
print('Storing :', db_path, '\n Table:', sTable) 
print('\n#################################') 
DimPersonIndex.to_sql(sTable, conn1, if_exists="replace") 
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace") 
################################################################ 
print('\n#################################') 
print('FactPersontime') 
print('\n#################################') 
IDFactNumber = str(uuid.uuid4()) 
PersonTimeLine = {
    'IDNumber': [IDFactNumber],
    'IDPersonNumber': [IDPersonNumber],
    'IDTimeNumber': [IDTimeNumber]
} 
PersonTimeFrame = pd.DataFrame(PersonTimeLine) 
################################################################ 
FctPersonTime = PersonTimeFrame 
FctPersonTimeIndex = FctPersonTime.set_index(['IDNumber'], inplace=False) 
################################################################ 
sTable = 'Fact_Person_Time' 
print('\n#################################') 
print('Storing :', db_path, '\n Table:', sTable) 
print('\n#################################') 
FctPersonTimeIndex.to_sql(sTable, conn1, if_exists="replace") 
FctPersonTimeIndex.to_sql(sTable, conn2, if_exists="replace") 
print('Done')
###Transform Superstep Sun Model

##Go to SQLite select * from Dim_Time & select * from Dim_Person##