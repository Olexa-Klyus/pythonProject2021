# l = ['a', 'b', 'c', 1, 2]


# for i in l:
#     print(i)
#
# for i in range (len(l)):
#     print(i)

# for i, v in enumerate(l):
#     print(i, v, sep='=')
#
# tuple1 = (1, 2, 3)
# print(tuple1)

# деструктуризація

# a, b, _, c, *_ = l
# print(a, b, c)
#
# # виводить список
# print(l)

# # розпаковує і виводить список
# print(*l)

# # розпаковує і оновлює список
# l = [*l, 33, 33, 33]
# print(l)
#
# розпаковує словник - тут не зрозуміло
# user = {
#     'name': 'oleg',
#     'age': 12
# }
# def func1(**kwargs):
#     return kwargs
#
#
# print(func1(**user))
# print(user)


# декоратори decorators
# передаємо нашу функцію в декоратор і там її виконуємо

# def greeting():
#     print('Hello')


#
# def decor(func_expl):
#     print('---------------------------')
#     func_expl()
#     print('---------------------------')
#
#
# decor(greeting)


# далі трохи ускладнюємо

# def decor(func_expl):
#     def inner():
#         print('---------------------------')
#         func_expl()
#         print('---------------------------')
#
#     return inner
#
#
# start = decor(greeting)
# # отримаємо подвійний декоратор
# start = decor(start)
# start()


# а якщо функція приймає аргументи

# def greeting2(name):
#     print(f'Hello,{name}')
#
#
# def greeting3(name, age):
#     print(f'Hello,{name}, I`m {age}')


# def decor(func_expl):
#     def inner(*args):
#         print('---------------------------')
#         func_expl(*args)
#         print('---------------------------')
#
#     return inner
#

# start = decor(greeting2)
# start('Max')
# # тобто ще так записав - теж працює
# # decor(greeting2)('Max')
#
# start2 = decor(greeting3)
# start2('Alex', 15)
# Або
# decor(greeting3)('Alex', 15)

# є спеціальна форма запису декорування
# @decor
# def greeting2(name):
#     print(f'Hello,{name}')
#
#
# @decor
# def greeting3(name, age):
#     print(f'Hello,{name}, I`m {age}')
#
#
# greeting2('Oleg')
# greeting3('serg', 25)

# область видноти
# scope

# в пайтоні дані зберігаються в словниках - глобальному і локальних
# print(globals())
# print(locals())
#
# for i in range(10):
#     pass
#
# print(i)

# name = 'MAx'
#
#
# def a():
#     name = 'Vasyl'
#
#     def b():
#         # nonlocal name
#         # global name
#         name = "lola"
#         print(name)
#
#     b()
#     print(name)
#
#
# a()
# print(name)
# якщо в підфункції є така сама змінна, то створюється нова локальна
# якщо не створюється - то прога бере з батьківського рівня
# nonlocal означає що ми хочемо користуватися змінною з батьківського рівня
# global - робота з глобальною змінною

# closure
# Замикання - внутрішня функція , берe значення змінної з зовнішньої функції,
# і повертається за посиланням(без виконання)




def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


print(counter())
count1 = counter()
# count2 = counter()
#
print(count1())
print(count1())
# print(count2())
# print(count1())
# print(count2())

# lambda function

# lambda використовується як колись колбек в JS

# l.map(value>=value+2) було
# m = map(lambda value: str(value) + '2', l)
# for i in m:
#     print(i)
