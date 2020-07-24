# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def figure(point, angle=0, length=100):
        start_point = point
        delta = 360 / n
        for _ in range(n-1):
            v1 = sd.get_vector(start_point=point, angle=angle, length=length)
            v1.draw()
            point = v1.end_point
            angle += delta
        sd.line(start_point=point, end_point=start_point)
    return figure


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()
