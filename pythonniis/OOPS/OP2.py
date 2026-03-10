class SI:
	def __init__(self,p,r,t):
		self.principal=p
		self.rate=r
		self.time=t
	def show(self):
		print("principal=",self.principal)
		print("rate=",self.rate)
		print("time=",self.time)
	def SIcal(self):
		return self.principal*self.rate*self.time/100
print("enter principal,rate,time")
p=float(input())
r=float(input())
t=float(input())
i1=SI(p,r,t)
print("simple interest=",i1.SIcal())