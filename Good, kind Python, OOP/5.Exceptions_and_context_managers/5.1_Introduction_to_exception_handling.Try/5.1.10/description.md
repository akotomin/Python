**Подвиг 10.** Объявите в программе класс `FloatValidator`, объекты которого создаются командой:

`fv = FloatValidator(min_value, max_value)` \
где `min_value`, `max_value` - минимальное и максимальное допустимое значение (диапазон `[min_value; max_value]`).

Объекты этого класса предполагается использовать следующим образом:

`fv(value)` \
где `value` - проверяемое значение. Если `value` не вещественное число или не принадлежит диапазону
`[min_value; max_value]`, то генерируется исключение командой:

`raise ValueError('значение не прошло валидацию')` \
По аналогии, объявите класс `IntegerValidator`, объекты которого создаются командой:

`iv = IntegerValidator(min_value, max_value)` \
и используются командой:

`iv(value)` \
Здесь также генерируется исключение:

`raise ValueError('значение не прошло валидацию')` \
если value не целое число или не принадлежит диапазону `[min_value; max_value]`.

После этого объявите функцию с сигнатурой:

`def is_valid(lst, validators): ...` 

где `lst` - список из данных; \
`validators` - список из объектов-валидаторов (объектов классов `FloatValidator` и `IntegerValidator`).

Эта функция должна отбирать из списка все значения, которые прошли хотя бы по одному валидатору.
И возвращать новый список с элементами, прошедшими проверку.

Пример использования классов и функции (эти строчки в программе не писать):

```python
fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
```

P.S. В программе нужно только объявить классы и функцию. На экран ничего выводить не нужно.