# coding=utf-8
import urllib
import re
import MySQLdb as mysql
global a
a=1


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getArea(html):
    reg = r' (?:\d*\.)?\d+平米 '
    arire = re.compile(reg)
    prilist = re.findall(arire, html)
    return prilist


def getPrice(html):
    reg = r'单价(?:\d*\.)?\d+元\/平米'
    prire = re.compile(reg)
    prilist = re.findall(prire, html)
    return prilist


def getTotal(html):
    reg = r'Price"><span>(?:\d*\.)?\d+<\/span>万'
    prire = re.compile(reg)
    prilist = re.findall(prire, html)
    return prilist


def getName(html):
    reg = r'>\S+ <\/a> '
    prire = re.compile(reg)
    prilist = re.findall(prire, html)
    return prilist



 for k in range(1,50):
  html = getHtml("http://bj.lianjia.com/ershoufang/dongcheng/pg"+str(k)+"/")
  Area = getArea(html)
  Price = getPrice(html)
  Total = getTotal(html)
  Name = getName(html)
  conn = mysql.Connection(host='localhost', user='root', passwd='123456', db='heatmap', charset='utf8')
  for j in range(0, 30):
     cou = a
     nam = str(Name[j]).replace(' </a> ', '')
     loa = '北京市'+str(locat)+ nam.replace('>', '')
     aea = str(Area[j]).replace('平米 ', '')
     prie = str(Price[j]).replace('单价', '').replace('元/平米', '')
     tot = str(Total[j]).replace('Price"><span>', '').replace('</span>万', '')
     sql = "insert into houseprice(ID,houseName,houseLocation,houseArea,housePrice,houseTotal) values(%s,%s,%s,%s,%s,%s);"
     arg = (cou, nam, loa, aea, prie, tot)
     with conn as cursor:
         n = cursor.execute(sql, arg)
     print '第'+str(cou)+'个数插入成功'
     a=a+1
