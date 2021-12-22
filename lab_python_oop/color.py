class Color:
    def __init__(self, color_str=None):
        self._color = color_str

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def del_color(self):
        del self._color

    color = property(get_color, set_color, del_color)
 # В чём разница, использовать конструкцию с @property или с property() ?
