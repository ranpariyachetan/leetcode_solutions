# https://leetcode.com/problems/partition-array-according-to-given-pivot

from typing import List
def pivotArray(nums: List[int], pivot: int) -> List[int]:
    answer = [0] * len(nums)
    left, i = 0, 0
    right, j = len(nums) - 1, len(nums) - 1

    
    while i < len(nums):
        if nums[i] < pivot:
            answer[left] = nums[i]
            left += 1
        if nums[j] > pivot:
            answer[right] = nums[j]
            right -= 1

        i += 1
        j -= 1

    while left <= right:
        answer[left] = pivot
        left +=1 
    return answer
    
nums = [9,12,5,10,14,3,10]
pivot = 10

print(pivotArray(nums, pivot))


nums = [-3,4,3,2]
pivot = 2
print(pivotArray(nums, pivot))