# # Задание №24
# 24.	Для удобства проведения вступительных экзаменов всеx абитуриентов
# в MIT разбивают на группы в зависимости от первых букв их фамилии.
# Группы называются ‘A-I’, ‘J-P’, ‘Q-T’, ‘U-Z’.
# Название группы определяет в какую группу попадает абитуриент,
# в зависимости от первой буквы его/ее фамилии. Например,
# Will Smith попадает в группу ‘Q-T’, т.к. первая буква его фамилии попадает
# в диапазон букв от ‘Q‘ до ‘Т‘ (включительно!).
# Абитуриент Jay Z попадает в группу ‘U-Z’ и т.д. Написать функцию,
# которая получает список имен студентов вида
# ['Name1 Surname1', 'Name2 Surname2', 'Name3 Surname3', ...]
# и возвращает количество абитуриентов в группах, сформированных по их фамилиям,
# описанным выше образом.
#      def group_by_surname(list_of_enrollees): # returns 4 ints
# 			pass

def group_by_surname(list_of_enrollees):


    number_names_from_a_to_i = 0
    number_names_from_j_to_p = 0
    number_names_from_q_to_t = 0
    number_names_from_u_to_z = 0
    names_from_a_to_i = ''
    names_from_j_to_p = ''
    names_from_q_to_t = ''
    names_from_u_to_z = ''


    for student_name in list_of_enrollees:
        part = student_name.split(' ')
        name = part[0]
        surname = part[1]
        if 'A' <= surname[0] <= 'I':
            number_names_from_a_to_i = number_names_from_a_to_i + 1
            names_from_a_to_i = names_from_a_to_i + student_name + ' '
        elif 'J' <= surname[0] <= 'P':
            number_names_from_j_to_p = number_names_from_j_to_p + 1
            names_from_j_to_p = names_from_j_to_p + student_name + ' '
        elif 'Q' <= surname[0] <= 'T':
            number_names_from_q_to_t = number_names_from_q_to_t + 1
            names_from_q_to_t = names_from_q_to_t + student_name + ' '
        elif 'U' <= surname[0] <= 'Z':
            number_names_from_u_to_z = number_names_from_u_to_z + 1
            names_from_u_to_z = names_from_u_to_z + student_name + ' '

    print('From A to I = ', number_names_from_a_to_i, 'students :', names_from_a_to_i)
    print('From J to P = ', number_names_from_j_to_p, 'students :', names_from_j_to_p)
    print('From Q to T = ', number_names_from_q_to_t, 'students :', names_from_q_to_t)
    print('From U to Z = ', number_names_from_u_to_z, 'students :', names_from_u_to_z)

list_of_enrollees = ['Alfred Duglas','John Abrmas','Tom Alien','Sam Smith', 'Kenny West', 'Jessi Pinkman', 'Wolter White']

group_by_surname(list_of_enrollees)





