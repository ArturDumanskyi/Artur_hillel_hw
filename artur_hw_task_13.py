import math

def triangle_square_and_perimeter(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    s = a * b / 2
    p = a + b + c
    return(s, p)

print("Площадь и периметр прямоугольного треугольника равны:",
      triangle_square_and_perimeter(3, 4))