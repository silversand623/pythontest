if __name__ == "__main__":
	linesA=[]
	linesB=[]
	num = 0
	with open('a', 'r') as f:
		linesA = f.readlines()

	with open('b', 'r') as f:
		linesB = f.readlines()

	with open('c', 'w') as f:
		for lineB in linesB:
			if not lineB.strip():
				pass
			for lineA in linesA:
				if lineB <> lineA:
					f.wirteline(lineB)
					num = num+1
					break
				else:
					pass

	print num