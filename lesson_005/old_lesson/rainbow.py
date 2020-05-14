# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# x = 50
# x_2 = 350
# for color in rainbow_colors:
#    point = sd.get_point(x, 50)
#    point_2 = sd.get_point(x_2, 450)
#    sd.line(point, point_2, color=color, width=4)
#    x = x + 5
#    x_2 = x_2 + 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

r = 300
for color in rainbow_colors:
    point = sd.get_point(300, 0)
    sd.circle(point, radius=r, color=color, width=4)
    r += 5


sd.pause()
