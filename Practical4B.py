import sys 
import os
import pandas as pd 
import sqlite3 as sq
################################################################ ################################################################
sDatabaseName='C:/Data Science/Practical 4A/srk.db'
conn = sq.connect(sDatabaseName) 
print('Loading :',sDatabaseName)
DataSet=pd.read_sql_query("select * from DataSet;", conn) ################################################################
print('Rows:', DataSet.shape[0]) 
print('Columns:', DataSet.shape[1])
print('### Raw Data Set #####################################')
for i in range(0,len(DataSet.columns)): 
    print(DataSet.columns[i],type(DataSet.columns[i]))
print('### Fixed Data Set ###################################')
DataSet_FIX=DataSet
for i in range(0,len(DataSet.columns)): 
    cNameOld=DataSet_FIX.columns[i] + '	' 
    print("Old : ",cNameOld); 
cNameNew=cNameOld.strip().replace(" ", ",") 
print("New : ",cNameNew); DataSet_FIX.columns.values[i] = cNameNew 
print(DataSet.columns[i],type(DataSet.columns[i]))
################################################################
#print(DataSet_FIX.head()) ################################################################ print('################')
print('Fixed Data Set with ID') 
print('################')
DataSet_with_ID=DataSet_FIX 
print('################') 
print(DataSet_with_ID.head()) 
print('################')
sTable2='Retrieve_IP_DATA' 
DataSet_with_ID.to_sql(sTable2,conn,index_label="RowID", if_exists="replace") ################################################################ print('### Done!! ############################################')

##performing operations on dataset