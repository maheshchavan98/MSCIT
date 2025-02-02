import sys 
import os 
import pandas as pd 
import sqlite3 as sq 
sDatabaseName='C:/DS/datawarehouse.db' 
conn1=sq.connect(sDatabaseName) 
################################################################ 
sDatabaseName='C:/DS/datamart.db' 
conn2=sq.connect(sDatabaseName) 
################################################################ 
print('################') 
sTable='Dim-BMI' 
print('Loading:',sDatabaseName,'Table:',sTable) 
sSQL="SELECT * FROM [Dim-BMI];" 
PersonFrame0=pd.read_sql_query(sSQL,conn1) 
################################################################ 
print('################') 
sTable='Dim-BMI' 
print('Loading:',sDatabaseName,'Table:',sTable) 
sSQL="SELECT Height, Weight, Indicator, CASE Indicator WHEN 1 THEN 'Pip' \
    WHEN 2 THEN 'Norman' ELSE 'Sam' END AS Name from [Dim-BMI] \
        where Height > 2 order by Height, Weight;" 
PersonFrame1=pd.read_sql_query(sSQL,conn1) 
################################################################ 
DimPerson=PersonFrame1 
DimPersonIndex=DimPerson.set_index(['Height'],inplace=False) 
################################################################ 
sTable='Dim-BMI-Secure' 
print('\n#################################') 
print('Storing:',sDatabaseName,'\nTable:',sTable) 
print('\n#################################') 
DimPersonIndex.to_sql(sTable,conn2,if_exists="replace") 
################################################################ 
print('################################') 
sTable='Dim-BMI-Secure' 
print('Loading:',sDatabaseName,'Table:',sTable) 
print('################################') 
sSQL="SELECT * FROM [Dim-BMI-Secure] WHERE Name = 'Sam';" 
PersonFrame2=pd.read_sql_query(sSQL,conn2) 
################################################################ 
print('################################') 
print('FullDataSet(Rows):',PersonFrame0.shape[0]) 
print('FullDataSet(Columns):',PersonFrame0.shape[1]) 
print('################################') 
print('SECUREDataSet(Rows):',PersonFrame2.shape[0]) 
print('SECUREDataSet(Columns):',PersonFrame2.shape[1]) 
print('OnlySamData') 
print(PersonFrame2.head()) 
print('################################')

##Organize Superstep Secure Vault