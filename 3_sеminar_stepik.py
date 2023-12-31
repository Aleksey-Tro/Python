"""
Задача №12.
Задача 1. Даны три целых числа. Определите, сколько среди
них совпадающих. Программа должна вывести одно из чисел: 
3 (если все совпадают), 2 (если два совпадает) или 0 
(если все числа различны).
"""

# Первый способ
# a, b, c = int(input()), int(input()), int(input())

# if a == b:
#     if b == c:
#         print(3)
#     else:
#         print(2)
# else:
#     if a == c:
#         print(2)
#     else:
#         if b == c:
#             print(2)
#         else:
#             print(0)


# Второй способ
# a, b, c = int(input()), int(input()), int(input())

# if a == b == c:
#     print(3)
# elif a == b:
#     print(2)
# elif b == c:
#     print(2)
# elif a == c:
#     print(2)
# else:
#     print(0)


# Третий способ
# a, b, c = int(input()), int(input()), int(input())

# if a == b == c:
#     print(3)
# elif a == b or b == c or a == c:
#     print(2)
# else:
#     print(0)



"""
Задача №13.
Зум бросил вызов Флэшу и предложил ему честный поединок
в виде гонки вокруг магнетара. В случае проигрыша эта
нейтронная звезда зарядится и уничтожит мир, поэтому
Флэш решил не рисковать без причины и узнать у своего
друга Циско Рамона, есть ли смысл принимать вызов. Циско
получил данные, что скорость Зума равна n, а скорость
Флэша равна k. Напишите программу, которая должна вывести
ответ Циско на вопрос Флэша.
"""

# n = int(input())
# k = int(input())

# if n > k:
#    print('NO')
# elif k > n:
#    print('YES')
# else:
#    print("Don't know")



"""
Задача №14.
Напишите программу, которая принимает три положительных
числа и определяет вид треугольника, длины сторон которого
равны введенным числам. Программа должна вывести на экран
текст – вид треугольника («Равносторонний», «Равнобедренный»
или «Разносторонний»).
"""

# a = int(input())
# b = int(input())
# c = int(input())

# if a == b == c:
#    print('Равносторонний')
# elif a == b or b == c or a == c:
#    print('Равнобедренный')
# else:
#    print('Разносторонний')



"""
Задача №15.
Даны три различных целых числа. Напишите программу,
которая находит среднее по величине число.
"""

# n1 = int(input())
# n2 = int(input())
# n3 = int(input())

# if n1 > n2 > n3 or n1 < n2 < n3:
#    print(n2)
# elif n2 > n1 > n3 or n2 < n1 < n3:
#    print(n1)
# elif n1 > n3 > n2 or n1 < n3 < n2:
#    print(n3)



"""
Задача №16.
Дан порядковый номер месяца (1, 2, …, 12) (1,2,…, 12).
Напишите программу, которая выводит на экран количество
дней в этом месяце. Принять, что год является невисокосным.
"""

# n = int(input())

# if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
#    print('31')
# elif n == 2:
#    print('28')
# else:
#    print('30')



"""
Задача № 17.
Известен вес боксера-любителя (целое число). Известно, что
вес таков, что боксер может быть отнесён к одной из трех
весовых категорий:
Легкий вес – до 60
60 кг (невключительно);
Первый полусредний вес – до 64
64 кг (невключительно);
Полусредний вес – до 69
69 кг (невключительно).
Напишите программу, определяющую, в какой категории будет
выступать данный боксер.
"""

# n = int(input())

# if n < 60:
#    print('Легкий вес')
# elif 59 < n < 64:
#    print('Первый полусредний вес')
# elif 63 < n < 69:
#    print('Полусредний вес')



"""
Задача №18
Напишите программу, которая считывает с клавиатуры
два целых числа и строку. Если эта строка является
обозначением одной из четырёх математических операций
(+, -, *, /), то выведите результат применения этой
операции к введённым ранее числам, в противном случае
выведите «Неверная операция» (без кавычек). Если
пользователь захочет поделить на ноль, выведите текст
«На ноль делить нельзя!» (без кавычек).
"""

