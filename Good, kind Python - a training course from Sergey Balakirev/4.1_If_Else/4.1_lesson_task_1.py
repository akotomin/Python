# Подвиг 1. Вводятся два вещественных числа в одну строку через пробел. Вывести на экран наибольшее из чисел. Задачу
# решить с помощью условного оператора.
# ====================
# Sample Input:
# 8.7 11.0
# ====================
# Sample Output:
# 11.0


x, y = map(float, input().split())
if x > y:
    print(x)
else:
    print(y)