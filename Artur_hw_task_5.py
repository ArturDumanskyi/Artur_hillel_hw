
# Задание №4 Найти результат выражения для произвольных значений
# a,b,c: [a - b] / (a + b)**3 - cos(c)

import math

a = 20
b = 4
c = 2
result = (math.fabs(a - b)) / (a + b)**3 - math.cos(c)
print("Результат выражения, при значении a = %d, b = %d, и c = %d, будет равен %.1f" % (a, b, c, result,))
