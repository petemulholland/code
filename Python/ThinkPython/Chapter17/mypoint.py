class Point(object):
    """Represents a point in 2D space."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def add_point(self, pt):
        return Point(self.x + pt.x, self.y + pt.y)

    def add_tuple(self, t):
        return Point(self.x + t[0], self.y + t[1])

