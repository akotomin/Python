# Подвиг 3. Известно, что порядок нот, следующий: до, ре, ми, фа, соль, ля, си. На вход программы поступает строка с
# набором этих нот, записанных через пробел. Необходимо сформировать список из входной строки с нотами,
# отсортированными указанным образом. Результат вывести в виде строки из нот, записанными через пробел.
# ====================
# Sample Input:
# до фа соль до ре фа ля си
# ====================
# Sample Output:
# до до ре фа фа соль ля си


notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
s = input().split()
print(*sorted(s, key=lambda x: notes.index(x)))