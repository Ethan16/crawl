#!C:\python27
#-*-coding:utf8-*-
#

import scrapy
from jiandan.items import JiandanItem
from scrapy.crawler import CrawlerProcess

class jiandanSpider(scrapy.Spider):
	name="jiandan"
	start_urls=["http://jandan.net/ooxx"]

	def parse(self,response):
		item=JiandanItem()
		item['image_urls']=response.xpath('//img//@src').extract()	#get pic hyper_link
		print 'image_urls',item['image_urls']
		yield item

		#new_url=response.xpath('//a[@class="previous-comment-page"]//@href').extract_first()	#pagedown
		#print 'new_url',new_url
		#if new_url:
		#	yield scrapy.Request(new_url,call_back=self.parse)
