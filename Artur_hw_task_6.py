
# Задание №6 Найти результат выражения для произвольных значений
# a,b,c: ( ln(1 + c) / -b)**4 + [a]

import math

a = -20
b = 2
c = 42
result = (math.log1p(c) / (-b))**4 + math.fabs(a)
print("Результат выражения, при значении a = %.f, b = %.f, и c = %.f, будет равен %.1f" % (a, b, c, result,))
