# This is an example program to demonstrate what the decorator is --

# 1. defined a normal function taking variable number of arguments and returning summation
# 2. defined decorator function which shall return n*sumr


def outer(n):
	def nsum(f):
		def inner(*args,**kwargs):	
			print("Inside inner function") 
			return f(*args,**kwargs) * n
	
		return inner
	return nsum

@outer(10)
def sum(*args,**kwargs):
	sumr = 0
	for arg in args:
		sumr  = sumr + arg
	return sumr

# The below line has been replaced with the decorator with paramters 
# sum = nsum(sum,5)

print(sum(5,6,7,2))
