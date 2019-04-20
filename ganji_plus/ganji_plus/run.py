#lusr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:NewDreamS
@file: .py
@time: 2019/04/20
"""
from scrapy.cmdline import execute
if __name__ == "__main__":
    execute('scrapy crawl zufang_plus'.split())