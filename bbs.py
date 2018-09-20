# -*- coding:utf-8 -*-

#为了学习单片机注册了***论坛  奇葩论坛每天都要登录领金币   
#So.....写了脚本保存cookies每天自动模拟登陆
#2018-06-19    于西安石油大学

import cookielib
import urllib2
import re
#import sys
#from bs4 import BeautifulSoup     #尽量不用BS4  便于在不同电脑上使用
import smtplib                               
from email.mime.text import MIMEText
from email.header import Header

 
#发送请求 
#type = sys.getfilesystemencoding()
url = 'http://www.***.com/bbs/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'      
headers = { 'User-Agent' : user_agent }
cookie = cookielib.MozillaCookieJar()
cookie.load('/etc/51hei/cookie.txt', ignore_discard=True, ignore_expires=True)
req = urllib2.Request(url,headers=headers)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
back=response.read()
#.decode('gbk')
# 返回值

#显示用
#paswrd=re.findall('<a.*?href="([^"]*)".*?>([\S\s]*?)</a>',back)
# 匹配所有超链接
paswrd=re.findall('<a.*?href="[^"]*".*?>([\S\s]*?)</a>',back)
# 匹配所有超链接标题
username=re.findall('<a.*?href="http://www.******.com/bbs/space-uid-342911.html".*?>([\S\s]*?)</a>',back)
name=username[1]
#匹配用户名  //存在问题
Score=re.findall(r"\xbb\xfd\xb7\xd6: (\d+)",back)
Score = '.'.join(Score)
#\u79ef\u5206: 
#\xbb\xfd\xb7\xd6: 
#积分: 117
# 匹配积分

#显示用第二部分
#print type(back)
#print back
#print paswrd

#print name
#print username
#print type(name)
#print Score
#bytes(Score)
#print type(Score)

#如果获取的论坛积分为空  就发邮件报错
if Score=="":
  print "51 hei is wrong,try to send mail"
  try:	
	mail_host="smtp.126.com"  #设置第三方SMTP服务器
	mail_user="my616422"    #用户名
	mail_pass="******"   #口令  
	sender = 'my616422@126.com'
	receivers = ['my616422@126.com']  # 接收邮件
	message = MIMEText('**** bbs is wrong', 'plain', 'utf-8')
	message['From'] = Header("****", 'utf-8')
	message['To'] =  Header("****", 'utf-8')
	subject = '****  bbs is wrong'
	message['Subject'] = Header(subject, 'utf-8')
	smtpObj = smtplib.SMTP() 
	smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
	smtpObj.login(mail_user,mail_pass)  
	smtpObj.sendmail(sender, receivers, message.as_string())
	print "E-mail is OK"
  except smtplib.SMTPException:
	print "Error"
else:
  print "everything is ok,try to send mail"
  try:
        mail_host="smtp.126.com"  #设置第三方SMTP服务器
        mail_user="my616422"    #用户名
        mail_pass="********"   #口令  
        sender = 'my616422@126.com'
        receivers = ['my616422@126.com']  # 接收邮件
        html = """\
        <html>
          <body>
           <p>积分: """ + Score+ """</p> 
           <p>用户名: """ + name+ """</p>
</body>
        </html>
        """
        # 请把 [img 换成 <img
        message = MIMEText(html,_subtype='html',_charset='utf-8')  #定义发送的形式和编码格式，这里以html形式发送
        message['From'] = Header("muzhi@****.com", 'utf-8')
        message['To'] =  Header("my616422@126.com", 'utf-8')
        subject = '***** bbs is ok'
        message['Subject'] = Header(subject, 'utf-8')
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "the ok E-mail is OK"
  except smtplib.SMTPException:
        print "Error"
  print name                          #print type(Score)
  #Score = '.'.join(Score)                  #list转换为字符串
  print Score                  
  #print type(Score)
