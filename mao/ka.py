for i in range(24):
	with open('%s.txt'% i,'r') as f:
		a=f.readline()
		print(a)