# -*- coding: utf-8 -*-

import simple_draw as sd

def tree(point, angle, length, delta):
    if length < 3:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - sd.random_number(delta-6, delta+6)
    next_angle_2 = angle + sd.random_number(delta-6, delta+6)
    next_length = length * (sd.random_number(70, 80) / 100)
    tree(point=next_point, angle=next_angle, length=next_length, delta=delta)
    tree(point=next_point, angle=next_angle_2, length=next_length, delta=delta)

# point_0 = sd.get_point(300, 5)
# tree(point=point_0, angle=90, length=100, delta=30)
#
# sd.pause()


