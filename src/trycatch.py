#demonstrate trycatch

def divide():
	'''demonstrate divide by zero'''
	numlist = [2, 4, 5, 1, 0, 3, 'i', 10]
	for num in numlist:
		try:
			print "100/%d=%d"%(num, 100/num)
		except ZeroDivisionError:
			print "Divide by Zero"
			continue
		except TypeError:
			print "Non numeric Value"
			continue

if __name__ == '__main__':
	divide()
