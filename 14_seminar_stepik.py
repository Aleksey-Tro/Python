"""
Задача №92.
На вход программе подается натуральное число n, а затем n строк.
Напишите программу, которая создает из указанных строк список и
выводит его.
Формат входных данных:
На вход программе подаются натуральное число n, а затем n строк,
каждая на отдельной строке.
Формат выходных данных:
Программа должна вывести список состоящий из указанных строк.
"""

# list_1 = []

# for _ in range(int(input())):
#    list_1.append(input())

# print(list_1)



"""
Задача №93.
Напишите программу, выводящую следующий список:
['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
Формат выходных данных
Программа должна вывести указанный список.
Примечание. Последний элемент списка состоит из 26 символов z.
"""

# list_1 = list()

# for i in range(1, 27):
#    list_1.append((chr(ord('a') + i -1) * i))

# print(list_1)



"""
Задача №94.
На вход программе подается натуральное число n, а затем n целых чисел.
Напишите программу, которая создает из указанных чисел список их кубов.
Формат входных данных:
На вход программе подаются натуральное число n, а затем n целых чисел,
каждое на отдельной строке.
Формат выходных данных:
Программа должна вывести список, состоящий из кубов указанных чисел.
"""

# print([int(input()) ** 3 for i in range(1, int(input()) + 1)])



# list_1 = []

# for i in range(int(input())):
#    list_1.append(int(input()) ** 3)

# print(list_1)



"""
Задача №95.
На вход программе подается натуральное число n. Напишите программу,
которая создает список, состоящий из делителей введенного числа.
Формат входных данных:
На вход программе подается натуральное число n.
Формат выходных данных:
Программа должна вывести список, состоящий из делителей введенного
числа.
"""

# n = int(input()); print([i for i in range(1, n + 1) if n % i == 0])



# n = int(input())
# list_1 = []

# for i in range(1, n + 1):
#    if n % i == 0:
#       list_1.append(i)

# print(list_1)



"""
Задача №96.
На вход программе подается натуральное число n ≥ 2, а затем n целых
чисел. Напишите программу, которая создает из указанных чисел список,
состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).
Формат входных данных
На вход программе подаются натуральное число n, а затем n целых чисел,
каждое на отдельной строке.
Формат выходных данных
Программа должна вывести список, состоящий из сумм соседних чисел.
"""

# list_1 = []
# n = 0

# for i in range(int(input())):
#    temp = n
#    n = int(input())
#    if i > 0:
#       list_1.append(n + temp)

# print(list_1)



# l = [int(input()) for _ in range(int(input()))]
# print([l[i] + l[i + 1] for i in range(len(l) - 1)])



"""
Задача №97.
На вход программе подается натуральное число n, а затем n целых чисел.
Напишите программу, которая создает из указанных чисел список, затем
удаляет все элементы стоящие по нечетным индексам, а затем выводит
полученный список.
Формат входных данных:
На вход программе подаются натуральное число n, а затем n целых чисел,
каждое на отдельной строке.
Формат выходных данных:
Программа должна вывести список в соответствии с условием задачи.
Примечание. Используйте оператор del.
"""

# list_1 = [int(input()) for _ in range(int(input()))]

# del list_1[1::2]

# print(list_1)



# print([int(input()) for _ in range(int(input()))][::2])



"""
Задача №97.
На вход программе подается натуральное число n и n строк, а затем число k.
Напишите программу, которая выводит k-ую букву из введенных строк на одной
строке без пробелов.
Формат входных данных:
На вход программе подается натуральное число n, далее n строк, каждая на
отдельной строке. В конце вводится натуральное число k – номер буквы
(нумерация начинается с единицы).
Формат выходных данных:
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Если некоторые строки слишком короткие, и в них нет символа с
заданным номером, то такие строки при выводе нужно игнорировать.
"""

# list_1 = [input() for _ in range(int(input()))]
# k = int(input()) - 1

# print(*[i[k] for i in list_1 if len(i) > k], sep = '')



# list_1 = []

# for _ in range(int(input())):
#     list_1.append(input())

# k = int(input())
# res = ""

# for i in range(len(list_1)):
#    if len(list_1[i]) > k:
#       res += list_1[i][k-1]

# print(res)



"""
Задача №98.
На вход программе подается натуральное число n, а затем n строк.
Напишите программу, которая создает список из символов всех строк,
а затем выводит его.
Формат входных данных:
На вход программе подаются натуральное число n, а затем n строк,
каждая на отдельной строке.
Формат выходных данных:
Программа должна вывести список состоящий из символов всех введенных строк.
Примечание. В результирующем списке могут содержаться одинаковые символы.
"""

# list_1 = [input() for _ in range(int(input()))]
# list_2 = []

# for i in list_1:
#    list_2.extend(i)

# print(list_2)



# list_1 = []
# for _ in range(int(input())):
#     list_1.extend(input())
# print(list_1)