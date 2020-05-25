import random

number = 0
bulls = 0
cows = 0

def make_number():
    global number
    number = random.randint(1000, 9999)
    return number

def bulls_check(check_number):
    global number, bulls
    bulls = 0
    for i in range(len(str(number))):
        n = str(number)[i]
        n_2 = str(check_number)[i]
        if n == n_2:
            bulls += 1

def cows_check(check_number):
    global number, cows
    cows = 0
    for i in str(check_number):
        list_i = []
        if i not in list_i:
            c = list(str(number)).count(i)
            cows += c
            list_i.append(i)


def check_mumber(input_number):
    bulls_check(input_number)
    cows_check(input_number)
    return print({'bulls': bulls, 'cows': cows})

def gameover():
    return bulls == 4