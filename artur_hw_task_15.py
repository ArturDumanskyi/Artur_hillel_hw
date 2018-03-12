#Задание №15

import math
print()


def circles_intersects(x1, y1, r1, x2, y2, r2):
    sum_radius = r1 + r2
    centr_dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if sum_radius < centr_dist or r1 > centr_dist + r2 or r2 > centr_dist + r1:
        return True
    else:
        return False

x1 = 5
y1 = 10
r1 = 5
x2 = 6
y2 = 11
r2 = 2
if circles_intersects(x1, y1, r1, x2, y2, r2):
    print ('Окружности не пересекаются')
else:
    print ('Окружности пересекаются')