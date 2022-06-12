# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи

def notebook():
    todo_list = []

    def add_todo(todo):
        nonlocal todo_list
        todo_list.append(todo)
        print(todo_list)

    # def get_all():
    #     nonlocal todo_list
    #     return todo_list
    #     pass

    return add_todo


todo1 = notebook()
todo1('7-00 підйом')
todo1('8-00 сніданок')
todo1('9-00 навчання')
todo1('12-00 обід')
todo1('17-00 вечеря')


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
