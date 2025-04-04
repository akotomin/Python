**Подвиг 8.** Объявите класс `Circle` (окружность), объекты которого должны создаваться командой:

`circle = Circle(x, y, radius)` \
где: `x`, `y` - координаты центра окружности; \
`radius` - радиус окружности 

В каждом объекте класса `Circle` должны формироваться локальные приватные атрибуты:

`__x`, `__y` - координаты центра окружности (вещественные или целые числа); \
`__radius` - радиус окружности (вещественное или целое положительное число).

Для доступа к этим приватным атрибутам в классе `Circle` следует объявить объекты-свойства (property):

`x`, `y` - для изменения и доступа к значениям `__x`, `__y`, соответственно; \
`radius` - для изменения и доступа к значению `__radius`.

При изменении значений приватных атрибутов через объекты-свойства нужно проверять, что присваиваемые значения - числа
(целые или вещественные). Дополнительно у радиуса проверять, что число должно быть положительным (строго больше нуля).
Сделать все эти проверки нужно через магические методы. При некорректных переданных
числовых значениях, прежние значения меняться не должны (исключений никаких генерировать при этом не нужно).

Если присваиваемое значение не числовое, то генерировать исключение командой:

`raise TypeError("Неверный тип присваиваемых данных.")`
При обращении к несуществующему атрибуту объектов класса `Circle` выдавать булево значение `False`.

Пример использования класса (эти строчки в программе писать не нужно):

```python
circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует
```

P.S. На экран ничего выводить не нужно. 