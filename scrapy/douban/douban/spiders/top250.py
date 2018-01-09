#coding:utf-8
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from douban.items import MoiveContentItem, MoiveItem
from scrapy.linkextractors import LinkExtractor
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import re

class DoubanSpider(CrawlSpider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']
    #start_urls = ["https://movie.douban.com/subject/26279289/?tag=%E7%83%AD%E9%97%A8&from=gaia"]
    #start_urls = ["https://movie.douban.com/subject/3025375/reviews"]
    #start_urls = ["https://movie.douban.com/subject/3025375/"]
    start_urls = ["https://movie.douban.com/top250"]
    #start_urls = ["https://movie.douban.com/subject/21318488/?from=subject-page"]
    #start_urls = ["https://movie.douban.com/review/8159547/"]
    rules = [
        Rule(LinkExtractor(allow=r"/subject/\d+/$",), callback="movie_item", follow=True),
        Rule(LinkExtractor(allow=r"/top250\?start=",)),

        #Rule(LinkExtractor(allow=r"/subject/\d+/reviews$")),
        #Rule(LinkExtractor(allow=r"/subject/\d+/\?from=subject-page$"), callback="movie_item", follow=True),

        Rule(LinkExtractor(allow=r"/review/\d+/$"), callback="parse_item", follow=False),

        #Rule(LinkExtractor(allow=r"/subject/\d+/reviews\?start=\d+$")),
    ]

    def parse_item(self, response):
        print '@' * 50
        item = MoiveContentItem()
        content = "".join(
            response.xpath('//*[@id="link-report"]/div[@property="v:description"]/text()').\
                           extract())
        item['content'] = content#.lstrip().rstrip().replace("\n", " ") 
        item['name'] = response.xpath('//header[@class="main-hd"]/a[2]/text()')[0].extract()
        item['title'] = response.xpath('//*[@id="content"]/h1/h1/span/text()')[0].extract()
        yield item

    def movie_item(self, response):
        item = MoiveItem()
        item['name'] = response.xpath('//span[@property="v:itemreviewed"]/text()').extract()[0]
        item['atrrs'] = response.xpath('//div[@class="subject clearfix"]/div[@id="info"]/span[1]/span[2]/a/text()').extract()[0]
        item['score'] = response.xpath('//strong[@class="ll rating_num"]/text()').extract()[0]
        m_name = response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/h2/i/text()').extract()[0]
        m_name = re.split(u"的剧情简介", m_name)
        item['m_name'] = m_name[0]
        yield item
