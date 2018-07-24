import urllib.request as r

f = open('江苏裙子.txt','w',encoding='utf-8')

for i in range(0,100):
   url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E6%B1%9F%E8%8B%8F&s='+str(i*44)+'&ajax=true'
   data=r.urlopen(url).read().decode('utf-8','ignore')
   #data写进文件中
   f.write(data+'\n')
   print("第"+str(i+1)+"条")
f.close()
print('finish')