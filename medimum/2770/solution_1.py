# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index

from typing import List
def maximumJumps(nums: List[int], target: int) -> int:
    n = len(nums)
    dp = [-1] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if dp[j] != -1 and abs(nums[i] - nums[j]) <= target:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[-1]



nums = [1, 3, 6, 4, 1, 2]
target = 2
print(maximumJumps(nums, target))  # Output: 3

nums = [1,3,6,4,1,2]
target = 3
print(maximumJumps(nums, target))  # Output: 5

nums = [1,3,6,4,1,2]
target = 0
print(maximumJumps(nums, target))  # Output: -1