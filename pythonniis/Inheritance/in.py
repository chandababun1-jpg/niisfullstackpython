class A:
	def f1(self):
		print("class A")
class B(A):
	def f2(self):
		print("class B")
class C(B):
	def f3(self):
		print("class C")
ob=c()
ob.f1()
ob.f2()
ob.f3()
