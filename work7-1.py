#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 22:13:50 2018

@author: apple
"""

def WeatherReminder():
    city = input('Please input the city name:')
    data = r.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+city+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')
    data = json.loads(data)
    cnt = int(len(data['list'])/8)
    
    print("Information about Everyday's 18:00:")
    for i in range(0,cnt):
        print('day'+str(i+1)+':')
        print("Time:"+data['list'][2+i*8]['dt_txt'])
        temp = data['list'][2+i*8]['main']['temp']
        print("今天的温度是:"+str(temp))
#        print("Main:"+data['list'][2+i*8]['weather'][0]['main'])
        if temp >= 40:
            print('温度极高，防止中暑')
        elif temp >= 30:
            print('温度较高，请注意防晒')
        elif temp >= 20:
            print('温度较舒适，穿衣适中')
        elif temp >= 10:
            print('温度较寒冷，注意穿衣')
        elif temp >=0:
            print('温度较低，注意保暖')
        else:
            print('温都极低，请待在室内取暖')
        desc = data['list'][2+i*8]['weather'][0]['description']
        print("今天的天气情况是:"+desc)
        if '晴' in desc:
            print('天晴，阳光高照')
        elif '大雨' in desc:
            print('雨势较大，注意躲雨')
        elif '小雨' in desc:
            print('出门注意带伞')
        elif '阴' in desc:
            print('天气阴天，适合外出')
        elif '雾' in desc :
            print('起雾，开车小心追尾')
        print('=======================================')
        
WeatherReminder()