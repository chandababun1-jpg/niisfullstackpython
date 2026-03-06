#factorial using recursion
f=1
def fact(no):
	global f
	if no>0:
		f=f*no
		no=no-1
		fact(no)
	return f
res = fact(4)
print("factorial=",res)	