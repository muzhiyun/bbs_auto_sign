# -*- coding:utf-8 -*-

#为了学习单片机注册了一个论坛  奇葩论坛每天都要登录领金币   
#So.....写了脚本保存cookies每天自动模拟登陆
#2018-06-19    于

import cookielib
import urllib2
import re
#from bs4 import BeautifulSoup     #尽量不用BS4  便于在不同电脑上使用
import smtplib                               
from email.mime.text import MIMEText
from email.header import Header
 
#发送请求 
url = 'http://www.com/bbs/'
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'      
#headers = { 'User-Agent' : user_agent }
#神特么设置UA会有问题 处理不好  选择狗带 放弃  
cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#req = urllib2.Request(url, headers)
#上面说了  我就是死外面 从这跳下去  也不会设置UA
req = urllib2.Request(url)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
back=response.read()                       # 返回值

#调试用
#paswrd=re.findall('<a.*?href="([^"]*)".*?>([\S\s]*?)</a>',back)
# 匹配所有超链接
#paswrd=re.findall('<a.*?href="[^"]*".*?>([\S\s]*?)</a>',back)
# 匹配所有超链接标题
username=re.findall('<a.*?href="http://www.com/bbs/space-uid-\d+.html".*?>([\S\s]*?)</a>',back)
#匹配用户名  //存在问题
Score=re.findall('\xbb\xfd\xb7\xd6: \d+',back)
# 匹配积分

#调试用第二部分
#print type(back)
#print back
#print paswrd
#paswrd = "".join(paswrd)
#paswrd = paswrd.decode('utf-8')
#print type(paswrd)
#print paswrd


#如果获取的论坛积分为空  就发邮件报错
if Score=="":
  print "51 hei is wrong,try to send mail"
  try:
	
	mail_host="smtp.126.com"  #设置第三方SMTP服务器
	mail_user="m2"    #用户名
	mail_pass="what are you doing？？"   #口令  
	sender = 'my616422@126.com'
	receivers = ['my616422@126.com']  # 接收邮件
	message = MIMEText('51hei bbs is wrong', 'plain', 'utf-8')
	message['From'] = Header("muzhi 51hei", 'utf-8')
	message['To'] =  Header("muzhi", 'utf-8')
	subject = '51 hei bbs is wrong'
	message['Subject'] = Header(subject, 'utf-8')
	smtpObj = smtplib.SMTP() 
	smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
	smtpObj.login(mail_user,mail_pass)  
	smtpObj.sendmail(sender, receivers, message.as_string())
	print "E-mail is OK"
  except smtplib.SMTPException:
	print "Error"
else:
  print username                          #print type(Score)
  Score = "".join(Score)                  #list转换为字符串
  print Score                            #print type(Score)

  
  
  
  
  
  
  
  
  
#正则表达式写失败的作品 真鸡儿丢人
  
# match = re.search(r'href=[\'"]?([^\'" >]+)', back)
# if match:
	# print match.group(0)

# urls = re.findall(r'href=[\'"]?([^\'" >]+)', back)
# print ', '.join(urls)


# paswrd=re.findall('>":"(*\d+)',back)
# #res_ta=r'<a href=*class="showmenu"*>*</a>'
#res_ta=r'\u79ef\u5206\uff1a(\d+)'

# class="showmenu">
#extcreditmenu
#\xbb\xfd\xb7\xd6: 41
#m_a =re.findall(res_ta,back,re.S|re.M)
# paswrd= "".join(list(paswrd))

# paswrd=re.findall('password":"(\d+)',test)  //
# paswrd= "".join(list(paswrd))   








#好吧  下面这些是过程中参考过的代码 感觉自己更丢人了 qwq 
#来源于互联网  对作者表示感谢 

# import urllib2
# import cookielib

# url = 'http://www.server.com/login'
# cookie = cookielib.CookieJar()
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
# headers = { 'User-Agent' : user_agent }  
# request = urllib2.Request(url, headers)  
# handler=urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
    # print 'Name = '+item.name
    # print 'Value = '+item.value


# import cookielib
# import urllib2
 
# url = 'http://www.51hei.com/bbs/'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
# headers = { 'User-Agent' : user_agent }  
# cookie = cookielib.MozillaCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# req = urllib2.Request(url, headers)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()	


# -*- coding: utf-8 -*-
	
	
	
# import urllib
# import urllib2
# import cookielib
 
# filename = 'cookie.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib.urlencode({
            # 'stuid':'201200131012',
            # 'pwd':'23342321'
        # })
# #登录教务系统的URL
# loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
# #模拟登录，并把cookie保存到变量
# result = opener.open(loginUrl,postdata)
# #保存cookie到cookie.txt中
# cookie.save(ignore_discard=True, ignore_expires=True)
# #利用cookie请求访问另一个网址，此网址是成绩查询网址
# gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# #请求访问成绩查询网址
# result = opener.open(gradeUrl)
# print result.read()
#也不知道哪位前辈的  作者发帖时就修改了密码 
	
# import urllib  
# import urllib2  
 


# values = {'username' : 'cqc',  'password' : 'XXXX' }  

# data = urllib.urlencode(values)  
# request = urllib2.Request(url, data, headers)  
# response = urllib2.urlopen(request)  
# page = response.read() 


