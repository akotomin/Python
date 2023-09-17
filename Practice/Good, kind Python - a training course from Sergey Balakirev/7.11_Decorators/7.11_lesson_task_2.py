# Подвиг 2. На вход программы поступает строка с названиями пунктов меню, записанные в одну строчку через пробел.
# Необходимо задать функцию с именем get_menu, которая преобразует эту строку в список из слов и возвращает этот список.
# Сигнатура функции, следующая:
# def get_menu(s): ...
# Определите декоратор для этой функции с именем show_menu, который отображает список на экран в формате:
# 1. Пункт_1
# 2. Пункт_1
# ...
# N. Пункт_N
# Примените декоратор show_menu к функции get_menu, используя оператор @. Более ничего в программе делать не нужно.
# Сами функции не вызывать.
# P.S. В программе необходимо только объявить декоратор и применить его к функции, более ничего делать не нужно.
# ====================
# Sample Input:
# Главная Добавить Удалить Выйти
# ====================
# Sample Output:
# 1. Главная
# 2. Добавить
# 3. Удалить
# 4. Выйти


def show_menu(func):
    def wrapper(*args):
        [print(f'{i+1}. {word}') for i, word in enumerate(func(*args))]

    return wrapper


@show_menu
def get_menu(s):
    s = s.split()
    return s


