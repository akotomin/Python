# Подвиг 3. Вводится таблица целых чисел. Используя функцию map и генератор списков, преобразуйте список строк lst_in
# (см. листинг) в двумерный список с именем lst2D, содержащий целые числа.
# Выводить на экран ничего не нужно, только сформировать список lst2D на основе введенных данных.
# ====================
# Sample Input:
# 8 11 -5
# 3 4 10
# -1 -2 3
# 4 5 6
# ====================
# Sample Output:
# True


import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst2D = [list(map(int, i.split())) for i in lst_in]


print(lst2D)