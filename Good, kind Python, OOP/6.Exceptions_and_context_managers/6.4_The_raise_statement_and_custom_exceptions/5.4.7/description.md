**Значимый подвиг 7.** Вам поручается разработать класс `TupleData`, элементами которого могут являются только объекты
классов: `CellInteger`, `CellFloat` и `CellString`.

![img.png](img.png)

Вначале в программе нужно объявить класс `CellInteger`, `CellFloat` и `CellString`, объекты которых создаются командами:

```python
cell_1 = CellInteger(min_value, max_value)
cell_2 = CellFloat(min_value, max_value)
cell_3 = CellString(min_length, max_length)
```

где `min_value`, `max_value` - минимальное и максимальное допустимое значение в ячейке; `min_length`, `max_length`
- минимальная и максимальная допустимая длина строки в ячейке.

В каждом объекте этих классов должны формироваться локальные атрибуты с именами `_min_value`, `_max_value` или
`_min_length`, `_max_length` и соответствующими значениями.

Запись и считывание текущего значения в ячейке должно выполняться через объект-свойство (`property`) с именем:

`value` - для записи и считывания значения в ячейке (изначально возвращает значение `None`).

Если в момент записи новое значение не соответствует диапазону `[min_value; max_value]` или `[min_length; max_length]`,
то генерируется исключения командами:

```python
raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
raise CellFloatException('значение выходит за допустимый диапазон')    # для объектов класса CellFloat
raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString
```

Все три класса исключений должны быть унаследованы от одного общего класса:

`CellException`

Далее, объявите класс `TupleData`, объекты которого создаются командой:

`ld = TupleData(cell_1, ..., cell_N)` \
где `cell_1`, `...`, `cell_N` - объекты классов `CellInteger`, `CellFloat` и `CellString` 
(в любом порядке и любом количестве).

Обращение к отдельной ячейке должно выполняться с помощью оператора:

`value = ld[index] # считывание значения из ячейке с индексом index` \
`ld[index] = value # запись нового значения в ячейку с индексом index` \
Индекс `index` отсчитывается с нуля (для первой ячейки) и является целым числом. 
Если значение `index` выходит за диапазон `[0; число ячеек-1]`, то генерировать исключение `IndexError`.

Также с объектами класса `TupleData` должны выполняться следующие функции и операторы:

```python
res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
    print(d)
```

Все эти классы в программе можно использовать следующим образом:

```python
ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
```

P.S. Данная программа должна быть выполнена штатно, без ошибок. На экран отображать ничего не нужно.