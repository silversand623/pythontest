import re

class logfile_checker:
	def __init__(self, filename):
		self.__filename = filename
		self.__logpattern = re.compile(r'(?P<timestamp>[^|]*)\|(?P<container>[^|]*)\|(?P<package>[^|]*)\|(?P<version>[^|]*)\|(?P<level>[^|]*)\|(?P<type>[^|]*)\|(?P<bundle>[^|]*)\|(?P<information>[^|]*)', re.VERBOSE)

	def SearchInFile(self, key):
		counter = {}
		for line in fileinput.input(self.__filename):
			matchs = self.__logpattern.match(line)
			if matchs!=None:
				data = matchs.group(key)
				counter[data] = 1 if not counter.has_key(data) else counter[data] + 1

if __name__ == "__main__":
	head=[]
	allitems=[]
	num = 0
	with open('e:\pythontest\examination_3.csv', 'r') as f:
		line = f.readline()
		head = re.findall(r'(\w+),',line)
		print head
		while line:  
   			line = f.readline()
   			print line
   			allitems = re.findall(r'\"[^,]*\",', line)
   			print allitems

