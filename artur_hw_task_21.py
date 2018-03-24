# Задание №21


def get_max_digit(number):
    max_digit = 0
    for i in str(number):
        if max_digit < int(i):
            max_digit = int(i)
    return max_digit


print('max digit is:', get_max_digit(123486734123))