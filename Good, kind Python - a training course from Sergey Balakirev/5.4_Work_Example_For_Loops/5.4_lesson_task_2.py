# Подвиг 2. Вводится строка с номером телефона. Ожидается формат ввода:
# +7(xxx)xxx-xx-xx
# где x - это цифра. Размер введенных символов считается верным (то есть, не может быть, чтобы отсутствовала какая-либо
# цифра или была лишняя). Необходимо проверить, что введенная строка соответствует этому формату. Вывести ДА, если
# соответствует и НЕТ - в противном случае.
# ====================
# Sample Input:
# +7(123)456-78-99
# ====================
# Sample Output:
# ДА


phone = input()
phone_template = "+7(ххх)ххх-хх-хх"

for index, symbol in enumerate(phone):
    if phone_template[index] == 'х':
        if not symbol.isdigit():
            print('НЕТ')
            break
    elif symbol != phone_template[index]:
        print('НЕТ')
        break
else:
    print('ДА')