class student:
    def __init__(self,n,r,m):
        self.__name = n
        self.__roll = r
        self.__mark = m
    def show(self):
        print("my name=",self.__name)
        print("my roll=",self.__roll)
        print("my mark=",self.__mark)
s=student("virat",18,90.50)
s.show()


