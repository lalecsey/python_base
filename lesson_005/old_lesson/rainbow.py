import simple_draw as sd

def rainbow(tochka, radius):
    rainbow_colors = (
        sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE
    )
    for color in rainbow_colors:
        point = sd.get_point(*tochka)
        sd.circle(point, radius=radius, color=color, width=5)
        radius += 5

# rainbow([100, 100], 50)
#
# sd.pause()
