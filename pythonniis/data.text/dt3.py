f=open("data.text","r")
L=f.readlines()
for i in L:
	print(i,end="")
f.close()