# Problem: Trionic Array II
# https://leetcode.com/problems/trionic-array-ii
from typing import List
def maxSumTrionic(nums: List[int]) -> int:
    n = len(nums)
    
    i = 0
    
    arr = []
    while(i < n - 1):
        
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
            
        start = i
        while i < n - 1 and nums[i] > nums[i + 1]:
            i += 1
            
        if start != i:
            arr.append((start, i))
    
    boundaris = []
    for start, end in arr:
        i = start
        j = end
        while i >= 0 and nums[i] > nums[i - 1]:
            i -=1
        while j < n - 1 and nums[j] < nums[j + 1]:
            j += 1

        boundaris.append((i, j))

    max_sum = float("-inf")
    for l, r in boundaris:
        max_sum = max(max_sum, sum(nums[l:r + 1]))
    return max_sum
    
# input = [1,3,5,4,2,6]
# print(maxSumTrionic(input))

# input = [9,2,9,1]
# print(maxSumTrionic(input))

# input = [6,4,3,2,1]
# print(maxSumTrionic(input))

# input = [1,2, 3]
# print(maxSumTrionic(input))

input = [0,-2,-1,-3,0,2,-1]
print(maxSumTrionic(input))