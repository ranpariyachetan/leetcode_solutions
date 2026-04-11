# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii

from typing import List

def minimumDistance(nums: List[int]) -> int:
    n = len(nums)
    indices = {}
    min_dist = float('inf')
    for i, num in enumerate(nums):
        if num not in indices:
            indices[num] = []
        indices[num].append(i)

    for num, idx_list in indices.items():
        if len(idx_list) >= 3:
            for i in range(len(idx_list) - 2):
                curr_dist = idx_list[i + 2] - idx_list[i]
                min_dist = min(min_dist, curr_dist * 2)
    return min_dist if min_dist != float('inf') else -1


nums = [1, 2, 1, 1, 3]
print(minimumDistance(nums))

nums = [1,1,2,3,2,1,2]
print(minimumDistance(nums))