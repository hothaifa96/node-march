import math
class Shape:
    def __init__(self):
        self.area=0
        self.perimeter=0
    def calc_area(self):
        print('hello this is my default')
    def calc_perimeter(self):
        pass
    def __str__(self):
        return f'  \narea-----> {self.area}\nperimeter -----> {self.perimeter}'

class Circle(Shape):
    def __init__(self,r):
        Shape.__init__(self)
        self.r=r
        self.calc_area()
        self.calc_perimeter()
    def calc_area(self):
        self.area = math.pi * self.r**2
    def calc_perimeter(self):
        self.perimeter = math.pi * self.r*2

    # def set_area(self):
    #     self.__area= self.r**2 * math.pi
class Triangle(Shape):
    def __init__(self,a,b,c,h):
        Shape.__init__(self)
        self.a=a
        self.b=b
        self.c=c
        self.h=h
        self.calc_area()
        self.calc_perimeter()
    def calc_area(self):
        self.area = self.b * self.h / 2
    def calc_perimeter(self):
        self.perimeter = self.a + self.b + self.c
class Rectangle(Shape):
    def __init__(self,a,b):
        super().__init__()
        self.a=a
        self.b=b
        self.calc_area()
        self.calc_perimeter()
    def calc_area(self):
        self.area = self.b * self.a
    def calc_perimeter(self):
        self.perimeter = self.a * 2 + self.b *2


s1 = Shape()
c1 = Circle(5)
t1= Triangle(3,4,5,4)
r1= Rectangle(14,5)
# print(isinstance(c1,Shape))
# print(isinstance(s1,Circle))
# print(c1)
# print(t1)
# print(s1)
# print(r1)

print(c1.r)