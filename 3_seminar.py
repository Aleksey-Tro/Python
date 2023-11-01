"""
Задача №17.
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
"""

# Первое (решение самостоятельное)
# from random import randint

# n = int(input('Введи кол-во элементов списка: ')) 
# l = [0] * n
# res = int(0)

# l = [randint(0, 10) for i in range(len(l))]
# print(l)

# for i in range(11):
#    if l.count(i) >= 1:
#       res += 1

# print(res)


# Второе (решение перподователя)
# from random import randint

# n = int(input('Введи кол-во элементов списка: ')) 
# l = [0] * n
# l = [randint(0, 10) for i in range(len(l))]
# j = []

# print(l)

# for i in l:
#    if i not in j:
#       j.append(i)

# print(len(j))



# Третье (решение преподавателя Простое)

# from random import randint

# n = int(input('Введи кол-во элементов списка: ')) 
# l = [0] * n
# l = [randint(0, 10) for i in range(len(l))]

# print(l)

# print(len(set(l)))



"""
Задача №18.
Требуется вычислить, сколько раз встречается
некоторое число k в массиве list_1.
Найдите количество и выведите его.
"""

# list_1 = [1, 3, 3, 4, 5]
# k = 3

# print(list_1.count(k))



"""
Задача №19.
Дана последовательность из N целых числе и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов впаво, K -
положительное число.
"""

# from random import randint

# n = int(input('Введите размерность массива: '))
# k = int(input('Введите k: '))
# a = [0] * n
# a = [randint(0, 10) for i in range(len(a))]

# print(a)

# a = a[-k:] + a[:-k]

# print(a)



"""
Задача №20.
Требуется найти в массиве list_1 самый близкий по
величине элемент к заданному числу k и вывести его.
"""

# Первое решение
# list_1 = [1, 2, 3, 4, 5]
# k = 6

# m = min(list_1, key=lambda x: abs(x-k))

# print(m)


# Второе решение
# list_1 = [1, 2, 3, 4, 5]
# k = 6

# m = abs(k - list_1[0])  
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

# Третье решение
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# c =[]

# for i in list_1:
#    c.append(abs(k-i))
# d=c.index(min(c))
# print(list_1[d])



"""
Задача №21.
Напишите программу для печати всех уникальных 
значений в словаре.
[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
{"VIII" : "S007"}]
Значения данны изначально.
"""

# Первое (решение самостоятельно)
# d = [{'V': "S001"}, {'V': "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {"V": " S009 "}, {"VIII" : " S007 "}]
# s = set()

# for i in d:
#    for j in i.values():
#       s.add(j)

# print(s)



# Второе (решение преподователя)

# d = [{'V': "S001"}, {'V': "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {"V": " S009 "}, {"VIII" : " S007 "}]
# s = set()

# for i in d:
#    for j in i.values():
#       s.add(j)

# print(s)



"""
В настольной игре Скрабл (Scrabble) каждая буква
имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.

А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного
пользователем слова k и выводит его. Будем считать, что на
вход подается только одно слово, которое содержит либо
только английские, либо только русские буквы.
"""

# k = input('Введите слово: ').lower()
# eng = 'AEIOULNSTRDGBCMPFHVWYKJZQZ'
# points_en = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JX', 10:'QZ'}
# points_ru = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}
# res = 0
# eng = eng.lower()

# if k[0] in eng:
#    for letter in k:
#       print(letter)
#       for key, value in points_en.items():
#          if letter in value.lower():
#             print(value.lower())
#             print(key)
#             res += key
# else:
#    for letter in k:
#       for key, value in points_ru.items():
#          if letter in value.lower():
#             res += key

# print((res))


# if k[0] in eng:
#    res = [key for letter in k for key, value in points_en.items() if letter in value]
# else:
#    res = [rey for letter in k for key, value in points_ru.items() if letter in value]

# print(sum(res))