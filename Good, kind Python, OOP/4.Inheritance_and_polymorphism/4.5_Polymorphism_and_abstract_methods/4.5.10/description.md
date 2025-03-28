**Подвиг 10 (на повторение, релакс).** Объявите класс с именем `Food` (еда), объекты которого создаются командой:

`food = Food(name, weight, calories)` \
где `name` - название продукта (строка); \
`weight` - вес продукта (любое положительное число); \
`calories` - калорийная ценность продукта (целое положительное число).

Объявите следующие дочерние классы с именами:

`BreadFood` - хлеб; \
`SoupFood` - суп; \
`FishFood` - рыба.

Объекты этих классов должны создаваться командами:

```python
bf = BreadFood(name, weight, calories, white) # white - True для белого хлеба, False - для остальных
sf = SoupFood(name, weight, calories, dietary) # dietary - True для диетического супа, False - для других видов
ff = FishFood(name, weight, calories, fish) # fish - вид рыбы (семга, окунь, сардина и т.д.)
```

В каждом объекте этих дочерних классов должны формироваться соответствующие локальные атрибуты с именами:

```
BreadFood: _name, _weight, _calories, _white
SoupFood: _name, _weight, _calories, _dietary
FishFood: _name, _weight, _calories, _fish
```

Пример использования классов (эти строчки в программе писать не нужно):

```python
bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
sf = SoupFood("Черепаший суп", 520, 890.5, False)
ff = FishFood("Консерва рыбная", 340, 1200, "семга")
```

P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.