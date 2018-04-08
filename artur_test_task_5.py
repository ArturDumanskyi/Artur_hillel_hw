# Задание 5

# Создать программу, выводящую на экран ближайшее к 10 из двух чисел,
# введенных пользователем.
# Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45.


def closest_number(first, second):
    num = 10
    if abs(10 - first) > abs(10 - second):
        return second
    else:
        return first


print(closest_number(8.5, 11.45))
