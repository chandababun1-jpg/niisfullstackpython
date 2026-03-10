amount=10000
def deposit(amt):
	global amount
	amount=amount+amt
	print("deposit",amt)
def withdraw(amt):
	global amount
	amount=amount-amt
	print("withdraw",amt)
print("balance=",amount)	
deposit(3000)
withdraw(6000)
print("balance=",amount)
