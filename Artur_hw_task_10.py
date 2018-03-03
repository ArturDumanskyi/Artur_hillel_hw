"""
Задание 10
Дана строка вида 'Lev Tolstoy*1828-08-28*1910-11-20'.
В этой строке даны имя человека, даты рождения и смерти
Написать программу, которая по строке определит возраст писателя и распечатает
его имя и возраст
"""

initial = "Kurt Cobain*1967-02-20*1994-04-05"
print()
print("Исходная строка -->", initial)


name = initial.split('*')[0]
date_of_born = initial.split('*')[1]
date_of_dead = initial.split('*')[2]

year_of_born = date_of_born.split('-')[0]
year_of_dead = date_of_dead.split('-')[0]
age = int(year_of_dead) - int(year_of_born)

print("Имя и фамилия ", name, "возраст", age, "лет")