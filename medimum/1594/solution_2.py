# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix

from itertools import count
from typing import List
import emoji


def maxProductPath(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    mx = [[0] * n for _ in range(m)]
    mn = [[0] * n for _ in range(m)]

    mx[0][0] = mn[0][0] = grid[0][0]

    for j in range(1, n):
        mx[0][j] = mn[0][j] = mx[0][j-1] * grid[0][j]

    for i in range(1, m):
        mx[i][0] = mn[i][0] = mx[i - 1][0] * grid[i][0]

    for i in range(1, m):
        for j in range(1, n):
            x = grid[i][j]

            a = mx[i - 1][j] * x
            b = mn[i - 1][j] * x
            c = mx[i][j - 1] * x
            d = mn[i][j - 1] * x

            mx[i][j] = max(a, b, c, d)
            mn[i][j] = min(a, b, c, d)

    result = mx[m - 1][n - 1]

    return -1 if result < 0 else result % (10 ** 9 + 7)

def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
expected = -1

print_test_result(grid, expected, maxProductPath(grid))

grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
expected = 8
print_test_result(grid, expected, maxProductPath(grid))