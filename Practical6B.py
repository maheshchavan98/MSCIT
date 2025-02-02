from datetime import datetime 
from pytz import timezone, all_timezones 
now_date=datetime(2025,2,17,13,26,6,18); 
now_utc=now_date.replace(tzinfo=timezone('GMT')) 
print('Date:',str(now_utc.strftime("%Y-%m-%d %H:%M:%S (%Z)"))) 
print('Year:',str(now_utc.strftime("%Y"))) 
print('Month:',str(now_utc.strftime("%m"))) 
print('Month:',str(now_utc.strftime("%B"))) 
print('Day:',str(now_utc.strftime("%d"))) 
print('Hours:',str(now_utc.strftime("%H"))) 
print('Minutes:',str(now_utc.strftime("%M"))) 
print('Seconds:',str(now_utc.strftime("%S"))) 
print('Mill.Seconds:',str(now_utc.strftime("%f"))) 
##Process Superstep Time.py