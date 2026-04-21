x=10
def show():
	x=30
	print(x)
	print(locals()['x'])
	print(globals()['x'])
	globals()['x']=50	
show()
print(x)