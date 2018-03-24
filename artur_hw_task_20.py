#Задание №20

import random
def diff_even_odd(num_limit, lower_bound, upper_bound):
    summ_even = 0
    summ_none_even = 0
    for i in range(num_limit+1):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num)

        if rand_num % 2 == 0:
            summ_even += rand_num
        else:
            summ_none_even += rand_num
    print('summ_even =', summ_even )
    print('summ_none_even =', summ_none_even)
    return summ_even - summ_none_even


print('diff_even_odd', diff_even_odd(7, 1, 20))