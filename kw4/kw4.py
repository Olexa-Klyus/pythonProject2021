# есть вот такой файл с email, ваша задача записать в новый текстовый файл только почты от gmail.com

FILE = 'emails.txt'
RES_FILE = 'res_emails.txt'

try:
    with open(FILE) as file, open(RES_FILE, 'a') as res_file:
        for line in file:
            # сплітуємо по пробілу файл, забираємо останній елемент
            email = line.split()[-1]
            if email.endswith('@gmail.com'):
                # res_file.write(f'{email}\n')
                # або через print
                print(email, file=res_file)
except Exception as err:
    print(err)

# 2) для хранения и чтения данных использовать файлы
#
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты


import json
from typing import TypedDict

NoteType = TypedDict('NoteBook', {'purchase': str, 'price': int})


class Note:
    # конструктор приймає file_name
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__notes: list[NoteType] = []
        # як тільки буде створюватися екземпляр класу, відразу буде читатися файл
        # якщо файлу нема то помилка не впаде
        try:
            with open(file_name) as file:
                self.__notes: list[NoteType] = json.load(file)

        except:
            pass

    # створюємо методи класу
    def add(self):
        try:
            with open(self.__file_name, 'w') as file:
                purchase = input('введіть назву товару: ')
                price = ''
                while not price.isdigit():
                    price = input('введіть ціну товару: ')
                self.__notes.append({'purchase': purchase, 'price': int(price)})
                json.dump(self.__notes, file)
        except:
            print('щось пішло не так')

    def show_all(self):
        if not self.__notes:
            print('немає записів')
            return
        for item in self.__notes:
            print(item)

    def sum_of_costs(self):
        sum_costs = sum(item['price'] for item in self.__notes)
        print(f'{sum_costs=}')

    def most_expensive(self):
        print(max(self.__notes, key=lambda item: item['price']))

    def find_by_name(self):
        find = input('введіть назву для пошуку: ')
        for item in self.__notes:
            if item['purchase'].lower() == find.lower():
                print(item)
                return
            print('не знайдено')


note = Note('purchases.json')
while True:
    print('1) Создать запись')
    print('2) Список все записей')
    print('3) Общая сумма всех покупок')
    print('4) Самая дорогая покупка')
    print('5) Поиск по названию покупки')
    print('9) Выход')
    print('_________________________________')

    choice=input('зробіть вибір: ')

    match choice:
        case '1':
            note.add()
        case '2':
            note.show_all()
        case '3':
            note.sum_of_costs()
        case '4':
            note.most_expensive()
        case '5':
            note.find_by_name()
        case '9':
            break

