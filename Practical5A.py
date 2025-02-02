#Drop the Columns Where All Elements Are Missing Values
import sys 
import os
import pandas as pd ################################################################
sFileName='C:/DS/Good-or-Bad.csv' ################################################################
print('Loading:',sFileName) 
RawData=pd.read_csv(sFileName,header=0) 
print('################################')
print('##RawDataValues') 
print('################################')
print(RawData) 
print('################################')
print('##DataProfile') 
print('################################')
print('Rows:',RawData.shape[0]) 
print('Columns:',RawData.shape[1]) 
print('################################')
################################################################
TestData=RawData.dropna(axis=1,how='all') ################################################################ print('################################')
print('##TestDataValues') 
print('################################')
print(TestData) 
print('################################')
print('##DataProfile') 
print('################################')
print('Rows:',TestData.shape[0]) 
print('Columns:',TestData.shape[1]) 
print('################################') ################################################################
sFileName='C:/DS/datasetoutput.csv' 
TestData.to_csv(sFileName,index=False) ################################################################ print('################################') print('###Done!!#####################') print('################################')
