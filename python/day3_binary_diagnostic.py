import unittest


def read_file():
    with open('../data/day3.txt', 'r') as f:
        lines = f.readlines()
        return lines


def split_lines(lines):
    return list(map(lambda line: split_line(line.strip()), lines))


def split_line(line):
    return list(map(lambda char: int(char), list(line)))


def sum_column(report):
    sums = [0] * len(report[0])
    for y in range(0, len(report)):
        for x in range(0, len(report[0])):
            sums[x] += report[y][x]
    return sums


def calc_gamma(sums, report):
    majority = len(report) / 2
    gamma = list(map(lambda sum: 1 if sum >= majority else 0, sums))
    return gamma


def inverse_gamma(sums):
    return list(map(lambda it: 0 if it == 1 else 1, sums))


def binary_list_to_decimal(bin_list):
    bin_list.reverse()
    acc = 0
    for i in range(0, len(bin_list)):
        acc += bin_list[i] * pow(2, i)
    return acc


def bit_criteria_filter(report, co2=False):
    for i in range(0, len(report)):
        if len(report) <= 1:
            return report[0]
        sums = sum_column(report)
        gamma = calc_gamma(sums, report)
        if co2:
            gamma = inverse_gamma(gamma)
        report = list(filter(lambda line: line[i] == gamma[i], report))


def main_gamma_epsilon():
    lines = read_file()
    report = split_lines(lines)
    sums = sum_column(report)
    gamma = calc_gamma(sums, report)
    epsilon = inverse_gamma(gamma)
    gamma_rate = binary_list_to_decimal(gamma)
    epsilon_rate = binary_list_to_decimal(epsilon)
    print(gamma_rate * epsilon_rate)


def calc_oxygen_generator_rating(report):
    report = split_lines(report)
    oxygen_generator_rating = bit_criteria_filter(report)
    actual = binary_list_to_decimal(oxygen_generator_rating)
    return actual


def calc_co2_scrubber_rating(report):
    report = split_lines(report)
    oxygen_generator_rating = bit_criteria_filter(report, co2=True)
    actual = binary_list_to_decimal(oxygen_generator_rating)
    return actual


def main_life_support_rating():
    report = read_file()
    o2 = calc_oxygen_generator_rating(report.copy())
    print(o2)
    co2 = calc_co2_scrubber_rating(report)
    print(co2)
    print(str(o2 * co2))


class MyTestCase(unittest.TestCase):
    def test_split_line(self):
        self.assertEqual([0, 0, 1, 0, 0], split_line("00100"))

    def test_split_lines(self):
        report = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        expected = [
            [0, 0, 1, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 1, 1, 0],
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0],
        ]
        self.assertEqual(expected, split_lines(report))

    def test_run_main(self):
        main_gamma_epsilon()
        self.assertTrue(True)

    def test_binary_list_to_decimal(self):
        self.assertEqual(0, binary_list_to_decimal([0]))
        self.assertEqual(1, binary_list_to_decimal([1]))
        self.assertEqual(2, binary_list_to_decimal([1, 0]))
        self.assertEqual(3, binary_list_to_decimal([1, 1]))
        self.assertEqual(4, binary_list_to_decimal([1, 0, 0]))

    def test_calc_gamma(self):
        self.assertEqual([0], calc_gamma([1], [[1], [0], [0]]))
        self.assertEqual([1], calc_gamma([2], [[1], [1], [0]]))
        self.assertEqual([1, 0], calc_gamma([2, 1], [[1], [1], [0]]))

    def test_oxygen_generator_rating(self):
        report = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        actual = calc_oxygen_generator_rating(report)
        self.assertEqual(23, actual)

    def test_co2_scrubber_rating(self):
        report = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
        actual = calc_co2_scrubber_rating(report)
        self.assertEqual(10, actual)

    def test_main_life_support_rating(self):
        main_life_support_rating()
        self.assertTrue(True)


if __name__ == '__main__':
    main_life_support_rating()
    # unittest.main()
