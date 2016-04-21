import fileinput
import re

class logfile_checker:
	def __init__(self, filename):
		self.__filename = filename
		self.__logpattern = re.compile(r'(?P<timestamp>[^|]*)\|(?P<container>[^|]*)\|(?P<package>[^|]*)\|(?P<version>[^|]*)\|(?P<level>[^|]*)\|(?P<type>[^|]*)\|(?P<bundle>[^|]*)\|(?P<information>[^|]*)', re.VERBOSE)

	def SearchInFile(self, key):
		counter = {}
		sorted(counter.iteritems(), key=lambda d:d[1], reverse = True )
		for line in fileinput.input(self.__filename):
			matchs = self.__logpattern.match(line)
			if matchs!=None:
				data = matchs.group(key)
				counter[data] = 1 if not counter.has_key(data) else counter[data] + 1
		fileinput.close()
		print sorted(counter.items(), key=lambda field:field[1], reverse=True)


if __name__ == "__main__":
	log = logfile_checker('e:\pythontest\examination_5.log')
	log.SearchInFile('timestamp')
	log.SearchInFile('package')

