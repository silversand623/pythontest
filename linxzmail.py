# coding: UTF-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

class mymail:
	def __init__(self, smtp_server,pop_server,imap_server):
		self.__smtp_server = smtp_server
		self.__pop_server = pop_server
		self.__imap_server = imap_server
		
	def SetUser(self, username, userpwd):
		self.__username = username
		self.__userpwd = userpwd

	# type=0, send text mail,type=1 send html mail
	def SendTextMail(self, to_addr, message, type):
		if type == 0:
			msg = MIMEText(message,'plain','UTF-8')
			msg['Subject'] = Header('Test Email by Python 我是你','UTF-8')
			msg['From'] = from_addr
			msg['To'] = to_addr
		else:
			msg = MIMEText(message,'html','UTF-8')
			msg['Subject'] = Header('Test Email by Python 我是你','UTF-8')
			msg['From'] = from_addr
			msg['To'] = to_addr

		# SMTP协议默认端口是25
		server = smtplib.SMTP(self.__smtp_server, 25)
		server.set_debuglevel(1)
		server.login(self.__username, self.__userpwd)
		server.sendmail(self.__username, [to_addr], msg.as_string())
		server.quit()

	def SendHtmlWithPic(self,to_addr, message,picfile):
		msgBase = MIMEMultipart('related')
		msgBase['Subject'] = 'test message' 
 
		msgText = MIMEText(message,'html','utf-8')
		msgBase.attach(msgText) 
		 
		fp = open('h:\\python\\1.jpg', 'rb')
		msgImage = MIMEImage(fp.read())
		fp.close() 
		 
		msgImage.add_header('Content-ID', '')
		msgBase.attach(msgImage)

		# SMTP协议默认端口是25
		server = smtplib.SMTP(self.__smtp_server, 25)
		server.set_debuglevel(1)
		server.login(self.__username, self.__userpwd)
		server.sendmail(self.__username, [to_addr], msgBase.as_string())
		server.quit()

if __name__ == "__main__":
	#imap server：imap.exmail.qq.com：993
	#smtp server：smtp.exmail.qq.com：465
	# 输入Email地址和口令:
	
	#from_addr = raw_input('From: ')
	#password = raw_input('Password: ')
	from_addr = 'snoopy_wmda@163.com'
	password = '36183721pi@163'
	
	# 输入SMTP服务器地址:
	#smtp_server = raw_input('SMTP server: ')
	smtp_server = 'smtp.163.com'

	pop_server = 'pop.163.com'

	imap_server = 'imap.163.com'
	# 输入收件人地址:
	#to_addr = raw_input('To: ')
	to_addr = 'snoopy_wmda@163.com'

	testmail = mymail('smtp.163.com','pop.163.com','imap.163.com')
	testmail.SetUser('snoopy_wmda@163.com','36183721pi@163')
	testmail.SendTextMail('snoopy_wmda@163.com','i am a big fox,哈哈哈哈',0)
	'<b>Some <i>HTML</i> text</b> and an image.<img alt="" src="cid:image1" />good!'