class Tuple(tuple):
    def __new__(cls, iter_obj):
        return super().__new__(cls, iter_obj)

    def __add__(self, other):
        if hasattr(other, '__iter__'):
            added_values = tuple(self) + tuple(other)
            return Tuple(added_values)
        else:
            return Tuple(tuple(self) + (other,))


t = Tuple([1, 2, 3])
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"