# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

figure_list = ['треугольник', 'квадрат', 'пятиугольник', 'шестиугольник']

def triangle(point, angle=0, length=100, delta=60, color=sd.COLOR_RED):
    if angle >= 360:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)
    next_point = v1.end_point
    angle = angle + delta
    triangle(next_point, angle, length, delta, color=color)

def shape(figure_cod):
    point = sd.get_point(400, 400)
    angle = 360 / int(figure_cod)+3
    triangle(sd.get_point(x, y), 0, 100, angle)


def global_color():
    print('Возможные фигуру:')
    for i in range(len(figure_list)):
        print( i, ':', figure_list[i])
    figure_number = int(input('Пожалуста выберите фигуру '))
    if 0 <= figure_number <= 3:
        shape(figure_list[figure_number])
    else:
        print('Введите число от 0 до 3')


global_color()


sd.pause()
