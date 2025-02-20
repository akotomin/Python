class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        return int(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5) > 1


print(bool(Line(0, 1, 0, 1)))
