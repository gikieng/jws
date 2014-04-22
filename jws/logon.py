# -*- coding:utf-8 -*-
import gtk, urllib2, urllib,sys
class LoginPage(gtk.Window):
    url = 'http://jw.hrbeu.edu.cn/ACTIONLOGON.APPPROCESS?mode=4'
    
    def __init__(self, opener, headers):
        
        super(LoginPage, self).__init__()
        
        self.set_title("哈工程学生成绩查询系统")
        self.set_size_request(420, 270)
        self.set_resizable(False)
        self.set_position(gtk.WIN_POS_CENTER)
#设置连接信息
        self.opener = opener
        self.headers = headers
        request = urllib2.Request(url = self.url, headers = self.headers)
        try:
            self.opener.open(request)
        except Exception,e:
            for item in e:
                print item
            sys.exit(1)
#设置窗口布局
        self.fixed = gtk.Fixed()
        self.pw_text = ""
        self.user_text = ""
        self.agonm_text = ''
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
        
        self.agnom_btn.add(self.agnom_image)
        self.fixed.put(self.login_button, 300, 100)
        self.fixed.put(self.user_label, 60, 40)
        self.fixed.put(self.user_entry, 120, 40)
        self.fixed.put(self.pword_label, 60, 82)
        self.fixed.put(self.pword_entry, 120, 82)
        self.fixed.put(self.agnom_label, 54, 124)
        self.fixed.put(self.agnom_entry, 120, 124)
        self.fixed.put(self.agnom_btn, 190, 120)
#加载验证码
        self.changeImage('')
#绑定窗口事件
        self.agnom_btn.connect("clicked", self.changeImage)
        self.user_entry.connect("key_release_event", self.user_gettext)
        self.pword_entry.connect("key_release_event", self.pass_gettext)
        self.agnom_entry.connect("key_release_event", self.agnom_gettext)
        self.login_button.connect("clicked", self.login)
        self.connect("destroy", gtk.main_quit)
        self.add(self.fixed)
        self.show_all()
        gtk.main()
#登录
    def login(self,event):
        data={'submit.x': '0', 'WebUserNO':self.user_text, 'Agnomen': self.agnom_text,'Password': self.pw_text, 'submit.y': '0'}
        request = urllib2.Request(url = self.url, data = urllib.urlencode(data),headers = self.headers)
        response = self.opener.open(request)
        print response.read()
        

#事件
    def user_gettext(self, widget, event):
        self.user_text = widget.get_text()
    def agnom_gettext(self, widget, event):
        self.agnom_text = widget.get_text()
    def pass_gettext(self, widget, event):
        self.pw_text = widget.get_text()

#改变验证码
    def changeImage(self, event):
        path = r"./tmp/agnomen.jpg"
        f=file(path,'wb')
        imageurl = 'http://jw.hrbeu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS'
        imrequest = urllib2.Request(url = imageurl,headers = self.headers)
        f.write(self.opener.open(imrequest).read())
        f.close()
        self.agnom_image.set_from_file("./tmp/agnomen.jpg")
