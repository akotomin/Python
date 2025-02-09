class Recipe:
    def __init__(self, *args):
        self.recipes = list(args)

    def __len__(self):
        return len(self.recipes)

    def add_ingredient(self, ing):
        self.recipes.append(ing)

    def remove_ingredient(self, ing):
        self.recipes.remove(ing)

    def get_ingredients(self):
        return tuple(self.recipes)

class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __setattr__(self, name, value):
        if name in ('name', 'measure'):
            if not isinstance(value, str):
                raise TypeError(f"Поле {name} должно быть строкового типа")
        if name == 'volume':
            if type(value) not in (int, float):
                raise TypeError(f"Поле {name} должно быть вещественным числом")
        return super().__setattr__(name, value)

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3