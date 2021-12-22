from lab_python_oop.GeometricFigure import Figure
from lab_python_oop.color import Color


class Rectangle(Figure):
    '''h - высота, w - ширина'''

    FIGURE_TYPE = 'Прямоугольник'

    def __init__(self, h, w, color):
        self._h, self._w, self._color = h, w, Color(color)

    def square(self):
        return self._h * self._w

    def __str__(self):
        return f'{self.FIGURE_TYPE} высотой {self._h} и шириной {self._w} цвета {self._color}'
