#задание №17

# ax**2 + bx + c = 0

import math

def solve_quadratic_equation(a, b, c):
    if b**2 - 4*a*c > 0:
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return x1, x2
    elif b**2 - 4*a*c == 0:
        x = -b / (2*a)
        return x
    else:
        return 'корней нет'

print(solve_quadratic_equation(4, 4, 1))

