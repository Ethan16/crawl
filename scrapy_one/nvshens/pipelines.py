# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib
import time

from nvshens import settings


class NvshensPipeline(object):
    def process_item(self, item, spider):
        # dir_path='%s/%s'%(settings.IMAGES_STORE,spider.name)+os.sep+time.strftime('%Y%m%d%H%M%S')	#stored path
        # dir_path='%s/%s'%(settings.IMAGES_STORE,spider.name)
        dir_path = '%s' % (settings.IMAGES_STORE)
        # dir_path='%s/%s'%(spider.name,settings.IMAGES_STORE)	#stored path
        print 'dirpath : ', dir_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # for image_url in item['image_urls'] and nvshens_name in item['nvshens_names']:

        for image_url in item['image_urls']:
            list_name = image_url.split('/')
            # https://t1.onvshen.com:85/gallery/25126/24390/s/004.jpg
            # file_name=nvshens_name+list_name[len(list_name)-1]	#get origin name
            file_name = list_name[len(list_name) - 1]  # get origin name
            print 'filename : ', file_name
            file_path = '%s/%s' % (dir_path, file_name)
            print 'filepath : ', file_path
            if os.path.exists(file_name):
                continue

            with open(file_path, 'wb') as file_writer:
                conn = urllib.urlopen(image_url)
                file_writer.write(conn.read())
            file_writer.close()
        return item
