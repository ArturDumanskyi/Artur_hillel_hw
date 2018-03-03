"""
Задание № 9
Написать программу, которая преобразует имя переменной в формате snake_case в формат
CamelCase

"""


data = "day_before_tomorrow"
print()
print("Выражение в формате snake_case --> ", data)

result = data.split('_')

word1 = result[0].capitalize()
word2 = result[1].capitalize()
word3 = result[2].capitalize()

list = [word1, word2, word3]

word = "".join(list)
print()
print("Выражение в формате CamelCase --> ", word)
