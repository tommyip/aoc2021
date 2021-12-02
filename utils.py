import sys


def read_input(f):
    return [f(line) for line in sys.stdin.readlines()]
