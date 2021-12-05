import unittest

import numpy as np
from multipledispatch import dispatch
from parameterized import parameterized


class Point:
    @dispatch(str)
    def __init__(self, string):
        split = string.split(",")
        self.x = int(split[0])
        self.y = int(split[1])

    @dispatch(int, int)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({repr(self.x)}, {repr(self.y)})"

    def __hash__(self):
        return self.x * 10000 + self.y


class Line:
    @dispatch(Point, Point)
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @dispatch(str)
    def __init__(self, entry):
        entries = entry.split(" -> ")
        self.a = Point(entries[0])
        self.b = Point(entries[1])

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __repr__(self):
        return f"({repr(self.a)}, {repr(self.b)})"

    def is_h(self):
        return self.a.x == self.b.x

    def is_v(self):
        return self.a.y == self.b.y

    def is_d(self):
        dx: int = abs(self.a.x - self.b.x)
        dy: int = abs(self.a.y - self.b.y)
        return dy != 0 and dx / dy == 1

    def is_hv(self):
        return self.is_h() or self.is_v()

    def direction(self):
        dx: int = self.b.x - self.a.x
        dy: int = self.b.y - self.a.y
        return int(np.sign(dx)), int(np.sign(dy))

    def step_distance(self):
        dx: int = abs(self.a.x - self.b.x)
        dy: int = abs(self.a.y - self.b.y)
        return max(dx, dy) + 1

    def get_range(self):
        direction = self.direction()
        steps = self.step_distance()
        for i in range(0, steps):
            yield Point(self.a.x + (direction[0] * i),
                        self.a.y + (direction[1] * i))


class OceanFloor:
    floor: dict[Point, int] = {}

    def __init__(self):
        self.floor = {}

    def add_line(self, line):
        for p in line.get_range():
            if not self.floor.get(p):
                self.floor[p] = 1
            else:
                self.floor[p] += 1

    def no_go_zones(self):
        return list(filter(lambda p: self.floor.get(p) >= 2, self.floor))


def read_file():
    with open('../data/day5.txt', 'r') as f:
        lines = f.readlines()
        return lines


def main():
    lines = list(map(lambda l: Line(l), read_file()))
    ocean = OceanFloor()
    for line in lines:
        ocean.add_line(line)
    print(len(ocean.no_go_zones()))


