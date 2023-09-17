# Подвиг 6. Вводятся два списка городов каждый с новой строки (в строке названия через пробел), которые объехал
# Сергей в 1-й и 2-й годы своего путешествия по России. Требуется определить, включал ли его маршрут во 2-й год все
# города 1-го года путешествия? Если это так, то вывести ДА, иначе - НЕТ.
# ====================
# Sample Input:
# Москва Казань Самара Москва
# Москва Владимир Новгород Казань Самара Москва
# ====================
# Sample Output:
# ДА


s1 = set(input().split())
s2 = set(input().split())

print('ДА' if s1 <= s2 else 'НЕТ')