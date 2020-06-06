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

    def __add__(self, other):
        if other.__name__ == Air:
            storm = Storm()
            return storm
        elif other.__name__ == Fire:
            steam = Steam()
            return steam
        elif other.__name__ == Earth:
            dirt = Dirt()
            return dirt
        else:
            return None
    def __str__(self):
        return print(Water(), '+', Air(), '=', Water() + Air())


class Air:

    def __add__(self):
        if other.__name__ == Water:
            storm = Storm()
            return storm
        elif other.__name__ == Fire:
            steam = Steam()
            return steam
        elif other.__name__ == Earth:
            dirt = Dirt()
            return dirt
        else:
            return None

    def __str__(self):
        return print(Water(), '+', Air(), '=', Water() + Air())

# class Fire:
#
#     def __add__(self):
#
#     def __str__(self):
#         print()
#
# class Earth:
#
#     def __add__(self):
#
#     def __str__(self):
#         print()
#
class Storm:

    def __add__(self):

    def __str__(self):
        print()

# class Steam:
#
#     def __add__(self):
#
#     def __str__(self):
#         print()
#
# class Dirt:
#
#     def __add__(self):
#
#     def __str__(self):
#         print()

# class Lightning:
#
#     def __add__(self):
#
#     def __str__(self):
#         print()
#
# class Dust:
#
#     def __add__(self):
#
#     def __str__(self):
#         print()
#
# class Lava:
#
#     def __add__(self):
#
#     def __str__(self):
#         print()

water = Water()
air = Air()

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
