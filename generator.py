# This is the example for generator 
# Also some denugging

import pdb

def print_c():
	n = 0
	print("Printing the output in the term = %d ",(n))
	yield n
	n = n + 1

x = print_c()
for _ in range(2):
	pdb.set_trace()
	print("inside the loop--beginning")
	try:
		next(x)
	except StopIteration:
		print("No more item to iterate")
	print("inside the loop--ending")
