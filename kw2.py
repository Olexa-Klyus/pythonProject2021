# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи

# можна ще по іншому типізувати, але в данеому випадку це не доцільно

# from typing import Callable
# def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:


# def notebook():
#     todo_list: list[str] = []
#
#     def add_todo(todo: str) -> None:
#         nonlocal todo_list
#         todo_list.append(todo)
#
#     def get_all() -> list[str]:
#         nonlocal todo_list
#         return todo_list
#
#     return add_todo, get_all
#
#
# todo_add, get_all = notebook()
#
# todo_add('7-00 підйом')
# todo_add('8-00 сніданок')
# todo_add('9-00 навчання')
# todo_add('12-00 обід')
# todo_add('17-00 вечеря')
#
# print(get_all())


# -----------------------------------------------------------------

# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)

# def summa1(n: int) -> str:
#     nums = list(str(n))
#     len_nums = len(nums) - 1
#     return ' + '.join([item + '0' * (len_nums - i) for i, item in enumerate(nums) if item != '0']) + f' = {n}'
#
#
# print(summa1(34005))


# -----------------------------------------------------------------
