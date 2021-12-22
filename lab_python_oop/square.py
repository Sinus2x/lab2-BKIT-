from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):

    FIGURE_TYPE = 'Квадрат'

    def __init__(self, side_length, color):
        """ a - длина стороны квадрата"""
        self._side = side_length
        super().__init__(side_length, side_length, color)

    def __str__(self):
        return f'{self.FIGURE_TYPE} стороной {self._side} цвета {self._color}'


