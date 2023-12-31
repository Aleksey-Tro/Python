"""
Задача №25.
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Кол-во повторов доболвяется к 
символам с помощью постфикса формата _n.
"""

# list_1 = str(input('Введите строку: ')).split()
# result = {}

# for el in list_1:
#    if el in result:
#       print(f'{el}_{result[el]}', end = ' ')
#       result[el] = result[el] + 1   # result[el] = result.get(el, 0) + 1
#    else:
#       print(el, end = ' ')
#       result[el] = 1



"""
Задача №26.
Даны два неупорядоченных набора целых чисел
(может быть, с повторениями). Выдать без повторений
в порядке возрастания все те числа, которые
встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через
пробел в виде строки. ! Писать input() не надо
"""

# var1 = '5 4' 
# var2 = '1 2 3'
# var3 = '1 2 3 4'

# var2 = var2.split()
# var3 = var3.split()
# var_res = set(var2).intersection(set(var3))

# print(*sorted(var_res))


"""
Задача №27.
Вользователь вводит текст(str). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одим или большим чисслом
пробелов. Определите, сколько различных слов 
содержится в этом тексте.
"""

# n = str(input('Введите строку: '))
# n1 = n.lower().replace('.', ' ').replace(',', ' ').split()

# print(len(set(n1)))




"""
Задача №28.
Урожайность черничных кустов представлена в
виде списка arr, где arr[i] - это урожайность
(количество ягод) i-го куста. В фермерском
хозяйстве внедрена система автоматического
сбора черники. Эта система состоит из управляющего
модуля и нескольких собирающих модулей. Каждый
собирающий модуль может собрать ягоды с одного
куста и с двух соседних кустов. Собирающий
модуль находится перед определенным кустом,
и он может выбирать, с какого куста начать
сбор ягод.
Ваша задача - написать программу, которая
определит максимальное число ягод, которое
может собрать один собирающий модуль за один
заход, находясь перед некоторым кустом грядки.
Входные данные:
На вход программе подается список arr, где
arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го
куста черники. Размер списка не превышает 1000 элементов.
Выходные данные:
Программа должна вывести одно целое число -
максимальное количество ягод, которое может
собрать собирающий модуль, находясь перед
некоторым кустом грядки.
"""

# # Первое решение
# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# result = arr[0] + arr[-1] + arr[-2]

# for i in range(len(arr)):
#    result1 = arr[i] + arr[i-1] + arr[i-2]
#    if result1 > result:
#       result = result1

# print(result)

# # Второе решение
# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])

# print(max(arr_count))