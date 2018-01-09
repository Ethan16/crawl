#!C:\python27
#-*-coding:utf8-*-

from lxml import etree

html=etree.parse("books.html")
result=html.xpath('//book/title')
print result
print result[0].text
for i in range(len(result)):
	print result[i].text

result=html.xpath('//book/author')
for i in range(len(result)):
	print 'result[%d].text is : '%i+result[i].text