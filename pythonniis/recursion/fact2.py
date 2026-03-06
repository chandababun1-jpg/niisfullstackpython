#factorial number using recursion
def fact(no):
	if no==0:
		return 1
	else:
		return no*fact(no-1)
res = fact(4)
print("factorial=", res)	