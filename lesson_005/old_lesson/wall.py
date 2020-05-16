import simple_draw as sd

def wall():
    for y in range(0, 400, 30):
        y_2 = y + 30
        for x in range(400, 780, 60):
            if y / 30 % 2 == 1:
                x -= 30
            x_2 = x + 60
            point = sd.get_point(x, y)
            point_2 = sd.get_point(x_2, y_2)
            sd.rectangle(point, point_2, color=sd.COLOR_YELLOW, width=1)

# wall()

# def wall_2(x=0, y=0, x_2=300, y_2=300, length=60):
#     width = length / 2
#     start_point = sd.get_point(x, y)
#     sd.square(start_point, side=width, width=1)
#     point = sd.get_point(x + width, y)
#     point_2 = sd.get_point(x + width + length, y + width)
#     sd.rectangle(point, point_2, width=1)
#
# wall_2(0,0, 500, 500, 100)
#
# sd.pause()