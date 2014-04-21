import urllib2
import urllib
cookies = urllib2.HTTPCookieProcessor()
print 'UserNO:'
UserNo = raw_input()
print 'PassWord:'
Passw = raw_input()

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding': 'gzip,deflate,sdch','Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4','User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36'}
url = 'http://jw.hrbeu.edu.cn/ACTIONLOGON.APPPROCESS?mode=3'
url2 = 'http://jw.hrbeu.edu.cn/ACTIONLOGON.APPPROCESS?mode=4'
kebiaourl = 'http://jw.hrbeu.edu.cn/ACTIONQUERYELECTIVERESULTBYSTUDENT.APPPROCESS?mode=1'
#proxy = urllib2.ProxyHandler({'http':'127.0.0.1:8888'})
#wopen = urllib2.build_opener(cookies,proxy)
wopen = urllib2.build_opener(cookies)
request = urllib2.Request(url = url,headers = headers)
path = r"./agnomen.jpg"
f=file(path,'wb')
imageurl = 'http://jw.hrbeu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS'
imrequest = urllib2.Request(url = imageurl,headers = headers)
response = wopen.open(imrequest)
f.write(response.read())
f.close()
data={'submit.x': '0', 'WebUserNO': '', 'Agnomen': '', 'Password': '', 'submit.y': '0'}
data['WebUserNO'] = UserNo
data['Password'] = Passw
print 'Agnomen:'
agnom = raw_input()
data['Agnomen']=agnom
request = urllib2.Request(url = url2, data = urllib.urlencode(data),headers = headers)
wopen.open(request)
request = urllib2.Request(url = kebiaourl, headers = headers)
response = response = wopen.open(request)
htmlpath = r"./index.html"
f=file(htmlpath,'wb')
f.write(response.read())
f.close()
