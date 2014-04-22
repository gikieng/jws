# -*- coding:utf-8 -*-
import urllib2, urllib, cookielib, gtk,sys
import logon
cookie = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookie)
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip,deflate,sdch',
           'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36'}
kebiaourl = 'http://jw.hrbeu.edu.cn/ACTIONQUERYELECTIVERESULTBYSTUDENT.APPPROCESS?mode=1'
login = logon.LoginPage(opener, headers)
request = urllib2.Request(url = kebiaourl, headers = headers)
response = opener.open(request)
htmlpath = r"./tmp/index.html"
f=file(htmlpath,'wb')
f.write(response.read())
f.close()
print 'success'