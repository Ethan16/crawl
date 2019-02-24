# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@163.com
@file: mMingYanSpider.py
@time: 2018/9/22 23:19
"""

import scrapy


class MingYanSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://lab.scrapyd.cn/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                '内容': quote.css('span.text:text').extract_first(),
                '作者': quote.xpath('span/small/text()').extract_first(),
            }

            next_page = response.css('li.next a::attr("href")').extract_firxt()

            if next_page is not None:
                yield scrapy.Request(next_page, self.parse)