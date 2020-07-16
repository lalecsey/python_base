# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

tochka = [300, 300]

def smile(tochka, color):
    point = sd.get_point(*tochka)
    sd.circle(point, radius=60, color=color, width=3)
    left_eye = [tochka[0] - 20, tochka[1] + 20]
    left_eye_point = sd.get_point(*left_eye)
    sd.circle(left_eye_point, radius=5, color=color, width=0)
    right_eye = [tochka[0] + 20, tochka[1] + 20]
    right_eye_point = sd.get_point(*right_eye)
    sd.circle(right_eye_point, radius=5, color=color, width=0)
    mouth = [tochka[0], tochka[1] - 25]
    mouth_point = sd.get_point(*mouth)
    v = sd.get_vector(mouth_point, angle=25, length=25, width=3)
    v.draw(color=color)
    v2 = sd.get_vector(mouth_point, angle=155, length=25, width=3)
    v2.draw(color=color)

smile(tochka, sd.COLOR_DARK_RED)

sd.pause()
