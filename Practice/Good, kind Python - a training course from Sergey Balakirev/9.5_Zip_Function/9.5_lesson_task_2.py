# Подвиг 2. Вводится неравномерная таблица целых чисел. С помощью функции zip выровнить эту таблицу, приведя ее к
# прямоугольному виду, отбросив выходящие элементы. Вывести результат на экран в виде такой же таблицы чисел.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# ====================
# Sample Input:
# 1 2 3 4 5 6
# 3 4 5 6
# 7 8 9
# 9 7 5 3 2
# ====================
# Sample Output:
# 1 2 3
# 3 4 5
# 7 8 9
# 9 7 5


import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))

for i, values in enumerate(lst_in):
    lst_in[i] = values.split()

zipped = list(zip(*lst_in))
lst_in = list(zip(*zipped))
for i in lst_in:
    print(*i, end="\n")