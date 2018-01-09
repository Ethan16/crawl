# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import codecs, json
from douban.items import MoiveContentItem

from sqlalchemy import Column, String, create_engine, Integer,TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

LOG = logging.getLogger(__name__)



Base = declarative_base()

class Info(Base):
    __tablename__ = 'info' 

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    score = Column(String(10))
    atrrs = Column(String(50))
    m_name = Column(String(200))

class Mov(Base):
    __tablename__ = 'mov'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    title = Column(String(200))
    content = Column(TEXT)

class DoubanPipeline(object):
    def __init__(self):
        #self.file = codecs.open("mov.json", 'wb', encoding='utf-8')
        #self.info = codecs.open("info.json", 'wb', encoding='utf-8')
        engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/scrapy?charset=utf8')
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()
 
    def process_item(self, item, spider):
        if item.__class__ == MoiveContentItem:
            #line = json.dumps(dict(item)) + '\n'
            #self.file.write(line.decode('unicode_escape'))
            new_info = Mov(name=item['name'],
                          title=item['title'],
                          content=item['content'])
 
        else:
            #line = json.dumps(dict(item)) + '\n'
            #self.info.write(line.decode('unicode_escape'))
            new_info = Info(name=item['name'],
                            score=item['score'],
                            atrrs=item['atrrs'],
                            m_name=item['m_name'])

        self.session.add(new_info)
        try:
            self.session.commit()
        except Exception as e:
            #self.session.flush()
            #self.session.clear()
            self.session.rollback()
            LOG.debug("aha the mysql data it wrong,[%s]" % e)


        return item
