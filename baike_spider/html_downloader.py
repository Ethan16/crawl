# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@163.com
@file: html_downloader.py
@time: 2017/12/27 13:41:20
"""


import urllib2


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        # Handle failed.
        if response.getcode != 200:
            return None

        return response.read()
