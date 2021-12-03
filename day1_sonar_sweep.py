from functools import reduce
from numpy import inf


def read_file_to_sweep():
    with open('sweep.txt', 'r') as f:
        lines = f.readlines()
        return list(map(lambda a: int(a), lines))


def foo(acc: (int, int), value: int):
    return (acc[0] + 1, value) if acc[1] < value else (acc[0], value)


def count_increases(sweep):
    if len(sweep) == 0:
        return 0

    increases = reduce(foo, sweep, (0, inf))
    return increases[0]


def main():
    sweep = read_file_to_sweep()
    print(count_increases(sweep))


if __name__ == '__main__':
    main()
