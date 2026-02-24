#wap take emp salary from keyboard if sal>=6000 da=30% hra=20%
print("enter basic salary")
sal=float(input())
if sal>=6000:
	da=sal*0.3
	hra=sal*0.2
else:
	da=sal*0.2
	hra=sal*0.1
totalsal=sal+da+hra
print("basic salary=",sal)
print("da",da)
print("hra",hra)
print("total salary",totalsal)	

