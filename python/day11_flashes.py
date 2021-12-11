import unittest

from parameterized import parameterized

from Point import Point
from python.Floor import Floor

directions = [
    Point(0, 1),
    Point(1, 1),
    Point(1, 0),
    Point(1, -1),
    Point(0, -1),
    Point(-1, -1),
    Point(-1, 0),
    Point(-1, 1),
]
example1_step0 = [
    '11111',
    '19991',
    '19191',
    '19991',
    '11111',
]
example1_step1 = [
    '34543',
    '40004',
    '50005',
    '40004',
    '34543',
]
example1_step2 = [
    '45654',
    '51115',
    '61116',
    '51115',
    '45654',
]

example2_steps = [
    [
        '5483143223',
        '2745854711',
        '5264556173',
        '6141336146',
        '6357385478',
        '4167524645',
        '2176841721',
        '6882881134',
        '4846848554',
        '5283751526',
    ], [
        '6594254334',
        '3856965822',
        '6375667284',
        '7252447257',
        '7468496589',
        '5278635756',
        '3287952832',
        '7993992245',
        '5957959665',
        '6394862637',
    ], [
        '8807476555',
        '5089087054',
        '8597889608',
        '8485769600',
        '8700908800',
        '6600088989',
        '6800005943',
        '0000007456',
        '9000000876',
        '8700006848',
    ], [
        '0050900866',
        '8500800575',
        '9900000039',
        '9700000041',
        '9935080063',
        '7712300000',
        '7911250009',
        '2211130000',
        '0421125000',
        '0021119000',
    ], [
        '2263031977',
        '0923031697',
        '0032221150',
        '0041111163',
        '0076191174',
        '0053411122',
        '0042361120',
        '5532241122',
        '1532247211',
        '1132230211',
    ], [
        '4484144000',
        '2044144000',
        '2253333493',
        '1152333274',
        '1187303285',
        '1164633233',
        '1153472231',
        '6643352233',
        '2643358322',
        '2243341322',
    ], [
        '5595255111',
        '3155255222',
        '3364444605',
        '2263444496',
        '2298414396',
        '2275744344',
        '2264583342',
        '7754463344',
        '3754469433',
        '3354452433',
    ], [
        '6707366222',
        '4377366333',
        '4475555827',
        '3496655709',
        '3500625609',
        '3509955566',
        '3486694453',
        '8865585555',
        '4865580644',
        '4465574644',
    ], [
        '7818477333',
        '5488477444',
        '5697666949',
        '4608766830',
        '4734946730',
        '4740097688',
        '6900007564',
        '0000009666',
        '8000004755',
        '6800007755',
    ], [
        '9060000644',
        '7800000976',
        '6900000080',
        '5840000082',
        '5858000093',
        '6962400000',
        '8021250009',
        '2221130009',
        '9111128097',
        '7911119976',
    ], [
        '0481112976',
        '0031112009',
        '0041112504',
        '0081111406',
        '0099111306',
        '0093511233',
        '0442361130',
        '5532252350',
        '0532250600',
        '0032240000',
    ]]

puzzle_input = [
    '8624818384',
    '3725473343',
    '6618341827',
    '4573826616',
    '8357322142',
    '6846358317',
    '7286886112',
    '8138685117',
    '6161124267',
    '3848415383',
]


class Game:
    def __init__(self, data):
        self.floor = Floor(data)
        self.flashes = Floor(data).empty()
        self.flash_sum = 0

    def step(self, step):
        for y in range(self.floor.y_size):
            for x in range(self.floor.x_size):
                p = Point(x, y)
                self.incr_point(p, step)

    def incr_point(self, p: Point, step: int):
        dumbo = self.floor[p]
        if dumbo is not None:
            if dumbo == 9:
                self.floor.set(p, 0)
                self.flashes.set(p, step)
                self.flash_sum += 1
                for d in directions:
                    n = p + d
                    self.incr_point(n, step)
            elif dumbo == 0 and self.flashes[p] == step:
                pass
            else:
                self.floor.set(p, self.floor[p] + 1)

    def output(self):
        result = []
        for row in self.floor.floor:
            output = ""
            for cell in row:
                output += str(cell)
            result.append(output)
        return result


class MyTestCase(unittest.TestCase):
    @parameterized.expand([
        [['0'], 1, ['1']],
        [['9'], 1, ['0']],
        [['0'], 10, ['0']],
    ])
    def test_one_by_one(self, data, steps, expected):
        g = Game(data)
        for s in range(1, steps + 1):
            g.step(s)
        actual = ["".join(str(cell)) for row in g.floor.floor for cell in row]
        self.assertEqual(expected, actual)

    @parameterized.expand([
        [['01'], 1, ['12']],
        [['89'], 1, ['00']],
    ])
    def test_one_by_two(self, data, steps, expected):
        g = Game(data)
        for s in range(1, steps + 1):
            g.step(s)
        self.assertEqual(expected, g.output())

    @parameterized.expand([
        [example1_step0, 1, example1_step1],
        [example1_step1, 1, example1_step2],
        [example1_step0, 2, example1_step2],
    ])
    def test_example1(self, data, steps, expected):
        g = Game(data)
        for s in range(1, steps + 1):
            g.step(s)
        print(data)
        self.assertEqual(expected, g.output())

    @parameterized.expand([
        [example2_steps[0], 1, example2_steps[1]],
        [example2_steps[1], 1, example2_steps[2]],
        [example2_steps[2], 1, example2_steps[3]],
        [example2_steps[3], 1, example2_steps[4]],
        [example2_steps[4], 1, example2_steps[5]],
        [example2_steps[5], 1, example2_steps[6]],
        [example2_steps[6], 1, example2_steps[7]],
        [example2_steps[7], 1, example2_steps[8]],
        [example2_steps[8], 1, example2_steps[9]],
        [example2_steps[9], 1, example2_steps[10]],
        [example2_steps[0], 5, example2_steps[5]],
        [example2_steps[0], 10, example2_steps[10]],
    ])
    def test_example2(self, data, steps, expected):
        g = Game(data)
        for s in range(1, steps + 1):
            g.step(s)
        self.assertEqual(expected, g.output())

    @parameterized.expand([
        [example2_steps[0], 10, 204],
        [example2_steps[0], 100, 1656],
    ])
    def test_example2_flashes(self, data, steps, expected):
        g = Game(data)
        for s in range(1, steps + 1):
            g.step(s)
        self.assertEqual(expected, g.flash_sum)

    def test_part1(self):
        g = Game(puzzle_input)
        steps = 100
        expected = 1667
        for s in range(1, steps + 1):
            g.step(s)
        self.assertEqual(expected, g.flash_sum)

    def test_part2(self):
        g = Game(puzzle_input)
        expected = 488
        step = 1
        while True:
            g.step(step)
            synchronized = len(set(g.floor.flatten())) == 1
            if synchronized:
                break
            step += 1
        self.assertEqual(expected, step)


if __name__ == '__main__':
    unittest.main()
