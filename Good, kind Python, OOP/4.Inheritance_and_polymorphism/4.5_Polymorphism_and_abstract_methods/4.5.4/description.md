**Подвиг 4.** Вам необходимо объявить базовый класс `ShopInterface` с абстрактным методом:

`def get_id(self): ...` \
В самом методе должно генерироваться исключение командой:

`raise NotImplementedError('в классе не переопределен метод get_id')` \
Инициализатор в классе `ShopInterface` прописывать не нужно.

Далее объявите дочерний класс `ShopItem` (от базового класса `ShopInterface`), объекты которого создаются командой:

`item = ShopItem(name, weight, price)` \
где `name` - название товара (строка); \
`weight` - вес товара (любое положительное число); \
`price` - цена товара (любое положительное число).

В каждом объекте класса `ShopItem` должны формироваться локальные атрибуты с именами `_name`, `_weight`, `_price` и
соответствующими значениями. Также в объектах класса `ShopItem` должен автоматически формироваться локальный приватный 
атрибут `__id` с уникальным (для каждого товара) целым значением.

В классе `ShopItem` необходимо переопределить метод `get_id()` базового класса так,
чтобы он (метод) возвращал значение атрибута `__id`.

P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.

