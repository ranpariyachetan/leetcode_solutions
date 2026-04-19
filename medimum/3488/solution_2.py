# https://leetcode.com/problems/closest-equal-element-queries
from typing import List

from bisect import bisect_left

def solveQueries(nums: List[int], queries: List[int]) -> List[int]:
    n = len(queries)
    m = len(nums)
    answer = [float("inf")] * n

    indices = {}

    for i, num in enumerate(nums):
        if not num in indices:
            indices[num] = []
        indices[num].append(i)

    for i, query in enumerate(queries):
        num = nums[query]

        pos = bisect_left(indices[num], query)
        index_list = indices[num]
        size = len(index_list)

        min_dist = answer[i]
        if size > 1:
            if pos == 0 or pos == size - 1:
                dist = min(abs(index_list[0] - index_list[-1]), m - abs(index_list[0] - index_list[-1]))
                min_dist = min(min_dist, dist)

            if pos - 1 >= 0:
                dist = min(abs(index_list[pos] - index_list[pos - 1]), m - abs(index_list[pos] - index_list[pos - 1]))
                min_dist = min(min_dist, dist)

            if pos + 1 < size:
                dist = min(abs(index_list[pos] - index_list[pos + 1]), m - abs(index_list[pos] - index_list[pos + 1]))
                min_dist = min(min_dist, dist)

            answer[i] = min_dist
        else:
            answer[i] = -1

    return answer



nums = [1,3,1,4,1,3,2]
queries = [0,3,5]

print(solveQueries(nums, queries))

# nums = [1,2,3,4]
# queries = [0,1,2,3]

# print(solveQueries(nums, queries))

nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
queries = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

print(solveQueries(nums, queries))