# Подвиг 3. Вводится вес боксера-любителя (в кг, в виде вещественного числа). Известно, что вес таков, что боксер может
# быть отнесен к одной из весовых категорий:
# 1) легкий вес – до 60 кг (включительно);
# 2) первый полусредний вес – до 64 кг (включительно);
# 3) полусредний вес – до 69 кг (включительно);
# 4) остальные - более 69 кг.
# Вывести на экран номер категории, в которой будет выступать боксер.
# ====================
# Sample Input:
# 62.4
# ====================
# Sample Output:
# 2


x = float(input())

if x <= 60.0:
    print(1)
elif 60.0 < x <= 64.0:
    print(2)
elif 64.0 < x <= 69.0:
    print(3)
else:
    print(4)