class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.track = []

    def add_point(self, x, y, speed):
        self.track.append([x, y, speed])

    def __getitem__(self, item):
        if not isinstance(item, int) or item < 0 or item >= len(self.track):
            raise IndexError('некорректный индекс')
        x, y, speed = self.track[item]
        return (x, y), speed

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0 or key >= len(self.track):
            raise IndexError('некорректный индекс')
        self.track[key][2] = value
