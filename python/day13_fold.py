import unittest

from python.Point import Point
from python.ReadFile import read_file


def fold(p: Point, axis: Point):
    if 0 < axis.x < p.x:
        return Point(axis.x - (p.x - axis.x), p.y)
    elif 0 < axis.y < p.y:
        return Point(p.x, axis.y - (p.y - axis.y))
    else:
        return p


class Game:
    def __init__(self, data):
        self.folds = []
        self.points = []
        for line in [line.strip() for line in data if len(line.strip()) > 0]:
            if line.startswith('fold'):
                line = line.removeprefix('fold along ')
                axis, value = line.split('=')
                fold_axis = Point(int(value), 0) if axis == 'x' else Point(0,
                                                                           int(value))
                self.folds.append(fold_axis)
            else:
                x, y = line.split(',')
                self.points.append(Point(int(x), int(y)))

    def apply_single_fold(self):
        new_points = []
        for p in self.points:
            new_points.append(fold(p, self.folds[0]))
        self.points = new_points

    def count_dots(self):
        return len({d.x * 10000 + d.y for d in self.points})

    def apply_folds(self):
        for f in self.folds:
            new_points = []
            for p in self.points:
                new_points.append(fold(p, f))
            self.points = new_points

    def print_points(self):
        max_x = 0
        max_y = 0
        min_x = 0
        min_y = 0

        for p in self.points:
            if p.x > max_x:
                max_x = p.x
            if p.y > max_y:
                max_y = p.y
            if p.x < min_x:
                min_x = p.x
            if p.y < min_y:
                min_y = p.y

        for y in range(min_y, max_y + 2):
            for x in range(min_x, max_x + 1):
                if len([pp for pp in self.points if pp == Point(x, y)]) > 0:
                    print('*', end='')
                else:
                    print('.', end='')
            print()


class MyTestCase(unittest.TestCase):
    def test_fold_below_x_axis(self):
        p = Point(0, 2)
        axis = Point(0, 1)
        actual = fold(p, axis)
        self.assertEqual(Point(0, 0), actual)  # add assertion here

    def test_fold_above_x_axis(self):
        p = Point(0, 2)
        axis = Point(0, 4)
        actual = fold(p, axis)
        self.assertEqual(Point(0, 2), actual)  # add assertion here

    def test_fold_right_y_axis(self):
        p = Point(2, 0)
        axis = Point(1, 0)
        actual = fold(p, axis)
        self.assertEqual(Point(0, 0), actual)  # add assertion here

    def test_fold_left_y_axis(self):
        p = Point(2, 0)
        axis = Point(4, 0)
        actual = fold(p, axis)
        self.assertEqual(Point(2, 0), actual)  # add assertion here

    def test_fold_sample_axis(self):
        p = Point(9, 10)
        axis = Point(7, 0)
        actual = fold(p, axis)
        self.assertEqual(Point(5, 10), actual)  # add assertion here

    def test_example(self):
        g = Game(example_data)
        g.print_points()
        g.apply_folds()
        g.print_points()
        self.assertEqual(True, True)  # add assertion here

    def test_puzzle_part1(self):
        g = Game(read_file('../data/day13.txt'))
        g.apply_single_fold()
        count = g.count_dots()
        self.assertEqual(810, count)

    def test_puzzle_part2(self):
        g = Game(read_file('../data/day13.txt'))
        g.apply_folds()
        g.print_points()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

example_data = [
    '6,10',
    '0,14',
    '9,10',
    '0,3',
    '10,4',
    '4,11',
    '6,0',
    '6,12',
    '4,1',
    '0,13',
    '10,12',
    '3,4',
    '3,0',
    '8,4',
    '1,10',
    '2,14',
    '8,10',
    '9,0',
    '',
    'fold along y=7',
    'fold along x=5',
]
"""
*..*.*....***..*..*.***...**..****.***.
*..*.*....*..*.*..*.*..*.*..*.*....*..*
****.*....***..*..*.***..*....***..*..*
*..*.*....*..*.*..*.*..*.*.**.*....***.
*..*.*....*..*.*..*.*..*.*..*.*....*.*.
"""
