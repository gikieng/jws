#! usr/bin/python
# -*- coding: utf-8 -*-
import sys
import gtk
import glib
import cairo
import random
import cookielib, urllib2, urllib

lgurl = "http://jw.hrbeu.edu.cn"
loginurl = "http://jw.hrbeu.edu.cn/ACTIONLOGON.APPPROCESS?mode=3"
kebiaourl2 = "http://jw.hrbeu.edu.cn/ACTIONQUERYELECTIVERESULTBYSTUDENT.APPPROCESS"
kebiaourl = "http://jw.hrbeu.edu.cn/ACTIONQUERYELECTIVERESULTBYSTUDENT.APPPROCESS?mode=1"
header = {"User-Agent":"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/31.0.1650.63 Chrome/31.0.1650.63 Safari/537.36"}
agnom_path = "http://jw.hrbeu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS"

class LoginPage(gtk.Window):
	def __init__(self):

		super(LoginPage, self).__init__()
		self.set_title("哈工程学生成绩查询系统")
		self.set_size_request(420, 270)
		self.set_resizable(False)
		self.set_position(gtk.WIN_POS_CENTER)
		
		self.fixed = gtk.Fixed()
		self.cookie = cookielib.CookieJar()
		self.cookie_handler = urllib2.HTTPCookieProcessor(self.cookie)
		self.opener = urllib2.build_opener(self.cookie_handler)
		#self.postdata = {'WebUserNO' :self.user_text,'Password': self.pw_text,'Agnomon': self.agnom_text,'submitit':'true'}
		self.pw_text = ""
		self.user_text = ""
		self.user_entry = gtk.Entry()
		self.user_label = gtk.Label("学号")
		self.pword_entry = gtk.Entry()
		self.pword_entry.set_visibility(False)
		self.pword_label = gtk.Label("密码")
		self.agnom_label = gtk.Label("验证码")
		self.agnom_image = gtk.Image()
		self.agnom_image.set_size_request(60, 30)
		self.agnom_btn = gtk.Button()
		self.agnom_btn.set_size_request(64, 34)
		self.agnom_entry = gtk.Entry()
		self.agnom_entry.set_size_request(60, 30)
		self.login_button = gtk.Button("登录")
		self.login_button.set_border_width(0)
		self.login_button.set_size_request(80, 50)
		self.getAgnom()
		
		self.agnom_image.set_from_file("agnom.jpg")
		self.agnom_btn.add(self.agnom_image)
		self.fixed.put(self.login_button, 300, 100)
		self.fixed.put(self.user_label, 60, 40)
		self.fixed.put(self.user_entry, 120, 40)
		self.fixed.put(self.pword_label, 60, 82)
		self.fixed.put(self.pword_entry, 120, 82)
		self.fixed.put(self.agnom_label, 54, 124)
		self.fixed.put(self.agnom_entry, 120, 124)
		self.fixed.put(self.agnom_btn, 190, 120)

		self.agnom_image.set_from_file("agnom.jpg")
		self.agnom_btn.connect("clicked", self.changeImage)
		self.user_entry.connect("key_release_event", self.user_gettext)
		self.pword_entry.connect("key_release_event", self.pass_gettext)
		self.agnom_entry.connect("key_release_event", self.agnom_gettext)
		self.login_button.connect("clicked", self.login)
		self.connect("destroy", gtk.main_quit)
		self.add(self.fixed)
		self.show_all()

	def login(self,event):

		self.postdata = {'WebUserNO' :self.user_text,'Password': self.pw_text,'Agnomon': self.agnom_text,'submit.z':'0','submit.y':'0'}
		psd = urllib.urlencode(self.postdata)
		print psd
		request = urllib2.Request(url = loginurl,data = psd,headers = header)
		response = self.opener.open(request)
		geturl = response.geturl()
		print geturl
		request = urllib2.Request(url = geturl,data = psd,headers = header)
		response = self.opener.open(request)
		#request = urllib2.Request(url = kebiaourl2, headers = header)
		#response = self.opener.open(request)
		print geturl
		html = response.read()
		sys.stdout = open("index.html","w")
		print html

	def changeImage(self, event):
		self.getAgnom()
		self.agnom_image.set_from_file("agnom.jpg")

	def user_gettext(self, widget, event):
		self.user_text = widget.get_text()
	def agnom_gettext(self, widget, event):
		self.agnom_text = widget.get_text()

	def pass_gettext(self, widget, event):
		self.pw_text = widget.get_text()

	def CheckEntry(self):
		if self.pw_text and self.user_text:
			print self.pw_text

	def getAgnom(self):
		self.path = r"./agnom.jpg"
		request = urllib2.Request(url = agnom_path, headers = header)
		self.data = self.opener.open(request)
		self.html = self.data.read()
		with open(self.path,"wb")as jpg:
			jpg.write(self.html)
		self.data.close

LoginPage()
gtk.main()
