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

# -----------------------------------------------------------------

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
# @decor_counter
# def greeting2(name, age):
#     print(f'Hello,{name}, I`m {age}')
#
#
# greeting3('jkjjj', 18)
# greeting3('jkjjj', 8)
# greeting3('jkjjj', 28)
# greeting2('jOOOj', 15)
# greeting3('jkjjj', 11)


# або записати по іншому
# func1 = decor_counter(greeting3, 10)
# func1('11', 33)
# func1('11', 33)
# func1('11', 33)
# func1('11', 33)

# ------------------------------------------------------------------
# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)

# def summa1(num1: int):
#     res_str = ''
#     l = list(str(num1))
#     for v, i in enumerate(l):
#         if i != '0':
#             # res_str = res_str + str(int(i) * 10 ** (len(l) - v - 1))
#             res_str = res_str + i + '0' * (len(l) - v - 1)
#             if len(l) - v > 1:
#                 res_str = res_str + ' + '
#     return res_str
#
#
# print(summa1(34005))

# ------------------------------------------------------------------

# сделайте функцию на замыкания которая будет возвращать декоратор который будет считать общее количество
# запущенных  функций декорированных этим декоратором

# count_all = 0
#
# def decor(func):
#     count = 0
#
#     def in_func():
#         global count_all
#         nonlocal count
#         count_all += 1
#         count += 1
#         func()
#         print(f'декоратор відпрацював {count_all} разів')
#         print(f'функція {func.__name__} відпрацювала {count} разів')
#
#         return count
#
#     return in_func
#
# @decor
# def func1():
#     print('func1')
#
# @decor
# def func2():
#     print('func2')
#
# func1()
# func2()
# func2()

# ------------------------------------------------------------------

# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)


# def fibonachi(count):
#     fibonachi_li = [1 for i in range(count)]
#
#     for i in range(count):
#         if i > 1:
#             fibonachi_li[i] = fibonachi_li[i-1]+fibonachi_li[i-2]
#     return fibonachi_li
#
#
# print(fibonachi(10))

# ------------------------------------------------------------------
