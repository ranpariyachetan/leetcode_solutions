# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid

from typing import List

import emoji

def minSwaps(grid: List[List[int]]) -> int:
    n = len(grid)
    maxRight = [-1] * n
    
    for i in range(n):
        for j in range(n-1, -1, -1):
            if grid[i][j] == 1:
                maxRight[i] = j
                break

        if maxRight[i] == -1: 
            return -1
    
    maxRight = sorted(maxRight)

    for i in range(n):
        if maxRight[i] > i:
            return -1


    return 0

def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

input = [[0,0,1],[1,1,0],[1,0,0]]
expected = 3
print_test_result(input, expected, minSwaps(input))

# input = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# expected = -1
# print_test_result(input, expected, minSwaps(input))

# input = [[1,0,0],[1,1,0],[1,1,1]]
# expected = 0
# print_test_result(input, expected, minSwaps(input))