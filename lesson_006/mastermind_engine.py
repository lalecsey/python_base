import random
number = ''
# {'bulls': 0, 'cows': 0}

def make_number():
    global number
    number = ''
    for i in range(4):
        if i == 0:
            a = str(random.randint(1, 9))
        else:
            a = str(random.randint(0, 9))
        number += a
    return print(number)


def check_mumber(input_number):
    int_number = int(number)
    for i in range(len(number)):
        b = 0
        if int(number[i]) == str(input_number)[i]:
            b += 1
    return print({'bulls': b})


make_number()
q = 1234
check_mumber(q)
