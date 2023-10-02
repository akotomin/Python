# Подвиг 6. Имеется список базовых нот:
# m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# Вводятся три целых числа в диапазоне от 1 до 7 - номера нот, в одну строчку через пробел. Необходимо отобразить
# указанные ноты в виде строки через пробел, но перед нотами до и фа дополнительно ставить символ диеза '#'. Реализовать
# эту программу с использованием тернарного условного оператора (он может использоваться несколько раз).
# ====================
# Sample Input:
# 1 6 7
# ====================
# Sample Output:
# #до ля си


m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
v, f, r = map(int, input().split())

a = m[m.index('до')] = '#до' if m[m.index('до')] == "до" else m
b = m[m.index('фа')] = '#фа' if m[m.index('фа')] == "фа" else m
print(m[v-1], m[f-1], m[r-1])