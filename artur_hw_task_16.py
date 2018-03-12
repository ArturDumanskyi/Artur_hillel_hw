#Задание №16

def have_trains_crashed(v1, v2):
    if (4 / v1) < ((10-4) / v2):
        return True
    else:
        return False

v1 = input('Введите скорость первого поезда: ')
v2 = input('Введите скорость второго поезда: ')
v1 = (int(v1))
v2 = (int(v2))
if have_trains_crashed(v1, v2):
    print('поезда не столкнуться', '\U0001F601', '\U0001F685')
else:
    print('поезда столкнуться', '\U0001F6A7', '\U0001F685', '\U0001F4A3', '\U0001F4A5')


