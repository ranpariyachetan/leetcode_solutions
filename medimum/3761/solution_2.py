# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs

from typing import List
from math import inf

def minMirrorPairDistance(nums: List[int]) -> int:    
    def reverse(x: int) -> int:
        res = 0

        while x > 0:
            rem = x % 10
            res = (res * 10) + rem
            x = x // 10
        return res
    
    answer = inf

    rev_idx = {}

    for i, num in enumerate(nums):
        if num in rev_idx:
            answer = min(answer, abs(i - rev_idx[num]))

        rev_idx[reverse(num)] = i

    return answer if answer != inf else -1

nums = [1, 23, 456, 321, 654, 12]
print(minMirrorPairDistance(nums))

nums = [4,9, 4]
print(minMirrorPairDistance(nums))

nums = [12,21,45,33,54]
print(minMirrorPairDistance(nums))

nums = [21, 10]
print(minMirrorPairDistance(nums))

nums = [120, 21]

print(minMirrorPairDistance(nums))
nums = [21, 120]

print(minMirrorPairDistance(nums))

nums = [1000,100,10,1,100,10,1]

print(minMirrorPairDistance(nums))