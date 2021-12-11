import unittest

from parameterized import parameterized

pairs = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<',
}
opens = pairs.values()
closes = pairs.keys()
pair_completion = {k: v for v, k in pairs.items()}
completion_score = {
    ')': 1,
    '}': 3,
    ']': 2,
    '>': 4,
}
valid_chunk1 = "([])"
valid_chunk2 = "{()()()}"
valid_chunk3 = "<([{}])>"
valid_chunk4 = "[<>({}){}[([])<>]]"
valid_chunk5 = "(((((((((())))))))))"

corrupted_chuck1 = "(]"
corrupted_chuck2 = "{()()()>"
corrupted_chuck3 = "(((()))}"
corrupted_chuck4 = "<([]){()}[{}])"

inconplete_example_chunk1 = "[({(<(())[]>[[{[]{<()<>"
inconplete_example_chunk2 = "[(()[<>])]({[<{<<[]>>("
inconplete_example_chunk3 = "(((({<>}<{<{<>}{[]{[]{}"
inconplete_example_chunk4 = "{<[[]]>}<{[{[{[]{()[[[]"
inconplete_example_chunk5 = "<{([{{}}[<[[[<>{}]]]>[]]"

corrupted_example_chunk1 = "{([(<{}[<>[]}>{[]{[(<()>"
corrupted_example_chunk2 = "[[<[([]))<([[{}[[()]]]"
corrupted_example_chunk3 = "[{[{({}]{}}([{[{{{}}([]"
corrupted_example_chunk4 = "[<(<(<(<{}))><([]([]()"
corrupted_example_chunk5 = "<{([([[(<>()){}]>(<<{{"

corrupted_example_expected1 = 1197
corrupted_example_expected2 = 3
corrupted_example_expected3 = 57
corrupted_example_expected4 = 3
corrupted_example_expected5 = 25137

example_data = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


class Score:
    def __init__(self):
        self.syntax_error_score = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137,
        }

    def score_line(self, line):
        stack = []
        for char in line:
            if char in opens:
                stack.append(char)
            elif char in closes:
                top = stack.pop()
                if pairs[char] != top:
                    print(char)
                    return self.syntax_error_score[char]
            else:
                print("Error", char, "in", line)
        return 0

    def complete_line(self, line):
        stack = []
        for char in line:
            if char in opens:
                stack.append(char)
            elif char in closes:
                top = stack.pop()
                if pairs[char] != top:
                    # print(char)
                    return None
        stack.reverse()
        return [pair_completion[char] for char in stack]

    def calculate_completion_score(self, chars):
        total_score = 0
        for char in chars:
            total_score *= 5
            total_score += completion_score[char]
        return total_score


class Game:
    def __init__(self, lines):
        self.lines = lines
        self.syntax_error_score = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137,
        }

    def score_lines(self):
        sum = 0
        for line in self.lines:
            s = Score()
            sum += s.score_line(line)
        return sum

    def complete_lines(self):
        scores = []
        for line in self.lines:
            s = Score()
            completed_line = s.complete_line(line)
            if completed_line is not None:
                scores.append(s.calculate_completion_score(completed_line))
        scores = sorted(scores)
        return scores[int(len(scores)/2)]


class MyTestCase(unittest.TestCase):
    @parameterized.expand([
        ["valid_chunk1", valid_chunk1, 0],
        ["valid_chunk2", valid_chunk2, 0],
        ["valid_chunk3", valid_chunk3, 0],
        ["valid_chunk4", valid_chunk4, 0],
        ["valid_chunk5", valid_chunk5, 0],
        ["corrupted_chuck1", corrupted_chuck1, 57],
        ["corrupted_chuck2", corrupted_chuck2, 25137],
        ["corrupted_chuck3", corrupted_chuck3, 1197],
        ["corrupted_chuck4", corrupted_chuck4, 3],
    ])
    def test_valid_chunks(self, name, line, expected):
        s = Score()
        result = s.score_line(line)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["corrupted_example_chunk1", corrupted_example_chunk1,
         corrupted_example_expected1],
        ["corrupted_example_chunk2", corrupted_example_chunk2,
         corrupted_example_expected2],
        ["corrupted_example_chunk3", corrupted_example_chunk3,
         corrupted_example_expected3],
        ["corrupted_example_chunk4", corrupted_example_chunk4,
         corrupted_example_expected4],
        ["corrupted_example_chunk5", corrupted_example_chunk5,
         corrupted_example_expected5],
    ])
    def test_corrupted_example(self, name, line, expected):
        s = Score()
        actual = s.score_line(line)
        self.assertEqual(expected, actual)

    def test_example_part1(self):
        g = Game(example_data)
        actual = g.score_lines()
        self.assertEqual(26397, actual)

    def test_part1(self):
        g = Game(read_file())
        actual = g.score_lines()
        print(actual)

    @parameterized.expand([
        ["}}]])})]", 288957],
        [")}>]})", 5566],
        ["}}>}>))))", 1480781],
        ["]]}}]}]}>", 995444],
        ["])}>", 294],
    ])
    def test_score(self, line, expected):
        s = Score()
        score = s.calculate_completion_score(list(line))
        self.assertEqual(expected, score)

    def test_part2(self):
        g = Game(read_file())
        actual = g.complete_lines()
        print(actual)

if __name__ == '__main__':
    unittest.main()


def read_file():
    with open('../data/day10.txt', 'r') as f:
        lines = f.readlines()
        return lines
