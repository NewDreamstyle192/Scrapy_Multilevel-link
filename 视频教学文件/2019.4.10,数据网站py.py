# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:36:27 2019

@author: 28137
"""

import requests
from lxml import etree
import numpy as np
import webbrowser

from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

# A.创建数据库
engine = create_engine('sqlite:///ganji_zufang_2.sqlite',echo = True)
Base = declarative_base()
DBSsession = sessionmaker(bind = engine)
session = DBSsession()

class Zufang(Base):
    __tablename__ = "zufang_2"
    id = Column(Integer,primary_key = True)
    title = Column(String(400))
    price = Column(String(400))
    adress = Column(String(400))
    people = Column(String(400))
    
    @classmethod
    def save(cls,data):
        session.add(data)
        session.commit()
        return data.id
Base.metadata.create_all(engine)

# B.爬虫脚本(赶集网)

base_url = 'http://bj.ganji.com/ershoufang/y{}/'
headers = {'Referer':'http://bj.ganji.com/ershoufang/',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

 #B.1 网页数据处理
def parase_data(response,url):
    html = etree.HTML(response.content.decode())
    items = html.xpath('.//div[@class = "f-main-list"]/div/div[contains(@class,"f-list-item ershoufang-list")]')
    
    #出现了访问限制 此时 itml返回了一个空列表,则使用网页可视化返回给用户让用户 填写验证码
    if len(items) == 0:
        webbrowser.open_new_tab(url)
        print(response.url)
        strs = input("请检查验证问题，输入enter继续")
        if strs.upper() == 'ENTER':
            print('继续爬取')
            parase_data(requests.get(url,headers = headers),url)
            return 0
    for i in items:
        size = i.xpath('.//dd[@class = "dd-item size"]/span/text()')
        adress = i.xpath('.//dd[@class = "dd-item address"]/span[@class = "area"]/a[@class = "address-eara"]/text()')
        price = i.xpath('.//dd[@class = "dd-item info"]/div[@class = "price"]/span/text()')
        people = i.xpath('.//dd[@class = "dd-item address"]/span/span[@class = "address-eara"]/text()')
        
        zf = Zufang()
        zf.title = ' '.join(size)
        zf.adress = ' '.join(adress)
        zf.price = ' '.join(price)
        zf.people = ' '.join(people)
        zf.save(zf)
    return 1

  #B.2 迭代翻页爬取
for i in range(1,10):
    request_url = base_url.format(i)
    response = requests.get(request_url)
    print(request_url,"status_code:",response.status_code)
    #防止因为一个网页gg导致整个程序崩溃
    try:
        parase_data(response,request_url)
    except:
        pass
    


#爬虫网页可视化
def response_view(response):

    request_url = response.url
    base_url = '<head><base href = "%s">'%(request_url)
    base_url = base_url.encode()
    content = response.content.replace(b"<head>",base_url)
    tem_html = open('tem.html','wb')
    tem_html.write(content)
    tem_html.close()
    
    webbrowser.open_new_tab('tem.html')
    
#response_try = requests.get('http://bj.ganji.com/ershoufang/y3/')
#response_view(response_try)






















        
        
        
        
        
        
        
        
        
        
        
        
        
    
