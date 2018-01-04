# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@163.com
@file: html_parser.py
@time: 2017/12/27 13:41:36
"""


from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):

    # https://baike.baidu.com/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6

    def get_new_urls(self, url, soup):
        new_urls = set()
        # TODO:should optimize re
        links = soup.find_all('a', href=re.compile(r'/item/[A-Za-z0-9/]+$'))

        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url, new_url)
            new_urls.add(new_full_url)

        return new_urls

    def get_new_datas(self, url, soup):
        new_dict = {}

        new_dict['url'] = url

        title_node = soup.find(
            'dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        new_dict['title'] = title_node.get_text()

        return new_dict

    def parse(self, url, content):

        if url is None or content is None:
            return

        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')

        new_urls = self.get_new_urls(url, soup)
        new_datas = self.get_new_datas(url, soup)

        return new_urls, new_datas
