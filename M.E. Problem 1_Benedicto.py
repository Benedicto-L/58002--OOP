import math


class Circle:
    def __init__(self):

        self.rad = float(input("Radius of a Circle: "))

    def perimeter(self):
        return 2*math.pi*self.rad

    def area(self):
        return math.pi*self.rad**2

    def display(self):
        print("Perimeter of a Circle:", self.perimeter())
        print("Area of a Circle:", self.area())


measurements = Circle()
measurements.display()
