import math

def next_hexagon_angle(x, y, radius, current_angle):
    theta = current_angle + math.pi / 3 # add 60 degrees in radians
    next_x = radius * math.cos(theta) + x
    next_y = radius * math.sin(theta) + y
    return next_x, next_y

def hexagon(center_x, center_y, radius):
    angle = 0
    points = []
    for i in range(6):
        x = int(center_x + radius * math.cos(angle))
        y = int(center_y + radius * math.sin(angle))
        points.append((x, y))
        angle += math.pi / 3
    return points
