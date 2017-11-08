# -*- coding:utf-8 -*-

import scrapy


class MyScrapySpider(scrapy.spiders.Spider):
    name = "MyScrapySpider"
    allowed_domains = [
        "http://www.itcast.cn/"
    ]
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml#ac"
    ]

    def parse(self, response):
        file_name = "D:/teacher.html"
        open(file_name, 'w').write(response.body)
