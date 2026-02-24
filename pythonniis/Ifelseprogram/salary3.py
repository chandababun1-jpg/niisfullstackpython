#wap take emp salary from keyboard if sal>=6000 da=30% hra=20%
print("enter basic salary")
sal=float(input())
da=sal*0.3 if sal>=6000 else sal*0.2
hra=sal*0.2 if sal>=6000 else sal*0.1
totalsal=sal+da+hra
print("basic salary=",sal)
print("da",da)
print("hra",hra)
print("total salary",totalsal)	

