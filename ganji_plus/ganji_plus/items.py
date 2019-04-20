# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GanjiPlusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    tilte = scrapy.Field()
    people= scrapy.Field()
    day = scrapy.Field()
    price = scrapy.Field()
    adress = scrapy.Field()

    pass
