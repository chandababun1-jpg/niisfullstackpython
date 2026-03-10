class Student:
    def __init__(self, name):
        self._name = name   # initial value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


s = Student("virat")
print(s.name)

s.name = "babun"
print(s.name)