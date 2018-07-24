from urllib import parse#转换为中文可搜索
modity=input('Please Input the Modity Name:')
modity=parse.quote(modity)#转换为中文可搜索
url='https://s.taobao.com/search?q='+modity+'&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json
data=json.loads(data)
cnt=len(data['mods']['itemlist']['data']['auctions'])
def modinfo():
    for i in range(0,cnt):
        title=data['mods']['itemlist']['data']['auctions'][i]['title']
        price=data['mods']['itemlist']['data']['auctions'][i]['view_price']
        sales=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
        fee=data['mods']['itemlist']['data']['auctions'][i]['view_fee']
        sales = int(sales.replace('人付款',''))
        if (int(float(fee)))!=0:
            print("该商品不包邮，无法显示")
            print('')
            continue
        print("商品名称:"+title)
        print("商品价格:"+str(price))
        print("销量:"+str(sales))
        print("该商品包邮")
        print(' ')
        if (i+1)%4==0:
            print('-----------------------------------------')
modinfo()

