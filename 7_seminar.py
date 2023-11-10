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



"""
Задача №45.
Напишите функцию print_operation_table(operation, num_rows,
num_columns), которая принимает в качестве аргумента функцию,
вычисляющую элемент по номеру строки и столбца. Аргументы
num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет
с единицы (подумайте, почему не с нуля). Если строк меньше двух,
выдайте текст ОШИБКА! Размерности таблицы должны быть больше 2!.
"""

# def print_operation_table(operation, num_rows, num_columns):
#    if num_rows < 2 or num_columns < 2:
#       return print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#    for i in range(1, num_columns + 1):
#       print(i, end = ' ')
#    print()
#    for i in range(2, num_rows + 1):
#       print(i, end = ' ')
#       for j in range(2, num_columns + 1):
#          print(operation(i, j), end = ' ')
#       print()

# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         header = ' '.join([str(i) for i in range(1, num_columns + 1)])
#         print(header)
#         for i in range(2, num_rows + 1):
#             row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
#             print(' '.join(row))


# print_operation_table(lambda x, y: x / y, 4, 4)
# print_operation_table(lambda x, y: x * y, 1, 2)
# print_operation_table(lambda x, y: x - y, 5, 5)



"""
Задача №46.
Напишите функцию same_by(characterisric, objects), которая
проверяет, все ли объекты имеют одинаковое значение
=некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов отличается
то False. Для пустого набора объектовБ функция должна возвращать
True. Аргумент chfracteristic - это функция, которая принимает
объект и вычисляет его характеристику
"""

# values = [0, 2, 10, 6]

# def same_by(c, objects):
#    return len(objects) == len(list(filter(c, objects)))


# if same_by(lambda x: x % 2 == 0, values):
#    print('same')
# else:
#    print('different')



"""
Задание №47.
Винни-Пух попросил Вас посмотреть, есть ли в его стихах
ритм. Поскольку разобраться в его кричалках не настолько
просто, насколько легко он их придумывает, Вам стоит
написать программу. Винни-Пух считает, что ритм есть,
если число слогов (т.е. число гласных букв) в каждой
фразе стихотворения одинаковое. Фраза может состоять из
одного слова, если во фразе несколько слов, то они
разделяются дефисами. Фразы отделяются друг от друга
пробелами. Стихотворение  Винни-Пух передаст вам
автоматически в переменную stroka в виде строки. В ответе
напишите Парам пам-пам, если с ритмом все в порядке и Пам
парам, если с ритмом все не в порядке. Если фраза только
одна, то ритм определить не получится и необходимо
вывести: Количество фраз должно быть больше одной!.
"""

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

# vowels = ['а', 'у', 'е', 'ё', 'и', 'й', 'о', "ы", "э", "ю", "я"]
# phrases = stroka.split()

# if len(stroka) < 1:
#   print('Количество фраз должно быть больше одной!')
# else:
#   for i in phrases:
#     countVowels = []
#     count = 0
#     for j in i:
#       if j.lower() in vowels:
#         count += 1
#     countVowels.append(count)
#   if countVowels.count(countVowels[0]) == len(countVowels):
#       print('Парам пам-пам')
#   else:
#        print('Пам парам')


# if len(phrases) < 2:
#    print('Количество фраз должно быть больше одной!')
# else:
#     countVowels = []
#     for i in phrases:
#         countVowels.append(len([x for x in i if x.lower() in vowels]))
#     if countVowels.count(countVowels[0]) == len(countVowels):
#       print('Парам пам-пам')
#     else:
#        print('Пам парам')