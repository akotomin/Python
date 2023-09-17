# Подвиг 1. Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список
# чисел и возвращает их сумму.
# Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
# Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:
# s = input()
# Результат отобразите на экране.
# ====================
# Sample Input:
# 5 6 3 6 -4 6 -1
# ====================
# Sample Output:
# 26


def start_param(start):
    def decorator(func):
        def wrapper(*args):
            lst = func(*args)
            return lst + start

        return wrapper
    return decorator


@start_param(start=5)
def get_list(s: str):
    return sum([int(i) for i in s.split()])


s = input()
summ = get_list(s)
print(summ)