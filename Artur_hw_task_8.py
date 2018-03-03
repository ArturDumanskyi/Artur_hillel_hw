
person = "Michael Jackson"
print("Имя и фамилия - ", person)
print()
result = person.split(' ')

family = result[1]
name = result[0]
list = [family, name]
result1 = " ".join(list)
print("Фамилия и имя - ", result1)

