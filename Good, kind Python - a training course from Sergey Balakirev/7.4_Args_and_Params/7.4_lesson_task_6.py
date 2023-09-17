# Подвиг 6. Функции из предыдущего подвига 5 добавьте еще один формальный параметр up с начальным булевым значением
# True. Если параметр up равен True, то тег (указанный в формальном параметре tag) следует записывать заглавными
# буквами, а иначе - малыми.
# После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите функцию (с выводом
# результата ее работы на экран):
# - первый раз со строкой и именованным аргументом tag со значением 'div'
# - второй раз со строкой, именованным аргументом tag со значением 'div' и именованным аргументом up со значением False.
# ====================
# Sample Input:
# Python is best!
# ====================
# Sample Output:
# <DIV>Python is best!</DIV>
# <div>Python is best!</div>


def wrap_text_in_tag(text, tag='h1', up=True):
    return f"<{tag.upper()}>{text}</{tag.upper()}>" if up else f"<{tag}>{text}</{tag}>"


input_string = input()
print(wrap_text_in_tag(input_string, tag='div'))
print(wrap_text_in_tag(input_string, tag='div', up=False))