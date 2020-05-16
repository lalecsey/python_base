import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

r = 300
for color in rainbow_colors:
    point = sd.get_point(300, 0)
    sd.circle(point, radius=r, color=color, width=10)
    r += 10


sd.pause()