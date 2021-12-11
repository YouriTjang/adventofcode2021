import unittest
from collections import Counter
from functools import reduce
from operator import mul

from python.Floor import Floor


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


def solve(data):
    floor = Floor(data)
    basin_map = Floor(data).empty()
    basin_count = 0
    low_points = []
    for y in range(floor.y_size):
        for x in range(floor.x_size):
            current_height = floor[Point(x, y)]
            neighbors_heights = [floor[Point(x, y) + d] for d in directions if
                                 floor[Point(x, y) + d] is not None]
            lower_neighbors = [n for n in neighbors_heights if
                               n <= current_height]
            if len(lower_neighbors) == 0:
                low_points.append(
                    (Point(x, y), current_height, neighbors_heights))
    sum_risk = sum([low[1] + 1 for low in low_points])
    return sum_risk


class Game:
    def __init__(self, data):
        self.floor = Floor(data)
        self.basin_map = Floor(data).empty()
        self.basin_count = 1

    def traverse_map(self):
        for y in range(self.floor.y_size):
            for x in range(self.floor.x_size):
                basin = self.traverse_basin(Point(x, y), True)
                if basin is not None:
                    self.basin_count = basin
        basins = {cell for row in self.basin_map.floor for cell in row if
                  cell != 0}
        flat_basin = self.basin_map.flatten()
        counter = Counter(flat_basin)
        counter.pop(0)
        top3 = sorted(counter.values(), reverse=True)[:3]
        return reduce(mul, top3)

    def traverse_basin(self, p: Point, initial=False):
        if self.floor[p] != 9:
            if self.basin_map[p] == 0:
                self.basin_map.set(p, self.basin_count)
                neighbors = [p + d for d in directions if
                             self.floor[p + d] is not None and self.basin_map[
                                 p + d] == 0]
                for n in neighbors:
                    self.traverse_basin(n)
                return self.basin_count + 1


def solve_part2(data):
    g = Game(data)
    return g.traverse_map()


class MyTestCase(unittest.TestCase):
    def test_example_part1(self):
        actual = solve(example_data)
        self.assertEqual(15, actual)

    def test_part1(self):
        data = read_file()
        actual = solve(data)
        print(actual)

    def test_example_part2(self):
        actual = solve_part2(example_data)
        self.assertEqual(4, actual)

    def test_part2(self):
        data = read_file()
        actual = solve_part2(data)
        print(actual)
        self.assertEqual(931200, actual)

    def test_list_comprehension(self):
        lst = [n for n in [9, 9, 9] if n < 9]
        print(lst)

        lst = list(filter(lambda n: n < 9, [9, 9, 9]))
        print(lst)


if __name__ == '__main__':
    unittest.main()

directions = [Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)]

example_data = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]


def read_file():
    with open('../data/day9.txt', 'r') as f:
        lines = f.readlines()
        return lines
