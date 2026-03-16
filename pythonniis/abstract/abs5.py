class VoterError(BaseException):
	def __init__(self,name):
		super().__init__()
print("enter a age")
age=int(input())
if age>=18:
	print("eligibal")
else:
	try:
		raise VoterError("age not allow")
	except:
		print("not allow")
print("main end")