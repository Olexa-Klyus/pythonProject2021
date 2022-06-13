# comment
# '''comment'''
# """comment"""

#
# print('hello world')
#
# print(1, 2, 3, sep='__', end='\nFinich\n')

#  примітивні змінні
# i = 3
# f = 1.2
# b = True
#
# # нічого
# n = None
#
# print(type(i))
# print(type(f))
# print(type(b))
#
# print(float(i))

# присвоєння
# a = b = c = 10
# print(a, b, c)
#
# a = 5
# b = 2
# print(a + b)
# print(a - b)
# print(a * b)
#
# # ділення float
# print(a / b)
#
# # ділення int
# print(a // b)
#
# print(round(a / b, 1))
#
# # щось незрозуміле показував
# print(int(2.2 + 0.5))
#
# # ділення по залишку
# print(a % b)
# # степінь
# print(a ** b)
#
# s = input('enter num: ')
# print('input', s)

# input повертає стрінг


# все пусте - масиви обєкти - все false

# a = 5
# b = 2
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# print(a == b)
# print(a != b)
#
# print(not True)
#
# # порівняти типи даних
# print(isinstance('string', str))
#
# -----------------------------------------------
# num = input('num :')
# if num == '5':
#     print(True)
# elif num == "8" or num == '18':
#     print(8)
# else:
#     print('some')

# -----------------------------------------------
# тернарка
# res = 'yes' if num > 5 else 'no'

# # список
# # list
# l = [1, 2, 3, 4]
# print(l[2])
# # можна йти з кінця
# print(l[-1])
#
# l[0] = 555
#
# del l[3]
# # довжина масиву- len(l)
# print(len(l))
#
# # копія масиву
# a = l.copy()
#
# # якщо порівнювати масиви за значеннями
# print(a == l)
# # за посиланням на комірку памяті
# print(a is l)
# print(a is not l)


# -----------------------------------------------
# методи

# lst = [2, 23, 5, 4, 6]
#
# lst.append(15)
# lst.insert(1, 555)
# # вирізає і повертає останнє значення або по індексу
# print(lst.pop())
# print(lst.pop(0))
#
# # видаляє 1 знайдений елемент по значенню
# lst.remove(555)
#
# # розширити список - додає в кінець
# lst.extend([5, 5, 5])
# lst = lst + [0, 4, 2]
# lst += [8]
#
# # знайти індекс по значенню
# print(lst.index(2, 2))
#
# # розвернути сотрувати
# lst.reverse()
# lst.sort(reverse=True)
#
# # повернути кількість однакових елементів
# print(lst.count(44))
# # очистити
# # lst.clear()
#
# # зріз від 0 ел до 3 з кроком 2
# l = lst[0:3:2]
# або кожний другий з кінця
# l = lst[::-2]

# print(l)

# print(lst)

# -----------------------------------------------

# tuple кортеж
