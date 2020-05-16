# -*- coding: utf-8 -*-
import simple_draw as sd
from old_lesson.rainbow import rainbow
from old_lesson.tree import tree
from old_lesson.snowfall import snowfall, snowdrift
from old_lesson.wall import wall

sd.set_screen_size(width=1400, height=780)

rainbow_point = [500, 0]
rainbow(rainbow_point, 950)

tree_point = sd.get_point(1200, 0)
tree(point=tree_point, angle=90, length=90, delta=30)
tree_point = sd.get_point(1120, 250)
tree(point=tree_point, angle=90, length=70, delta=30)
tree_point = sd.get_point(1150, 400)
tree(point=tree_point, angle=90, length=55, delta=30)

wall()
snowdrift()

sd.pause()



# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)



# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
