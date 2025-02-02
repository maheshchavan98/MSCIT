#3)	Keep Only the Columns that missing only 2 values.

import sys 
import os
import pandas as pd ### Import Warehouse
sFileName='C:/DS/Good-or-Bad.csv' 
print('Loading :',sFileName) 
RawData=pd.read_csv(sFileName,header=0) 
print('## Raw Data Values')
print(RawData) 
print('## Data Profile')
print('Rows :',RawData.shape[0]) 
print('Columns :',RawData.shape[1]) 
print('################################')
TestData=RawData.dropna(thresh=2,axis=1) 
print('## Test Data Values')
print(TestData) 
print('## Data Profile')
print('Rows :',TestData.shape[0]) 
print('Columns :',TestData.shape[1]) 
sFileName='C:/DS/output2.csv' 
TestData.to_csv(sFileName, index = False) 
print('### Done!! #####################')
