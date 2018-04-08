# Задание № 4

number = input('Введите число - ')

print('число=', number)


def sum_noteven_digits(number):
    sum = 1
    for num in (number):
        if int(num) % 2 != 0:
            sum = sum * int(num)
    return sum


print('произведение нечетных цифр числа -', sum_noteven_digits(number))
