#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:29:14 2018

@author: apple
"""

ls=open('all_school.txt',encoding= 'utf-8').readlines()
schoolls=[]
for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
import urllib. request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest'}
f=open('34_1.txt','a', encoding='utf-8')
n=1
for schoolid in schoolls:
    for kemu in [1]:
        for i in [34]:
            try:
                req=r.Request(url,data='id={}&type={}&city={}&state=1'.format(schoolid, kemu,i).encode(),headers=headers)
                data = r.urlopen(req).read().decode('utf-8',' ignore')
                if data[0]!='{':
                    print('error_1')
                else:
                    f.write(data+"\n")
                    print(n)
                    n=n+1
            except:
                print('error_2')
                    
f .close()