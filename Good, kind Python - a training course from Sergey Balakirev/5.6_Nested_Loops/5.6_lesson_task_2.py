# Подвиг 2. Вводится список из URL-адресов (каждый с новой строки). Требуется в них заменить все пробелы на символ
# дефиса (-). Следует учесть, что может быть несколько подряд идущих пробелов. Результат преобразования вывести на экран
# в виде строк из URL-адресов.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# ====================
# Sample Input:
# django chto  eto takoe    poryadok ustanovki
# model mtv   marshrutizaciya funkcii  predstavleniya
# marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya
# ====================
# Sample Output:
# django-chto-eto-takoe-poryadok-ustanovki
# model-mtv-marshrutizaciya-funkcii-predstavleniya
# marshrutizaciya-obrabotka-isklyucheniy-zaprosov-perenapravleniya


import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst = []

for i, line in enumerate(lst_in):
    while "  " in line:
        line = line.replace("  ", " ")
    lst.append(line)

lst2 = []

for j, line2 in enumerate(lst):
    while " " in line2:
        line2 = line2.replace(" ", "-")
    lst2.append(line2)

for m, n in enumerate(lst2):
    print(*n, sep="", end="\n")