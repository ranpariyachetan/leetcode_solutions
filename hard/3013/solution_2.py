# Problem: Divide an Array Into Subarrays With Minimum Cost II
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii

from typing import List

def minimumCost(nums: List[int], k: int, dist: int) -> int:
    k -= 2

    cost = nums.pop(0)
    result = float("inf")
    w = sorted(nums[:dist])

    cost += sum(w[:k])

    for l, r in zip(nums, nums[dist:]):
        w.append(r)
        w = sorted(w)
        cost += min(w[k], r)
        result = min(result, cost)
        
        print(w)
        cost -= min(w[k], l)
        w.remove(l)

    return result
    

# This solution does not pass all the tests in LeetCode due to time limit exceeded.

nums = [30,40,42,19,50,8,23,33,25,6]
k = 7
dist = 6

print(minimumCost(nums, k, dist))