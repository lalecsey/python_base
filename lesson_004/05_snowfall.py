# -*- coding: utf-8 -*-
from random import randint
import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

N = 20

x = [randint(100, 500) for i in range(N)]
y = [randint(450, 600) for i in range(N)]
length_list = [randint(5, 50) for i in range(N)]

while True:
    sd.start_drawing()
    for i in range(N):
        point = sd.get_point(x[i], y[i])

        sd.snowflake(center=point, length=length_list[i], color=sd.COLOR_WHITE)
        sd.clear_screen()
        if y[i] > length_list[i]:
            y[i] -= randint(5, 15)
            x[i] += randint(-15, 15)
        # sd.snowflake(center=point, length=length_list[i], color=sd.COLOR_WHITE)
    sd.sleep(0.1)
    sd.finish_drawing()
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


