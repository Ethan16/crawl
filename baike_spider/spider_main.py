# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence
@contact: euler52201044@163.com
@file: spider_main.py
@time: 2017-12-28 13:26:45
"""


import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url, num):
        count = 1
        self.urls.add_new_url(root_url)
        while(self.urls.has_new_url()):
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s ' % (count, new_url)

                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

            except:
                print 'craw failed.'

            count = count + 1
            if count > num:
                break

        self.outputer.output_html()

if __name__ == '__main__':
    root_url = "https://baike.baidu.com/item/Python/407313"
    num = 100
    obj_spider = SpiderMain()
    obj_spider.craw(root_url, 100)
