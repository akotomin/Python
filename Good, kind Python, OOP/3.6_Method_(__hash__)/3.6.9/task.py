class Dimensions:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        if isinstance(other, Dimensions):
            return (self.a, self.b, self.c) == (other.a, other.b, other.c)
        return False


s_inp = input()  # эту строку (переменную s_inp) в программе не менять

lst_dims = []
for item in s_inp.split("; "):
    a, b, c = map(float, item.split())
    lst_dims.append(Dimensions(a, b, c))

lst_dims.sort(key=hash)
