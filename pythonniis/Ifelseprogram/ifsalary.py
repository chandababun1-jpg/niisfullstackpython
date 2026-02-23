print("enter basic salary")
sal=float(input())
da,hra=0,0
if sal>=6000:
	da=sal*0.3
	hra=sal*0.2
	totalsal=sal+da+hra
print("basic salary=",sal)
print("da",da)
print("hra",hra)
print("total salary",totalsal)	

