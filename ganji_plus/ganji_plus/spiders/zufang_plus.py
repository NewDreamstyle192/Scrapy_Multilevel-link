# lusr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:NewDreamS
@file: .py
@time: 2019/04/20
"""

if __name__ == "__main__":
    pass
import scrapy
from ..items import GanjiPlusItem
from scrapy import Request


class GanjiplusSpider(scrapy.Spider):
    name = 'zufang_plus'
    headers = {
        'User_Agent': " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

    def start_requests(self):
        start_urls = ['http://sh.ganji.com/shangpucs/']
        for url in start_urls:
            yield Request(url,headers=self.headers)


    def parse(self, response):
        node_list = response.xpath('.//dd[@class = "dd-item title"]/a/@href')
        for i in range(len(node_list)-30):
            zf = GanjiPlusItem()
            tmp_url = node_list[i].extract()
            # if "//" in tmp_url and "http://" not in tmp_url:
            if tmp_url.startswith('//'):
                tmp_url = tmp_url.replace('//','http://')
            yield scrapy.Request(tmp_url, meta={'zufang': zf}, callback=self.detail_parse)

        # 翻页爬取
        next_links = response.xpath('.//a[@class = "next"]/@href').extract()
        if len(next_links) > 0:
            next_link = next_links[0]
            yield Request(next_link, callback=self.parse)
        else:
            pass

    def detail_parse(self, response):
        zf = response.meta['zufang']
        zf['tilte'] = response.xpath('.//p[@class = "card-title"]/i/text()').extract()
        zf['people'] = response.xpath('//div[@class = "name"]/a/text()').extract()
        zf['day'] = response.xpath('.//div[@class = "phone"]/a/text()').extract()
        zf['price'] = response.xpath('.//div[@class = "price-wrap"]/span[2]/text()').extract()
        zf['adress'] = response.xpath('.//li[@class="er-item f-fl"]/span[2]/text()').extract()

        return zf
