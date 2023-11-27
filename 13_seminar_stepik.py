"""
Задача №84.
На вход программе подается строка текста, состоящая из слов, разделенных
ровно одним пробелом. Напишите программу, которая подсчитывает количество
слов в ней.
Формат входных данных:
На вход программе подается строка текста.
Формат выходных данных:
Программа должна вывести количество слов.
Примечание 1. Строка текста не содержит пробелов в начале и конце.
Примечание 2. Используйте для решения задачи метод count.
"""

# print(input().count(' ') + 1)



"""
Задача №85.
На вход программе подается строка генетического кода, состоящая
из букв А (аденин), Г (гуанин), Ц (цитозин), Т (тимин). Напишите
программу, которая подсчитывает сколько аденина, гуанина, цитозина
и тимина входит в данную строку генетического кода.
Формат входных данных:
На вход программе подается строка генетического кода, состоящая из
символов А, Г, Ц, Т, а, г, ц, т.
Формат выходных данных:
Программа должна вывести сколько гуанина, тимина, цитозина, аденина
входит в данную строку генетического кода.
Примечание. Строка не содержит символов, кроме как
А, Г, Ц, Т, а, г, ц, т.
"""

# s = input()

# print('Аденин: ', s.lower().count('а'), '\n',
#       'Гуанин: ', s.lower().count('г'), '\n', 
#       'Цитозин: ', s.lower().count('ц'), '\n',
#       'Тимин: ', s.lower().count('т'), sep = '')



"""
Задача №86.
Джим Хоппер с помощью радиоприемника пытается получить сообщение Оди.
На приемник ему поступает n различных последовательностей кода Морзе.
Декодировав их, он получает последовательности из цифр и букв строчного
латинского алфавита, при этом во всех сообщениях Оди содержится число 11,
причем минимум 3 раза. Помогите определить Джиму количество сообщений от Оди.
Формат входных данных:
В первой строке подаётся число n – количество сообщений, в последующих
n строках вводятся строки, содержащие латинские строчные буквы и цифры.
Формат выходных данных:
Программа должна вывести количество строк в которых содержится число 11
минимум 3 раза.
Примечание: Числа 11 необязательно должны быть разделены другими символами,
нужно подсчитать вхождение последовательности символов " 11" т.е. например
в строке " 111" содержится одна такая последовательность, в то время как в
"1111" их уже две.
"""

# n = int(input())
# total = 0

# for i in range(n):
#    s = input()
#    if s.count('11') >= 3:
#       total += 1

# print(total)



"""
Задача №87.
На вход программе подается строка текста. Напишите программу, которая
подсчитывает количество цифр в данной строке.
Формат входных данных:
На вход программе подается строка текста.
Формат выходных данных:
Программа должна вывести количество цифр в данной строке.
"""

# total = 0

# for i in input():
#    if i in '1234567890':
#       total += 1

# print(total)



# print(sum(1 for i in input() if i in '1234567890'))



# text = input()
# cnt = 0

# for i in range(10):
#     cnt += text.count(str(i))

# print(cnt)



"""
Задача №88.
На вход программе подается строка текста. Напишите программу, которая
проверяет, что строка заканчивается подстрокой .com или .ru.
Формат входных данных:
На вход программе подается строка текста.
Формат выходных данных:
Программа должна вывести «YES» если введенная строка заканчивается
подстрокой .com или .ru и «NO» в противном случае.
"""

# s = input()

# print('YES' if s.endswith('.com') or s.endswith('.ru') else 'NO')



"""
Задача №89.
На вход программе подается строка текста. Напишите программу, которая
выводит на экран символ, который появляется наиболее часто.
Формат входных данных:
На вход программе подается строка текста. Текст может содержать
строчные и заглавные буквы английского и русского алфавита, а также цифры.
Формат выходных данных:
Программа должна вывести символ, который появляется наиболее часто.
Примечание 1. Если таких символов несколько, следует вывести последний
по порядку символ.
Примечание 2. Следует различать заглавные и строчные буквы, а также буквы
русского и английского алфавита.
"""

# s = input()
# max_1 = 0
# res = ''

# for i in set(s):
#    if s.count(i) > max_1:
#       max_1 = s.count(i)
#       res = i

# print(res)



"""
Задача №90.
На вход программе подается строка текста. Если в этой строке буква
«f» встречается только один раз, выведите её индекс. Если она
встречается два и более раз, выведите индекс её первого и последнего
вхождения на одной строке, разделенных символом пробела. Если буква
«f» в данной строке не встречается, следует вывести «NO».
Формат входных данных:
На вход программе подается строка текста.
Формат выходных данных:
Программа должна вывести текст в соответствии с условием задачи.
"""

# s = input()

# if s.count('f') > 1:
#    print(s.startswith('f'), s.endswith('f'))
# elif s.count('f') == 1:
#    print(s.startswith('f'))
# else:
#    print('NO')



"""
Задача №91.
На вход программе подается строка текста, в которой буква «h»
встречается минимум два раза. Напишите программу, которая удаляет
из этой строки первое и последнее вхождение буквы «h», а также
все символы, находящиеся между ними.
Формат входных данных:
На вход программе подается строка текста.
Формат выходных данных:
Программа должна вывести текст в соответствии с условием задачи.
"""

# s = input()

# print(s[:s.find('h')] + s[s.rfind('h') + 1:])