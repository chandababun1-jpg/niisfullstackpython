from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, n, r):
        super().__init__(n)
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


class Triangle(Shape):
    def __init__(self, n, b, h):
        super().__init__(n)
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h


c1 = Circle("circle", 7)
print(c1.area())

t1 = Triangle("triangle", 10, 5)
print(t1.area())
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, n, l, b):
        super().__init__(n)
        self.l = l
        self.b = b

    def perimeter(self):
        return 2 * (self.l + self.b)


class Square(Shape):
    def __init__(self, n, s):
        super().__init__(n)
        self.s = s

    def perimeter(self):
        return 4 * self.s


r1 = Rectangle("Rectangle", 8, 5)
print("Perimeter of Rectangle:", r1.perimeter())

s1 = Square("Square", 6)
print("Perimeter of Square:", s1.perimeter())