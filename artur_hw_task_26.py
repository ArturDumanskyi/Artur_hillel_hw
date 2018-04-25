import random

def calc_frequency():
    num_zero = 0
    num_one = 0
    num_minus_one = 0
    for i in range(11):
        rand_num = random.randint(-1, 1)
        if rand_num == -1:
            num_minus_one = num_minus_one + 1
        elif rand_num == 0:
            num_zero = num_zero + 1
        elif rand_num == 1:
            num_one = num_one + 1
        print(rand_num)

    print('number of -1 = ', num_minus_one)
    print('number of 0 = ', num_zero)
    print('number of 1 = ', num_one)

    if num_minus_one == num_zero or num_zero == num_one or num_one == num_minus_one:
        return None
    elif num_minus_one > num_zero and num_minus_one > num_one:
        return -1
    elif num_zero > num_minus_one and num_zero > num_one:
        return 0
    elif num_one > num_zero and num_one > num_minus_one:
        return 1

print('Максимально встречающийся элемент : ', calc_frequency())


