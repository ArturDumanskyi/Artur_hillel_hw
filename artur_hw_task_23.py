#Задание №23


def chess_reward():
    cell_number = 0
    total_number_of_corns = 0
    for i in range(1, 64):
        if total_number_of_corns < 1000000:
            total_number_of_corns = 2**i
            i += i + 1
            cell_number += 1
    return (cell_number, total_number_of_corns)
print(chess_reward())