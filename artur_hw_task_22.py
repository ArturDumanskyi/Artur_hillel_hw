# Задание №22
import random

def game():
    print('Welcome!')
    while True:
        print('Я хочу сыграть с вами в игру!')
        choice = input('Введите на клаиваитаре y - если хотите играть, n - если хотите покинуть игру')
        if choice == 'y':
            computer_choice = random.randint(1, 10)
            while True:
                user_choice = int(input(('введите число:')))
                if user_choice == computer_choice:
                    print('Поздравляю! Загаданное число =', user_choice)
                    break
                elif user_choice < computer_choice:
                    print('Загаданное компьюетром число больше')
                elif user_choice > computer_choice:
                    print ('Загаданное компьютером число меньше')
        elif choice == 'n':
            print('Всего наилучшего!')
            break
game()