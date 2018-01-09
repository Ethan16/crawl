# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MoiveContentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    m_name = scrapy.Field()

class MoiveItem(scrapy.Item):
    name = scrapy.Field()
    atrrs = scrapy.Field()
    score = scrapy.Field()
    m_name = scrapy.Field()
    pass
