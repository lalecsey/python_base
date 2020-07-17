
from random import randint
import simple_draw as sd

snow_flakes = []

def creating_snowflakes(N):
    global snow_flakes
    for i in range(N):
        x = randint(100, 500)
        y = randint(450, 600)
        length = randint(5, 50)
        point = sd.get_point(x, y)
        snow_flakes.append(sd.snowflake(center=point, length=length, color=sd.COLOR_DARK_YELLOW))

def transparent_snowflake():
    global snow_flakes
    for i in range(len(snow_flakes)):
        print(snow_flakes[i])



# while True:
#     sd.clear_screen()
#     for i in range(20):
#         point = sd.get_point(x[i], y[i])
#         sd.snowflake(center=point, length=length_list[i])
#         if y[i] > length_list[i]:
#             y[i] += (randint(5, 15) * -1)
#             x[i] += randint(-15, 15)
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
