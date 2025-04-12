# Подвиг 6. Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число).
# По введенным m и n (в одну строку через пробел) определить:
# а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
# б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).
# В задаче принять, что год не является високосным. Вывести предыдущую дату и следующую дату (в формате: mm.dd, где m
# - число месяца; d - номер дня) в одну строчку через пробел.
# P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
# ====================
# Sample Input:
# 8 31
# ====================
# Sample Output:
# 08.30 09.01


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month, day = map(int, input().split())
if day == 1:
    prev_day = days[month-1]
    prev_month = month - 1
    next_day = day + 1
    next_month = month
elif day == days[month -1]:
    prev_day = day - 1
    prev_month = month
    next_day = 1
    next_month = month + 1
else:
    prev_day = day - 1
    prev_month = month
    next_day = day + 1
    next_month = month

print(f"{str(prev_month).rjust(2,'0')}.{str(prev_day).rjust(2,'0')}"
      f" {str(next_month).rjust(2,'0')}.{str(next_day).rjust(2,'0')}")