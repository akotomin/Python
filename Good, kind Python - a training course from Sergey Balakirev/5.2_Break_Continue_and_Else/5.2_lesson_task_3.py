# Подвиг 3. На каждой итерации цикла вводится целое число. Необходимо подсчитать произведение только положительных
# чисел, до тех пор, пока не будет введено значение 0. Реализовать пропуск вычислений с помощью оператора continue, а
# также использовать цикл while. Результат произведения вывести на экран.
# ====================
# Sample Input:
# 2
# -1
# 3
# 2
# -5
# 7
# 0
# ====================
# Sample Output:
# 84


mult = 1
a = 1

while a != 0:
    a = int(input())
    if a > 0:
        mult *= a
    else:
        continue

print(mult)