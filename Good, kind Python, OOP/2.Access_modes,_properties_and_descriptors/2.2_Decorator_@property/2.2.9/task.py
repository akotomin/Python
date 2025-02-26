import math


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.__all_path = list((LineTo(0, 0), ) + args)

    def get_path(self):
        return self.__all_path[1:]

    def get_length(self):
        prev_line = self.__all_path[0]
        path = []
        for line in self.__all_path[1:]:
            path.append(
                math.sqrt(math.pow(line.x - prev_line.x, 2) + math.pow(line.y - prev_line.y, 2))
            )
            prev_line = line

        return sum(path)

    def add_line(self, line):
        self.__all_path.append(line)


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(dist)
