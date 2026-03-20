L1=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(L1),1):
	for j in range(0,len(L1[i]),1):
		if i>=j:
			print(L1[i][j],end="\t")
		else:
			print(end="\t")
print()