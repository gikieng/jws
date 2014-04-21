#usr/bin/python
import urllib2, urllib, cookielib
url = 'http://jw.hrbeu.edu.cn/ACTIONLOGON.APPPROCESS?mode=4'
para = 'WebUserNO=2012061512&Password=765137&Agnomen=2487&submit.x=20&submit.y=6'
cj = cookielib.CookieJar() 
cookie = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie)
response = opener.open("http://baidu.com")
print cookie
