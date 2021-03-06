# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class GanjiPlusPipeline(object):
    def open_spider(self, spider):  # 打开爬虫时连接数据库
        self.con = sqlite3.connect('zufang_plus.sqlite')
        self.cu = self.con.cursor()  # 光标（很重要的一个概念）


    def process_item(self, item, spider):
        print(spider.name, 'pipelines')
        insert_sql = "insert into zufang(tilte,people,day,price,adress) values('{}','{}','{}','{}','{}')".format(
            item['tilte'], item['people'], item['price'], item['day'], item['adress'])
        print(insert_sql)
        self.cu.execute(insert_sql)  # 执行插入语句
        self.con.commit()  # 提交数据
        return item

    def spider_close(self, spider):  # 爬虫结束 务必将数据库关闭
        self.con.close()
