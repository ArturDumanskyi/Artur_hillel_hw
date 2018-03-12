# Задание №14
# Написать функцию, которая будет проверять четность некоторого числа

import math


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = 12
if is_even(number):
    print('Число парное')
else:
    print('Число непарное')



