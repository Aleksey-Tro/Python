"""
Задача №44.
В списке хранятся числа. Нужно выбрать только четные числа и
составить список пар из этих чисел(число; квадрат числа).
"""

# Первое решение
# from random import randint


# list_1 = [randint(2, 20) for i in range(10)]
# list_2 = list()

# print(list_1)

# for i in list_1:
#    if i % 2 == 0:
#       list_2.append([i, i**2])

# print(list_2)


# Второе решение
# from random import randint


# def select(f, col):
#    return [f(x) for x in col]

# def where(f, col):
#    return [x for x in col if f(x)]

# list_1 = [randint(2, 20) for i in range(10)]
# list_2 = select(int, list_1)
# list_2 = where(lambda x: x % 2 == 0, list_2)
# list_2 = list(select(lambda x: [x, x**2], list_2))

# print(list_2)