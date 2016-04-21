import re
import os
import sys
import fileinput

class logfile_checker:
	def __init__(self, filename):
		self.__filename = filename
		self.__logpattern = re.compile(r'(?P<IssueType>[^,]*)\,(?P<Key>[^,]*)\,(?P<Summary>[^,|\"]*)\,(?P<Assignee>[^,]*)\,(?P<Reporter>[^,]*)\,(?P<Priority>[^,]*)\,(?P<Status>[^,]*)\,(?P<Resolution>[^,]*)\,(?P<Created>[^,]*)\,(?P<Updated>[^,]*)\,(?P<DueDate>[^,]*)', re.VERBOSE)

	def SearchInFile(self, key):
		counter = {}
		num = 0
		for line in fileinput.input(self.__filename):
			if num == 0:
				num= num+1
				pass
			else:
				matchs = self.__logpattern.match(line)
				if matchs!=None:
					data = matchs.group(key)
					counter[data] = 1 if not counter.has_key(data) else counter[data] + 1
		fileinput.close()
		print sorted(counter.items(), key=lambda field:field[1], reverse=True)

def main():
    args = sys.argv[1:]
    if not args:
        print "usage: key";
        sys.exit(1)
    if len(args) == 0:
        print "error: must specify one or more key"
        sys.exit(1)   # Gather all the special files
    log = logfile_checker('e:\pythontest\examination_3.csv')
    for key in args:
        log.SearchInFile(key)
        
if __name__ == "__main__":
    main()