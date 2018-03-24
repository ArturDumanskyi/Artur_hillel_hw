#Задание №19

import random
def diff_min_max(num_limit, lower_bound, upper_bound):
    curr_min = upper_bound
    curr_max = lower_bound
    for i in range(num_limit+1):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num)

        if curr_min > rand_num:
            curr_min = rand_num
        elif curr_max < rand_num:
            curr_max = rand_num


    return curr_max - curr_min

print('diff_min_max:', diff_min_max(12, 100, 200))