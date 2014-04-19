
import sys
import pygtk
import gtk
import urllib2
import urllib

url = "jw.hrbeu.edu.cn"
user_agent = ""
user_agent = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/31.0.1650.63 Chrome/31.0.1650.63 Safari/537.36"
header = {'User-Agent',user_agent}
image_path = r"http://jw.hrbeu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS"
data = urllib2.urlopen(image_path)
html = data.read()
path = r"./daemon.jpg"
with open(path, "wb") as jpg:
    jpg.write(html)
data.close
