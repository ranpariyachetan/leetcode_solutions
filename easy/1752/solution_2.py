# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

from typing import List
def check(nums: List[int]) -> bool:
    n = len(nums)

    inv_count = 0

    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            inv_count += 1
            if inv_count > 1:
                return False

    if nums[0] < nums[-1]:
        inv_count += 1

    return inv_count <= 1


input = [3,4,5,1,2]
print(check(input))
input = [2,1,3,4]
print(check(input))
input = [1,2,3]
print(check(input))