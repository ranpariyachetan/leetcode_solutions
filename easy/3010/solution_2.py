# Divide an Array Into Subarrays With Minimum Cost I
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i

from typing import List
def minimumCost(nums: List[int]) -> int:
    min1 = 100
    min2 = 100

    for num in nums[1:]:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    return nums[0] + min1 + min2

nums = [1,15,7,9,2,5,10]

print("expected = 8")
print(f"actual = {minimumCost(nums)}")

nums = [3,7,1,12,4,11,8,2,6]
print("expected = 6")
print(f"actual = {minimumCost(nums)}")