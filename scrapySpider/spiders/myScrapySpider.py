# -*- coding:utf-8 -*-

import scrapy

from scrapySpider.items import PeopleItem


class MyScrapySpider(scrapy.spiders.Spider):
    name = "MyScrapySpider"
    allowed_domains = [
        "http://www.itcast.cn/"
    ]
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml#ac"
    ]

    def parse(self, response):
        items = []
        # file_name = "D:/teacher.html"
        # open(file_name, 'w').write(response.body)
        for site in response.xpath('//div[@class="li_txt"]'):
            item = PeopleItem()

            teacher_name = site.xpath('h3/text()').extract()
            teacher_level = site.xpath('h4/text()').extract()
            teacher_info = site.xpath('p/text()').extract()
            print teacher_name
            print teacher_level
            print teacher_info
            print '====================='

            item['name'] = teacher_name[0]
            item['level'] = teacher_level[0]
            item['info'] = teacher_info[0]

            items.append(item)

        return items
