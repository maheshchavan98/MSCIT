import sys 
import os
import sqlite3 as sq 
import pandas as pd
sDatabaseName='C:/Data Science/Practical 4A/srk.db' 
conn = sq.connect(sDatabaseName) 
################################################################
sFileName='C:/Data Science/Practical 4A/DataSet.csv' 
print('Loading :',sFileName)
data=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin- 1")
data.index.names = ['RowIDCSV'] 
sTable='DataSet'
print('Storing :',sDatabaseName,' Table:',sTable) 
data.to_sql(sTable, conn, if_exists="replace") 
print('Loading :',sDatabaseName,' Table:',sTable)
TestData=pd.read_sql_query("select * from DataSet;", conn) 
print('################')
print('## Data Values') 
print('################')
print(TestData) 
print('################')
print('## Data Profile') 
print('################')
print('Rows :',TestData.shape[0]) 
print('Columns :',TestData.shape[1]) 
print('################')
################################################################ 
print('### Done!! ############################################')



