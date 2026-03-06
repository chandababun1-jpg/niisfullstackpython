def sum_of_digits(n):
	if n==0:
		return 0
	else:
		return(n%10)+ sum_of_digits(n//10)
number=int(input("enter a number:"))
print(f"The sum of digits of{number}is:{sum_of_digits(number)}")

