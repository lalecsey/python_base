# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import district.central_street.house2.room1 as house_room1
import district.central_street.house1.room2 as house_room2
import district.central_street.house2.room1 as room1
from district.central_street.house2.room2 import folks

print('На районе живут:', ', '.join(folks), ', '.join(room1.folks), ', '.join(house_room2.folks) , ', '.join(house_room1.folks))



