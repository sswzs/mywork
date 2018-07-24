# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

city=input('Please Input the City Name:')
url='http://api.openweathermap.org/data/2.5/forecast?q='+city+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r#导入联网工具包，名为为r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

n=int(len(data['list'])/8)
newlist=list()
for i in range(0,n-1):
    print('Day'+str(i+1)+' '+str(data['list'][1+i*8]['dt_txt']))
    print("Temperature:"+str(data['list'][1+i*8]['main']['temp']))
    print("Max Temperature:"+str(data['list'][1+i*8]['main']['temp_max']))
    print("Min Temperature:"+str(data['list'][1+i*8]['main']['temp_min']))
    print("Pressure:"+str(data['list'][1+i*8]['main']['pressure']))
    print("Weather Description:"+data['list'][1+i*8]['weather'][0]['description'])
    newlist.append(data['list'][1+i*8]['main']['temp'])
    

print('-----Temperature Line Chart-----')
for i in range(0,n-1):
    print("Day"+str(i+1)+':'+'-'*int(data['list'][1+i*8]['main']['temp']))
print('-----Temperature Line Chart-----')

print('The Rank of the Temperature:')
sorted(newlist)
print(newlist)

