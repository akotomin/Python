# Подвиг 7. Вводится натуральное число n. Вывести первое найденное натуральное число (то есть, перебирать числа, начиная
# с 1), квадрат которого больше значения n. Реализовать программу с использованием цикла while.
# ====================
# Sample Input:
# 10
# ====================
# Sample Output:
# 4


n = int(input())
number = 1

while n:
    if number**2 > n:
        break
    number += 1

print(number)