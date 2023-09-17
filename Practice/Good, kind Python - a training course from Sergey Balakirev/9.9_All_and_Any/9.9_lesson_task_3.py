# Подвиг 3. Объявить функцию с именем is_string, на вход которой поступает коллекция (список, кортеж, множество).
# Она должна возвращать True, если все элементы коллекции строки и False - в противном случае.
# Сигнатура функции должна быть, следующей:
# def is_string(lst): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран. Задачу реализовать с
# использованием одной из функций: any или all.
# ====================
# Sample Input:
# ====================
# Sample Output:
# True


def is_string(lst):
    return all(map(lambda x: isinstance(x, str), lst))