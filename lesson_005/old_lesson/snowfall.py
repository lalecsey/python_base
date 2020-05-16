import simple_draw as sd
from random import randint

def snowfall():
    x = [randint(100, 500) for i in range(20)]
    y = [randint(450, 600) for i in range(20)]
    length_list = [randint(5, 50) for i in range(20)]

    while True:
        sd.clear_screen()
        for i in range(20):
            point = sd.get_point(x[i], y[i])
            sd.snowflake(center=point, length=length_list[i])
            y[i] += (randint(5, 15) * -1)
            if y[i] < 0:
                break
            x[i] += randint(-15, 15)
        sd.sleep(0.1)
        if sd.user_want_exit():
            break
        sd.sleep(0.1)
        if sd.user_want_exit():
            break

def snowdrift():
    _ = 0
    while _ <= 20:
        x = randint(0, 200)
        y = randint(0, 150)
        length = randint(10, 50)
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=length)
        _ += 1



