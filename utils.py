import sys


def read_input(f):
    return [f(line.strip()) for line in sys.stdin.readlines()]
