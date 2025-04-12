# Дан следующий список:
lst = [2, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7]
# необходимо написать функцию, которая отбирает только те значения из списка,
# которые встречаются лишь единожды:


d = dict.fromkeys(lst, 0)


def find_single_number(lst, d):
    for i in lst:
        if i in d:
            d[i] += 1

    return [key for key, value in d.items() if value == 1]


print(find_single_number(lst, d))
