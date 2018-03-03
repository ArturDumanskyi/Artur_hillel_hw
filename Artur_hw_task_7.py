# Задание №7
# Преобразовать строку с американским форматом даты в европейский. Например,
# 05.17.2016 преобразуется в 17.05.2016

american_date = "03.08.2017"
print()
print("Американский формат -->", american_date)

result = american_date.split('.')

day = result[1]
month = result[0]
year = result[2]

list = [day, month, year]
european_date = ".".join(list)

print()
print("Европейский формат -->", european_date)

