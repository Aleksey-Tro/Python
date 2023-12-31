"""
Задача №68.
Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу
размером n * 3, состоящую из данного числа (числа отделены одним пробелом).
Формат входных данных:
На вход программе подается одно натуральное число.
Формат выходных данных:
Программа должна вывести таблицу размером n * 3, состоящую из данного числа.
Примечание. В конце строки может быть пробел.
"""

# n = int(input())

# for i in range(n): 
#     for j in range(3):
#         print(n, end = ' ')
#     print()


# for i in range(n): print(n, n, n)



"""
Задача №69.
Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу
размером n * 5, где в i-ой строке указано число i (числа отделены одним пробелом).
Формат входных данных:
На вход программе подается одно натуральное число.
Формат выходных данных:
Программа должна вывести таблицу размером n * 5 в соответствии с условием.
Примечание. В конце строки может быть пробел.
"""

# for i in range(1, int(input()) + 1): print(i, i, i, i, i)



"""
Задача №70.
Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу
сложения для всех чисел от 1 до n (включительно) в соответствии с примером.
Формат входных данных:
На вход программе подается одно натуральное число.
Формат выходных данных:
Программа должна вывести таблицу сложения для всех чисел от 1 до n.
Примечание 1. Таблицу сложения подразумеваем от 1 до 9 (включительно).
Примечание 2. В конце строки может быть пробел.
"""

# for i in range(1, int(input()) + 1):
#     for j in range(1, 10): print(i, '+', j, '=', i + j)
#     print()



"""
Задача №71.
Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный
звездный треугольник с основанием, равным n в соответствии с примером:
Формат входных данных:
На вход программе подается одно нечетное натуральное число.
Формат выходных данных:
Программа должна вывести треугольник в соответствии с условием.
Примечание. Используйте вложенный цикл for.
"""

# n = int(input())

# for i in range(1, n//2+2):
#     print('*' * i)

# for i in range(n//2, 0, -1):
#     print('*' * i)


# n = int(input())

# for i in range(n):
#     cur_cnt = (n // 2 + 1) - abs(n // 2 - i)
#     print(cur_cnt * "*")


# n = int(input())

# for i in range(n):
#     cur_cnt = (n // 2 + 1) - abs(n // 2 - i)
#     for j in range(cur_cnt):
#         print("*", end="")
#     print()



"""
Задача №72.
Дано натуральное число n. Напишите программу, которая печатает численный треугольник
в соответствии с примером:
Формат входных данных:
На вход программе подается одно натуральное число.
Формат выходных данных:
Программа должна вывести треугольник в соответствии с условием.
Примечание. Используйте вложенный цикл for.
"""

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(i): print(i, end = '')
#     print()