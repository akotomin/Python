# Подвиг 4. Вводится двумерный список размерностью 5 х 5 элементов, состоящий из нулей и, в некоторых позициях,
# единиц (см. пример ввода ниже). Требуется проверить, не касаются ли единицы друг друга по горизонтали, вертикали и
# диагонали. То есть, вокруг каждой единицы должны быть нули. Если проверка проходит вывести ДА, иначе - НЕТ.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
# ====================
# Sample Input:
# 1 0 0 0 0
# 0 0 1 0 1
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0
# ====================
# Sample Output:
# ДА


import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

coordinates = []
for y in range(len(lst_in)):
    for x in range(len(lst_in[y])):
        if lst_in[y][x] == 1: coordinates.append((x, y))

flag = True

for coordinate_check_ind in range(len(coordinates)):
    for coordinate in coordinates[coordinate_check_ind + 1:]:
        # Проверка горизонтали (x)
        if coordinates[coordinate_check_ind][0] == coordinate[0] and abs(coordinates[coordinate_check_ind][1] - coordinate[1]) == 1: flag = False
        # Проверка вертикали (y)
        if coordinates[coordinate_check_ind][1] == coordinate[1] and abs(coordinates[coordinate_check_ind][0] - coordinate[0]) == 1: flag = False
        # Проверка диагонали
        if abs(coordinates[coordinate_check_ind][0] - coordinate[0]) == 1 and abs(coordinates[coordinate_check_ind][1] - coordinate[1]) == 1: flag = False
print("ДА" if flag else "НЕТ")