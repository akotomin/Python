# Подвиг 5. Объявите функцию, которая имеет один параметр - вес предмета и выводит на экран сообщение (без кавычек):
# "Предмет имеет вес: x кг."
# где x - переданное значение функции. После объявления функции прочитайте (с помощью функции input) вещественное
# число и вызовите функцию с этим значением.
# ====================
# Sample Input:
# 12.67
# ====================
# Sample Output:
# Предмет имеет вес: 12.67 кг.


def print_subject_weight(weight):
    print(f"Предмет имеет вес: {weight} кг.")

print_subject_weight(float(input()))