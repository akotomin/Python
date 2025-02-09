from math import sqrt

class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1 and type(args[0]) == int:
            self.coords = list(0 for _ in range(args[0]))
        elif all(map(lambda i: type(i) in (int, float), args)):
            self.coords = list(args)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        summ = 0
        for i in self.coords:
            summ += i*i
        return sqrt(summ)

    def set_coords(self, *args):
        if len(args) > len(self.coords):
            self.coords = list(args[:len(self.coords)])
        else:
            self.coords[:len(args)] = args

    def get_coords(self):
        return tuple(self.coords)


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
