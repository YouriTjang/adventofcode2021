import unittest

from day1_sonar_sweep import count_increases, sweep_window


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sweep = [
            134,
            138,
            142,
            143,
            141,
            142,
            145,
            140,
            144,
        ]
        actual = count_increases(sweep)
        self.assertEqual(6, actual)

    def test_sweep_window(self):
        sweep = [
            134, 138, 142, 143, 141, 142, 145, 140, 144,
        ]

        actual = list(sweep_window(sweep))
        self.assertEqual([
            [134, 138, 142],
            [138, 142, 143],
            [142, 143, 141],
            [143, 141, 142],
            [141, 142, 145],
            [142, 145, 140],
            [145, 140, 144]
        ], actual)


if __name__ == '__main__':
    unittest.main()
