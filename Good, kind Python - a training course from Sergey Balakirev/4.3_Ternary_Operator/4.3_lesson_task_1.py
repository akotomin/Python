# Подвиг 1. Вводится два вещественных числа, каждое с новой строки. Необходимо с помощью тернарного условного оператора
# наибольшее значение присвоить переменной d и вывести ее на экран.
# ====================
# Sample Input:
# 5.4
# -3.8
# ====================
# Sample Output:
# 5.4


a = float(input())
b = float(input())

d = a if a > b else b
print(d)