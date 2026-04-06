#write 3 student record into file
import pickle
#creat class
class student:
	def __init__(self,roll,name,mark):
		self.roll=roll
		self.name=name
		self.mark=mark
	def show(self):
		print(self.roll,self.name,self.mark)
# create student objects
s1 = student(1, "Rahul", 85)
s2 = student(2, "Amit", 90)
s3 = student(3, "Priya", 88)

# open file in binary write mode
f = open("student.dat", "wb")

# write objects into file
pickle.dump(s1, f)
pickle.dump(s2, f)
pickle.dump(s3, f)

# close file
f.close()
print("3 student records written successfully!")

