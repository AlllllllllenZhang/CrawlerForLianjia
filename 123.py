# coding=utf-8
import urllib
import re
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getExist(html):
    if r'下一页' in html:
        print 'A'
url='http://bj.lianjia.com/ershoufang/chaoyang/pg99/'
html=getHtml(url)
f=open('D://123.txt','w')
f.write(html)
f.close()