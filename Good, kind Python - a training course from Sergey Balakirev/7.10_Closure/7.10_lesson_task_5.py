# Подвиг 5. Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел,
# записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции.
# Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.
# Далее, на вход программы поступают две строки: первая - это значение для параметра tp; вторая - список целых чисел,
# записанных через пробел. С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию.
# Результат вывести на экран командой (lst - ссылка на коллекцию):
# print(lst)
# ====================
# Sample Input:
# list
# -5 6 8 11 0 111 -456 3
# ====================
# Sample Output:
# [-5, 6, 8, 11, 0, 111, -456, 3]


def replace_lst(tp, ls):
    def replacer():
        nonlocal tp, ls
        tpl = [int(x) for x in ls.split()]
        return tpl if tp == "list" else tuple(tpl)
    return replacer


lst_replace = replace_lst(input(), input())
print(lst_replace())
