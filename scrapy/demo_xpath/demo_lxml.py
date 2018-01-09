#!C:\python27
#-*-coding:utf8-*-

from lxml import etree

html=etree.parse("hello.html")
result=etree.tostring(html,pretty_print=True)
print type(html)
result=html.xpath('//li')	#1.获取所有的 <li> 标签
print result
print len(result)
print type(result)
print type(result[0])
result=html.xpath('//li/@class')	#2.获取 <li> 标签的所有 class
print result
result=html.xpath('//li/a[@href="link1.html"]')	#3.获取 <li> 标签下 href 为 link1.html 的 <a> 标签
print result
result=html.xpath('//li//span')	#4.获取 <li> 标签下的所有 <span> 标签。因为 / 是用来获取子元素的，而 <span> 并不是 <li> 的子元素，所以，要用双斜杠
print result
result=html.xpath('//li/a//@class')	#5.获取 <li> 标签下的所有 class，不包括 <li>。只取了/a的子节点，父节点的class属性不要
print '5 is here:',result
result=html.xpath('//li[last()]/a/@href')	#6.获取最后一个 <li> 的 <a> 的 href
print result
result=html.xpath('//li[last()-1]/a')	#7.获取倒数第二个元素的内容
print result[0].text
result=html.xpath('//*[@class="bold"]')	#8.获取 class 为 bold 的标签名
print result[0].tag
