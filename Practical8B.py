import sys 
import os 
import pandas as pd 
import sqlite3 as sq 
sDatabaseName='C:/DS/datawarehouse.db' 
conn1=sq.connect(sDatabaseName) 
################################################### 
############# 
sDatabaseName='C:/DS/datamart.db' 
conn2=sq.connect(sDatabaseName) 
print('################################') 
sTable='Dim-BMI' 
print('Loading:',sDatabaseName,'Table:',sTable) 
sSQL="SELECT * FROM [Dim-BMI];" 
PersonFrame0=pd.read_sql_query(sSQL,conn1) 
################################################### 
############# print('################################') 
sTable='Dim-BMI' 
print('Loading:',sDatabaseName,'Table:',sTable) 
print('################################') 
sSQL="SELECT Weight, Height, Indicator FROM [Dim-BMI];" 
PersonFrame1=pd.read_sql_query(sSQL,conn1) 
################################################### ############# 
DimPerson=PersonFrame1 
DimPersonIndex=DimPerson.set_index(['Height'],inplace=False) 
################################################### ############# 
sTable='Dim-BMI-Vertical' 
print('\n#################################') 
print('Storing:',sDatabaseName,'\nTable:',sTable) 
print('\n#################################') 
DimPersonIndex.to_sql(sTable,conn2,if_exists="replace") 
################################################### ############# 
print('################') 
sTable='Dim-BMI-Vertical'
print('Loading:',sDatabaseName,'Table:',sTable) 
sSQL="SELECT * FROM [Dim-BMI-Vertical];" 
PersonFrame2=pd.read_sql_query(sSQL,conn2) 
################################################### 
############# print('################################') 
print('FullDataSet(Rows):',PersonFrame0.shape[0]) 
print('FullDataSet(Columns):',PersonFrame0.shape[1]) 
print('################################') 
print('VerticalDataSet(Rows):',PersonFrame2.shape[0]) 
print('VerticalDataSet(Columns):',PersonFrame2.shape[1]) 
print('################################') 
###################################################

##Organize Superstep Vertical