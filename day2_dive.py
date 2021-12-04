import unittest


class Pos:
    def __init__(self, x, y, aim):
        self.x = x
        self.y = y
        self.aim = aim

    def vector(self):
        return self.x * self.y

    def __add__(self, other):
        return Pos(self.x + other.x, self.y, self.aim + other.aim)

    def __mul__(self, other):
        return Pos(self.x + other.x, self.y + (self.aim * other.y), self.aim)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.aim == other.aim

    def __repr__(self):
        return f"({repr(self.x)}, {repr(self.y)}, {repr(self.aim)})"


class Sub(object):
    pos = Pos(0, 0, 0)

    def __init__(self, pos: Pos = Pos(0, 0, 0)):
        self.pos = pos

    def dive(self, command):
        parsed_command = Sub.parse_command(command)
        if command.startswith("forward"):
            self.pos = self.pos * parsed_command
        else:
            self.pos = self.pos + parsed_command
        return self.pos

    @staticmethod
    def parse_command(command):
        split = command.split(" ")
        action = split[0]
        unit = int(split[1])

        switch = {
            'forward': Pos(unit, unit, 0),
            'down': Pos(0, 0, unit),
            'up': Pos(0, 0, -unit),
        }
        return switch.get(action, Pos(0, 0, 0))

    def dives(self, commands):
        for command in commands:
            self.dive(command)

    @staticmethod
    def read_file_to_commands():
        with open('commands.txt', 'r') as f:
            lines = f.readlines()
            return list(map(lambda a: a, lines))


class MyTestCase(unittest.TestCase):
    def test_forward(self):
        command = "forward 5"
        sub = Sub()
        actual = sub.dive(command)
        expected = Pos(5, 0, 0)
        self.assertEqual(expected, actual)

    def test_down(self):
        command = "down 5"
        sub = Sub()
        actual = sub.dive(command)
        expected = Pos(0, 0, 5)
        self.assertEqual(expected, actual)

    def test_up(self):
        command = "up 5"
        sub = Sub()
        actual = sub.dive(command)
        expected = Pos(0, 0, -5)
        self.assertEqual(expected, actual)

    def test_vector(self):
        actual = Pos(3, 5, 0).vector()
        self.assertEqual(15, actual)

    def test_commands(self):
        commands = ["forward 5", "down 5", "forward 8"]
        sub = Sub()
        sub.dives(commands)
        actual = sub.pos
        expected = Pos(13, 40, 5)
        self.assertEqual(expected, actual)

    def test_commands_full(self):
        commands = ["forward 5", "down 5", "forward 8",
                    "up 3", "down 8", "forward 2"]
        sub = Sub()
        sub.dives(commands)
        actual = sub.pos
        expected = Pos(15, 60, 10)
        self.assertEqual(expected, actual)

    def test_run_commands(self):
        commands = Sub.read_file_to_commands()
        sub = Sub()
        sub.dives(commands)

        print(sub.pos.vector())
        self.assertTrue(True)

    def test_position_multiply(self):
        before = Pos(5, 0, 5)
        action = Pos(8, 8, 0)
        expected = Pos(13, 40, 5)
        self.assertEqual(expected, before * action)


if __name__ == '__main__':
    unittest.main()
