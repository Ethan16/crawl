# -*- coding: utf-8 -*-
import scrapy
import os
from nvshens.items import NvshensItem


class NvshensspiderSpider(scrapy.Spider):
    name = 'nvshensSpider'
    allowed_domains = ['www.nvshens.com']
    start_urls = ['http://www.nvshens.com/']

    def parse(self, response):
        pass
