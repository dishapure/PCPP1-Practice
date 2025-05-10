from abc import ABC, abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        return "this is a shape"


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius;

    def area(self):
        return 3.14  * self.radius*self.radius
circle = Circle(5);
print(circle.area())
print(circle.describe())