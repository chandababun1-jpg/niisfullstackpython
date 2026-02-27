def show():
	x=10
	print("A")
	disp(x)#call by value integer float string tuple bool complex
	print("B")
def disp(x):
	print("C")
	x=30
	print("D")
print("start")
show()
print("end")