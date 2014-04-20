#! usr/bin/python
# -*- coding: utf-8 -*-
import sys
import gtk
import glib
import cairo
import random
import cookielib, urllib2, urllib

url = "http:\\jw.hrbeu.edu.cn"
user_agent = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/31.0.1650.63 Chrome/31.0.1650.63 Safari/537.36"
agnom_path = "http://jw.hrbeu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS"

class getAgnom():
	def __init__(self):
		self.path = r"./agnom.jpg"
		self.data = urllib2.urlopen(agnom_path)
		self.html = self.data.read()
		with open(self.path,"wb")as jpg:
			jpg.write(self.html)
		self.data.close
class LoginPage(gtk.Window):
	def __init__(self):

		super(LoginPage, self).__init__()
		self.set_title("哈工程学生成绩查询系统")
		self.set_size_request(420, 270)
		self.set_resizable(False)
		self.set_position(gtk.WIN_POS_CENTER)

		self.fixed = gtk.Fixed()

		self.pw_text = ""
		self.user_text = ""
		self.user_entry = gtk.Entry()
		self.user_label = gtk.Label("学号")
		self.pword_entry = gtk.Entry()
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
		self.connect("destroy", gtk.main_quit)
		self.add(self.fixed)
		self.show_all()

	def changeImage(self, event):
		getAgnom()
		self.agnom_image.set_from_file("agnom.jpg")

	def user_gettext(self, widget, event):
		self.user_text = widget.get_text()
		self.CheckEntry()

	def pass_gettext(self, widget, event):
		self.pw_text = widget.get_text()
		self.CheckEntry()

	def CheckEntry(self):
		if self.pw_text and self.user_text:
			print self.pw_text

LoginPage()
gtk.main()
