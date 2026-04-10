# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i
from typing import List
def minimumDistance(nums: List[int]) -> int:
        n = len(nums)
        min_dist = float("inf")
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if i != j and j != k and k != i:
                        if nums[i] == nums[j] == nums[k]:
                            min_dist = min(min_dist, abs(i - j) + abs(j - k) + abs(k - i))
        
        return -1 if min_dist == float("inf") else min_dist

nums = [1, 2, 1, 1, 3]

print(minimumDistance(nums))