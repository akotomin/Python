# Подвиг 3. Имеется список городов:
# cities = ["Москва", "Казань", "Ярославль"]
# Необходимо вставить во вторую позицию этого списка строку "Ульяновск" и вывести список командой:
# print(*cities)
# ====================
# Sample Input:
# ====================
# Sample Output:
# Москва Ульяновск Казань Ярославль


cities = ["Москва", "Казань", "Ярославль"]

cities.insert(1, "Ульяновск")
print(*cities)