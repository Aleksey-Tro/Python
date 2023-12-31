"""
Задача №22.
Напишите программу, которая выводит слова «Python is awesome!»
(без кавычек) 10 раз.
Формат выходных данных:
Программа должна вывести 10 раз текст «Python is awesome!»,
каждый на отдельной строке.
"""

# for i in range(10):
#    print('Python is awesome!')



"""
Задача №23.
Дано предложение и количество раз которое его надо повторить.
Напишите программу, которая повторяет данное предложение нужное
количество раз.
Формат входных данных:
В первой строке записано текстовое предложение, во второй —
количество повторений.
Формат выходных данных:
Программа должна вывести указанное текстовое предложение нужное
количество раз. Каждое повторение должно начинаться с новой строки.
"""

# string = input()
# n = int(input())

# for i in range(n):
#    print(string)



"""
Задача №24.
Напишите программу, которая использует ровно три цикла for для
печати последовательности символов.
"""

# for i in range(3):
#    print('AAA')
#    print('AAA')

# for i in range(5):
#    print('BBBB')

# print('E')

# for i in range(9):
#    print('TTTTT')

# print('G')



"""
Задача №25.
Напишите программу, которая печатает звездный прямоугольник
размерами n x 19.
Формат входных данных:
На вход программе подаётся натуральное число n ∈ [1;20] —
высота звездного прямоугольника.
Формат выходных данных:
Программа должна вывести звездный прямоугольник размерами n x 19.
Подсказка. Для печати звездной линии используйте умножение строки
на число.
"""

# n = int(input())
# string = '*'

# for i in range(n):
#    print(string * 19)



"""
Задача №26.
Напишите программу, которая считывает одну строку текста
и выводит 10 строк, пронумерованных от 0 до 9, каждая с
указанной строкой текста.
Формат входных данных:
На вход программе подается одна строка текста.
Формат выходных данных:
Программа должна вывести десять строк в соответствии с
условием задачи.
"""

# string = input()

# for i in range(10):
#    print(i, string)



"""
Задача №27.
На вход программе подается натуральное число n. Напишите
программу, которая для каждого из чисел от 0 до n (включительно)
выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).
Формат входных данных:
На вход программе подается натуральное число n.
Формат выходных данных:
Программа должна вывести текст в соответствии с условием задачи.
"""

# n = int(input())

# for i in range(n + 1):
#    print('Квадрат числа', i, 'равен', i ** 2)



"""
Задача №28.
На вход программе подается натуральное число n(n≥2) – катет
прямоугольного равнобедренного треугольника. Напишите программу,
которая выводит звездный треугольник в соответствии с примером.
Формат входных данных:
На вход программе подается одно натуральное число n(n≥2).
Формат выходных данных:
Программа должна вывести треугольник в соответствии с условием
задачи.На вход программе подается натуральное число n(n≥2) –
катет прямоугольного равнобедренного треугольника.
"""

# n = int(input())

# for i in range(-n, 0):
#    print('*' * abs(i))


"""
Задача №29.
На вход программе подается три натуральных числа m,p,n:
m: стартовое количество организмов;
p: среднесуточное увеличение в %;
n: количество дней для размножения.
Напишите программу, которая предсказывает размер популяции
организмов. Программа должна выводить размер популяции в
каждый день, начиная с 1 и заканчивая n-м днем.
Формат входных данных:
На вход программе подается три натуральных числа.
Формат выходных данных:
Программа должна вывести текст в соответствии с условием задачи.
"""

# m = int(input())
# p = int(input())
# n = int(input())

# for i in range(n):
#    print(i + 1, m)
#    m = m + m * (p / 100)



"""
Задача №30.
Даны два целых числа (m ≤ n). Напишите программу, которая
выводит все целые числа от m до n включительно.
Формат входных данных:
На вход программе подаются два целых числа m и n, каждое на
отдельной строке.
Формат выходных данных:
Программа должна вывести числа в соответствии с условием задачи.
"""

# m = int(input())
# n = int(input())

# for i in range(m, n + 1):
#    print(i)



"""
Задача №31.
Даны два целых числа m и n. Напишите программу, которая
выводит все целые числа от m до n включительно в порядке
возрастания, если m < n, или в порядке убывания в противном
случае.
Формат входных данных:
На вход программе подаются два целых числа m и n, каждое на
отдельной строке.
Формат выходных данных:
Программа должна вывести числа в соответствии с условием задачи.
"""

# m = int(input())
# n = int(input())

# if n < m:
#    for i in range(m, n - 1, -1):
#       print(i)
# elif m <= n:
#    for i in range(m, n + 1):
#       print(i)



"""
Задача №32.
Даны два целых числа (m > n). Напишите программу, которая
выводит все нечетные целые числа от m до n включительно в
порядке убывания.
Формат входных данных:
На вход программе подаются два целых числа m и n, каждое
на отдельной строке.
Формат выходных данных:
Программа должна вывести числа в соответствии с условием задачи.
Примечание. Попробуйте решить задачу двумя способами: с
использованием условного оператора if и без него.
"""

# m, n= int(input()), int(input())

# for i in range(m, n - 1, -1):
#    if i % 2 == 1:
#       print(i)

# m = ((m - 1) // 2) * 2 + 1

# for i in range(m, n - 1, -2):
#    print(i)



"""
Задача №33.
Даны два натуральных числа m и n (m ≤ n). Напишите программу,
которая выводит все целые числа от m до n включительно,
удовлетворяющие хотя бы одному из условий:
число кратно 17;
число оканчивается на 9;
число кратно 3 и 5 одновременно.
Формат входных данных:
На вход программе подаются два натуральных числа (m ≤ n),
каждое на отдельной строке.
Формат выходных данных:
Программа должна вывести числа в соответствии с условием задачи.
Примечание. Если нет чисел, удовлетворяющих условию, выводить ничего не надо.
"""

# m, n= int(input()), int(input())

# for i in range(m, n + 1):
#    if i % 17 == 0 or i % 10 == 9 or i % 3 == 0 and i % 5 == 0:
#       print(i)



"""
Задача №34.
Дано натуральное число n. Напишите программу, которая выводит
таблицу умножения на n (от 1 до 10 включительно).
Формат входных данных:
На вход программе подается натуральное число.
Формат выходных данных:
Программа должна вывести таблицу умножения на введенное число.
Примечание. В качестве знака умножения используйте английскую букву x.
"""

# n = int(input())

# for i in range(11):
#    print(n, 'x', i, '=', n * i)