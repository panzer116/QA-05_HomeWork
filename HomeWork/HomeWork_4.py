from my_calc import *

"""
4.1.Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3
    значения(с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
"""

# def square(x):
#     return x * 4, x ** 2, (2 * x ** 2) ** 0.5,
#
#
# result = square(int(input("Введите значение стороны квадрата: ")))
# print(result)


"""
4.2.Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит
    их построчно в формате аргумент: значение.Например:
    name: John
    last_name: Smith
    age: 35
    position: web
    developer
"""

# def fn(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ':', value)
#
#
# fn(name="John", last_name='Smith', age=35, position='web')

"""
4.3.Используя лямбда - выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый
    список, содержащий только положительные числа 
"""

# my_list = [20, -3, 15, 2, -1, -21]
# func = list(filter(lambda x: x > 0, my_list))
# print(func)

"""
4.4.Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
"""

# my_list = [20, -3, 15, 2, -1, -21]
#
# from functools import reduce
#
# res = reduce(lambda x, y: x * y, my_list)
# print(res)

"""
4.5.Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические
    вычисления. Примените эти функции в качестве методов в другом файле. 
"""

x = 10
y = 22.5
sign = '*'

if sign in ['+', '-', '/', '*']:
    print(my_calc(x=x, y=y, sign=sign))
else:
    print("Incorrect operation")

"""(Здесь нужно будет прописать обработку исключения - что делать в случае 
появления ислючения)"""

"""Вариант 1"""

# def sum_it(**kwargs):
#     print(type(kwargs))
#     result = 0
#     for i in kwargs.values():
#         result += i
#     # return result
#     return sum(kwargs.values())
#
#
# print(sum_it(num1=4, num2=5, num3=10))

"""Вариант 2"""

# def sum_i(*args):
#     print(type(args))
#     return sum(args)
#
#
# print(sum_i(5, 6, 12))
#
# list_2 = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x*x, list_2)))
# print([x*x for x in list_2])
