# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __init__(self):
        self.__name__ = 'water'

    def __str__(self):
        return 'вода'

    def __add__(self, other):
        if other.__name__ == 'air':
            return Storm()
        elif other.__name__ == 'fire':
            return Steam()
        elif other.__name__ == 'earth':
            return Dirt()
        else:
            return None

class Air:
    def __init__(self):
        self.__name__ = 'air'

    def __str__(self):
        return 'воздух'

    def __add__(self):
        if other.__name__ == 'water':
            return Storm()
        elif other.__name__ == 'fire':
            return Lightning()
        elif other.__name__ == 'earth':
            return Dust()
        else:
            return None

class Fire:

    def __init__(self):
        self.__name__ = 'fire'

    def __str__(self):
        return 'огонь'

    def __add__(self):
        if other.__name__ == 'water':
            return Steam()
        elif other.__name__ == 'air':
            return Lightning()
        elif other.__name__ == 'earth':
            return Lava()
        else:
            return None

class Earth:

    def __init__(self):
        self.__name__ = 'earth'

    def __str__(self):
        return 'земля'

    def __add__(self):
        if other.__name__ == 'water':
            return Dirt()
        elif other.__name__ == 'air':
            return Dust()
        elif other.__name__ == 'fire':
            return Lava()
        else:
            return None

class Storm:

    def __init__(self):
        self.__name__ = 'storm'

    def __str__(self):
        return 'шторм'

class Steam:

    def __init__(self):
        self.__name__ = 'steam'

    def __str__(self):
        return 'пар'

class Dirt:

    def __init__(self):
        self.__name__ = 'dirt'

    def __str__(self):
        return 'грязь'

class Lightning:

    def __init__(self):
        self.__name__ = 'lightning'

    def __str__(self):
        return 'молния'

class Dust:

    def __init__(self):
        self.__name__ = 'dust'

    def __str__(self):
        return 'пыль'

class Lava:

    def __init__(self):
        self.__name__ = 'lava'

    def __str__(self):
        return 'лава'



print(Water(), '+', Air(), '=', Water() + Air())

print(Water(), '+', Fire(), '=', Water() + Fire())
