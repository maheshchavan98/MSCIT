import sys 
import os 
import pandas as pd 
import sqlite3 as sq 
################################################################ 
sDatabaseName = 'C:/DS/datawarehouse.db' 
conn1 = sq.connect(sDatabaseName) 
################################################################ 
sDatabaseName1 = 'C:/DS/datamart.db' 
conn2 = sq.connect(sDatabaseName1) 
################################################################ 
print('################') 
sTable = "Dim-BMI" 
print('Loading :', sDatabaseName, ' Table:', sTable)  ## id, key, tempo, year 
sSQL = "SELECT * FROM [Dim-BMI];" 
PersonFrame0 = pd.read_sql_query(sSQL, conn1) 
################################################################ 
print('################################') 
sTable = "Dim-BMI" 
print('Loading :', sDatabaseName, ' Table:', sTable, 'After applying Horizontal style') 
print('################################') 
sSQL = "SELECT * FROM [Dim-BMI] WHERE Height > 1.5 AND Indicator = 1 ORDER BY Height, Weight;" 
PersonFrame1 = pd.read_sql_query(sSQL, conn1) 
################################################################ 
DimPerson = PersonFrame1 
DimPersonIndex = DimPerson.set_index(['Height'], inplace=False) 
################################################################ 
sTable = "Dim-BMIHorizontal" 
print('\n#################################') 
print('Storing :', sDatabaseName1, '\n Table:', sTable) 
print('\n#################################') 
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace") 
sSQL = "SELECT * FROM [Dim-BMIHorizontal];" 
PersonFrame2 = pd.read_sql_query(sSQL, conn2) 
print(PersonFrame2) 
################################################################ 
print('################################') 
print('Full Data Set (Rows):', PersonFrame0.shape[0]) 
print('Full Data Set (Columns):', PersonFrame0.shape[1]) 
print('################################') 
print('Horizontal Data Set (Rows):', PersonFrame2.shape[0]) 
print('Horizontal Data Set (Columns):', PersonFrame2.shape[1]) 
print('################################')
##Organize Superstep Horizontal