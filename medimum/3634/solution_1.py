# https://leetcode.com/problems/minimum-removals-to-balance-array

from typing import List
import emoji
def minRemoval(nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        output = float("inf")
        j = 0
        for i in range(n):
            while j < n and nums[j] <= k * nums[i]:
                j = j + 1
            output = min(output, n - (j - i))

        return output
def print_test_result(input, expected, actual):
     print(f"{emoji.emojize(':check_mark_button:') if expected == actual else emoji.emojize(':cross_mark:')} Input = {input}, Expected = {expected}, Actual = {actual}")

input = [4,3,2,6,1,2]
k = 2
expected = 2
print_test_result(input, expected, minRemoval(input, k))


input = [1,6,2,9]
k = 3
expected = 2
print_test_result(input, expected, minRemoval(input, k))

input = [4,6]
k = 2
expected = 0
print_test_result(input, expected, minRemoval(input, k))