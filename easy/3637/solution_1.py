# Problem: Trionic Array I
# https://leetcode.com/problems/trionic-array-i

from typing import List
def isTrionic(nums: List[int]):
    n = len(nums)
   
    peaks = 0
    valleys = 0
    i = 1

    for i in range(1, n - 1):
        if nums[i-1] == nums[i] or nums[i] == nums[i+ 1]:
            return False
        if nums[i - 1] < nums[i] > nums[i + 1]:
            peaks += 1
        elif nums[i - 1] > nums[i] < nums[i + 1]:
            if peaks == 0:
                return False
            valleys += 1
    return peaks == valleys

input = [4,1,5,2,3]
expected = False

print(isTrionic(input) == expected)

input = [9,2,9,1]
expected = False
print(isTrionic(input) == expected)

input = [1,3,5,4,2,6]
expected = True
print(isTrionic(input) == expected)