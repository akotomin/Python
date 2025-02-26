# Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать объекты
# каждого класса следующими командами:
# g1 = Line(a, b, c, d)
# g2 = Rect(a, b, c, d)
# g3 = Ellipse(a, b, c, d)
# Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов (произвольные
# числа). В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний
# левый) в виде кортежей (a, b) и (c, d) соответственно.
# Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно
# (или Line, или Rect, или Ellipse). Координаты также генерируются случайным образом (числовые значения).
# Все объекты сохраните в списке elements.
# В списке elements обнулите координаты объектов только для класса Line.
# P.S. На экран в программе ничего выводить не нужно.

import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


classes = ('Line', 'Rect', 'Ellipse')
numbers = [i for i in range(100)]
i = 0
elements = []

while i < 217:
    if random.choice(classes) == 'Line':
        elements.append(Line(0, 0, 0, 0))
        i += 1
        continue

    elif random.choice(classes) == 'Rect':
        a, b, c, d = random.sample(numbers, 4)
        elements.append(Rect(a, b, c, d))
        i += 1
        continue

    else:
        a, b, c, d = random.sample(numbers, 4)
        elements.append(Ellipse(a, b, c, d))
        i += 1
        continue

print(len(elements))
