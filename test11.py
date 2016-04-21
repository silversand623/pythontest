# -*- coding: UTF-8 -*-  
#-------------------------------------------------------------------------------  
# Name:        模块2  
# Purpose:  
#  
# Author:      lenovo  
#  
# Created:     06/09/2013  
# Copyright:   (c) lenovo 2013  
# Licence:     <your licence>  
#-------------------------------------------------------------------------------  
#coding=utf-8  
import re  
import urllib  
import urllib.request  
import urllib.request  
import http.cookiejar  
import re
import io
class xiaobai:  
    post_data=b""#登陆提交的参数  
    def __init__(self):  
        '''''初始化类，并建立cookies值'''  
        cj = http.cookiejar.CookieJar()  
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))  
        opener.addheaders = [('User-agent', 'Opera/9.23')]  
        urllib.request.install_opener(opener)  
                                  
    def login(self,loginurl,bianma):  
        '''''模拟登陆'''  
        req = urllib.request.Request(loginurl,self.post_data)  
        _response = urllib.request.urlopen(req)  
        _d=_response.read()  
        _d =_d.decode(bianma)  
        return _d  
                                  
    def getpagehtml(self,pageurl,bianma):  
        '''''获取目标网站任意一个页面的html代码'''  
        req2=urllib.request.Request(pageurl)  
        _response2=urllib.request.urlopen(req2)  
        _d2=_response2.read()  
        _d22 = _d2.decode(bianma)  
        return _d2  
if __name__=="__main__":
        try:
            x=xiaobai()
            f = open('e:\PythonTest\lu.html','wb')
            #参递一个post参数
            text = x.getpagehtml("https://my.lu.com/my/user-msg","utf_8")
            #print (text)
            f.write(text)
            #x.post_data=urllib.parse.urlencode({'uname':'usernamexxxx','password':'pwdxxxx','op':'login','xoops_redirect':'/user.php'}).encode(encoding='UTF8')  
            #print('x.post_data:',urllib.parse.parse_qs(x.post_data))  
            #y=x.login("http://www.lvye.org/user.php","utf-8")#登陆  
            #获取一个页面的html并输出  
            #print (x.getpagehtml("http://www.lvye.org/userinfo.php?uid=404071","utf-8"))  
            #print (x.getpagehtml("http://www.lvye.org","cp720"))
        finally:
            if f:
                f.close()
