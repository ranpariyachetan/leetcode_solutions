# https://leetcode.com/problems/maximum-total-subarray-value-i

from typing import List

def maxTotalValue(nums: List[int], k: int) -> int:
    return k * (max(nums) - min(nums))

nums = [1,3,2]
k = 2

print(maxTotalValue(nums, k))