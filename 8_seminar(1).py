"""
Задача №51.
Создать телефонный справочник с возможностью импорта и экспорта
данных в формате .txt. Фамилия, имя, отчество, номер телефона -
данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска
определенной записи(например имя или фамилию человек)
4. Использование ффункций. Ваша программа не должна быть линейной
"""

# import os


# def work_with_phonebook():

#    choice = show_menu()
#    phone_book = read_csv('phonebook.csv')

#    while (choice != 7):
#       if choice == 1:
#          print_phone_book(phone_book)
#       elif choice == 2:
#          last_name = input('lastname ')
#          print(find_by(phone_book, last_name))
#       elif choice == 3:
#          last_name = input('lastname ')
#          new_number = input('new number ')
#          print(change_number(phone_book, last_name, new_number))
#       elif choice == 4:
#          last_name = input('lastname ')
#          print(delete_by_lastname(phone_book, last_name))
#       elif choice == 5:
#          number = input('number ')
#          print(find_by(phone_book, number))
#       elif choice == 6:
#          user_data = input('new data ')
#          add_user('phonebook.csv', phone_book, user_data)
#          write_csv('phonebook.csv', phone_book)
#       choice = show_menu()


# def print_phone_book(data):                             # 1. Распечатать справочник
#    for i in data:
#       print(i)


# def find_by(phone_book, last_name):                     # 2. Найти телефон по фамилии
#    flag = 1                                             # 5. Найти абонента по номеру телефона
#    for line in phone_book:
#       if str(last_name).lower() in str(line).lower():
#          flag = 0
#          print(line)
#    if flag == 1:
#       print('no name given')


# def change_number(phone_book, last_name, new_number):   # 3. Изменить номер телефона
#    flag = 1
#    for line in phone_book:
#       if str(last_name).lower() in str(line).lower():
#          flag = 0
#          line['Телефон'] = new_number
#    if flag == 1:
#       print('no name given')


# def delete_by_lastname(phone_book, last_name):          # 4. Удалить запись
#    flag = 1
#    for line in phone_book:
#       if str(last_name).lower() in str(line).lower():
#          flag = 0
#          del line['Фамилия']
#          del line['Имя']
#          del line['Телефон']
#          del line['Описание']
#    if flag == 1:
#       print('no name given')


# def show_menu():
#    print('1. Распечатать справочник'
#          '2. Найти телефон по фамилии'
#          '3. Изменить номер телефона'
#          '4. Удалить запись'
#          '5. Найти абонента по номеру телефона'
#          '6. Добавить абонента в справочник'
#          '7. Закончить работу', sep = '\n')
#    choice = int(input())
#    return choice


# def read_csv(filename):
#    phone_book = []
#    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
#    with open(filename, 'r', encoding = 'utf-8') as phb:
#       for i in phb:
#          record = dict(zip(fields, i.split(',')))
#          phone_book.append(record)
#    return phone_book


# def write_csv(filename, phone_book):
#    with open(filename, 'w', encoding = 'utf-8') as phout:
#       for i in range(len(phone_book)):
#          s = ''
#          for v in phone_book[i].values():
#             s += v + ','
#             phout.write(f'{s[:-1]}\n')


# work_with_phonebook()