def read_file(file):
    with open(file, 'r') as f:
        lines = [line for line in f.readlines()]
        return lines
