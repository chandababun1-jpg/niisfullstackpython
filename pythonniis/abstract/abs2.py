from abc import *
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, n, L, B):
        super().__init__(n)
        self.L = L
        self.B = B

    def perimeter(self):
        return 2 * (self.L + self.B)
class Square(Shape):
    def __init__(self, n, L):
        super().__init__(n)
        self.L = L
    def perimeter(self):
        return 4 * self.L
r1 = Rectangle("rect", 5, 7)
print(r1.perimeter())
s1 = Square("sq", 7)
print(s1.perimeter())