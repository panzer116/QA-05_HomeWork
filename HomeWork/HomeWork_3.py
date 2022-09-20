"""
3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
"""

# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[2])

"""
3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'
"""

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print('Original list: ', list_1)
# print('Sum of all numbers: ', sum([x for x in list_1 if type(x) == int ]))
# print('All words with a: ', [y for y in list_1 if type(y) == str and "a" in y])

"""
3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
"""

# List = ['cat', 'dog', 'horse', 'cow']
# list2 = tuple(List)
# print(type(list2))

# print(tuple(['cat', 'dog', 'horse', 'cow']))


"""
3.4. Напишите программу, которая определяет, какая семья больше.
      1) Программа имеет два input() - например, family_1, family_2.
      2) Членов семьи нужно перечислить через запятую.
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
"""

# family_1 = input("Перечислите через запятую имена членов первой семьи: \n").split(',')
# family_2 = input("Перечислите через запятую имена членов второй семьи: \n").split(',')

# family_1_members = len(family_1)
# family_2_members = len(family_2)
# print(f"В первой семье {family_1_members} чл.")
# print(f"Во второй семье {family_2_members} чл.")
# if family_1_members > family_2_members:
#     print("Первая семья больше. The first family is the biggest")
# elif family_2_members > family_1_members:
#     print("Вторая семья больше. The second family is the biggest")
# else:
#     print("Семьи равны. Equal")

# print("Equal" if len(family_1) == len(family_2) else family_2 if len(family_2) > len(family_1) else family_1)

"""
3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. 
    В значения можете передать информацию
    о вашем любимом фильме.
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение
"""

film = {
    "title": "Небо",
    "director": "Игорь Копылов",
    "year": "2021",
    "budget": "1000000",
    "main_actor": "Игорь Петренко",
    "slogan": "...Не изменяй себе!"
}


for key in film.keys():
    print(key)


for value in film.values():
    print(value)


for key, value in film.items():
    print(key, ':', value)


"""
3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
"""

# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))

"""
3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
"""

# i = [1, 2, 3, 4, 5, 3, 2, 1]
# print(list(set(i)))

# new_list = set([1, 2, 3, 4, 5, 3, 2, 1])
# print(new_list)

"""
3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга
"""
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# print(set1.issubset(set2))
# print(set2.issubset(set1))
