#2)	Drop the Columns Where Any of the Elements Is Missing Values

import sys 
import os
import pandas as pd 
sFileName='C:/DS/Good-or-Bad.csv' 
print('Loading:',sFileName) 
RawData=pd.read_csv(sFileName,header=0) 
print('##RawDataValues')
print(RawData) 
print('##DataProfile') 
print('Rows:',RawData.shape[0]) 
print('Columns:',RawData.shape[1])
print('################################')
TestData=RawData.dropna(axis=1,how='any') 
print('##TestDataValues')
print(TestData) 
print('##DataProfile') 
print('Rows:',TestData.shape[0]) 
print('Columns:',TestData.shape[1])
sFileName='C:/DS/output.csv' 
TestData.to_csv(sFileName,index=False) 
print('###Done!!#####################')
