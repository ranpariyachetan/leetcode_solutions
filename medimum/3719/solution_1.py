# https://leetcode.com/problems/longest-balanced-subarray-i

from typing import List
import emoji

def longestBalanced(nums: List[int]) -> int:
    n = len(nums)
    max_length = 0

    for i in range(n):
        odds = set()
        evens = set()
        for j in range(i, n):
            if nums[j] % 2 == 0:
                evens.add(nums[j])
            else:
                odds.add(nums[j])

            if len(evens) == len(odds):
                max_length = max(max_length, j - i + 1)

    return max_length

def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

input = [1,2,3,4]
expected = 4
print_test_result(input, expected, longestBalanced(input))

input = [3,2,2,5,4]
expected = 5
print_test_result(input, expected, longestBalanced(input))

input = [1,2,3,2]
expected = 3
print_test_result(input, expected, longestBalanced(input))