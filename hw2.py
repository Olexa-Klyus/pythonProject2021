# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи

# def notebook(*get):
#     todo_list = ['hhh']
#
#     def add_todo(todo):
#         nonlocal todo_list
#         todo_list.append(todo)
#         print(todo_list)
#
#         def get_all():
#             nonlocal todo_list
#             print(todo_list)
#             return todo_list
#
#         if not get:
#             get_all()
#
#     return add_todo
#
#
# todo_add = notebook()
# todo_add('7-00 підйом')
# todo_add('8-00 сніданок')
# todo_add('9-00 навчання')
# todo_add('12-00 обід')
# todo_add('17-00 вечеря')
#
# todo_add = notebook(1)
# print(todo_add)

# def decor_counter(func_in, count=0):
#     def counter(*args, **kwargs):
#         nonlocal count
#         count += 1
#         func_in(*args, **kwargs)
#         print(f'функція виконалась, {count} ,разів')
#
#     return counter
#
#
# @decor_counter
# def greeting3(name, age):
#     print(f'Hello,{name}, I`m {age}')
#
#
# greeting3('jkjjj', 18)
# greeting3('jkjjj', 8)
# greeting3('jkjjj', 28)

# або записати по іншому
# func1 = decor_counter(greeting3, 10)
# func1('11', 33)
# func1('11', 33)
# func1('11', 33)
# func1('11', 33)


def summa1(num1: int):
    res_str = ''
    l = list(str(num1))
    for v, i in enumerate(l):
        if i != '0':
            res_str = res_str + str(int(i) * 10 ** (len(l) - v - 1))
            if len(l) - v > 1:
                res_str = res_str + ' + '
    return res_str


print(summa1(34005))
