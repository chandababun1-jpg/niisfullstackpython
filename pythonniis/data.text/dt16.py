# write 3 student record into file
import pickle

# create class
class student:
    def __init__(self, roll, name, mark):
        self.roll = roll
        self.name = name
        self.mark = mark

    def show(self):
        print(self.roll, self.name, self.mark)


f = open("student.dat", "rb")

print("Students record:")

while True:
    try:
        s = pickle.load(f)   # read object
        s.show()             # display object
    except EOFError:
        break

f.close()
