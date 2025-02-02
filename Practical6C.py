import sys 
import os 
import pandas as pd 
import sqlite3 as sq 
from pandas.io import sql 
################################################################ 
InputFileName='C:/DS/Dataset.csv' 
################################################################ 
################################################################ 
sDatabaseName='C:/DS/Vermeulen.db' 
conn1 = sq.connect(sDatabaseName) 
################################################################ 
################################################################ 
sDatabaseName='C:/DS/datavault.db' 
conn2 = sq.connect(sDatabaseName) 
################################################################ 
sFileName=InputFileName 
print('Loading :',sFileName) 
EventRawData=pd.read_csv(sFileName,header=0,low_memory=False, 
encoding="latin-1") 
EventRawData.index.names=['EventID'] 
EventHubIndex=EventRawData 
################################################################ 
sTable = 'ProcessEvent' 
print('Storing :',sDatabaseName,' Table:',sTable) 
EventHubIndex.to_sql(sTable, conn1, if_exists="replace") 
################################################################ # 
sTable = 'HubEvent' 
print('Storing :',sDatabaseName,' Table:',sTable) 
EventHubIndex.to_sql(sTable, conn2, if_exists="replace") 
################################################################ # 
print('################') 
print('Vacuum_Databases') 

sSQL="VACUUM" 
sql.execute(sSQL,conn1) 
sql.execute(sSQL,conn2) 
print('################') 
################################################################ 
print('### Done!! ############################################') 
##Process Superstep Event.py
#Open db in sqlite and show table hubevent