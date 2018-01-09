import scrapy

#class CmsSpider(scrapy.Spider):
#	name="CmsSpider"
#	host="http://200.200.0.17/"
#
#	start_urls=["http://200.200.0.17/cms/supesite/?action-model-name-creative-itemid-24445",]
#
#	def parse(self,response):
#		print response.body

class QuotesSpider(scrapy.Spider):
	name="Quotes"
	start_urls=['http://quotes.toscrape.com/tag/humor/',]

	def parse(self,response):
		for quote in response.css('div.quote'):
			yield {
			'text':quote.css('span.text::text').extract_first(),
			'author':quote.xpath('span/small/text()').extract_first()
			}
		next_page=response.css('li.next a::attr("href")').extract_first()

		if next_page is not None:
			yield response.follow(next_page,self.parse)
