class parent:
	def parent_info(self):
		print("this is the parent class")
class child(parent):
	def child_info(self):
		print("this is the child class")
class engineering(child):
	def eng_info(self):
		print("i am studying in engieering")
obj=engineering()
obj.parent_info()
obj.child_info()
obj.eng_info()


