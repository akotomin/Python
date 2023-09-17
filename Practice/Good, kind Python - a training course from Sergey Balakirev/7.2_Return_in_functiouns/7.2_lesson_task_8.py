# Подвиг 8. Объявите функцию, которая принимает строку (в качестве аргумента) и возвращает два значения в виде кортежа:
# переданная строка и ее длина.
# После объявления функции прочитайте (с помощью функции input) список названий городов, записанных в одну строку
# через пробел. Затем, используя генератор словарей и созданную функцию, сформируйте словарь d в формате:
# d = {<город 1>: <число символов>, ..., <город N>: <число символов>}
# Выведите этот словарь в порядке возрастания длин строк с помощью команд:
# a = sorted(d, key=lambda x: d[x])
# print(*a)
# P. S. Пока просто запишите эти команды. Как они работают станет ясно позже, когда мы подробнее изучим функции
# сортировки и работу оператора *.
# ====================
# Sample Input:
# Воронеж Лондон Тверь Омск Уфа
# ====================
# Sample Output:
# Уфа Омск Тверь Лондон Воронеж


def check_len(string):
    return (string, len(string))

lst_in = input().split()

d = {check_len(i)[0]: check_len(i)[1] for i in lst_in}
a = sorted(d, key=lambda x: d[x])
print(*a)