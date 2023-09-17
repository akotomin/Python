# Подвиг 8. Пользователь с клавиатуры вводит названия городов, пока не введет букву q. Определить общее уникальное число
# городов, которые вводил пользователь. На экран вывести это число. Из коллекций при реализации программы использовать
# только множества.
# ====================
# Sample Input:
# Уфа
# Москва
# Тверь
# Екатеринбург
# Томск
# Уфа
# Москва
# q
# ====================
# Sample Output:
# 5


city = input()
s = set()

while city != 'q':
    s.add(city)
    city = input()

print(len(s))


