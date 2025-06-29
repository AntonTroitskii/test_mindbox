from task_1.figures import Circle, Rectangle, Triangle
import sys
import os
import math
import pytest
import itertools


def test_circle_area():
    r = 1
    circle = Circle(r)
    assert math.pi * 1 == circle.get_area()

    r = 2
    circle = Circle(r)
    assert math.pi * r * r == circle.get_area()

    r = 1.1
    circle = Circle(r)
    assert math.pi * r * r == circle.get_area()

    r = 0
    circle = Circle(r)
    assert 0 == circle.get_area()


def test_rect_area():
    a, b = 1, 2
    rect = Rectangle(a, b)
    assert a * b == rect.get_area()

    a, b = 1.1, 2.2
    rect = Rectangle(a, b)
    assert a * b == rect.get_area()


def test_triangle_area():
    a, b, c = 1, 1, 1
    triangle = Triangle(a, b, c)
    area = triangle.get_area()
    assert area == pytest.approx(0.433013, rel=1e-6)

    a, b, c = 4, 3, 5
    triangle = Triangle(a, b, c)
    area = triangle.get_area()
    assert area == pytest.approx(6, rel=1e-6)

    a, b, c = 1.1, 1.1, 1.1
    triangle = Triangle(a, b, c)
    area = triangle.get_area()
    assert area == pytest.approx(0.523945, rel=1e-6)


def test_is_triangel_right():
    abc = [3, 4, 5]

    for p in list(itertools.permutations(abc)):
        triangle = Triangle(*p)
        assert True == triangle.is_right_triangle()

    a, b, c = 1, 1, 1
    triangle = Triangle(a, b, c)
    assert False == triangle.is_right_triangle()
