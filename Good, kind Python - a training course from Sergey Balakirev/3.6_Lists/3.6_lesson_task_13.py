# Подвиг 13. Вводятся названия городов в одну строку через пробел. На основе этой строки необходимо создать список lst
# и добавить его в начало другого списка:
# cities = ["Москва", "Тверь", "Вологда"]
# Вывести результат на экран командой:
# print(*lst)
# ====================
# Sample Input:
# Уфа Казань Севастополь
# ====================
# Sample Output:
# Уфа Казань Севастополь Москва Тверь Вологда


lst1 = list(input().split())
cities = ["Москва", "Тверь", "Вологда"]
lst = lst1 + cities
print(*lst)