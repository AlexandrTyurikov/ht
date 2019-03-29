import math


class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def coord(self):
        return self.x, self.y

    def __str__(self):
        return '{}({}, {})'.format(self.name, self.x, self.y)


a = Point('a', 2, 1)
b = Point('b', 1, 3)


class Segment:
    def __init__(self, name):
        self.name = name

    def coord_ab(self, a, b):
        return a.coord(), b.coord()

    # первоначальные координаты ab
    def __str__(self):
        return '{} ({}, {})'.format(self.name, a.coord(), b.coord())

    # длина
    def len_ab(self):
        self.l = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
        return self.l

    # угол
    def corner(self):
        self.u = math.degrees(math.atan((abs(a.y - b.y)) / (abs(a.x - b.x))))
        return self.u

    # сдвиг по оси x и y
    def n_coord_ab(self, x1, y1):
        self.x1 = x1 + a.x
        self.x2 = x1 + b.x
        self.y1 = y1 + a.y
        self.y2 = y1 + b.y
        return (self.x1, self.y1), (self.x2, self.y2)


ab = Segment('ab')
print(a)
print(b)
# длина
print(ab.len_ab())
# угол
print(ab.corner())
print(ab)
# сдвиг по оси x и y
print(ab.name, ab.n_coord_ab(3, 2))
