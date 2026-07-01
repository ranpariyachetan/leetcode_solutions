# https://leetcode.com/problems/partition-array-according-to-given-pivot

from typing import List
def pivotArray(nums: List[int], pivot: int) -> List[int]:
    answer = []
    right = []
    equal = []

    for num in nums:
        if num < pivot:
            answer.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)

    answer.extend(equal)
    answer.extend(right)

    return answer
    
nums = [9,12,5,10,14,3,10]
pivot = 10

print(pivotArray(nums, pivot))


nums = [-3,4,3,2]
pivot = 2
print(pivotArray(nums, pivot))