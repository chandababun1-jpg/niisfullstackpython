print("enter two number")
no1=int(input())
no2=int(input())
print("enter your choice\n1.add\n2.sub\n3.mult")
ch=int(input())
match ch:

    case1 :print("sum=",no1+no2)

	case2:print("sub=",no1-no2)
	case3:print("mult=",no1*no2)
	case_:print("invalid choice")
