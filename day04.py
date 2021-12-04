import sys
import re
from typing import List

lines = sys.stdin.read().split('\n\n')

numbers = [int(x) for x in lines[0].split(',')]
grids = [[[int(x) for x in re.split('\s+', line.strip())]
          for line in grid.strip().split('\n')] for grid in lines[1:]]


def isGridWinning(grid: List[List[int]]):
    # First check rows
    for line in grid:
        if sum(line) == -5:
            return True
    # Then check cols
    for col in range(5):
        if sum((grid[i][col] for i in range(5))) == -5:
            return True
    return False


def mark(grid: List[List[int]], x: int):
    for j in range(5):
        for i in range(5):
            if grid[j][i] == x:
                grid[j][i] = -1


def score(num, grid):
    sumOfGrid = sum(x for line in grid for x in line if x != -1)
    return num * sumOfGrid


def main():
    firstFound = False
    notWon = set(range(len(grids)))
    for num in numbers:
        for i, grid in enumerate(grids):
            if i in notWon:
                mark(grid, num)
                if isGridWinning(grid):
                    if not firstFound:
                        print('Part 1:', score(num, grid))
                        firstFound = True
                    if len(notWon) == 1:
                        print('Part 2:', score(num, grid))
                        return
                    notWon.remove(i)


main()
