import sys


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name if isinstance(name, str) else None
        self.weight = weight if isinstance(weight, (int, float)) else None
        self.price = price if isinstance(price, (int, float)) else None


    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        if not isinstance(other, ShopItem):
            raise TypeError("Операнд справа должен иметь тип ShopItem")

        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))
shop_items = dict()

for i in lst_in:
    start = i.split(':')
    end = start[1].split()

    name = start[0]
    weight = int(end[0]) if '.' not in end[0] else float(end[0])
    price = int(end[1]) if '.' not in end[1] else float(end[1])

    obj = ShopItem(name, weight, price)

    if obj in shop_items:
        shop_items[obj][1] += 1
    else:
        shop_items[obj] = [obj, 1]

print(shop_items)