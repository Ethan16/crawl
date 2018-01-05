# -*- coding: utf-8 -*-

"""
@version: 1.0
@author: James
@license: Apache Licence 
@contact: euler52201044@163.com
@file: html_outputer.py
@time: 2017/12/27 13:41:51
"""


class HtmlOutputer(object):
    """docstring for HtmlOutputer"""

    def __init__(self, arg):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('result.htm', 'W')
        fout.write("<html>")
        fout.write("<head>")
        # fout.write("<meta charset="utf-8"></meta>")
        fout.write("<title>Crawl Result</title>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write('<h1 style="text-align:center">Crawl Result</h1>')
        fout.write('<table style="border-collapse:collapse;"  border="1">')
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td><a href='%s'>%s</a></td>" %
                       (data["url"].encode("utf-8"), data["title"].encode("utf-8")))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write('<br /><br /><p style="text-align:center">Power By James</p>')
        fout.write("</body>")
        fout.write("<html>")
