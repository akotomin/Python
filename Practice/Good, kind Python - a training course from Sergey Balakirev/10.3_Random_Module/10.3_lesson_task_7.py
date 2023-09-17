# Значимый подвиг 7. Имеется двумерное игровое поле размером N x N (N - натуральное число, вводится с клавиатуры),
# представленное в виде вложенного списка:
# P = [[0] * N for i in range(N)]
# Требуется расставить в нем случайным образом M = 10 единиц (целочисленных) так, чтобы они не соприкасались друг с
# другом (то есть, вокруг каждой единицы должны быть нули, либо граница поля).
# P.S. Поле на экран выводить не нужно (вообще ничего не нужно выводить), только сформировать.
# ====================
# Sample Input:
# 10
# ====================
# Sample Output:
# True


import random


random.seed(1)
N = int(input())
P = [[0] * N for i in range(N)]

count = 0
while sum(map(sum, P)) < 10:
    P[random.randrange(0, N, 2)][random.randrange(0, N, 2)] = 1
    count += 1