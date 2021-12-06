import unittest
from datetime import datetime


class LanternFish:
    def __init__(self, days=8):
        self.days = days

    def reset(self):
        self.days = 6

    def a_day_passes(self):
        if self.days > 0:
            self.days -= 1
            return False
        else:
            self.reset()
            return True

    def __repr__(self):
        return repr(self.days)

    def __eq__(self, other):
        return self.days == other.days


def simulate(days_left: int, data: [int]):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time, days_left, len(data))
    if days_left == 0:
        return data
    else:
        result = []
        new_fishes = []
        for days in data:
            fish = LanternFish(days)
            new_fish = fish.a_day_passes()
            result.append(fish)
            if new_fish:
                new_fishes.append(LanternFish())
        result = result + new_fishes
        result = list(map(lambda f: f.days, result))
        return simulate(days_left - 1, result)


class MyTestCase(unittest.TestCase):
    def test_one_fish(self):
        fish = LanternFish(2)
        result = fish.a_day_passes()
        self.assertFalse(result)
        self.assertEqual(1, fish.days)
        result = fish.a_day_passes()
        self.assertFalse(result)
        self.assertEqual(0, fish.days)
        result = fish.a_day_passes()
        self.assertTrue(result)
        self.assertEqual(6, fish.days)

    def test_one_example(self):
        data = [3, 4, 3, 1, 2]
        expected = [2, 3, 2, 0, 1]
        self.assertEqual(expected, simulate(1, data))

    def test_full_example(self):
        data = [3, 4, 3, 1, 2]
        expected = [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2,
                    3, 3, 4, 6, 7, 8, 8, 8, 8]
        self.assertEqual(expected, simulate(18, data))

    def test_main(self):
        data = [4, 1, 1, 1, 5, 1, 3, 1, 5, 3, 4, 3, 3, 1, 3, 3, 1, 5, 3, 2, 4,
                4, 3, 4, 1, 4, 2, 2, 1, 3, 5, 1, 1, 3, 2, 5, 1, 1, 4, 2, 5, 4,
                3, 2, 5, 3, 3, 4, 5, 4, 3, 5, 4, 2, 5, 5, 2, 2, 2, 3, 5, 5, 4,
                2, 1, 1, 5, 1, 4, 3, 2, 2, 1, 2, 1, 5, 3, 3, 3, 5, 1, 5, 4, 2,
                2, 2, 1, 4, 2, 5, 2, 3, 3, 2, 3, 4, 4, 1, 4, 4, 3, 1, 1, 1, 1,
                1, 4, 4, 5, 4, 2, 5, 1, 5, 4, 4, 5, 2, 3, 5, 4, 1, 4, 5, 2, 1,
                1, 2, 5, 4, 5, 5, 1, 1, 1, 1, 1, 4, 5, 3, 1, 3, 4, 3, 3, 1, 5,
                4, 2, 1, 4, 4, 4, 1, 1, 3, 1, 3, 5, 3, 1, 4, 5, 3, 5, 1, 1, 2,
                2, 4, 4, 1, 4, 1, 3, 1, 1, 3, 1, 3, 3, 5, 4, 2, 1, 1, 2, 1, 2,
                3, 3, 5, 4, 1, 1, 2, 1, 2, 5, 3, 1, 5, 4, 3, 1, 5, 2, 3, 4, 4,
                3, 1, 1, 1, 2, 1, 1, 2, 1, 5, 4, 2, 2, 1, 4, 3, 1, 1, 1, 1, 3,
                1, 5, 2, 4, 1, 3, 2, 3, 4, 3, 4, 2, 1, 2, 1, 2, 4, 2, 1, 5, 2,
                2, 5, 5, 1, 1, 2, 3, 1, 1, 1, 3, 5, 1, 3, 5, 1, 3, 3, 2, 4, 5,
                5, 3, 1, 4, 1, 5, 2, 4, 5, 5, 5, 2, 4, 2, 2, 5, 2, 4, 1, 3, 2,
                1, 1, 4, 4, 1, 5]
        print("-----------")
        print(len(simulate(80, data)))
        print("-----------")


if __name__ == '__main__':
    unittest.main()
