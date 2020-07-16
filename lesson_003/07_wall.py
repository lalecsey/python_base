# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


for y in range(0, 600, 50):
    y_2 = y + 50
    for x in range(0, 600, 100):
        if y / 50 % 2 == 1:
            x -= 50
        x_2 = x +100
        point = simple_draw.get_point(x, y)
        point_2 = simple_draw.get_point(x_2, y_2)
        simple_draw.rectangle(point, point_2, color=simple_draw.COLOR_YELLOW, width=1)





simple_draw.pause()
