# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib.request
import time

from nvshens import settings


class NvshensPipeline(object):
    def process_item(self, item, spider):
        # dir_path='%s/%s'%(settings.IMAGES_STORE,spider.name)+os.sep+time.strftime('%Y%m%d%H%M%S')	#stored path
        # dir_path='%s/%s'%(settings.IMAGES_STORE,spider.name)
        dir_path = '%s' % (settings.IMAGES_STORE)
        # print 'dirpath : ', dir_path
        # image_urls = ['https://www.nvshens.com/g/26884/',]

        for image_url in item['image_urls']:
            list_name = image_url.split('/')
            file_name = list_name[len(list_name) - 1]
            file_path = '%s/%s' % (dir_path, file_name)
            if os.path.exists(file_name):
                continue

            with open(file_path, 'wb') as file_writer:
                # conn = urllib.urlopen(image_url)
                conn = urllib.request.urlopen(image_url)
                file_writer.write(conn.read())
            file_writer.close()
        return item
