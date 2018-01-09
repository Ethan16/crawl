#coding:utf-8
import re

hello = u"奇异博士的剧情简介"
hello = re.split(u"的剧情简介", hello)

print hello[0]
