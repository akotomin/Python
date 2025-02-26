class RadiusVector:
    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return tuple(self.coords[key])
        return self.coords[key]

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            self.coords[key] = value
        else:
            self.coords[key] = value
