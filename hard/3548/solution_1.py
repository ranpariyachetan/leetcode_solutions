# https://leetcode.com/problems/equal-sum-grid-partition-ii

from typing import List
import emoji

def canPartitionGrid(grid: List[List[int]]) -> bool:
    total = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            total += grid[i][j]
    for _ in range(4):
        exist = set()
        exist.add(0)
        sum_val = 0
        m = len(grid)
        n = len(grid[0])
        if m < 2:
            grid = rotation(grid)
            continue
        if n == 1:
            for i in range(m - 1):
                sum_val += grid[i][0]
                tag = sum_val * 2 - total
                if tag == 0 or tag == grid[0][0] or tag == grid[i][0]:
                    return True
            grid = rotation(grid)
            continue
        for i in range(m - 1):
            for j in range(n):
                exist.add(grid[i][j])
                sum_val += grid[i][j]
            tag = sum_val * 2 - total
            if i == 0:
                if tag == 0 or tag == grid[0][0] or tag == grid[0][n - 1]:
                    return True
                continue
            if tag in exist:
                return True
        grid = rotation(grid)
    return False

def rotation(grid: List[List[int]]) -> List[List[int]]:
    m = len(grid)
    n = len(grid[0])
    tmp = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            tmp[j][m - 1 - i] = grid[i][j]
    return tmp


def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")
grid = [[1,2],[3,4]]
expected = True
print_test_result(grid, expected, canPartitionGrid(grid))

grid = [[1,2,4],[2,3,5]]
expected = False
print_test_result(grid, expected, canPartitionGrid(grid))

grid = [[10, 20, 30],
 [15, 10, 15],
 [10, 10, 10]]
expected = True
print_test_result(grid, expected, canPartitionGrid(grid))

grid = [[10, 20, 30],
 [10, 15, 15],
 [12, 11, 7]]
expected = True
print_test_result(grid, expected, canPartitionGrid(grid))

grid = [[4,1,8],[3,2,6]]
expected = False
print_test_result(grid, expected, canPartitionGrid(grid))   

grid = [[7, 8, 6],[10, 1, 11]]
expected = False
print_test_result(grid, expected, canPartitionGrid(grid))

grid = [[10,5,4,5]]
expected = False
print_test_result(grid, expected, canPartitionGrid(grid))

grid = [[29700],[29700]]
expected = True
print_test_result(grid, expected, canPartitionGrid(grid))