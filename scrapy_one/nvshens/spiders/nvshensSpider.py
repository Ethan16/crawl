#!/usr/bin/env python
# -*-coding:utf8-*-

import scrapy
import os

from nvshens.items import NvshensItem

from scrapy.crawler import CrawlerProcess


# from scrapy import optional_features

# scrapy URLerror:<urlopen error [Error 10051]>
# optional_features.remove('boto')


class nvshensSpider(scrapy.Spider):
    name = 'nvshens'
    allowed_domains = []
    start_urls = ["https://www.nvshens.com/g/28064/", ]
    # num_urls = ((url.split('/'))[len(url.split('/')) - 1] for url in start_urls)
    num_urls=start_urls[0].split('/')[len(start_urls[0].split('/')) - 2]
    # print("====debug====")
    # print(start_urls[0].split('/')[len(start_urls[0].split('/')) - 2])

    # nvshens_name=response.xpath('//li/a[@target="_blank"]')[0]

    def parse(self, response):
        item = NvshensItem()
        # https://t1.onvshen.com:85/gallery/25126/24390/s/004.jpg
        item['image_urls'] = response.xpath('//img//@src').extract()  # get picture
        # print 'image_urls', item['image_urls']
        # item['nvshens_names']=response.xpath('//li/a[@target="_blank"]')[0].text
        # print 'nvshens_name',item['nvshens_names']
        yield item

        for i in range(2, 15):
            new_url = "https://www.nvshens.com/g/28064/%d.html" % i
            # print 'new url : ', new_url
            if new_url:
                yield scrapy.Request(new_url, callback=self.parse)
