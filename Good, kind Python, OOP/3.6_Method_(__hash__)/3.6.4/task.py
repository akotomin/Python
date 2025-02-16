class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        if isinstance(other, Thing):
            return self.name.lower() == other.name.lower() and self.mass == other.mass
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Box:
    def __init__(self):
        self.things = []

    def add_thing(self, obj):
        if isinstance(obj, Thing):
            self.things.append(obj)

    def get_things(self):
        return self.things

    def __eq__(self, other):
        if isinstance(other, Box):
            if len(self.things) != len(other.things):
                return False

            for thing in self.things:
                if thing not in other.things:
                    return False
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
