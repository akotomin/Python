# Подвиг 5. Вводятся названия городов в одну строку через пробел. На их основе формируется кортеж.
# Если в этом кортеже присутствует город "Ульяновск", то этот элемент следует удалить (создав новый кортеж).
# Результат вывести на экран в виде строки с названиями городов через пробел.
# ====================
# Sample Input:
# Воронеж Самара Тольятти Ульяновск Пермь
# ====================
# Sample Output:
# Воронеж Самара Тольятти Пермь


cities = tuple(input().split())

if 'Ульяновск' in cities:
    new_cities = list(cities)
    new_cities.remove('Ульяновск')
    new_cities = tuple(new_cities)
    print(*new_cities)
else:
    print(*cities)
