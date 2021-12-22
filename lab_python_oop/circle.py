from math import pi
from lab_python_oop.GeometricFigure import Figure
from lab_python_oop.color import Color


class Circle(Figure):
    """r - радиус"""

    FIGURE_TYPE = 'Круг'

    def __init__(self, r, color):
        self._r, self._color = r, Color(color)

    def square(self):
        return pi * self._r ** 2

    def __str__(self):
        return f'{self.FIGURE_TYPE} радиуса {self._r} цвета {self._color}'
