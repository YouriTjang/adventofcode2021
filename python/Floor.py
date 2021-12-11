from Point import Point


class Floor:
    def __init__(self, data):
        self.floor = [[int(cell) for cell in row.strip()] for row in data]
        self.x_size = len(self.floor[0])
        self.y_size = len(self.floor)

    def __getitem__(self, point: Point):
        y = point.y
        x = point.x
        if 0 <= x < len(self.floor[0]) and 0 <= y < len(self.floor):
            return self.floor[y][x]
        else:
            return None

    def set(self, point: Point, value: int):
        self.floor[point.y][point.x] = value

    def empty(self):
        for y in range(self.y_size):
            for x in range(self.x_size):
                self.set(Point(x, y), 0)
        return self

    def floor(self):
        return self.floor

    def flatten(self):
        flat = []
        for row in self.floor:
            flat = flat + row
        return flat
