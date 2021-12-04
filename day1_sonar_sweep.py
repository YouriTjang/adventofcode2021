from functools import reduce

from numpy import inf


def sweep_window(sweep):
    if len(sweep) < 3:
        return 0
    for i in range(len(sweep) - 2):
        yield sweep[i:i+3]


def sum_window(windows):
    return list(map(lambda window: sum(window), windows))


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
    windows = list(sweep_window(sweep))
    windowed_sweeps = sum_window(windows)
    print(count_increases(windowed_sweeps))


if __name__ == '__main__':
    main()
