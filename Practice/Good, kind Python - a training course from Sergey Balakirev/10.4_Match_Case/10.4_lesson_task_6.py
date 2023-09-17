# Подвиг 6. В функцию get_data() передается параметр value:
# Необходимо дописать оператор match/case в этой функции так, чтобы для каждого типа данных (int, float и str)
# формировалась переменная со значением value и возвращалась функцией (непосредственно из блока case).
# P. S. Вызывать функцию не нужно, только дописать.


def get_data(value):
    match value:
        case int() as value:
            return value
        case float() as value:
            return value
        case str() as value:
            return value

    return None

print(get_data(input()))