

def sum_of_digits(a):
    return (a // 100) + (a // 10 % 10) + (a % 10)

print("Сумма цифр в числе равна:", sum_of_digits(345))

