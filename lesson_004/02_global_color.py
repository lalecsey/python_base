# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

dict_print = {0 : 'красный', 1 : 'оранжевый', 2 : 'желтый', 3 : 'зеленый', 4 : 'голубой', 5 : 'синий', 6 : 'фиолетовый'}

color_list = [
    sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE
]

def triangle(point, angle=0, length=100, delta=60, color=sd.COLOR_RED):
    if angle >= 360:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)
    next_point = v1.end_point
    angle = angle + delta
    triangle(next_point, angle, length, delta, color=color)

def shape(color):
    i = 3
    for x in range(100, 401, 300):
        for y in range(100, 401, 300):
            angle = 360 / i
            triangle(sd.get_point(x, y), 0, 100, angle, color)
            i += 1

def global_color():
    color_input = int(input('Возможные цвета:\n'
                        '   0: Красный\n'
                        '   1: Оранжевый\n'
                        '   2: Жёлтый\n'
                        '   3: Зелёный\n'
                        '   4: Голубой\n'
                        '   5: Синий\n'
                        '   6: фиолетовый\n'))
    if 0 <= color_input <= 6:
        shape(color_list[color_input])
    else:
        print('Введите число от 0 до 6')
        global_color()

global_color()

sd.pause()
