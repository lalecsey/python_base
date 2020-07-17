# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
import random

class IamGodError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass

class SuicideError(Exception):
    pass

def error_message():
    dice = random.randint(1, 6)
    if dice == 1:
        raise IamGodError
    elif dice == 2:
        raise DrunkError
    elif dice == 3:
        raise CarCrashError
    elif dice == 4:
        raise GluttonyError
    elif dice == 5:
        raise DepressionError
    elif dice == 6:
        raise SuicideError

def one_day():
    dice = random.randint(1, 13)
    if dice == 13:
        error_message()
    else:
        return random.randint(1, 7)



ENLIGHTENMENT_CARMA_LEVEL = 777
carma = 0
day = 1

while carma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        print(f'-----День {day}-----')
        carma_day = one_day()
        print(f'Добавили к карме {carma_day}')
        carma += carma_day
        day += 1
    except IamGodError:
        print('Я бог!!!')
    except DrunkError:
        print('Я напился!')
    except CarCrashError:
        print('Я разбился в автокатастрофе.')
    except GluttonyError:
        print('Я обожрался.')
    except DepressionError:
        print('У меня депресия.')
    except SuicideError:
        print('Я покончил с собой.')

# https://goo.gl/JnsDqu
