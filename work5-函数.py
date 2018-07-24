# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib.request as r#导入联网工具包，名为为r
import json#将字符串转换为字典

city=input('Please Input the City Name:')
url='http://api.openweathermap.org/data/2.5/forecast?q='+city+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'

data=r.urlopen(url).read().decode('utf-8','ignore')


data=json.loads(data)

def temp(a,b):
    print('Day'+str(a))
    print("Temperature:"+str(data['list'][b]['main']['temp']))
    print("Max Temperature:"+str(data['list'][b]['main']['temp_max']))
    print("Min Temperature:"+str(data['list'][b]['main']['temp_min']))
    print("Pressure:"+str(data['list'][b]['main']['pressure']))
    print('Weather Description:'+str(data['list'][b]['weather'][0]['main']))
temp(1,2)
temp(2,10)
temp(3,18)
temp(4,26)
temp(5,34)


print('-----Temperature Line Chart-----')
def chart(c,d):
    pic=str("Day"+str(c)+':')+str('-')*int(data['list'][d]['main']['temp'])
    return pic
print(chart(1,2))
print(chart(2,10))
print(chart(3,18))
print(chart(4,26))
print(chart(5,34))
print('-----Temperature Line Chart-----')


