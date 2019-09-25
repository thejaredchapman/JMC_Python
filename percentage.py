def myfunc(a,b,c,d)
	#Returns sum of 10% of the sum of a,b,c,d
	return sum((a,b,c,d)) * 0.10

myfunc(5,10,8,30)

def myfunc(*args):
	print(args)

myfunc(50,28,100,6,1000)