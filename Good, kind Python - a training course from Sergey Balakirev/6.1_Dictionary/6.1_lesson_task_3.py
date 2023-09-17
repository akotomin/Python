# Подвиг 3. Вводятся данные в формате ключ=значение в одну строчку через пробел.
# Значениями здесь являются целые числа (см. пример ниже). Необходимо на их основе создать словарь d с помощью
# функции dict() и вывести его на экран командой:
# print(*sorted(d.items()))
# ====================
# Sample Input:
# one=1 two=2 three=3
# ====================
# Sample Output:
# ('one', 1) ('three', 3) ('two', 2)


lst = input().split()
d = dict()
for pair in lst:
    key, value = pair.split('=')
    d[key] = int(value)
print(*sorted(d.items()))


