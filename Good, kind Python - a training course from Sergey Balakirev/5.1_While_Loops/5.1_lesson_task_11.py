# Подвиг 11. Вводятся два натуральных четных числа n и m в одну строчку через пробел, причем n < m. Напечатать все
# нечетные числа из интервала [n, m]. Задачу решить без применения условного оператора. Результат вывести на экран в
# виде строки чисел, записанных через пробел. Программу реализовать при помощи цикла while.
# ====================
# Sample Input:
# 2 10
# ====================
# Sample Output:
# 3 5 7 9


n, m = map(int, input().split())
n -= 1
m -= 1

while n <= m - 1:
    n += 2
    print(n, end=" ")