# Подвиг 4. Объявите функцию с именем get_list и следующим описанием в теле функции:
# '''Функция для формирования списка целых значений'''
# Сама функция должна формировать и возвращать список целых чисел, который поступает на ее вход в виде строки из целых
# чисел, записанных через пробел.
# Определите декоратор, который выполняет суммирование значений из списка этой функции и возвращает результат.
# Внутри декоратора декорируйте переданную функцию get_list с помощью команды @wraps (не забудьте сделать импорт: from
# functools import wraps). Такое декорирование необходимо, чтобы исходная функция get_list сохраняла свои локальные
# свойства: __name__ и __doc__.
# Примените декоратор к функции get_list, но не вызывайте ее.


from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args):
        lst = func(*args)
        return sum(lst)
    return wrapper



@decorator
def get_list(string: str):
    '''Функция для формирования списка целых значений'''
    return [int(i) for i in string.split()]


s = input()
summ = get_list(s)
print(summ)