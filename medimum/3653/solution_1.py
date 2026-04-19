# https://leetcode.com/problems/xor-after-range-multiplication-queries-i

from typing import List
def xorAfterQueries(nums: List[int], queries: List[List[int]]) -> int:
    MOD = 10 ** 9 + 7
    
    result = 0
    for l, r, k, v in queries:
        idx = l

        while idx <= r:
            nums[idx] =  (nums[idx] * v) % MOD
            idx += k

    for num in nums:
        result ^= num
    return result

nums = [1,1,1]
queries = [[0,2,1,4]]

print(xorAfterQueries(nums, queries))

nums = [2,3,1,5,4]
queries = [[1,2,3,4],[0,2,1,2]]

print(xorAfterQueries(nums, queries))