

if __name__ == "__main__":
	str = raw_input('put show in console string')
	num = 0
	space = 0
	alpha = 0
	other = 0
	for ch in str:
		if ch.isdigit():
			num=num+1
		elif ch.isalpha():
			alpha=alpha+1
		elif ch.isspace():
			space=space+1
		else:
			other=other+1

	print num
	print space
	print alpha
	print other