# a, b = int(input()), int(input())
# s = input()
# if s == '+':
#     print(a + b)
# elif s == '-':
#     print(a - b)
# elif s == '*':
#     print(a * b)
# elif s == '/':
#     if b == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(a / b)
# else:
#     print('Неверная операция')



"""
Задача №19.
Красный, синий и желтый называются основными цветами, потому что
их нельзя получить путем смешения других цветов. При смешивании
двух основных цветов получается вторичный цвет:

если смешать красный и синий, то получится фиолетовый;
если смешать красный и желтый, то получится оранжевый;
если смешать синий и желтый, то получится зеленый.

Напишите программу, которая считывает названия двух основных
цветов для смешивания. Если пользователь вводит что-нибудь помимо
названий «красный», «синий» или «желтый», то программа должна
вывести сообщение об ошибке. В противном случае программа должна
вывести название вторичного цвета, который получится в результате.
"""

# a = input()
# b = input()

# if (a == 'красный' or b == 'красный') and (a == 'синий' or b == 'синий'):
#    print('фиолетовый')
# elif (a == 'красный' or b == 'красный') and (a == 'желтый' or b == 'желтый'):
#    print('оранжевый')
# elif (a == 'синий' or b == 'синий') and (a == 'желтый' or b == 'желтый'):
#    print('зеленый')
# elif (a == 'синий' or a == 'красный' or a == 'желтый') and a == b:
#    print(a)
# else:
#    print('ошибка цвета')



"""
Задача №20.
На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены
цвета карманов: карман 0 зеленый;
для карманов с 1 по 10 карманы с нечетным номером имеют
красный цвет, карманы с четным номером – черный;
для карманов с 11 по 18 карманы с нечетным номером имеют
черный цвет, карманы с четным номером – красный;
для карманов с 19 по 28 карманы с нечетным номером имеют
красный цвет, карманы с четным номером – черный;
для карманов с 29 по 36 карманы с нечетным номером имеют
черный цвет, карманы с четным номером – красный.
Напишите программу, которая считывает номер кармана и показывает,
является ли этот карман зеленым, красным или черным. Программа
должна вывести сообщение об ошибке, если пользователь вводит
число, которое лежит вне диапазона от 0 до 36.
"""

# n = int(input())

# if n == 0:
#    print('зеленый')
# elif 1 <= n <= 10:
#    if n % 2 == 0:
#       print('черный')
#    else:
#       print('красный')
# elif 11 <= n <= 18:
#    if n % 2 == 0:
#       print('красный')
#    else:
#       print('черный')
# elif 19 <= n <= 28:
#    if n % 2 == 0:
#       print('черный')
#    else:
#       print('красный')
# elif 29 <= n <= 36:
#    if n % 2 == 0:
#       print('красный')
#    else:
#       print('черный')
# else:
#    print('ошибка ввода')



"""
Задача №21.
На числовой прямой даны два отрезка: [a1 ; b1] и [a2 ; b2].
Напишите программу, которая находит их пересечение.
Пересечением двух отрезков может быть:
отрезок;
точка;
пустое множество.
"""

# Первое решение
# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())

# if a1 > b2 or a2 > b1:
#    print('пустое множество')
# elif a1 < a2 and b2 < b1:
#    print(a2, b2)
# elif (a2 < a1 and b1 < b2) or (a1 == a2 and b1 == b2):
#    print(a1, b1)
# elif b1 == a2:
#    print(b1)
# elif b2 == a1:
#    print(b2)
# elif a1 < a2 and b1 == b2:
#    print(a2, b2)
# elif a2 < a1 and b1 == b2:
#    print(a1, b1)
# elif a1 < a2 and a2 < b1 and b1 < b2:
#    print(a2, b1)
# elif a2 < a1 and a1 < b2 and b2 < b1:
#    print(a1, b2)
# elif a1 == a2 and b1 < b2:
#    print(a1, b1)
# elif a1 == a2 and b2 < b1:
#    print(a1, b2)


# Второе решение
# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input()) 
# if min(b1, b2) < max(a1, a2): 
#     print('пустое множество')
# elif min(b1, b2) == max(a1, a2):
#     print(min(b1, b2))
# else:
#     print(max(a1, a2), min(b1, b2))