# Problem: Divide an Array Into Subarrays With Minimum Cost II
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii

from typing import List
from sortedcontainers import SortedList

def minimumCost(nums: List[int], k: int, dist: int) -> int:
    k -= 2

    cost = nums.pop(0)
    result = float("inf")
    w = SortedList(nums[:dist])

    cost += sum(w[:k])

    for l, r in zip(nums, nums[dist:]):
        w.add(r)
        cost += min(w[k], r)
        result = min(result, cost)
        
        print(w)
        cost -= min(w[k], l)
        w.remove(l)

    return result
    
nums = [30,40,42,19,50,8,23,33,25,6]
k = 7
dist = 6

print(minimumCost(nums, k, dist))