import sys 
import os
import pandas as pd 
import matplotlib as ml
from matplotlib import pyplot as plt 
ml.style.use('ggplot')
data=[['Keep A Song In Your Soul',129.2,20.8],['I Put A Spell On You',110.5,15.5],['Golfing Papa',305.9,15.2],['Head Off',16.2,9.2],['High Rated',216.9,18.7],['Bang Bang',212.3,17.9]]
new_data=pd.DataFrame(data) 
new_data.rename(columns={0:"Song Name"},inplace=True) 
new_data.rename(columns={1:"loudness"},inplace=True) 
new_data.rename(columns={2:"mode"},inplace=True) 
colors_name=['blue','red','green','gold','pink','yellow'] 
explode=(0,0,0,0,0,0)
label= new_data["Song Name"] 
new_data.plot(figsize=(10,10),kind="hexbin" ,y="loudness",x="mode") 
plt.savefig('C:/Data Science/Practical 9B/Music3.png',dpi=600)
plt.show()
#Report Superstep Hexbin Graph