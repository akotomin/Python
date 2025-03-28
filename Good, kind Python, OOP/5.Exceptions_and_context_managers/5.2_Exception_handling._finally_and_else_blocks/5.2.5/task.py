class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


try:
    x, y = input().split()
    try:
        x, y = int(x), int(y)
        pt = Point(x, y)
    except:
        x, y = float(x), float(y)
        pt = Point(x, y)
except:
    pt = Point()
finally:
    print(f"Point: x = {pt.x}, y = {pt.y}")
