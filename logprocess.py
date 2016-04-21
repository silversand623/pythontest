import re
import os
import datetime

class logfile_checker: 
	name = ''  
	def __init__(self,filename):  
	    self.name = filename
          
	def SearchInfile(self,key): 
		file_name= self.name
		file=open(file_name,'r')
		acnum=[];time_res=[];lnum=0
		iplist = []
		timelist = []
		methodlist = []
		agentlist = []
		statuslist = []
		lenlist = []
		urllist = []

		for (num,line) in enumerate(file):
			reip = re.match(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])',line) 
			#print reip.group(0)
			if reip:
				iplist.append(reip.group())

			retime = re.search(r'(\[.*?\])',line) 
			#print retime.group(0)
			if retime:
				timelist.append(retime.group())

			method = re.findall(r'\".*?\"',line)
			#print method
			if len(method) >=3:
				methodlist.append(method[0])
				urllist.append(method[1])
				agentlist.append(method[2])

			status = re.findall(r'\ (\d+)\ (\d+)\ ',line)
			#print status
			if len(status) >=1:
				#print status[0][0]
				statuslist.append(status[0][0])
				lenlist.append(status[0][1])
				

		ipdic = {} #ip
		timedic = {} #time
		methoddic = {} #method
		statusdic = {} #status
		lendic = {} #length
		agentdic = {} #agent
		urldic = {}

		for item in iplist:
			if iplist.count(item) >= 1:
				ipdic[item] = iplist.count(item)

		for item1 in timelist:
			if timelist.count(item1) >=1:
				timedic[item1] = timelist.count(item1)
				
		for item in methodlist:
			if methodlist.count(item) >= 1:
				methoddic[item] = methodlist.count(item)

		for item in statuslist:
			if statuslist.count(item) >= 1:
				statusdic[item] = statuslist.count(item)

		for item in lenlist:
			if lenlist.count(item) >= 1:
				lendic[item] = lenlist.count(item)

		for item in agentlist:
			if agentlist.count(item) >= 1:
				agentdic[item] = agentlist.count(item)

		for item in urllist:
			if urllist.count(item) >= 1:
				urldic[item] = urllist.count(item)

		orderip = sorted(ipdic.iteritems(), key=lambda d:d[1], reverse = True )
		ordertime = sorted(timedic.iteritems(), key=lambda d:d[1], reverse = True )
		ordermethod = sorted(methoddic.iteritems(), key=lambda d:d[1], reverse = True )
		orderstatus = sorted(statusdic.iteritems(), key=lambda d:d[1], reverse = True )
		orderlen = sorted(lendic.iteritems(), key=lambda d:d[1], reverse = True )
		orderagent = sorted(agentdic.iteritems(), key=lambda d:d[1], reverse = True )
		orderurl = sorted(urldic.iteritems(), key=lambda d:d[1], reverse = True )

		if key =='ipaddress':
			print orderip
		elif key =='timestamp':
			print ordertime
		elif key =='httpmethod':
			print ordermethod
		elif key =='httpstatus':
			print orderstatus
		elif key =='httpcontent':
			print orderlen
		elif key =='userAgent':
			print orderagent
		elif key =='httpurl':
			print orderurl
		else:
			pass


if __name__ == "__main__":
	logchecker = logfile_checker(r'e:\pythontest\template.log')
	logchecker.SearchInfile('ipaddress')