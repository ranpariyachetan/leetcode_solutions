# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i
from typing import List
def minimumDistance(nums: List[int]) -> int:
        n = len(nums)
        min_dist = n + 1
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[j] == nums[k]:
                        min_dist = min(min_dist, k - i)
        
        return -1 if min_dist == n + 1 else min_dist * 2

nums = [1, 2, 1, 1, 3]

print(minimumDistance(nums))