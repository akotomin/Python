# Подвиг 7. Вводятся две строки (каждая с новой строчки). Из первой строки выделить все символы с четными индексами,
# а из второй - с нечетными. Объединить строки через пробел и вывести на экран.
# ====================
# Sample Input:
# Hello
# Python
# ====================
# Sample Output:
# Hlo yhn


a = input()
b = input()

print(a[0::2], b[1::2], sep=" ")
