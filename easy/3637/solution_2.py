# Problem: Trionic Array I
# https://leetcode.com/problems/trionic-array-i

from typing import List

def isTrionic(nums: List[int]):
    n = len(nums)

    p = 0
    v = 0
    i = 1
    while i < n and nums[i] > nums[i - 1]:
        i += 1
    p = i - 1

    i = n - 1
    while i > 0 and nums[i] > nums[i - 1]:
        i -= 1
    v = i
    
    if p < v and p != 0 and v != n - 1:
        for i in range(p, v):
            if nums[i] <= nums[i + 1]:
                return False
        return True
        
    return False

input = [4,1,5,2,3]
expected = False

print(isTrionic(input) == expected)

input = [9,2,9,1]
expected = False
print(isTrionic(input) == expected)

input = [1,2,2,3]
expected = False
print(isTrionic(input) == expected)

input = [6,4,3,2,1]
expected = False
print(isTrionic(input) == expected)

input = [1,3,5,4,2,6]
expected = True
print(isTrionic(input) == expected)

input = [1,2, 3]
expected = False
print(isTrionic(input) == expected)

input = [1,4, 3]
expected = False
print(isTrionic(input) == expected)
