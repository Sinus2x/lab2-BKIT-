from abc import ABC, abstractmethod


class Figure(ABC):
    FIGURE_TYPE = 'Фигура'  # можно же наследовать статические переменные?
    '''Пример абстрактного класса'''

    # Вроде для user-friendly вывода переопределяют str, а не repr, как требуется в задании?
    def __str__(self):
        return 'geometric figure'

    @abstractmethod
    def square(self):
        pass

    @classmethod
    def get_type(cls):
        return cls.FIGURE_TYPE
