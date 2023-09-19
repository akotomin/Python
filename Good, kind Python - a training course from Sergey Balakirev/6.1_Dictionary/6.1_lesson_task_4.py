# Подвиг 4. На вход программы поступают данные в виде набора строк в формате:
# ключ1=значение1
# ключ2=значение2
# ...
# ключN=значениеN
# Ключами здесь выступают целые числа (см. пример ниже). Необходимо их преобразовать в словарь d
# (без использования функции dict()) и вывести его на экран командой:
# print(*sorted(d.items()))
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# ====================
# Sample Input:
# 5=отлично
# 4=хорошо
# 3=удовлетворительно
# ====================
# Sample Output:
# (3, 'удовлетворительно') (4, 'хорошо') (5, 'отлично')


import sys

lst = list(map(str.strip, sys.stdin.readlines()))
lst2 = []
for i in range(len(lst)):
    lst2.append(lst[i].split('='))

for k in range(len(lst2)):
    lst2[k][0] = int(lst2[k][0])

d = dict(lst2)
print(*sorted(d.items()))