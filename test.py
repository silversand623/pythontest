#import urlparse  
import urllib  
#import urllib2  
#import cookielib  
import string  
import re  
  
#登录的主页面  
hosturl = 'https://my.lu.com/my/user-msg' 
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）  
posturl = '******' 
  
#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie  
cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)  
  
#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）  
h = urllib2.urlopen(hosturl)  
text1 = h.read()
print(text1)
  
#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。  
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',  
           'Referer' : '******'}  
#构造Post数据，他也是从抓大的包里分析得出的。  
postData = {'op' : 'dmlogin',  
            'f' : 'st',  
            'user' : '******',  
            'pass' : '******',  
            'rmbr' : 'true',     
            'tmp' : '0.7306424454308195'   
  
            }  
  
#需要给Post数据编码  
postData = urllib.urlencode(postData)  
  
#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程  
request = urllib2.Request(posturl, postData, headers)  
print(request)  
response = urllib2.urlopen(request)  
text = response.read()  
print(text) 
