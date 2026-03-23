# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix

from itertools import count
from typing import List
import emoji


# Solution using DFS. Time complexity is O(2^(m+n)) and space complexity is O(m+n)
# This solution will give TLE for large inputs. We can optimize it using memoization or dynamic programming.
def maxProductPath(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    def traverse(r, c, curr_product):
        if r == m or c == n:
            return float("-inf")

        curr_product = curr_product * grid[r][c]
        if r == m - 1 and c == n - 1:
            return curr_product
        
        result = max(traverse(r + 1, c, curr_product), traverse(r, c + 1, curr_product))
        return result

    max_value = traverse(0, 0, 1)
    return -1 if max_value < 0 else max_value % (10 ** 9 + 7)

def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
expected = -1

print_test_result(grid, expected, maxProductPath(grid))

grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
expected = 8
print_test_result(grid, expected, maxProductPath(grid))