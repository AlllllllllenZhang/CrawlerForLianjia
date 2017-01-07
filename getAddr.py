#coding=utf-8
import geocoder
import re
import MySQLdb as mysql

def getAddr(addr):
    address=geocoder.baidu(addr,key='V6CLFD6xWiHKXrCb0c8p4qGheETOImaQ')
    return address.json
conn = mysql.Connection(host='localhost', user='root', passwd='123456', db='heatmap', charset='utf8')
sql='select distinct(houseLocation) from houseprice;'
with conn as cursor:
    cursor.execute(sql)
    for i in range(cursor.rowcount):
        locat=cursor.fetchone()
        Addr=getAddr(locat)
        print '纬度'+str(Addr['lat'])+'经度'+str(Addr['lng'])+'地址'+str(Addr['location'])