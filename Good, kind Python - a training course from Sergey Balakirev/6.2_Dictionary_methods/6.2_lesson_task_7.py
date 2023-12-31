# Подвиг 7. Имеется словарь с наименованиями предметов и их весом (в граммах):
things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
# Сергей собирается в поход и готов взвалить на свои хрупкие плечи максимальный вес в N кг (вводится с клавиатуры).
# Он решил класть в рюкзак предметы в порядке убывания их веса (сначала самые тяжелые, затем, все более легкие) так,
# чтобы их суммарный вес не превысил значения N кг. Все предметы даны в единственном экземпляре. Выведите список
# предметов (в строчку через пробел), которые берет с собой Сергей в порядке убывания их веса.
# P. S. 1 кг = 1000 грамм
# ====================
# Sample Input:
# 10
# ====================
# Sample Output:
# палатка брезент удочка брюки пила карандаш спички


d = dict(sorted([(value, key) for key, value in things.items()], reverse=True))
a = []
n = int(input()) * 1000
s = 0
for k, v in d.items():
    s += k
    if n < s:
        s -= k
        continue
    a.append(v)
print(*a)