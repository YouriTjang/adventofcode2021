import unittest

from day1_sonar_sweep import count_increases


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
        self.assertEqual(6, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
