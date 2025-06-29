from abc import ABC, abstractmethod
import math


class Figure(ABC):

    def get_area(self):
        pass


class Circle(Figure):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_area(self):
        return math.pi * math.pow(self.radius, 2)


class Rectangle(Figure):

    def __init__(self, a, b):
        super().__init__()

        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Triangle(Figure):

    def __init__(self, a, b, c):
        super().__init__()

        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_triangle(self):
        a2 = math.pow(self.a, 2)
        b2 = math.pow(self.b, 2)
        c2 = math.pow(self.c, 2)

        return (a2 == b2 + c2) or (b2 == a2 + c2) or (c2 == a2 + b2)

    def check_pifagor_eq(a, b, c):
        return
