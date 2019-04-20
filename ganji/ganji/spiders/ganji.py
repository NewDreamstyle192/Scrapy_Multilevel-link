#lusr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:NewDreamS
@file: .py
@time: 2019/04/18
"""

if __name__ == "__main__":
    pass
from scrapy import Request
import scrapy
from ..items import GanjiItem

class GanjiSpider(scrapy.Spider):
    name = 'zufang'
    headers = {'User_Agent':" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}
    host_name = 'http://sh.ganji.com{}'
    def start_requests(self):
        urls = ['http://sh.ganji.com/shangpucs/']
        for url in urls:
            yield Request(url,headers=self.headers)

    def parse(self,response):
        print(response)
        zf = GanjiItem()
        title_list = response.xpath(".//dd[@class = 'dd-item title']/a/text()").extract()
        price_list = response.xpath('.//div[@class = "price"]/span[1]/text()').extract()
        for i,j in zip(title_list,price_list):
            zf['title'] = i
            zf['price'] = j
            yield zf
        next_links = response.xpath('.//a[@class = "next"]/@href').extract()
        if len(next_links) > 0:
            next_link = next_links[0]
            yield Request(next_link,callback = self.parse)
        else:
            pass