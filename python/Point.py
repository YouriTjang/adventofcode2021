class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return 10 * self.x + self.y

    def __repr__(self):
        return f'({self.x}, {self.y})'
