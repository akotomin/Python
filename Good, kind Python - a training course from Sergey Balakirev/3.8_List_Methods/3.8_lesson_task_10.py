# Подвиг 10. Вводятся названия рек в одну строчку через пробел. Необходимо все их отсортировать по именам (по
# возрастанию) и в отсортированном списке удалить первый элемент. Результат отобразить на экране в одну строчку через
# пробел.
# ====================
# Sample Input:
# Лена Обь Волга Дон Енисей
# ====================
# Sample Output:
# Дон Енисей Лена Обь


a = input().split()
a.sort()
del a[0]
print(*a)