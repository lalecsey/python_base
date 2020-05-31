# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

class Snowflake:

    def __init__(self, x, y, length):
        self.length = length
        self.x = x
        self.y = y
        self.draw()

    def clear(self):
        sd.clear_screen()

    def move(self):
        self.x += 10
        self.y -= 10

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(point, self.length)

    def can_fall(self):
        var = 50 < self.y
        return var

flake = Snowflake(x=50, y=550, length=50)

while True:
    flake.clear()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
