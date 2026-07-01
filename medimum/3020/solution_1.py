# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset

from typing import List
from collections import defaultdict, Counter
from math import inf
def maximumLength(nums: List[int]) -> int:
    m = {}
    ones = 0
    for num in sorted(nums)[::-1]:
        if num ** 2 in m and num in m and num != 1:
            m[num] = m[num ** 2] + 2
        else:
            m[num] = 1

        if num == 1:
            ones += 1

    return max(max(m.values()), ones - (ones % 2 == 0))


nums = [5,4,1,2,2]
print(maximumLength(nums))

nums = [5,4,1,2,2,4,16]
print(maximumLength(nums))
                
nums = [1,1,1,1,1,1,1,1,1,1,2,4,8,16,32,64,128,256,512,1024]
print(maximumLength(nums))

nums = [2,4,8,16,32,64,128,256,512,1024,2,2,4,16,256]

print(maximumLength(nums))