class MyTestCase(unittest.TestCase):
    def test_str_init_line(self):
        entry = "645,570 -> 517,570"
        actual = Line(entry)
        expected = Line(Point(645, 570), Point(517, 570))
        self.assertEqual(expected, actual)

    def test_is_horizontal(self):
        line = Line(Point(645, 570), Point(517, 570))
        self.assertEqual(True, line.is_hv())

    def test_is_vertical(self):
        line = Line(Point(645, 1), Point(645, 570))
        self.assertEqual(True, line.is_hv())

    @parameterized.expand([
        ["RD45", Point(0, 0), Point(1, 1), True],
        ["RU45", Point(0, 1), Point(1, 0), True],
        ["LD45", Point(1, 0), Point(0, 1), True],
        ["LU45", Point(1, 1), Point(0, 0), True],
        ["RD-x", Point(0, 0), Point(1, 2), False],
        ["RU-x", Point(0, 1), Point(4, 0), False],
        ["LD-x", Point(1, 0), Point(0, 2), False],
        ["LU-x", Point(1, 2), Point(0, 0), False],
    ])
    def test_is_diagonal(self, name, a, b, expected):
        line = Line(a, b)
        self.assertEqual(expected, line.is_d())

    def test_floor_add_line(self):
        ocean = OceanFloor()
        ocean.add_line(Line(Point(0, 0), Point(0, 2)))
        self.assertEqual(1, ocean.floor.get(Point(0, 0)))
        self.assertEqual(1, ocean.floor.get(Point(0, 1)))
        self.assertEqual(1, ocean.floor.get(Point(0, 2)))

    def test_floor_add_line_reverse(self):
        ocean = OceanFloor()
        ocean.add_line(Line(Point(0, 2), Point(0, 0)))
        self.assertEqual(1, ocean.floor.get(Point(0, 0)))
        self.assertEqual(1, ocean.floor.get(Point(0, 1)))
        self.assertEqual(1, ocean.floor.get(Point(0, 2)))

    def test_floor_add_lines(self):
        ocean = OceanFloor()
        ocean.add_line(Line(Point(0, 0), Point(0, 2)))
        ocean.add_line(Line(Point(0, 0), Point(2, 0)))
        self.assertEqual(2, ocean.floor.get(Point(0, 0)))
        self.assertEqual([Point(0, 0)], ocean.no_go_zones())

    def test_example(self):
        data = [
            "0,9 -> 5,9",
            "8,0 -> 0,8",
            "9,4 -> 3,4",
            "2,2 -> 2,1",
            "7,0 -> 7,4",
            "6,4 -> 2,0",
            "0,9 -> 2,9",
            "3,4 -> 1,4",
            "0,0 -> 8,8",
            "5,5 -> 8,2",
        ]
        lines = list(map(lambda l: Line(l.strip()), data))
        ocean = OceanFloor()
        for line in lines:
            ocean.add_line(line)
        actual = len(ocean.no_go_zones())
        self.assertEqual(12, actual)

    def test_range(self):
        self.assertEqual([0, 1, 2], list(range(0, 3)))
        self.assertEqual([2, 1, 0], list(range(2, -1, -1)))

    def test_main(self):
        main()
        self.assertTrue(False)  # fail on purpose, just so it stands out ;)

    @parameterized.expand([
        ["R", Point(0, 0), Point(1, 0), (1, 0)],
        ["RD45", Point(0, 0), Point(1, 1), (1, 1)],
        ["D", Point(0, 0), Point(0, 1), (0, 1)],
        ["LD45", Point(1, 0), Point(0, 1), (-1, 1)],
        ["L", Point(0, 0), Point(0, 1), (0, 1)],
        ["LU45", Point(1, 1), Point(0, 0), (-1, -1)],
        ["U", Point(1, 1), Point(1, 0), (0, -1)],
        ["RU45", Point(0, 1), Point(1, 0), (1, -1)],
    ])
    def test_direction(self, name, a, b, direction):
        line = Line(a, b)
        self.assertEqual(direction, line.direction())

    @parameterized.expand([
        ["R", Point(0, 0), Point(1, 0),    [Point(0, 0), Point(1, 0)]],
        ["RD45", Point(0, 0), Point(1, 1), [Point(0, 0), Point(1, 1)]],
        ["D", Point(0, 0), Point(0, 1),    [Point(0, 0), Point(0, 1)]],
        ["LD45", Point(1, 0), Point(0, 1), [Point(1, 0), Point(0, 1)]],
        ["L", Point(0, 0), Point(0, 1),    [Point(0, 0), Point(0, 1)]],
        ["LU45", Point(1, 1), Point(0, 0), [Point(1, 1), Point(0, 0)]],
        ["U", Point(1, 1), Point(1, 0),    [Point(1, 1), Point(1, 0)]],
        ["RU45", Point(0, 1), Point(1, 0), [Point(0, 1), Point(1, 0)]],

        ["big - R", Point(0, 0), Point(2, 0),    [Point(0, 0), Point(1, 0), Point(2, 0)]],
        ["big - RD45", Point(0, 0), Point(2, 2), [Point(0, 0), Point(1, 1), Point(2, 2)]],
        ["big - D", Point(0, 0), Point(0, 2),    [Point(0, 0), Point(0, 1), Point(0, 2)]],
        ["big - LD45", Point(2, 0), Point(0, 2), [Point(2, 0), Point(1, 1), Point(0, 2)]],
        ["big - L", Point(0, 0), Point(0, 2),    [Point(0, 0), Point(0, 1), Point(0, 2)]],
        ["big - LU45", Point(2, 2), Point(0, 0), [Point(2, 2), Point(1, 1), Point(0, 0)]],
        ["big - U", Point(1, 2), Point(1, 0),    [Point(1, 2), Point(1, 1), Point(1, 0)]],
        ["big - RU45", Point(0, 2), Point(2, 0), [Point(0, 2), Point(1, 1), Point(2, 0)]],
    ])
    def test_range(self, name, a, b, range):
        line = Line(a, b)
        self.assertEqual(range, list(line.get_range()))


if __name__ == '__main__':
    unittest.main()
