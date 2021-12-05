import unittest
from functools import reduce
import numpy
import numpy as np


class Board:
    def __init__(self, lines):
        self.grid = list(map(lambda line:
                             list(map(lambda char: int(char),
                                      line.split())), lines))
        self.x_size = len(self.grid[0])
        self.y_size = len(self.grid)
        self.x_range = range(0, self.x_size)
        self.y_range = range(0, self.y_size)
        self.checks = numpy.full_like(self.grid, False, dtype=object)

    def get(self, x, y):
        return self.grid[y][x], self.checks[y][x]

    def check(self, n):
        for x in self.x_range:
            for y in self.y_range:
                value = self.get(x, y)
                if value[0] == n:
                    self.checks[y][x] = True

    def transpose_checks(self):
        return np.array(self.checks).T

    def line_wins(self, checks, range1):
        for line in range1:
            yield reduce(lambda a, b: a and b, checks[line])

    def wins(self):
        a_line_wins = reduce(lambda a, b: a or b,
                             self.line_wins(self.checks, self.y_range))
        a_column_wins = reduce(lambda a, b: a or b,
                               self.line_wins(self.transpose_checks(),
                                              self.x_range))
        return a_line_wins or a_column_wins

    def unmarked_numbers(self):
        for x in self.x_range:
            for y in self.y_range:
                if not self.checks[y][x]:
                    yield self.get(x, y)[0]

    def calc_score(self, num):
        return sum(self.unmarked_numbers()) * num


def read_file():
    with open('day4_bingo.txt', 'r') as f:
        lines = f.readlines()
        return lines


def get_boards(lines):
    lines = lines[1:]
    lst = []
    board_num = -1
    for line in lines:
        if line == "\n":
            board_num += 1
            lst.insert(board_num, list())
        else:
            lst[board_num].append(line)
    return lst


class MyTestCase(unittest.TestCase):
    def test_read_file(self):
        lines = read_file()
        self.assertEqual(True, True)

    def test_board_init(self):
        b = [
            "22 13 17 11  0",
            " 8  2 23  4 24",
            "21  9 14 16  7",
            " 6 10  3 18  5",
            " 1 12 20 15 19",
        ]
        board = Board(b)
        self.assertEqual((22, False), board.get(0, 0))
        self.assertEqual((8, False), board.get(0, 1))
        self.assertEqual((19, False), board.get(4, 4))

    def test_board_check(self):
        b = [
            "22 13 17 11  0",
            " 8  2 23  4 24",
            "21  9 14 16  7",
            " 6 10  3 18  5",
            " 1 12 20 15 19",
        ]
        board = Board(b)
        self.assertEqual((8, False), board.get(0, 1))
        board.check(8)
        self.assertEqual((8, True), board.get(0, 1))

    def test_board_win_line(self):
        b = [
            "22 13 17 11  0",
            " 8  2 23  4 24",
            "21  9 14 16  7",
            " 6 10  3 18  5",
            " 1 12 20 15 19",
        ]
        board = Board(b)
        board.check(22)
        board.check(13)
        board.check(17)
        board.check(11)
        board.check(0)
        self.assertTrue(board.wins())

    def test_board_win_col(self):
        b = [
            "22 13 17 11  0",
            " 8  2 23  4 24",
            "21  9 14 16  7",
            " 6 10  3 18  5",
            " 1 12 20 15 19",
        ]
        board = Board(b)
        board.check(22)
        board.check(8)
        board.check(21)
        board.check(6)
        board.check(1)
        self.assertTrue(board.wins())

    def test_calc_score(self):
        b = [
            "14 21 17 24  4",
            "10 16 15  9 19",
            "18  8 23 26 20",
            "22 11 13  6  5",
            " 2  0 12  3  7",
        ]
        nums = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14,
                21, 24, 10, 16, 13, 6, 15, 25, 12,
                22, 18, 20, 8, 19, 3, 26, 1]
        board = Board(b)
        for num in nums:
            board.check(num)
            if board.wins():
                print("winning number: " + str(num))
                print("score: " + str(board.calc_score(num)))
                break
        self.assertTrue(True)

    def test_main(self):
        lines = read_file()
        nums = list(map(lambda a: int(a), lines[0].split(",")))
        boards = get_boards(lines)
        boards = list(map(lambda board: Board(board), boards))

        for num in nums:
            for board in boards:
                board.check(num)
                if board.wins():
                    print("winning number: " + str(num))
                    print("score: " + str(board.calc_score(num)))
                    self.assertTrue(False) # fail to stop the game on win


if __name__ == '__main__':
    unittest.main()
