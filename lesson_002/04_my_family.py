#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mama', 'papa', 'i']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['mama', 162], ['papa', 176], ['i', 134]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

print(my_family_height[1][1])
print(my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] )