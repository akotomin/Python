# Подвиг 3. Вводятся: два целых числа в одну строку через пробел. С помощью F-строки отобразить их по возрастанию в одну
# строку через пробел. Результат вывести на экран.
# P. S. Реализовать программу без использования условных операторов. Подумайте, как это можно сделать.
# ====================
# Sample Input:
# 18 11
# ====================
# Sample Output:
# 11 18


a, b = input().split()
print(f"{min(a, b)} {max(a, b)}")