# Подвиг 6. Вводится список в виде вещественных чисел в одну строку через пробел. С помощью цикла for необходимо найти
# наименьшее значение в этом списке. Полученный результат вывести на экран.  Реализовать программу без использования
# функции min, max и сортировки.
# ====================
# Sample Input:
# 8.6 9.11 -4.567 -10.0 1.45
# ====================
# Sample Output:
# -10.0


numbers = list(map(float, input().split()))
a = numbers[0]

for i, n in enumerate(numbers):
    if a > n:
        a = n

print(a)