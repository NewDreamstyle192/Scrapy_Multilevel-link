# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:46:50 2019

@author: 28137
"""

from selenium import webdriver
from lxml import etree

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer

engine = create_engine('sqlite:///JD_Apple.sqlite',echo = True)
Base = declarative_base()
DBSseeeion = sessionmaker(bind = engine)
session = DBSseeeion()

class JD(Base):
    __tablename__ = "Apple pencil"
    id  = Column(Integer,primary_key = True)
    title = Column(String(400))
    price = Column(String(400))
    shop = Column(String(400))
    
    @classmethod
    def save(cls,data):
        session.add(data)
        session.commit()
        return data.id
Base.metadata.create_all(engine)

br  = webdriver.Chrome()
br.get('http://www.JD.com')
input_element = br.find_element_by_xpath('//*[@id="key"]')
input_element.clear()
input_element.send_keys('apple pencil')
search_element = br.find_element_by_xpath('//*[@id="search"]/div/div[2]/button/i')
search_element.click()


html_str = br.page_source

html = etree.HTML(html_str)
products = html.xpath('.//*[@id="J_goodsList"]/ul/li')
print(len(products))
for item in products:
    title = item.xpath('./div/div[4]/a/@title')
    price = item.xpath('./div/div[3]/strong/i/text()')
    shop = item.xpath('./div/div[7]/span/a/@title')
    print(title,price,shop)
    jd = JD()
    jd.title = ' '.join(title)
    jd.price = ' '.join(price)
    jd.shop = ' '.join(shop)
    jd.save(jd)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    