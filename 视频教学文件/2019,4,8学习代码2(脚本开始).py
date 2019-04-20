# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:01:43 2019

@author: 28137
"""

import requests
from lxml import etree

def requests_view(response):
    import webbrowser as web
    requests_url = response.url
    
    base_url = '<head><base href="%s">'%(requests_url)
    base_url = base_url.encode()
    
    content = response.content.replace(b'<head>',base_url)
    tem_html = open('tmp.html','wb')
    tem_html.write(content)
    tem_html.close()
    
    web.open_new_tab('tmp.html')





response = requests.get('https://www.mzitu.com/')

requests_view(response)

content = response.content.decode()
html = etree.HTML(content)



#新建本地文件，请求图片并拿到响应，将图片保存到本地
srcs = html.xpath('//*[@id="pins"]/li/a/img/@src')
path = ('C:\\Users\\28137\\Desktop\\imgs')
headers = {'Referer':'https://www.mzitu.com/xinggan/',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
for src in srcs:
    print('nmsl')
    resp = requests.get(src,headers = headers)
    filename = src.split('/')[-1]
    with open(path+'/'+filename,'wb') as f:
        f.write(resp.content)












